#!/usr/bin/env python3
"""Testes sintéticos locais do módulo. Nenhuma geração ou chamada de rede."""
import importlib.util,json,os,subprocess,sys,tempfile
from pathlib import Path
import numpy as np
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
def module(name):
    s=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
raster=module('raster_ops');request=module('prepare_request');doctor=module('doctor')

def rejected(fn,cls=ValueError):
    try:fn()
    except cls:return
    raise AssertionError('Operação inválida não foi recusada')

def run():
    module('unpack_provider').unpack()
    checks=[]
    with tempfile.TemporaryDirectory(prefix='avatar-raster-test-') as tmp:
        p=Path(tmp);a=np.array([[[255,0,0,255],[0,255,0,128],[0,0,255,255]],[[90,30,10,255],[70,10,20,0],[30,80,10,255]]],dtype=np.uint8)
        Image.fromarray(a).save(p/'source.png');original=(p/'source.png').read_bytes()
        rep=raster.transform(p/'source.png',p/'integer.png',12,8)
        got=np.array(raster.load(p/'integer.png'));assert np.array_equal(got,np.repeat(np.repeat(a,4,axis=0),4,axis=1))
        assert rep['transform']=={'scale_x':4.,'scale_y':4.,'offset_x':0,'offset_y':0}
        checks.append('Nearest inteiro preserva exatamente os RGBA amostrados, inclusive alfa parcial')
        rep=raster.transform(p/'source.png',p/'contain.png',12,12)
        b=np.array(raster.load(p/'contain.png'));assert (b[:2,:,3]==0).all() and (b[-2:,:,3]==0).all()
        assert np.array_equal(b[2:10],got) and rep['transform']['offset_y']==2
        checks.append('Contain adiciona margens sem cortar ou acumular alfa')
        rep=raster.transform(p/'source.png',p/'cover.png',4,4,'cover')
        assert rep['cropped'] and rep['transform']['offset_x']==-1
        expected=np.repeat(np.repeat(a,2,axis=0),2,axis=1)[:,1:5]
        assert np.array_equal(np.array(raster.load(p/'cover.png')),expected)
        checks.append('Cover declara e aplica o recorte registrado')
        for method in ['box','bilinear','bicubic','lanczos']:
            raster.transform(p/'source.png',p/f'{method}.png',7,5,'stretch',method)
            expected=Image.fromarray(a).convert('RGBa').resize((7,5),raster.FILTERS[method]).convert('RGBA')
            assert raster.load(p/f'{method}.png').tobytes()==expected.tobytes()
        checks.append('Filtros de mistura usam a referência de alfa pré-multiplicado')
        mask=np.array([[0,255,0],[255,255,0]],dtype=np.uint8);Image.fromarray(mask).save(p/'mask.png')
        raster.transform(p/'mask.png',p/'mask_big.png',10,10,kind='mask')
        m=np.array(raster.load(p/'mask_big.png'));assert set(np.unique(m[...,0]))<={0,255} and (m[...,3]==255).all()
        rejected(lambda:raster.transform(p/'mask.png',p/'badmask.png',10,10,method='lanczos',kind='mask'))
        checks.append('Máscaras permanecem binárias e recusam filtro suave')
        raster.mask_for_api(p/'mask.png',p/'mask_api.png');m=np.array(raster.load(p/'mask_api.png'))
        assert np.array_equal(m[...,3],255-mask)
        checks.append('Máscara branca editável converte para alfa zero da API')
        rejected(lambda:raster.transform(p/'source.png',p/'integer.png',12,8),FileExistsError)
        rejected(lambda:raster.transform(p/'source.png',p/'zero.png',0,8))
        rejected(lambda:raster.transform(p/'source.png',p/'huge.png',32769,8))
        assert (p/'source.png').read_bytes()==original and not (p/'zero.png').exists()
        checks.append('Originais e saídas existentes preservados; dimensões inválidas recusadas')
        cfg={'action':'edit','instruction':'Mudar somente a expressão','images':[{'file':'source.png','role':'alvo e identidade'}],
            'invariants':['cabelo','óculos'],'allowed_changes':['boca']}
        (p/'config.json').write_text(json.dumps(cfg))
        rec=request.prepare(p/'config.json',p/'request')
        assert rec['execution']=='not_executed' and rec['images'][0]['sha256']==raster.sha(p/'source.png')
        assert 'Preservar: cabelo; óculos' in (p/'request/prompt.txt').read_text()
        rejected(lambda:request.prepare(p/'config.json',p/'request'),FileExistsError)
        cfg['images']=[];(p/'bad.json').write_text(json.dumps(cfg));rejected(lambda:request.prepare(p/'bad.json',p/'badreq'))
        checks.append('Preparo de edição registra instrução e referências sem fingir execução')
        env={k:v for k,v in os.environ.items() if k!='OPENAI_API_KEY'}
        cli=ROOT/'providers/openai-imagegen/scripts/image_gen.py'
        for args in [
            ['generate','--prompt','Avatar sintético de teste','--out',str(p/'generated.png'),'--dry-run'],
            ['edit','--image',str(p/'source.png'),'--prompt','Mudar expressão','--out',str(p/'edited.png'),'--dry-run']]:
            result=subprocess.run([sys.executable,str(cli),*args],env=env,capture_output=True,text=True)
            assert result.returncode==0,result.stderr
        assert not (p/'generated.png').exists() and not (p/'edited.png').exists()
        checks.append('CLI integral prepara geração e edição em dry-run sem chave ou saída fictícia')
        state=doctor.doctor();assert not state['missing_files'] and state['network_calls']==0
        assert not state['api_connection_tested'] and state['native_image_tool']=='agent_must_check'
        checks.append('Diagnóstico verifica o pacote sem rede ou falsas promessas de geração')
    for c in checks:print('PASS',c)
    print(f'{len(checks)} grupos passaram. Geração real não executada.')
    return checks

if __name__=='__main__':run()
