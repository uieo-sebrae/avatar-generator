#!/usr/bin/env python3
"""Preparar dependências em venv local somente com --install. Não gera imagens."""
import argparse,subprocess,sys,venv
from pathlib import Path

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--install',action='store_true')
    p.add_argument('--api',action='store_true');p.add_argument('--venv',default='.avatar-env');a=p.parse_args()
    if not a.install:
        print('Sem mudanças. Use --install para criar ambiente com Pillow e NumPy; --api inclui SDK OpenAI.');raise SystemExit(0)
    dest=Path(a.venv).resolve()
    if dest.exists():p.error('Destino do ambiente já existe; use outro caminho')
    venv.EnvBuilder(with_pip=True).create(dest)
    exe=dest/('Scripts/python.exe' if sys.platform=='win32' else 'bin/python')
    packages=['Pillow>=10','numpy>=1.24']+(['openai>=2'] if a.api else [])
    subprocess.run([str(exe),'-m','pip','install',*packages],check=True)
    print('Ambiente preparado. Python:',exe)
