# Resize de avatar

Alterar tamanho ou encaixar num canvas usando scripts/raster_ops.py. Não usar geração de imagem para uma mudança geométrica de resolução.

## Escolher modo

- contain preserva o conteúdo inteiro, centraliza e adiciona margens transparentes quando necessário.
- cover preenche o canvas e pode cortar bordas. Usar apenas quando o recorte fizer parte do pedido e conferir cabelo, mãos e pés.
- stretch usa as duas dimensões exatas e pode deformar a aparência. Evitar no personagem completo; usar somente com intenção técnica declarada.

## Executar

```sh
python scripts/raster_ops.py resize base.png avatar_4x.png --width 1024 --height 2048 --mode contain --method nearest --report resize.json
```

Escolher as dimensões a partir da fonte real e do uso; os números acima são ilustrativos. Preferir fatores inteiros para ampliar pixel art. O relatório informa escala efetiva e deslocamento. Saída sempre PNG RGBA de 8 bits. Não sobrescrever o original. Não anunciar ganho de detalhe.

## Atualizar encaixes

Transformar coordenadas de pivôs e pontos por x novo = x antigo vezes scale_x mais offset_x, e o equivalente em y. Registrar os valores arredondados usados pelo destino. Aplicar a mesma transformação às máscaras e aos outros quadros da série. Para máscaras, usar kind mask e nearest; margens ficam pretas e protegidas.

Conferir escala, contorno, alfa, margem e integridade. Uma mudança de canvas não altera automaticamente o manifesto de uma biblioteca; atualizar todos os registros afetados.
