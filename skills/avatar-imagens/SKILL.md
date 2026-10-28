---
name: avatar-imagens
description: Gerar avatares raster com referências de identidade, editar imagens por texto, redimensionar e reamostrar imagens, compor mudanças locais e personalizar cores e acessórios. Usar na distro de avatares hi-bit e em pedidos de geração, edição por texto, resize ou resample de um avatar.
---

# Imagens para avatares

Executar a habilidade pedida com os recursos desta pasta. Ler [condução](references/conducao.md) para iniciar um avatar novo e avaliar fotos antes da geração. Usar a folha mestra aprovada para variações. Atender qualquer gênero e idade representada, sem padrão anatômico masculino adulto.

## Verificar capacidades

Executar `python scripts/unpack_provider.py` e depois `python scripts/doctor.py` quando houver terminal. O primeiro extrai o snapshot integral já incluído em assets, sem rede. Verificar separadamente se o agente consegue ver imagens e chamar geração/edição nativa; um script local não descobre essas capacidades. Não afirmar que o pacote contém pesos do modelo, credenciais, Python ou acesso ao serviço. Não exigir uma skill de imagem instalada fora desta pasta: a implementação fornecida está em `providers/openai-imagegen/`.

## Escolher a operação

| Pedido | Procedimento integral | Implementação |
| --- | --- | --- |
| Gerar com texto e referências | [Geração](references/geracao.md) | Geração nativa; CLI fornecida como alternativa explícita |
| Editar a imagem por texto | [Edição por texto](references/edicao-texto.md) | Edição nativa ou CLI; composição local para proteção exata |
| Alterar dimensões ou encaixar no canvas | [Resize](references/resize.md) | `scripts/raster_ops.py resize` |
| Mudar a amostragem ao redimensionar | [Resample](references/resample.md) | `scripts/raster_ops.py resample` |
| Cores máscaras acessórios ou animação | [Operações complementares](references/operacoes.md) | `scripts/avatar_tools.py` |

## Preservar a identidade

Identificar imagens como folha mestra, alvo de edição, guia de gesto ou roupa. Inspecionar as imagens antes de editar. Repetir os invariantes em cada pedido. Manter os originais e produzir saídas novas. Distinguir identidade aceita, arte revisada, testes técnicos e aplicativo de destino. Uma máscara entregue ao gerador orienta a edição, mas não prova preservação exata; compor e comparar os pixels quando necessário.

## Executar geração ou edição

Preferir a ferramenta nativa quando disponível, seguindo as instruções da skill original fornecida em [imagegen integral](providers/openai-imagegen/SKILL.md). Inspecionar entradas locais antes de enviá-las à ferramenta. Solicitar transparência real e verificar o alfa. Não criar uma imagem por código como substituição da geração solicitada.

Usar a CLI incluída somente se o usuário escolher ou confirmar a rota API/CLI. Não enviar fotos à API durante diagnóstico ou dry-run. Manter a chave no ambiente, nunca na conversa ou no pacote. Ler [compatibilidade](references/compatibilidade.md): a cópia original é um snapshot; modelos e parâmetros podem mudar. Não editar o script do provedor para contornar seus limites. Validar o modelo escolhido e não trocá-lo silenciosamente.

## Executar resize e resample

Usar os scripts locais sem chamada generativa. Preferir nearest para o contrato de pixel art e para máscaras. Usar outros filtros somente em uma derivação com propósito definido. Registrar escala, deslocamento e recorte. Não afirmar ganho de detalhe. Não quantizar ou reduzir o master automaticamente. Manter âncoras e máscaras sincronizadas com a transformação.

## Preparar pedidos reproduzíveis

Usar `scripts/prepare_request.py` com um JSON de ação, instrução, papéis das imagens e invariantes. O comando valida caminhos e produz um prompt e registro para execução pela IA. Ele não chama geração. Para converter uma máscara branca editável da distro para a convenção de alfa usada pela API, usar `mask-for-api` de raster_ops. Não confundir as convenções.

## Concluir

Inspecionar o resultado em tamanho de uso, verificar alfa e arquivos e registrar a revisão visual pendente quando o usuário não avaliou. Informar se foi usada geração nativa, CLI, composição ou reamostragem. Não declarar um teste de geração real quando só houve dry-run. Entregar ao usuário explicações simples e executar os comandos por ele quando o ambiente permitir.
