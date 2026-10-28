#!/usr/bin/env python3
"""Diagnóstico local sem chamadas de rede ou exposição de credenciais."""
import importlib.util,json,os,sys
from pathlib import Path

def doctor():
    root=Path(__file__).resolve().parents[1]
    modules={m:importlib.util.find_spec(m) is not None for m in ['PIL','numpy','openai']}
    required=['SKILL.md','scripts/raster_ops.py','scripts/prepare_request.py','scripts/avatar_tools.py',
        'providers/openai-imagegen/SKILL.md','providers/openai-imagegen/LICENSE.txt',
        'providers/openai-imagegen/scripts/image_gen.py','providers/openai-imagegen/references/cli.md']
    missing=[p for p in required if not (root/p).is_file()]
    return {'python':sys.version.split()[0],'python_compatible':sys.version_info>=(3,10),
        'modules':modules,'missing_files':missing,
        'local_raster_ready':modules['PIL'] and modules['numpy'] and not missing,
        'api_prerequisites_present':modules['openai'] and bool(os.getenv('OPENAI_API_KEY')),
        'api_connection_tested':False,'native_image_tool':'agent_must_check',
        'models_or_credentials_bundled':False,'network_calls':0}

if __name__=='__main__':print(json.dumps(doctor(),ensure_ascii=False,indent=2))
