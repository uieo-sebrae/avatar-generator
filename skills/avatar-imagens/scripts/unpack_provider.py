#!/usr/bin/env python3
"""Extrair o snapshot integral incluído no pacote, sem rede."""
from pathlib import Path
import zipfile

def unpack():
    root=Path(__file__).resolve().parents[1]
    destination=root/'providers';destination.mkdir(exist_ok=True)
    with zipfile.ZipFile(root/'assets/imagegen-integral.zip') as z:
        for member in z.infolist():
            path=destination/member.filename
            if not path.resolve().is_relative_to(destination.resolve()):
                raise ValueError('Caminho inválido no snapshot')
            if member.is_dir():path.mkdir(parents=True,exist_ok=True);continue
            data=z.read(member)
            if path.exists():
                if path.read_bytes()!=data:raise ValueError('Snapshot local diverge; preservar e revisar antes de extrair')
            else:path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
    return destination/'openai-imagegen'

if __name__=='__main__':print(unpack())
