#!/usr/bin/env python3
"""Resize, resample e conversão de máscara locais. Sem geração ou chamadas de rede."""
from __future__ import annotations
import argparse,json,hashlib
from pathlib import Path
from PIL import Image,ImageOps

FILTERS={name:getattr(Image.Resampling,name.upper()) for name in ('nearest','box','bilinear','bicubic','lanczos')}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def load(p):
    with Image.open(p) as im:
        im.load()
        if getattr(im,'n_frames',1)!=1:raise ValueError('Forneça uma imagem estática por operação')
        return ImageOps.exif_transpose(im).convert('RGBA')

def save_new(p,im):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    made=False
    try:
        with p.open('xb') as f:
            made=True;im.save(f,format='PNG')
        if load(p).tobytes()!=im.tobytes():raise ValueError('PNG gravado diverge dos pixels esperados')
    except Exception:
        if made:p.unlink(missing_ok=True)
        raise

def transform(source,output,width,height,mode='contain',method='nearest',kind='image'):
    if (isinstance(width,bool) or isinstance(height,bool) or not isinstance(width,int)
            or not isinstance(height,int) or min(width,height)<=0
            or max(width,height)>32768 or width*height>64_000_000):
        raise ValueError('Dimensões inteiras positivas; limite 32768 por lado e 64 milhões de pixels')
    if mode not in ('contain','cover','stretch'):raise ValueError('Modo inválido')
    if method not in FILTERS:raise ValueError('Filtro inválido')
    if kind not in ('image','mask'):raise ValueError('Tipo inválido')
    if kind=='mask' and method!='nearest':raise ValueError('Máscaras só admitem nearest')
    im=load(source);w,h=im.size
    if kind=='mask':
        pixels=list(im.getdata())
        if any(r!=g or g!=b or r not in (0,255) or a!=255 for r,g,b,a in pixels):
            raise ValueError('Máscara deve ser opaca, em preto e branco binário')
    if mode=='stretch':nw,nh=width,height
    else:
        scale=(min if mode=='contain' else max)(width/w,height/h)
        nw=max(1,round(w*scale));nh=max(1,round(h*scale))
        if mode=='contain':nw=min(nw,width);nh=min(nh,height)
        else:nw=max(nw,width);nh=max(nh,height)
    if nw*nh>64_000_000 or max(nw,nh)>32768:raise ValueError('Imagem intermediária excede o limite')
    # Nearest conserva os valores RGBA amostrados. Outros filtros usam alfa pré-multiplicado.
    resized=(im.resize((nw,nh),FILTERS[method]) if method=='nearest' else
        im.convert('RGBa').resize((nw,nh),FILTERS[method]).convert('RGBA'))
    ox=(width-nw)//2;oy=(height-nh)//2
    fill=(0,0,0,255) if kind=='mask' else (0,0,0,0)
    out=Image.new('RGBA',(width,height),fill)
    # Paste sem máscara copia os canais em vez de acumular alfa.
    out.paste(resized,(ox,oy))
    save_new(output,out)
    return {'source_sha256':sha(source),'output_sha256':sha(output),
        'source_size':[w,h],'output_size':[width,height],'resized_size':[nw,nh],
        'mode':mode,'method':method,'kind':kind,
        'transform':{'scale_x':nw/w,'scale_y':nh/h,'offset_x':ox,'offset_y':oy},
        'cropped':nw>width or nh>height,'new_detail_created':False,
        'alpha_processing':'sampled_rgba' if method=='nearest' else 'premultiplied_resampling',
        'note':'Atualizar pivôs, recortes e máscaras com a mesma transformação. Revisão visual necessária.'}

def mask_for_api(source,output):
    im=load(source);px=list(im.getdata())
    if any(r!=g or g!=b or r not in (0,255) or a!=255 for r,g,b,a in px):
        raise ValueError('Use máscara opaca binária; branco indica edição na distro')
    out=Image.new('RGBA',im.size)
    out.putdata([(0,0,0,255-r) for r,g,b,a in px])
    save_new(output,out)
    return {'source_sha256':sha(source),'output_sha256':sha(output),
        'convention':'branco editável convertido para alfa zero; preto protegido para alfa 255'}

def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='action',required=True)
    for action in ('resize','resample'):
        c=sub.add_parser(action);c.add_argument('source');c.add_argument('output')
        c.add_argument('--width',type=int,required=True);c.add_argument('--height',type=int,required=True)
        c.add_argument('--mode',choices=['contain','cover','stretch'],default='contain')
        c.add_argument('--method',choices=list(FILTERS),default='nearest')
        c.add_argument('--kind',choices=['image','mask'],default='image');c.add_argument('--report')
    c=sub.add_parser('mask-for-api');c.add_argument('source');c.add_argument('output');c.add_argument('--report')
    args=p.parse_args()
    try:
        result=(mask_for_api(args.source,args.output) if args.action=='mask-for-api' else
            transform(args.source,args.output,args.width,args.height,args.mode,args.method,args.kind))
        if args.report:
            with Path(args.report).open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
        print(json.dumps(result,ensure_ascii=False,indent=2));return 0
    except (ValueError,OSError) as e:
        print(f'Erro: {e}');return 1

if __name__=='__main__':raise SystemExit(main())
