# Operação de máscaras e calibração de cores

Este roteiro complementa o manual para quem prepara as imagens em um editor raster. Ele não depende de um programa específico.

## Criar uma máscara de peça

1. Abra o PNG final da pose sem alterar seu tamanho. Guarde o original.
2. Crie uma camada auxiliar com exatamente as mesmas dimensões, preenchida de preto opaco.
3. Na imagem do avatar, selecione o tecido da peça desejada. Seleção por cor pode ajudar no início, mas precisa de revisão manual.
4. Preencha de branco a área correspondente na camada auxiliar. Use borda dura, sem suavização, e valores 0 ou 255.
5. Retire da seleção a pele, o cabelo, o relógio, os óculos, a fivela, botões e qualquer detalhe de cor fixa.
6. Decida se o contorno da roupa deve manter a cor. Em geral, deixe o contorno fixo fora da máscara para evitar perda de leitura; documente qualquer outra escolha.
7. Remova da máscara os pixels em que o alfa do avatar é zero. Preserve pixels de borda com alfa parcial se eles realmente pertencem à peça.
8. Visualize a seleção como uma sobreposição colorida temporária sobre o avatar. Amplie mãos, gola, cintura, mangas e junções.
9. Exporte a máscara como PNG em tons de cinza opaco, sem cortar margens. O branco seleciona e o preto protege.
10. Faça o mesmo para cada peça, sem sobreposição entre máscaras. Uma peça escondida nessa pose não precisa de máscara vazia no JSON; retire-a da configuração.
11. Teste uma troca de cor bem diferente para revelar vazamentos. Aplique também uma comparação de pixels.
12. Revise o conjunto no tamanho de uso. Guarde máscara, configuração e hash ligados à versão exata da pose.

Uma máscara de manga com o braço baixo não serve automaticamente para um braço levantado. Cada quadro exige sua própria máscara ou uma transformação de máscara registrada e depois revisada. Escalar o canvas muda também as coordenadas das máscaras.

## Escolher o método de recoloração

Use exact quando os pixels selecionados tiverem uma paleta pequena e intencional. Liste todos os RGBs da peça e associe cada um à sua cor de destino. Guarde a ordem perceptiva entre sombra, base e luz. O código recusa uma seleção com cores não mapeadas para evitar uma troca parcial silenciosa.

Use ramp quando houver muitos tons e o remapeamento exato for impraticável. Observe os tons escuros, médios e claros da mesma roupa em várias poses e escolha pontos fixos de luminância. O arquivo de exemplo usa três pontos ilustrativos, que precisam ser substituídos pelos valores do novo avatar.

Não faça uma calibração independente por quadro. A mesma cor de origem deve receber o mesmo tratamento ao longo da animação. Se a iluminação mudar de modo intencional, crie outro perfil documentado em vez de ajustar silenciosamente cada quadro.

## Máscara para expressão ou reparo

Para compose, delimite a área da boca, dos olhos ou do reparo. A proposta deve estar alinhada no mesmo canvas antes da operação. Substitua a região inteira selecionada, com uma margem de transição coerente com a textura. Evite uma caixa que inclua o nariz ou o contorno facial sem necessidade.

Se a máscara for apenas um retângulo muito grande, o teste pode passar mesmo com um rosto indevidamente alterado dentro dele. Escolher a região correta faz parte da revisão visual. O código só protege o que a máscara efetivamente deixa de fora.

