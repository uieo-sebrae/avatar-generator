# Validação da versão 1 ponto 2

Data: 28 de outubro de 2026.

## Ferramentas

Dezessete grupos de testes sintéticos passaram em run_selftest.py. Os doze anteriores foram reexecutados para verificar preservação por máscaras, composição, alfa, arquivos corrompidos, atlas e APNG. Cinco grupos adicionais conferem acessórios com alfa parcial e oclusão; camadas desativadas e limites do canvas; recoloração de partes com nomes livres; orientação EXIF e recorte facial informado; fotos ausentes ou ilegíveis e revisão visual pendente.

Os testes usam imagens sintéticas, sem fotos pessoais. Não certificam anatomia, semelhança ou a qualidade de referência de uma pessoa real. Ambiente: Pillow 12.3.0 e NumPy 2.3.5.

## Condução

INICIAR_AVATAR.md especifica verificação de ferramentas, perguntas graduais, avaliação das fotos antes da geração, aceite da identidade e customização por tipo de operação. O estado do projeto tem um modelo próprio. O arquivo foi conferido como protocolo; uma criação completa conduzida por outra IA e um piloto com outra pessoa ainda não foram realizados.

## HTML

ABRA_AQUI.html substitui o manual Word. O guia tem navegação por âncoras, instruções de início, cópia da mensagem, download do protocolo e consulta técnica recolhida. O conteúdo essencial fica legível sem JavaScript e não depende de rede, fontes ou imagens externas. REFERENCIA_TECNICA.html mantém os detalhes do método para consulta.

A estrutura HTML, as âncoras, os arquivos referidos e a incorporação exata do protocolo foram verificados. A lógica dos botões foi exercitada em ambiente simulado. A renderização em navegador real permanece por conferir: não há mecanismo Chromium instalado neste ambiente. Não se declara que uma simulação comprova o layout em dispositivos reais.

## Reexecutar

Na raiz do pacote: python testes/run_selftest.py. Se houver Node.js, node testes/test_manual_logic.cjs ABRA_AQUI.html verifica a lógica do manual sem navegador. Para um preview produzido por pack, node testes/test_preview_logic.cjs caminho/preview.html verifica seus controles em DOM simulado. Abra os HTMLs no navegador de destino antes de distribuir amplamente.

## Módulo de imagem integral

Foram acrescentados dez grupos de testes: nearest com alfa parcial; contain com margens; cover com recorte; filtros com alfa pré-multiplicado; máscaras binárias; conversão de máscara para API; preservação de originais e recusa de dimensões inválidas; preparo de edição; dry-run de geração e edição na CLI original; e diagnóstico sem rede. Somados aos dezessete anteriores, são 27 grupos. Não houve geração real nem teste de conexão autenticada à API.

Um agente independente usou a skill para preparar imagem e máscara em 240 por 240, com contain e nearest, conferindo escala 2x e deslocamento 40,0, igualdade dos blocos 2x2, alfa e margens. O relatório bruto está em validacao_resize_independente.json.

Cada arquivo do snapshot imagegen foi comparado por bytes com a fonte local. O manifesto registra os hashes. Os procedimentos e scripts estão fornecidos integralmente; Python, bibliotecas, modelos e credenciais são dependências de execução.
