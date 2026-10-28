# Resample e tratamento de alfa

Escolher o método de amostragem ao alterar dimensões. Resample não redesenha a identidade e não cria detalhe novo. Manter a fonte HD antes de qualquer derivação.

| Método | Uso |
| --- | --- |
| nearest | Pixel art e máscaras; conserva valores dos pixels amostrados |
| box | Redução por média, quando a mistura for aceitável |
| bilinear | Interpolação simples, com suavização |
| bicubic | Suavização de imagens raster contínuas |
| lanczos | Redução de imagens contínuas; revisar halos e contorno |

Para avatar hi-bit, usar nearest como padrão. Outros filtros podem modificar a linguagem visual, por isso precisam de uma derivação identificada e revisão. Não quantizar automaticamente nem chamar uma redução de ganho de fidelidade.

```sh
python scripts/raster_ops.py resample fonte.png derivacao.png --width 320 --height 640 --method nearest --mode contain --report resample.json
```

Quando o filtro mistura pixels, o script usa alfa pré-multiplicado para reduzir contaminação de RGB invisível nas bordas. Para nearest, ele amostra diretamente RGBA e evita um ciclo de pré-multiplicação que poderia arredondar cores sem necessidade.

Máscaras binárias só admitem nearest. Redimensionar uma máscara com filtro suave tornaria as bordas parcialmente selecionadas, alterando o contrato de preservação. O programa recusa essa combinação.

Inspecionar tamanho de uso e ampliação, sobre fundos claro, escuro e saturado. Conferir transparência e junções. Registrar método, canvas, escala e eventual recorte. Não substituir os originais por derivações.
