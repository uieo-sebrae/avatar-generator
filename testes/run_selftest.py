#!/usr/bin/env python3
"""Testes funcionais sintéticos; não avaliam um avatar real."""
import importlib.util
import json
from pathlib import Path
import tempfile

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('avatar_tools', ROOT / 'tools/avatar_tools.py')
tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)


def expect_error(fn, cls=ValueError):
    try:
        fn()
    except cls:
        return
    raise AssertionError(f'Esperava {cls.__name__}')


def run():
    passed=[]
    with tempfile.TemporaryDirectory(prefix='avatar-selftest-') as tmp:
        p=Path(tmp)
        a=np.zeros((24,24,4),dtype=np.uint8)
        a[2:22,4:20]=[80,100,180,255]
        a[2:4,4:20,3]=128
        a[6:10,8:16,:3]=[210,150,110]
        Image.fromarray(a).save(p/'base.png')
        m=np.zeros((24,24),dtype=np.uint8);m[12:20,5:19]=255
        Image.fromarray(m).save(p/'mask.png')
        cfg={'parts':{'camisa':{'mask':'mask.png','mode':'exact','map':{'#5064B4':'#229955'}}}}
        tools.write_json(p/'exact.json',cfg)
        r=tools.recolor(p/'base.png',p/'exact.json',p/'verde.png')
        b=tools.rgba(p/'verde.png')
        assert np.array_equal(a[m==0],b[m==0]) and np.array_equal(a[...,3],b[...,3])
        assert np.all(b[m==255,:3]==[34,153,85]) and r['changed_outside']==0
        passed.append('Recoloração exata preserva pixels externos e alfa parcial')
        r=tools.compare(p/'base.png',p/'verde.png',p/'mask.png')
        assert r['outside_preserved'] and r['changed_inside']==int((m==255).sum())
        bad=b.copy();bad[0,0]=[255,0,0,255];Image.fromarray(bad).save(p/'bad.png')
        assert tools.compare(p/'base.png',p/'bad.png',p/'mask.png')['changed_outside']==1
        passed.append('Comparação detecta uma alteração externa')
        proposal=b.copy();proposal[...,3]=100;proposal[0,0]=[255,255,255,255]
        Image.fromarray(proposal).save(p/'proposal.png')
        tools.compose(p/'base.png',p/'proposal.png',p/'mask.png',p/'composed.png')
        comp=tools.rgba(p/'composed.png')
        assert np.array_equal(comp[...,3],a[...,3]) and np.array_equal(comp[m==0],a[m==0])
        assert np.array_equal(comp[m==255,:3],proposal[m==255,:3])
        tools.compose(p/'base.png',p/'proposal.png',p/'mask.png',p/'alpha_edit.png',preserve_alpha=False)
        edited=tools.rgba(p/'alpha_edit.png')
        assert np.array_equal(edited[m==255],proposal[m==255]) and np.array_equal(edited[m==0],a[m==0])
        passed.append('Composição substitui somente a máscara e controla a autorização de alfa')
        original=(p/'verde.png').read_bytes()
        expect_error(lambda:tools.recolor(p/'base.png',p/'exact.json',p/'verde.png'),FileExistsError)
        assert (p/'verde.png').read_bytes()==original
        passed.append('Saída existente não é sobrescrita nem apagada')
        cfg['parts']['outra']=dict(cfg['parts']['camisa']);tools.write_json(p/'overlap.json',cfg)
        expect_error(lambda:tools.recolor(p/'base.png',p/'overlap.json',p/'overlap.png'))
        assert not (p/'overlap.png').exists()
        cfg['parts'].pop('outra');cfg['parts']['camisa']['map']={'#000000':'#FFFFFF'}
        tools.write_json(p/'incomplete.json',cfg)
        expect_error(lambda:tools.recolor(p/'base.png',p/'incomplete.json',p/'incomplete.png'))
        passed.append('Sobreposição e paleta incompleta são recusadas')
        soft=m.copy();soft[12,5]=128;Image.fromarray(soft).save(p/'soft.png')
        expect_error(lambda:tools.mask(p/'soft.png',a.shape[:2]))
        invisible=m.copy();invisible[0,0]=255;Image.fromarray(invisible).save(p/'invisible.png')
        cfg={'parts':{'camisa':{'mask':'invisible.png','mode':'ramp','source_luma':[0,128,255],
            'colors':['#111111','#888888','#FFFFFF']}}}
        tools.write_json(p/'invisible.json',cfg)
        expect_error(lambda:tools.recolor(p/'base.png',p/'invisible.json',p/'invisible_out.png'))
        passed.append('Máscaras suaves e seleção invisível são recusadas')
        cfg['parts']['camisa']['mask']='mask.png';tools.write_json(p/'ramp.json',cfg)
        tools.recolor(p/'base.png',p/'ramp.json',p/'ramp.png')
        c=a.copy();c[8,8,:3]=[255,255,255];Image.fromarray(c).save(p/'other_frame.png')
        tools.recolor(p/'other_frame.png',p/'ramp.json',p/'other_ramp.png')
        assert np.array_equal(tools.rgba(p/'ramp.png')[m==255],tools.rgba(p/'other_ramp.png')[m==255])
        passed.append('Rampa compartilhada independe das cores fora da máscara')
        data=(p/'base.png').read_bytes();(p/'truncated.png').write_bytes(data[:-12])
        expect_error(lambda:tools.png_frames(p/'truncated.png'))
        broken=bytearray(data);broken[45]^=1;(p/'crc.png').write_bytes(broken)
        expect_error(lambda:tools.png_frames(p/'crc.png'))
        passed.append('PNG sem IEND e CRC corrompido são recusados')
        seq={'avatar_id':'teste','action':'teste','direction':'sul','master_version':'teste',
            'pivot':[12,22],'loop':True,'frames':[
                {'file':'base.png','duration_ms':125,'phase':'a'},
                {'file':'verde.png','duration_ms':250,'phase':'b'},
                {'file':'other_frame.png','duration_ms':375,'phase':'c'}]}
        tools.write_json(p/'seq.json',seq)
        manifest=tools.pack(p/'seq.json',p/'pack')
        frames,durations=tools.png_frames(p/'pack/animacao.apng')
        assert durations==[125,250,375] and len(frames)==3
        assert np.array_equal(frames[0],a) and np.array_equal(frames[1],b) and np.array_equal(frames[2],c)
        atlas=tools.rgba(p/'pack/atlas.png')
        assert all(np.array_equal(atlas[:,i*24:(i+1)*24],fr) for i,fr in enumerate(frames))
        assert manifest['duration_ms']==750 and manifest['pivot']==[12,22]
        assert all(tools.digest(p/'pack'/name)==sha for name,sha in manifest['files_sha256'].items())
        passed.append('Atlas, APNG, duração, pivô e hashes correspondem às fontes')
        html=(p/'pack/preview.html').read_text(encoding='utf-8')
        assert '__DATA__' not in html and html.count('data:image/png;base64,')==3
        passed.append('Preview incorpora todos os quadros sem dependência de rede')
        seq['frames'][1]['file']='base.png';tools.write_json(p/'repeat.json',seq)
        expect_error(lambda:tools.pack(p/'repeat.json',p/'repeat'))
        seq['frames'][1]['file']='verde.png';seq['frames'][0]['duration_ms']=0
        tools.write_json(p/'duration.json',seq)
        expect_error(lambda:tools.pack(p/'duration.json',p/'duration'))
        seq['frames'][0]['duration_ms']=125;seq['pivot']=[999,999]
        tools.write_json(p/'pivot.json',seq)
        expect_error(lambda:tools.pack(p/'pivot.json',p/'pivot'))
        seq['pivot']=[12,22];tools.write_json(p/'memory.json',seq)
        expect_error(lambda:tools.pack(p/'memory.json',p/'memory',max_mib=0.0001))
        passed.append('Repetições, duração, pivô e atlas acima do limite são recusados')
        Image.fromarray(a[:12]).save(p/'smaller.png');seq['frames'][1]['file']='smaller.png'
        tools.write_json(p/'size.json',seq)
        expect_error(lambda:tools.pack(p/'size.json',p/'size'))
        expect_error(lambda:tools.pack(p/'seq.json',p/'pack'),FileExistsError)
        assert tools.audit([p/'base.png',p/'pack/animacao.apng'])[1]['frame_count']==3
        passed.append('Canvas incompatível e destino existente são recusados; auditoria lê APNG inteiro')
        layer=np.zeros((4,4,4),dtype=np.uint8);layer[:]=[220,150,20,128]
        Image.fromarray(layer).save(p/'earring.png')
        occ=np.zeros((24,24),dtype=np.uint8);occ[5:7,6:8]=255
        Image.fromarray(occ).save(p/'occlusion.png')
        ac={'layers':[{'id':'brinco','file':'earring.png','position':[6,5],'occlusion_mask':'occlusion.png'}]}
        tools.write_json(p/'accessory.json',ac)
        r=tools.accessories(p/'base.png',p/'accessory.json',p/'with_earring.png')
        got=tools.rgba(p/'with_earring.png');area=np.zeros((24,24),bool);area[5:9,6:10]=True;area[occ==255]=False
        assert np.array_equal(got[~area],a[~area]) and np.any(got[area]!=a[area])
        assert r['changed_outside']==0
        passed.append('Acessório com alfa parcial respeita posição, oclusão e pixels externos')
        ac['layers'][0]['enabled']=False;tools.write_json(p/'disabled.json',ac)
        tools.accessories(p/'base.png',p/'disabled.json',p/'without_earring.png')
        assert np.array_equal(tools.rgba(p/'without_earring.png'),a)
        ac['layers'][0]['enabled']=True;ac['layers'][0]['position']=[23,23]
        tools.write_json(p/'off_canvas.json',ac)
        expect_error(lambda:tools.accessories(p/'base.png',p/'off_canvas.json',p/'off_canvas.png'))
        passed.append('Acessório desativado retorna à base; camada fora do canvas é recusada')
        cfg={'parts':{'brinco':{'mask':'mask.png','mode':'exact','map':{'#5064B4':'#DDBB44'}}}}
        tools.write_json(p/'accessory_color.json',cfg)
        tools.recolor(p/'base.png',p/'accessory_color.json',p/'accessory_color.png')
        assert np.all(tools.rgba(p/'accessory_color.png')[m==255,:3]==[221,187,68])
        passed.append('Nomes livres permitem recolorir máscara de acessório ou qualquer roupa')
        exif=Image.Exif();exif[274]=6
        Image.new('RGB',(20,30),(140,140,140)).save(p/'photo.jpg',exif=exif)
        before=tools.digest(p/'photo.jpg')
        pc={'photos':[{'id':'F01','file':'photo.jpg','face_bbox':[0,0,20,15]},
            {'id':'F02','file':'base.png'},{'id':'F03','file':'truncated.png'},
            {'id':'F04','file':'missing.jpg'}]}
        tools.write_json(p/'photos.json',pc);photos=tools.photo_audit(p/'photos.json')
        assert photos['photos'][0]['oriented_size']==[30,20]
        assert photos['photos'][0]['face_height_px']==15 and photos['photos'][0]['warnings']
        assert tools.digest(p/'photo.jpg')==before and not photos['automatic_identity_approval']
        assert photos['set_status']=='pending_visual_and_coverage_review'
        passed.append('Triagem de fotos respeita EXIF e recorte sem modificar original ou aprovar identidade')
        assert photos['photos'][1]['indicators']['region']=='whole_image'
        assert not photos['photos'][2]['readable'] and not photos['photos'][3]['readable']
        assert all(x['visual_review']=='pending' for x in photos['photos'])
        passed.append('Fotos ilegíveis ou ausentes são sinalizadas; revisão visual permanece pendente')
    for item in passed:
        print('PASS',item)
    print(f'{len(passed)} grupos de verificação passaram. Mérito artístico não avaliado.')
    return passed


if __name__=='__main__':
    run()
