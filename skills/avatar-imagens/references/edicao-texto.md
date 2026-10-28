# Edição de imagem por instrução textual

## Preparar

Identificar a imagem alvo, a folha mestra e a instrução, por exemplo “trocar o sorriso por surpresa preservando cabelo e óculos”. Delimitar alterações permitidas e invariantes. Não tratar uma referência de roupa ou gesto como nova identidade. Para troca exclusivamente de cor, usar recolor em vez do gerador.

## Executar

1. Ver a imagem alvo e referências. Pedir esclarecimento apenas quando a região ou o efeito estiverem ambíguos.
2. Preparar o pedido com action edit em prepare_request.py, se útil.
3. Chamar a edição nativa com as imagens efetivamente anexadas, seguindo o módulo imagegen fornecido. Para API explicitamente escolhida, usar o subcomando edit da CLI fornecida com --image e --prompt ou --prompt-file.
4. Preservar a proposta original. Comparar identidade, câmera, anatomia, cores e alfa.
5. Se for edição local, alinhar a proposta à base e compor apenas a máscara autorizada. Não preservar uma cabeça de perspectiva incompatível por colagem.
6. Executar compare e registrar a quantidade de diferenças fora da máscara. Só declarar preservação exata se o resultado demonstrar zero alterações externas.

## Máscaras

No kit, branco significa região editável e preto significa protegida. Para máscara enviada à API de imagens, a região com alfa zero indica edição. Converter com:

```sh
python scripts/raster_ops.py mask-for-api mascara_branca_editavel.png mascara_api.png
```

A máscara do gerador orienta a edição e não garante conformidade exata. A máscara de composição local determina efetivamente quais pixels podem substituir a base. Não confundir esses dois mecanismos.

## Composição determinística

Base, proposta alinhada e máscara precisam ter o mesmo canvas. Executar:

```sh
python scripts/avatar_tools.py compose base.png proposta_alinhada.png mascara.png final.png --report composicao.json
python scripts/avatar_tools.py compare base.png final.png mascara.png --report comparacao.json
```

O primeiro comando substitui pixels na máscara e preserva o alfa da base. Para uma correção de transparência autorizada, acrescentar --allow-alpha e revisar a área. Não usar alpha-over repetidamente para substituir patches com alfa parcial.

## Saída

Original, proposta, máscara, resultado, instrução, fontes, transformações e estado de aceite. Geração de edição e composição local devem ser registradas como operações diferentes.
