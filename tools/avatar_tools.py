#!/usr/bin/env python3
"""Ferramentas determinísticas para avatares raster. Não geram arte ou máscaras."""
from __future__ import annotations
import argparse
import base64
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import struct
import sys
import tempfile
import zlib

import numpy as np
from PIL import Image, ImageOps


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def png_frames(path):
    """Valida todos os chunks, IEND, CRC e decodifica todos os quadros."""
    path = Path(path)
    data = path.read_bytes()
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError(f'Não é PNG: {path}')
    pos, ended = 8, False
    while pos < len(data):
        if pos + 12 > len(data):
            raise ValueError(f'Chunk truncado: {path}')
        length = struct.unpack('>I', data[pos:pos+4])[0]
        end = pos + 12 + length
        if end > len(data):
            raise ValueError(f'Dados PNG incompletos: {path}')
        kind = data[pos+4:pos+8]
        payload = data[pos+8:pos+8+length]
        crc = struct.unpack('>I', data[pos+8+length:end])[0]
        if zlib.crc32(kind + payload) & 0xffffffff != crc:
            raise ValueError(f'CRC inválido: {path}, {kind!r}')
        pos = end
        if kind == b'IEND':
            if length != 0 or pos != len(data):
                raise ValueError(f'IEND ou dados finais inválidos: {path}')
            ended = True
            break
    if not ended:
        raise ValueError(f'IEND ausente: {path}')
    with Image.open(io.BytesIO(data)) as im:
        frames, durations = [], []
        for i in range(getattr(im, 'n_frames', 1)):
            im.seek(i)
            im.load()
            frames.append(np.array(im.convert('RGBA')))
            durations.append(float(im.info.get('duration', 0)))
    return frames, durations


def rgba(path):
    frames, _ = png_frames(path)
    if len(frames) != 1:
        raise ValueError(f'Use PNG estático neste comando: {path}')
    return frames[0]


def mask(path, shape):
    a = rgba(path)
    if a.shape[:2] != shape:
        raise ValueError(f'Máscara com tamanho diferente da base: {path}')
    if not (np.all(a[..., 0] == a[..., 1]) and np.all(a[..., 1] == a[..., 2])):
        raise ValueError(f'Máscara precisa ser em tons de cinza: {path}')
    if not np.all(a[..., 3] == 255):
        raise ValueError(f'Máscara precisa ter alfa opaco: {path}')
    v = a[..., 0]
    if not np.all((v == 0) | (v == 255)):
        raise ValueError(f'Máscara precisa conter somente 0 e 255: {path}')
    selected = v == 255
    if not selected.any():
        raise ValueError(f'Máscara vazia: {path}')
    return selected


def color(value):
    if not isinstance(value, str) or len(value) != 7 or not value.startswith('#'):
        raise ValueError('Use cor #RRGGBB')
    return np.array([int(value[i:i+2], 16) for i in (1, 3, 5)], dtype=np.uint8)


def write_json(path, obj):
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def save_png_new(path, a):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Criação exclusiva: nunca sobrescreve um original existente.
    created = False
    try:
        with path.open('xb') as f:
            created = True
            Image.fromarray(a).save(f, format='PNG')
        if not np.array_equal(rgba(path), a):
            raise ValueError('PNG gravado diverge dos pixels esperados')
    except Exception:
        # Não apagar um arquivo que já existia antes da operação.
        if created and path.exists():
            path.unlink()
        raise


def audit(paths):
    results = []
    for path in paths:
        p = Path(path)
        frames, durations = png_frames(p)
        a = frames[0]
        alpha = a[..., 3]
        results.append({
            'file': str(p), 'sha256': digest(p), 'width': a.shape[1], 'height': a.shape[0],
            'frame_count': len(frames), 'durations_ms': durations,
            'first_frame_alpha': {'transparent': int((alpha == 0).sum()),
                'partial': int(((alpha > 0) & (alpha < 255)).sum()), 'opaque': int((alpha == 255).sum())},
            'technical_decode': 'passed', 'artistic_approval': 'not_evaluated'
        })
    return results


def compare(base, candidate, mask_file):
    a, b = rgba(base), rgba(candidate)
    if a.shape != b.shape:
        raise ValueError('Base e candidata precisam ter as mesmas dimensões')
    m = mask(mask_file, a.shape[:2])
    changed = np.any(a != b, axis=2)
    return {
        'base_sha256': digest(base), 'candidate_sha256': digest(candidate),
        'mask_sha256': digest(mask_file),
        'changed_inside': int((changed & m).sum()),
        'changed_outside': int((changed & ~m).sum()),
        'alpha_changed': int((a[..., 3] != b[..., 3]).sum()),
        'outside_preserved': bool(not (changed & ~m).any()),
        'artistic_approval': 'not_evaluated'
    }


def recolor(base, config_file, output):
    cfg_path = Path(config_file)
    cfg = json.loads(cfg_path.read_text(encoding='utf-8'))
    if not isinstance(cfg.get('parts'), dict) or not cfg['parts']:
        raise ValueError('Configuração precisa de parts não vazio')
    a = rgba(base)
    out = a.copy()
    union = np.zeros(a.shape[:2], dtype=bool)
    records = []
    luma = a[..., :3].astype(float) @ np.array([0.299, 0.587, 0.114])
    for name, part in cfg['parts'].items():
        mp = cfg_path.parent / part['mask']
        m = mask(mp, a.shape[:2])
        if (union & m).any():
            raise ValueError(f'Máscaras sobrepostas: {name}')
        if (m & (a[..., 3] == 0)).any():
            raise ValueError(f'Máscara seleciona pixels invisíveis: {name}')
        union |= m
        mode = part.get('mode')
        if mode == 'exact':
            mapping = part.get('map', {})
            covered = np.zeros_like(m)
            for old, new in mapping.items():
                hit = m & np.all(a[..., :3] == color(old), axis=2)
                out[hit, :3] = color(new)
                covered |= hit
            if (m & ~covered).any():
                raise ValueError(f'Paleta incompleta em {name}: {int((m & ~covered).sum())} pixels')
        elif mode == 'ramp':
            anchors = np.array(part['source_luma'], dtype=float)
            ramp = np.array([color(c) for c in part['colors']], dtype=float)
            if (len(anchors) < 2 or len(anchors) != len(ramp)
                    or not np.isfinite(anchors).all() or np.any(np.diff(anchors) <= 0)
                    or anchors[0] < 0 or anchors[-1] > 255):
                raise ValueError(f'Rampa inválida: {name}')
            pixels = luma[m]
            mapped = np.stack([np.interp(pixels, anchors, ramp[:, c]) for c in range(3)], axis=1)
            out[m, :3] = np.rint(mapped).clip(0, 255).astype(np.uint8)
        else:
            raise ValueError(f'Modo desconhecido: {mode}')
        records.append({'part': name, 'mask_sha256': digest(mp), 'selected_pixels': int(m.sum()), 'mode': mode})
    if not np.array_equal(a[~union], out[~union]) or not np.array_equal(a[..., 3], out[..., 3]):
        raise AssertionError('Falha na preservação')
    save_png_new(output, out)
    return {'source_sha256': digest(base), 'output_sha256': digest(output),
        'config_sha256': digest(config_file), 'parts': records,
        'changed_outside': 0, 'alpha_changed': 0, 'artistic_approval': 'pending'}


def compose(base, proposal, mask_file, output, preserve_alpha=True):
    """Substitui pixels da proposta já alinhada; não usa alpha-over."""
    a, b = rgba(base), rgba(proposal)
    if a.shape != b.shape:
        raise ValueError('Base e proposta precisam estar alinhadas no mesmo canvas')
    m = mask(mask_file, a.shape[:2])
    out = a.copy()
    out[m] = b[m]
    if preserve_alpha:
        out[..., 3] = a[..., 3]
    if not np.array_equal(a[~m], out[~m]):
        raise AssertionError('Composição alterou pixels externos')
    save_png_new(output, out)
    return {'source_sha256':digest(base),'proposal_sha256':digest(proposal),
        'mask_sha256':digest(mask_file),'output_sha256':digest(output),
        'operation':'pixel_replace','changed_outside':0,
        'alpha_changed':int((a[...,3]!=out[...,3]).sum()),
        'preserve_alpha':preserve_alpha,'artistic_approval':'pending'}


HTML = '''<!doctype html>
<html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Revisão de sequência do avatar</title>
<style>
body{font:16px system-ui;margin:24px;background:#f5f6f8;color:#152033}main{max-width:1000px;margin:auto}
h1{font-size:24px}button,input,select{font:inherit;padding:8px;margin:4px}button{cursor:pointer}
#stage{height:60vh;min-height:240px;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #bbb}
#stage img{max-width:100%;max-height:100%;image-rendering:pixelated;object-fit:contain}
.controls{display:flex;align-items:center;flex-wrap:wrap;margin-top:14px}#slider{flex:1;min-width:140px}
</style><main><h1>Revisão de sequência do avatar</h1>
<p id="meta"></p><div id="stage"><img id="frame" alt="Quadro do avatar"></div>
<div class="controls"><button id="play">Pausar</button><button id="prev" aria-label="Quadro anterior">Anterior</button>
<input id="slider" aria-label="Selecionar quadro" type="range" min="0" step="1" value="0">
<button id="next">Próximo</button><select id="bg" aria-label="Fundo"><option value="#ffffff">Branco</option>
<option value="#111827">Escuro</option><option value="#2654c7">Azul</option></select></div>
<p id="label" aria-live="polite"></p><p>Conferir identidade, anatomia, transparência e emenda do ciclo. Este preview não certifica aprovação artística.</p>
<script>
const data=__DATA__;let index=0,playing=!matchMedia('(prefers-reduced-motion: reduce)').matches,timer=null;
const $=id=>document.getElementById(id);$('slider').max=data.frames.length-1;
$('meta').textContent=[data.avatar_id,data.action,data.direction].filter(Boolean).join(' • ');
function draw(){const f=data.frames[index];$('frame').src=f.uri;$('slider').value=index;
$('label').textContent=`Quadro ${index+1}/${data.frames.length} • ${f.phase||''} • ${f.duration_ms} ms`;
$('play').textContent=playing?'Pausar':'Reproduzir';}
function schedule(){clearTimeout(timer);if(playing)timer=setTimeout(()=>{
if(index===data.frames.length-1&&!data.loop){playing=false;draw();return;}
index=(index+1)%data.frames.length;draw();schedule();},data.frames[index].duration_ms);}
function manual(i){playing=false;index=(i+data.frames.length)%data.frames.length;draw();schedule();}
$('play').onclick=()=>{if(!playing&&!data.loop&&index===data.frames.length-1)index=0;playing=!playing;draw();schedule();};
$('prev').onclick=()=>manual(index-1);$('next').onclick=()=>manual(index+1);
$('slider').oninput=()=>manual(Number($('slider').value));
$('bg').onchange=()=>$('stage').style.background=$('bg').value;
draw();schedule();
</script></main></html>'''


def pack(config_file, output, max_mib=256):
    cfg_path = Path(config_file)
    cfg = json.loads(cfg_path.read_text(encoding='utf-8'))
    records = cfg.get('frames', [])
    if not 2 <= len(records) <= 256:
        raise ValueError('Forneça de 2 a 256 quadros distintos; use PNG para imagem estática')
    frames, sources, times = [], [], []
    pixel_hashes = set()
    for rec in records:
        p = cfg_path.parent / rec['file']
        a = rgba(p)
        if frames and a.shape != frames[0].shape:
            raise ValueError('Todos os quadros precisam ter o mesmo canvas')
        t = rec['duration_ms']
        if isinstance(t, bool) or not isinstance(t, int) or not 1 <= t <= 65535:
            raise ValueError('Duração inteira entre 1 e 65535 ms')
        ph = hashlib.sha256(a.tobytes()).hexdigest()
        if ph in pixel_hashes:
            raise ValueError('Quadros idênticos: represente pausas pela duração, sem repetir o PNG')
        pixel_hashes.add(ph)
        frames.append(a);sources.append(p);times.append(t)
    h, w = frames[0].shape[:2]
    pivot = cfg.get('pivot')
    if (not isinstance(pivot, list) or len(pivot) != 2
            or any(isinstance(v, bool) or not isinstance(v, int) for v in pivot)
            or not (0 <= pivot[0] <= w and 0 <= pivot[1] <= h)):
        raise ValueError('Pivô precisa ser [x,y] inteiro dentro do canvas ou em seu limite')
    loop = cfg.get('loop', True)
    if not isinstance(loop, bool):
        raise ValueError('loop precisa ser true ou false')
    width = w * len(frames)
    mib = width * h * 4 / 1024**2
    if width > 16384 or h > 16384 or mib > max_mib:
        raise ValueError(f'Atlas excede limite conservador de memória ou dimensão ({mib:.1f} MiB). Divida a sequência.')
    target = Path(output)
    if target.exists():
        raise FileExistsError(f'Destino já existe: {target}')
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = Path(tempfile.mkdtemp(prefix='avatar-pack-', dir=target.parent))
    try:
        atlas = np.zeros((h, width, 4), dtype=np.uint8)
        frame_records = []
        view = {k: cfg.get(k) for k in ('avatar_id', 'action', 'direction')}
        view.update(loop=loop, frames=[])
        for i, (a, p, duration) in enumerate(zip(frames, sources, times)):
            x = i * w
            atlas[:, x:x+w] = a
            name = f'f{i:03}.png'
            Image.fromarray(a).save(temp / name)
            phase = records[i].get('phase', '')
            frame_records.append({'index': i, 'file': name, 'duration_ms': duration, 'phase': phase,
                'rect': [x, 0, w, h], 'source_file': records[i]['file'],
                'source_sha256': digest(p), 'sha256': digest(temp / name)})
            uri = 'data:image/png;base64,' + base64.b64encode((temp / name).read_bytes()).decode('ascii')
            view['frames'].append({'uri': uri, 'duration_ms': duration, 'phase': phase})
        Image.fromarray(atlas).save(temp / 'atlas.png')
        images = [Image.fromarray(a) for a in frames]
        images[0].save(temp / 'animacao.apng', format='PNG', save_all=True,
            append_images=images[1:], duration=times, loop=0 if loop else 1, disposal=0, blend=0)
        decoded, encoded_times = png_frames(temp / 'animacao.apng')
        if len(decoded) != len(frames) or any(not np.array_equal(a,b) for a,b in zip(decoded,frames)):
            raise ValueError('APNG não corresponde aos PNGs')
        if len(frames) > 1 and any(abs(a-b) > 0.01 for a,b in zip(times,encoded_times)):
            raise ValueError('Durações APNG divergem')
        atlas_check = rgba(temp / 'atlas.png')
        if not np.array_equal(atlas_check, atlas):
            raise ValueError('Atlas não corresponde aos PNGs')
        payload = json.dumps(view, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
        (temp / 'preview.html').write_text(HTML.replace('__DATA__', payload), encoding='utf-8')
        result = {k: cfg.get(k) for k in ('avatar_id','master_version','action','direction','status')}
        result.update(schema_version='1.0', canvas=[w,h], pivot=pivot,
            coordinates={'origin':'top_left','rect':'x_y_width_height','bbox_end':'exclusive'},
            loop=loop, duration_ms=sum(times), atlas='atlas.png', atlas_rgba_mib=round(mib,3),
            apng='animacao.apng', frames=frame_records,
            files_sha256={p.name:digest(p) for p in sorted(temp.iterdir()) if p.is_file()},
            technical={'png_decode': 'passed', 'atlas_pixels':'passed', 'apng_pixels':'passed',
                'browser_render':'not_evaluated', 'artistic_approval':'not_evaluated'})
        write_json(temp / 'manifest.json', result)
        # Publica o diretório somente depois das verificações.
        os.rename(temp, target)
        return result
    except Exception:
        shutil.rmtree(temp, ignore_errors=True)
        raise


def accessories(base, config_file, output):
    """Aplica camadas preparadas sem alterar a base fora da área visível do acessório."""
    cfg_path=Path(config_file)
    cfg=json.loads(cfg_path.read_text(encoding='utf-8'))
    layers=cfg.get('layers')
    if not isinstance(layers,list) or not layers:
        raise ValueError('Forneça layers com ao menos uma camada, mesmo se desativada')
    a=rgba(base);out=a.copy();h,w=a.shape[:2]
    footprint=np.zeros((h,w),dtype=bool);records=[]
    for item in layers:
        if item.get('enabled',True) is False:
            records.append({'id':item.get('id'),'enabled':False});continue
        p=cfg_path.parent/item['file'];local=rgba(p)
        xy=item.get('position',[0,0])
        if (not isinstance(xy,list) or len(xy)!=2
                or any(isinstance(v,bool) or not isinstance(v,int) for v in xy)):
            raise ValueError('position precisa ser [x,y] inteiro')
        x,y=xy;lh,lw=local.shape[:2]
        if x<0 or y<0 or x+lw>w or y+lh>h:
            raise ValueError('Acessório excede o canvas; ajuste a posição ou prepare outra camada')
        layer=np.zeros_like(a);layer[y:y+lh,x:x+lw]=local
        occlusion=item.get('occlusion_mask')
        if occlusion:
            hidden=mask(cfg_path.parent/occlusion,(h,w));layer[hidden]=0
        visible=layer[...,3]>0;footprint|=visible
        # Ordem de layers é a ordem de sobreposição; máscara resolve oclusões locais.
        out=np.array(Image.alpha_composite(Image.fromarray(out),Image.fromarray(layer)))
        records.append({'id':item.get('id'),'enabled':True,'source_sha256':digest(p),
            'position':xy,'visible_pixels':int(visible.sum()),
            'occlusion_sha256':digest(cfg_path.parent/occlusion) if occlusion else None})
    if not np.array_equal(a[~footprint],out[~footprint]):
        raise AssertionError('Acessório modificou pixels fora de sua região')
    save_png_new(output,out)
    return {'source_sha256':digest(base),'config_sha256':digest(config_file),
        'output_sha256':digest(output),'layers':records,'changed_outside':0,
        'operation':'prepared_layers_alpha_over','artistic_approval':'pending'}


def photo_audit(config_file):
    """Triagem técnica; a qualidade facial e a suficiência do conjunto exigem revisão visual."""
    cp=Path(config_file);cfg=json.loads(cp.read_text(encoding='utf-8'))
    photos=cfg.get('photos')
    if not isinstance(photos,list) or not photos:
        raise ValueError('Forneça photos com os caminhos das fotos')
    results=[]
    for item in photos:
        p=cp.parent/item['file'];rec={'id':item.get('id'),'file':item['file'],
            'visual_review':'pending','identity_features_verified':False}
        try:
            with Image.open(p) as im:
                if im.format=='PNG':
                    png_frames(p)
                im.load()
                if getattr(im,'n_frames',1)!=1:
                    raise ValueError('Forneça uma foto estática')
                oriented=ImageOps.exif_transpose(im).convert('RGB')
                w,h=oriented.size
                rec.update(readable=True,sha256=digest(p),oriented_size=[w,h],warnings=[])
                bbox=item.get('face_bbox')
                if bbox is not None:
                    if (not isinstance(bbox,list) or len(bbox)!=4
                            or any(isinstance(v,bool) or not isinstance(v,int) for v in bbox)):
                        raise ValueError('face_bbox precisa ser [x,y,largura,altura] inteiro')
                    x,y,bw,bh=bbox
                    if min(x,y)<0 or min(bw,bh)<=0 or x+bw>w or y+bh>h:
                        raise ValueError('face_bbox fora da foto já orientada')
                    sample=oriented.crop((x,y,x+bw,y+bh));region='face_bbox_provided'
                    rec['face_height_px']=bh
                    if bh<500:rec['warnings'].append('Rosto com menos de 500 px de altura; revisar detalhe visível')
                else:
                    sample=oriented;region='whole_image'
                    rec['warnings'].append('Sem recorte facial marcado; métricas globais não medem nitidez do rosto')
                gray=np.asarray(sample.convert('L'),dtype=float)
                black=float((gray<=5).mean());white=float((gray>=250).mean())
                if min(gray.shape)>=3:
                    lap=gray[:-2,1:-1]+gray[2:,1:-1]+gray[1:-1,:-2]+gray[1:-1,2:]-4*gray[1:-1,1:-1]
                    sharpness=float(lap.var())
                else:sharpness=None
                rec['indicators']={'region':region,'luma_mean':round(float(gray.mean()),2),
                    'dark_fraction':round(black,4),'bright_fraction':round(white,4),
                    'laplacian_variance':round(sharpness,2) if sharpness is not None else None}
                if black>.25 or white>.25:
                    rec['warnings'].append('Extremos de luminosidade acima de 25% da região; verificar sombras e detalhes')
                rec['technical_status']='readable_needs_visual_review'
                rec['note']='Indicadores não aprovam fotos nem identificam automaticamente rosto, idade ou gênero'
        except (OSError,ValueError) as error:
            rec.update(readable=False,technical_status='review_input',error=str(error))
        results.append(rec)
    return {'photos':results,'set_status':'pending_visual_and_coverage_review',
        'automatic_identity_approval':False,'originals_modified':False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('audit');p.add_argument('files', nargs='+');p.add_argument('--report')
    p = sub.add_parser('compare');p.add_argument('base');p.add_argument('candidate');p.add_argument('mask');p.add_argument('--report')
    p = sub.add_parser('recolor');p.add_argument('base');p.add_argument('config');p.add_argument('output');p.add_argument('--report')
    p = sub.add_parser('compose');p.add_argument('base');p.add_argument('proposal');p.add_argument('mask');p.add_argument('output');p.add_argument('--allow-alpha',action='store_true');p.add_argument('--report')
    p = sub.add_parser('accessories');p.add_argument('base');p.add_argument('config');p.add_argument('output');p.add_argument('--report')
    p = sub.add_parser('photo-audit');p.add_argument('config');p.add_argument('--report')
    p = sub.add_parser('pack');p.add_argument('config');p.add_argument('output');p.add_argument('--max-atlas-mib',type=float,default=256)
    args = parser.parse_args()
    try:
        if args.command == 'audit': result = audit(args.files)
        elif args.command == 'compare': result = compare(args.base,args.candidate,args.mask)
        elif args.command == 'recolor': result = recolor(args.base,args.config,args.output)
        elif args.command == 'compose': result = compose(args.base,args.proposal,args.mask,args.output,not args.allow_alpha)
        elif args.command == 'accessories': result = accessories(args.base,args.config,args.output)
        elif args.command == 'photo-audit': result = photo_audit(args.config)
        else: result = pack(args.config,args.output,args.max_atlas_mib)
        if getattr(args,'report',None):
            path=Path(args.report)
            # Relatórios também devem usar um destino novo.
            with path.open('x',encoding='utf-8') as f:
                json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
        print(json.dumps(result,ensure_ascii=False,indent=2))
        if args.command == 'compare' and not result['outside_preserved']:
            return 2
        return 0
    except (ValueError,KeyError,TypeError,OSError) as error:
        print(f'Erro: {error}',file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
