#!/usr/bin/env python3
"""Preparar um pedido de geração ou edição por texto. Não envia imagens à rede."""
import argparse,hashlib,json
from pathlib import Path

def prepare(config,output):
    cp=Path(config);cfg=json.loads(cp.read_text(encoding='utf-8'))
    action=cfg.get('action');prompt=cfg.get('instruction','').strip()
    if action not in ('generate','edit') or not prompt:raise ValueError('Informar action generate/edit e instruction')
    refs=cfg.get('images',[])
    if not isinstance(refs,list):raise ValueError('images precisa ser uma lista')
    records=[];lines=[f'Ação: {action}',f'Pedido: {prompt}']
    for i,item in enumerate(refs,1):
        role=item.get('role','').strip();p=(cp.parent/item['file']).resolve()
        if not role or not p.is_file():raise ValueError('Cada imagem exige arquivo existente e role')
        records.append({'index':i,'file':str(p),'role':role,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
        lines.append(f'Imagem {i}: {role}')
    if action=='edit' and not records:raise ValueError('Edição exige imagem alvo')
    for key,label in [('identity','Identidade'),('invariants','Preservar'),('allowed_changes','Pode mudar'),('style','Estilo')]:
        value=cfg.get(key)
        if value:
            if isinstance(value,list):value='; '.join(value)
            lines.append(f'{label}: {value}')
    lines.append('Fundo: '+cfg.get('background','realmente transparente; verificar alfa na saída'))
    lines.append('Produzir somente o avatar e acessórios usados no corpo, sem cena ou peças de jogo.')
    out=Path(output)
    out.mkdir(parents=True,exist_ok=False)
    (out/'prompt.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    record={'action':action,'images':records,'config_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),
        'prompt':'prompt.txt','execution':'not_executed','artistic_approval':'pending'}
    (out/'request.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return record

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('config');parser.add_argument('output')
    a=parser.parse_args()
    try:print(json.dumps(prepare(a.config,a.output),ensure_ascii=False,indent=2))
    except (ValueError,OSError,KeyError) as e:parser.exit(1,f'Erro: {e}\n')
