# Ferramentas locais

Na versão 1.2, o módulo completo de geração, edição por texto, resize e resample está em skills/avatar-imagens. Seus procedimentos são autossuficientes dentro do pacote; o motor nativo ou a API autorizada continuam necessários para geração semântica. Os exemplos abaixo permanecem válidos para as operações complementares.

Para o diagnóstico do módulo, a IA pode executar:

```sh
python skills/avatar-imagens/scripts/unpack_provider.py
python skills/avatar-imagens/scripts/doctor.py
python skills/avatar-imagens/scripts/selftest.py
```

Para preparar uma instrução de edição sem chamar geração:

```sh
python skills/avatar-imagens/scripts/prepare_request.py modelos/pedido_imagem.json pedido_preparado
```

A IA preenche os caminhos e campos antes de executar. O resultado é um pedido pronto, não uma imagem gerada. Os procedimentos de geração e edição ficam em skills/avatar-imagens/references. A CLI original integral está em skills/avatar-imagens/providers/openai-imagegen depois da extração local; seus próprios requisitos e limites precisam ser respeitados.

Requer Python 3.10 ou superior. Use um ambiente virtual. Os comandos abaixo partem da raiz da distro; no Windows substitua python por py quando necessário.

```sh
python -m venv .venv
```

Ative o ambiente conforme seu sistema: `.venv\Scripts\activate` no Windows ou `source .venv/bin/activate` em um shell compatível no macOS ou Linux. Depois execute:

```sh
python -m pip install -r tools/requirements.txt
python testes/run_selftest.py
```

## Auditar imagens

```sh
python tools/avatar_tools.py audit seu_avatar/base.png --report audit_v1.json
```

Aceita vários caminhos. Valida assinatura PNG, chunks, CRC, IEND e decodificação de todos os quadros. Informa alfa do primeiro quadro, dimensões e hashes. Não analisa o mérito artístico. A presença de algum alfa não prova que toda a silhueta foi recortada corretamente.

## Conferir uma edição localizada

```sh
python tools/avatar_tools.py compare seu_avatar/base.png seu_avatar/expressao.png seu_avatar/mascara.png --report compare_v1.json
```

Máscara branca permite mudança; preto protege. Retorna código 2 se houver diferença RGBA fora da máscara. O relatório também conta mudanças de alfa. O comando não compensa transformações; alinhe a imagem antes ou compare um recorte compensado quando houver translação.

## Recolorir sem gerar arte

Copie modelos/recolor_config.json e preencha máscaras, cores e calibração. Caminhos dentro dos JSONs são relativos à pasta do próprio JSON, não ao terminal. Cada máscara deve ser um PNG estático opaco em tons de cinza, contendo apenas 0 e 255, com o mesmo tamanho da base e pelo menos um pixel selecionado.

```sh
python tools/avatar_tools.py recolor seu_avatar/base.png modelos/recolor_config.json seu_avatar/verde_v1.png --report recolor_v1.json
```

Use apenas as partes que existem. Remova partes ausentes do JSON. Máscaras não podem se sobrepor nem selecionar pixels invisíveis. Em mode exact, todos os RGBs selecionados precisam constar no map; se faltar cor, o script recusa. Essa é a opção que mantém uma paleta discreta controlada. Em mode ramp, source_luma fixa os pontos de origem e colors fixa as cores correspondentes. O algoritmo usa luminância aproximada 0,299 R + 0,587 G + 0,114 B e interpolação por canal, com arredondamento para 8 bits. É uma escolha operacional, não um modelo colorimétrico de materiais.

A rampa preserva a organização de claro e escuro, mas pode mudar contraste e saturação; revise o resultado. O alfa é copiado integralmente. Para uma animação, use a mesma calibração de cor em todos os quadros e a máscara correspondente a cada quadro. O script processa uma imagem por comando e não gera segmentação automática.

## Compor uma expressão por máscara

Alinhe previamente base e proposta no mesmo canvas, sem redimensionar o master. A máscara seleciona os pixels da proposta que podem substituir os da base.

```sh
python tools/avatar_tools.py compose seu_avatar/base.png seu_avatar/proposta_alinhada.png seu_avatar/mascara.png seu_avatar/expressao_v1.png --report compose_v1.json
```

O comando faz substituição de pixels e mantém o alfa da base. Não usa sobreposição alpha-over. Se uma correção de transparência tiver sido autorizada, acrescente --allow-alpha; nesse caso, o alfa pode mudar somente dentro da máscara. As lentes e junções devem ser revisadas visualmente depois. O alinhamento, a perspectiva e a qualidade do desenho não são corrigidos automaticamente.

## Exportar uma sequência

Copie modelos/sequencia_config.json, preencha caminhos, durações, pivô, versão mestre e estados. Todos os PNGs precisam ter o mesmo canvas. O script não faz redimensionamento ou alinhamento automático. Ele aceita uma sequência por configuração.

```sh
python tools/avatar_tools.py pack modelos/sequencia_config.json exportacao_sul_v1
```

O diretório de destino não pode existir. Forneça de 2 a 256 quadros distintos. São produzidos PNGs normalizados em RGBA, atlas horizontal, APNG, manifesto e preview HTML autocontido. O arquivo original de cada quadro fica intacto e seu hash é registrado. O hash do PNG normalizado pode diferir do original por compressão ou metadados; os pixels decodificados são a base da comparação.

O limite conservador do atlas é 16384 px por dimensão e 256 MiB de RGBA. Isso não garante compatibilidade com todos os destinos. Divida sequências quando necessário. Durações devem ser inteiras entre 1 e 65535 ms. O pivô usa coordenadas inteiras dentro do canvas ou em sua borda. Quadros idênticos são recusados: represente pausas aumentando a duração em vez de duplicar PNGs. A ferramenta não serve para preservar repetições semanticamente diferentes com pixels iguais.

Abra preview.html e teste reprodução, pausa, quadros, fundos e leitura no tamanho de uso. O manifesto inicialmente registra browser_render como not_evaluated. Documente a conferência real no checklist; não transforme a mera geração do HTML em um teste de navegador.

## Aplicar acessórios preparados

Use modelos/acessorios_config.json. Uma camada precisa estar desenhada para a pose, vista e escala corretas. O programa não reconhece orelhas, pulsos ou roupas para encaixar sozinho. A IA deve preparar os arquivos e configurações para o usuário leigo quando tiver essas capacidades.

```sh
python tools/avatar_tools.py accessories seu_avatar/base_sem_acessorio.png modelos/acessorios_config.json seu_avatar/com_brinco_v1.png --report acessorio_v1.json
```

Cada camada contém position em pixels inteiros. A lista define a ordem de sobreposição. Uma occlusion_mask opcional, do tamanho da base, esconde o acessório nos pixels brancos, permitindo que cabelo ou outro elemento apareça na frente. Camadas podem ser desativadas com enabled false. Rode sempre a partir da base limpa para retirar uma camada opcional; um acessório já fundido ao master pode exigir reparo da área escondida.

O script aplica alpha-over apenas na área visível da camada e verifica igualdade fora dela. O alfa dessa área pode mudar porque o acessório acrescenta pixels. Não há redimensionamento, desenho ou encaixe anatômico automático. Cor de acessórios pode ser trocada com recolor, usando partes livremente nomeadas e máscaras separadas; consulte modelos/recolor_acessorios_config.json.

## Triagem técnica das fotos

```sh
python tools/avatar_tools.py photo-audit modelos/fotos_config.json --report fotos_v1.json
```

Aceita fotos estáticas que o Pillow consiga ler, como JPEG, PNG e WebP. Respeita orientação EXIF em memória e não modifica originais. Se face_bbox for informado, ele precisa usar coordenadas da imagem já orientada. O script não detecta rostos. Sem a caixa, os indicadores descrevem a imagem inteira.

O relatório registra legibilidade, dimensões e indicadores de luminosidade e textura. O aviso de rosto abaixo de 500 px e o de extremos luminosos são sinais de revisão, não requisitos do gerador ou reprovação automática. Variância do Laplaciano não tem limiar universal de foco e não recebe aprovação automática neste script. A IA precisa ver as fotos, avaliar traços e cobertura e preencher modelos/AVALIACAO_FOTOS.md antes da geração.

## Preservação e limites

Os comandos recusam sobrescrever a imagem de saída ou o diretório de exportação já existentes. Relatórios com --report também precisam de nome novo. Se um relatório falhar após a imagem ter sido gravada, a imagem pode continuar existente; confira a mensagem e use novo nome para retomar. O script não altera o master, não cria máscaras, não corrige anatomia, não determina apoio de pés e não certifica semelhança.

