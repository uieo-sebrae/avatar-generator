# Metodologia para criar avatares hi bit

Autoria da metodologia e da documentação da distro: **Felipe Cruz de Melo**.

Manual de produção e distribuição • Versão 1.2 • 28 de outubro de 2026

Esta metodologia permite transformar referências reais de uma pessoa em um avatar hi-bit consistente, personalizável e preparado para animação em diferentes aplicações. Ela reúne direção visual, geração de imagens, composição por máscaras, troca de cores e verificação técnica. O resultado esperado é uma biblioteca de versões do mesmo personagem com origem, limites e estado de aprovação conhecidos.

O trabalho começa pela validação humana de uma folha mestra. A geração de imagens propõe novas representações; a edição localizada e a composição por código preservam o que já foi aceito. Nenhum prompt, medição ou teste de arquivo substitui o reconhecimento da pessoa pelo titular do avatar.

O escopo abrange identidade, vistas, expressões, fala visual, poses, roupas, acessórios usados no corpo, personalização e movimentos. Cenários, objetos independentes, tokens, itens, interfaces e peças de jogo ficam fora da distro. As aplicações de destino podem usar os PNGs e as animações, mas suas regras e conteúdos não fazem parte deste manual.

## Como usar esta distro

Para o usuário, o ponto de entrada é ABRA_AQUI.html. Ao receber o ZIP ou INICIAR_AVATAR.md com o pedido de início, a IA conduz as perguntas, a avaliação das fotos e a geração, preenchendo os registros conforme as respostas. As seções seguintes são consulta técnica para a IA ou operador; o leigo não precisa estudá-las para começar. Se faltar uma ferramenta, a IA informa a limitação na etapa correspondente.

Os arquivos de prompts são instruções portáveis para uma conversa com uma IA que gere e edite imagens. Não instalam uma skill nem garantem acesso a ferramentas em outra conta. O kit de código funciona localmente e realiza somente operações determinísticas sobre imagens fornecidas.

### Mapa de leitura

| Seção | Decisão ou execução |
| --- | --- |
| 1 a 3 | Evidência, ferramentas e responsabilidades |
| 4 a 7 | Fotos, identidade, folha mestra e regras de fidelidade |
| 8 a 10 | Geração, expressões e poses |
| 11 a 12 | Roupas, cores e acessórios |
| 13 a 15 | Animação e exportação |
| 16 a 18 | Qualidade, reparos e distribuição |
| 19 a 21 | Replicação, ferramentas e limites |
| Anexos | Fontes, decisões e glossário |

## 1 Origem e força das evidências

Esta versão se baseia na leitura dos documentos, manifestos e scripts dos onze ZIPs fornecidos no projeto Avatar para gamificação, na inspeção das principais pranchas e nas instruções disponíveis para geração de imagem. Não corresponde a uma nova auditoria integral de todos os quadros antigos. Os estados históricos abaixo reproduzem os registros dos pacotes, com as ressalvas neles documentadas.

O início realizado no Claude é conhecido pelo relato do titular: várias fotos reais foram usadas para definir e validar a folha mestra do personagem. As instruções exatas, a seleção original das fotos e todas as iterações dessa conversa não estão disponíveis. A etapa de entrada deste manual é, portanto, uma reconstrução operacional proposta para reproduzir esse objetivo. Ela pode ser executada em outra ferramenta que aceite referências e edição de imagens.

Três categorias orientam a leitura. Uma prática observada consta dos arquivos do projeto. Uma recomendação da distro generaliza essa prática para novos avatares. Um parâmetro ilustrativo demonstra uma configuração e precisa ser calibrado. Os números de Felipe não são padrões anatômicos para outras pessoas.

### Lições verificáveis no acervo

| Registro do projeto | Consequência para o processo replicável |
| --- | --- |
| Onda 1 e pranchas fiéis mantidas como origem da identidade | Uma geração nova não redefine o rosto automaticamente |
| Lote 01 preserva regiões fora das máscaras faciais | Usar composição localizada quando a base já está aceita |
| Lente externa corrigida em revisão posterior | Testar transparência também em áreas internas e acessórios |
| Lotes 02 e 03 distinguem arte nova de aprovação visual | Registrar aceite artístico separado da verificação técnica |
| Lote 04 revisa rigidez de cabeça e ombros | Preservar o rosto não exige mantê-lo imóvel no canvas |
| Lote 05 registra reconstrução e correção de lateralidade | Registrar fontes, transformações e exceções por quadro |

Uma proposta antiga sugeria reduzir a cabeça a 114 px e quantizar 40 cores. Os critérios posteriores do lote 01 orientam preservar o HD disponível e não aplicar essa redução automaticamente. A proposta de fidelidade também registra proporções medidas diferentes da ficha inicial. Esta distro preserva o original, calibra proporções na arte aprovada e trata redução e quantização como derivações opcionais.

## 2 Princípios de produção

A identidade tem uma origem explícita. Antes da estilização, as fotos e a declaração do titular orientam a aparência. Depois do aceite, a folha mestra assinada visualmente define a tradução gráfica. Fotos continuam úteis para resolver dúvidas, mas uma nova pose deve seguir a identidade estilizada já aprovada. Se houver conflito entre foto e estilização, interrompa a expansão e registre qual decisão o titular quer preservar.

A produção usa uma base operacional por enquadramento e direção. Uma base HD aprovada pode facilitar o encaixe, sem substituir a origem da identidade. Mantenha a folha mestra disponível durante a revisão de cada lote; depender apenas da última geração acumula desvios.

Separe quatro classes de mudança. Identidade envolve características reconhecíveis. Estilo envolve linguagem visual, textura e iluminação. Personalização envolve roupa e acessórios. Atuação envolve gesto, expressão e movimento. Definir uma classe não autoriza modificar as demais.

Mudanças pequenas devem afetar regiões pequenas. Uma boca nova em um busto aceito pode ser proposta pelo gerador e montada somente na região autorizada. Trocar azul por verde em uma camisa deve usar uma máscara da camisa, sem nova geração. Uma manga curta, porém, muda a silhueta e pede outra geometria, seguida de revisão.

### Responsabilidades mínimas

| Papel | Responsabilidade |
| --- | --- |
| Titular do avatar | Selecionar referências e aprovar semelhança e personalizações |
| Direção visual | Definir estilo e conferir coerência entre vistas e expressões |
| Operação de imagem | Gerar propostas e registrar fontes e instruções |
| Preparação técnica | Compor, mascarar, alinhar, exportar e testar arquivos |

Uma pessoa pode acumular papéis. O importante é registrar qual avaliação foi feita. A frase “os arquivos passaram nos testes” não equivale a “o titular aprovou o rosto”.

## 3 Ferramentas e condições de execução

O percurso básico exige uma interface que receba várias imagens, gere e edite imagens, uma forma de visualizar PNGs com transparência e uma pasta para registrar referências e aprovações. Para máscaras e camadas, use um editor que permita selecionar regiões e exportar PNG sem alterar dimensões. Para automação local, o kit requer Python 3.10 ou superior, Pillow e NumPy.

No ChatGPT Work, use a geração integrada de imagens para propor arte e edições. O módulo de imagem está integralmente fornecido em skills/avatar-imagens. Ler seu SKILL.md e os procedimentos de geração, edição por texto, resize e resample. Não é necessária uma skill externa; a geração ainda exige motor nativo da IA ou acesso autorizado à API. Uma máscara mencionada no prompt é uma orientação semântica; ela não comprova que os pixels externos foram preservados. A garantia técnica de preservação exige comparar arquivos e, quando necessário, compor efetivamente a alteração por máscara.

Os prompts deste kit não dependem de um nome específico de modelo. Parâmetros de API, tamanhos, suporte a transparência e disponibilidade de ferramentas variam. Antes de automatizar uma API, confirme na documentação do provedor os parâmetros do modelo escolhido e faça um teste pequeno. Instruções como qualidade e fidelidade no texto do prompt não se tornam parâmetros técnicos automaticamente.

A documentação oficial da OpenAI reconhece limitações de consistência e de posicionamento preciso e orienta verificar referências e transparência na saída [E1, E2]. Por isso, a distro acrescenta revisão visual e composição determinística. Não há promessa de reproduzir exatamente a mesma geração a partir do mesmo prompt.

Registre a interface, a data, o modelo quando ele for exposto, as imagens anexadas e a instrução final usada. Se a interface não revelar o modelo, registre “não informado”. Nunca preencha metadados por suposição. A recriação de uma geração artística é diferente da reconstrução de uma composição a partir de fontes já guardadas.

## 4 Preparação das referências reais

Para começar o busto, reúna de quatro a seis fotos atuais de frente, sorriso e três quartos. Um acervo ampliado de seis a doze fotos pode atender corpo e outras vistas nas etapas seguintes. Esses intervalos são recomendações e não exigências do gerador. Mais fotos conflitantes podem atrapalhar. Não há necessidade de copiar documentos pessoais ou enviar informações sem relação com a aparência.

### Conjunto de entrada sugerido

| Referência | Quantidade sugerida | Informação principal |
| --- | --- | --- |
| Rosto frontal neutro e sorrindo | 2 | Formato, proporções e sorriso |
| Rosto em três quartos de ambos os lados | 2 | Volume, nariz, mandíbula e cabelo |
| Perfis de ambos os lados | 2 | Silhueta e assimetrias |
| Corpo inteiro de frente e costas | 2 | Postura, proporção e roupa |
| Detalhes pertinentes | 0 a 4 | Óculos, cabelo, acessórios e mãos |

Prefira luz difusa, foco no rosto, ausência de filtros e distância que evite distorção de grande angular. Como ponto de partida, procure fotos em que o rosto tenha ao menos cerca de 500 px de altura; é uma recomendação de legibilidade, não um limite técnico. Preserve os originais e a orientação correta, especialmente em selfies que possam estar espelhadas.

Nomeie as fotos como F01, F02 e assim por diante. Indique data aproximada, vista, expressão, lado anatômico visível e finalidade. Se algumas imagens mostram barba, cabelo ou óculos antigos, marque-as como históricas. O titular deve escolher a aparência atual desejada, sem pedir que a IA faça uma média entre épocas diferentes.

Antes de gerar, peça uma leitura descritiva dos traços visuais relevantes e confira com o titular. Não use a imagem para inferir etnia, saúde, personalidade ou outras características que não sejam necessárias à representação. Confirme explicitamente o lado de relógio, brincos, tatuagens e outros detalhes assimétricos.

Antes da geração, a IA deve preencher modelos/AVALIACAO_FOTOS.md. Cada foto recebe usar, usar com ressalva ou substituir, com motivo sobre foco, luz, cor, filtro, cortes e partes escondidas. O conjunto precisa ser suficiente para a próxima saída; lacunas pedem fotos complementares. photo-audit auxilia com leitura, orientação EXIF, dimensão e indicadores de textura ou iluminação, sem detectar rostos ou certificar traços.

Ao distribuir o método, entregue os modelos vazios. Fotos de uma pessoa e suas autorizações pertencem ao projeto individual. Esta distro não redistribui fotos nem imagens do avatar Felipe.

## 5 Briefing e ficha da identidade

Preencha modelos/BRIEFING.md e modelos/FICHA_IDENTIDADE.md. O briefing registra o uso previsto, a intensidade da estilização e as entregas iniciais. A ficha registra o que torna o personagem reconhecível e quais mudanças foram autorizadas. Uma boa ficha descreve o que se vê, em vez de depender de adjetivos como bonito ou simpático.

Para cada traço, anote sua forma, posição relativa, cor observada e comportamento em outras vistas. “Cabelo castanho curto” é insuficiente se o reconhecimento depende de volume no topo, risca lateral e entradas específicas. Em óculos, registre formato, espessura da armação, visibilidade das hastes e tratamento das lentes.

### Classes de atributos

| Classe | Exemplos | Regra de alteração |
| --- | --- | --- |
| Identidade fixa | Silhueta facial, implantação do cabelo, proporções reconhecíveis | Novo aceite de identidade |
| Aparência versionada | Corte de cabelo, barba, óculos característicos | Versão alternativa explicitamente aprovada |
| Roupa | Modelo, comprimento, material e cores | Aceite da roupa; cores podem usar máscaras |
| Acessório opcional | Chapéu, brinco, relógio, colar | Definir lado, escala, oclusão e compatibilidade |
| Atuação | Boca, sobrancelha, olhar, gesto | Preservar estrutura e coerência anatômica |

Não imponha ao novo avatar os traços de Felipe. A metodologia deve servir a pessoas de diferentes idades, tons de pele, corpos e apresentações. Particularidades como barba e óculos só entram se forem pertinentes ao personagem em questão. O método atende homens, mulheres e pessoas de qualquer gênero ou idade representada. A idade e a aparência desejadas são informadas pelo usuário. Não se inferem identidade de gênero pelas fotos nem se adota uma anatomia adulta como padrão para crianças; pessoas idosas também devem manter os traços escolhidos, sem rejuvenescimento automático.

Defina também o contrato de estilo: pixel art hi-bit, densidade visual, tipos de contorno, rampas de sombra, fonte de luz, tamanho dos olhos e grau de simplificação. Hi-bit designa aqui uma aparência de pixel art com mais detalhe e cores que estilos de baixa resolução; não é um formato de arquivo nem uma resolução universal. Um PNG grande pode conter ilustração lisa. O acabamento precisa ser visto no tamanho real de uso.

## 6 Construção e validação da folha mestra

Esta seção reconstrói a etapa inicial feita fora deste ambiente. Use prompts/01_FOTOS_E_DIAGNOSTICO.md e prompts/02_FOLHA_MESTRA.md. Comece com um busto neutro em três quartos, suficiente para discutir cabelo, olhos, nariz, boca, contorno facial e acessórios característicos. Proponha poucas alternativas comparáveis e peça que o titular aponte diferenças concretas. Evite produzir uma biblioteca inteira antes de acertar esse núcleo.

Após aceitar o rosto, produza corpo inteiro frontal com roupa simples e confira a relação entre cabeça, tronco, membros e postura. O estilo pode exagerar proporções, desde que isso seja uma escolha aprovada. Não copie automaticamente razões antigas como 1 para 6 ou 1 para 4,2. Registre os pontos usados na medição; topo do cabelo até gola é diferente de topo do crânio até queixo.

### Conteúdo mínimo da folha mestra

| Grupo | Conteúdo a validar |
| --- | --- |
| Identidade | Busto neutro e sorriso discreto em vista principal |
| Vistas | Frente, três quartos, perfis e costas com lados identificados |
| Corpo | Corpo inteiro na roupa base e proporções aceitas |
| Expressões | Neutro, sorriso, fala, surpresa, pensativo e sério |
| Especificação | Cores amostradas, iluminação, lateralidade e invariantes |

Produza e revise vistas individualmente, quando a geração conjunta provocar deriva. Monte a prancha por composição dos arquivos escolhidos. Uma prancha de apresentação pode ter rótulos adicionados por código ou editor; os recortes de produção devem permanecer sem rótulos, textos ou elementos de fundo.

O titular confere a folha em tamanho de uso e ampliada. Registre o aceite com data, versão, nomes e SHA-256 dos arquivos. Uma observação como “rosto aprovado, corpo pendente” deve permanecer parcial. Quando tudo estiver aceito, congele a versão mestre e guarde uma cópia sem edições.

Uma folha bonita que mostra rostos diferentes entre vistas não está pronta. Corrija a vista divergente usando o núcleo aprovado. Uma mudança posterior de identidade requer uma nova versão mestre e uma avaliação do impacto nos materiais derivados.

## 7 Contrato de fidelidade e medidas

As referências têm funções distintas. A folha mestra define a identidade estilizada; a base operacional define o encaixe de uma série; a imagem de gesto define a atuação; a amostra de roupa define a personalização. Rotule cada anexo no prompt para que um guia de pose não seja interpretado como novo rosto.

Escreva um bloco fixo de identidade com descrições curtas dos traços decisivos. Reutilize esse bloco a cada solicitação, junto da referência visual. Acrescente apenas o que muda na tarefa atual. Se uma descrição antiga divergir da arte aprovada, corrija a ficha e registre a decisão antes de continuar.

### Medições úteis por enquadramento

| Medida | Como registrar | Uso |
| --- | --- | --- |
| Cabeça | Largura e altura com marcos definidos | Detectar alteração de volume |
| Face | Linhas dos olhos, nariz e boca em proporção da cabeça | Comparar a mesma vista |
| Corpo | Ombros, cintura e altura em relação à cabeça | Conferir escala e proporção |
| Acessórios | Lado anatômico e relação com marcos locais | Evitar inversões e mudanças de tamanho |
| Acabamento | Escala aparente dos blocos e rampas de cor | Detectar mudança de linguagem visual |

Meça primeiro as referências aceitas e só depois defina faixas. Como ponto inicial proposto, uma variação de até 5% em uma razão geométrica comparável pode gerar uma revisão, não uma aprovação automática. A tolerância real depende da vista, da expressão e da liberdade artística contratada. Valores não comparáveis devem ficar como “não aplicável”.

Classificação automática por cor é particularmente frágil quando cabelo, roupa e armação compartilham tons. O projeto antigo chegou a excluir métricas instáveis. Medições ajudam a encontrar diferenças e não certificam que se trata da mesma pessoa. Expressões extremas e mudanças de câmera exigem critérios próprios.

Na edição localizada, o teste mais forte é a igualdade RGBA fora da máscara. Se a cabeça só se desloca, compare-a depois de compensar a translação registrada. Não aplique esse teste a uma cabeça que deveria girar: uma rotação muda o que está visível e exige uma referência adequada à nova vista.

### Registro geométrico antes da composição

Escolha marcos visíveis equivalentes na base e na proposta, como topo do cabelo, centro entre os olhos e início da gola. Estime a escala uniforme pela razão entre as distâncias correspondentes. Depois calcule a translação necessária para sobrepor o marco principal. Confira os demais marcos; se eles não se encaixarem, há mudança de perspectiva ou deformação e a proposta precisa de revisão. Não force o alinhamento esticando o rosto em eixos diferentes.

Reamostre apenas a proposta que será encaixada, mantendo o master intacto. Use vizinho mais próximo quando o contrato de pixel art exigir e confira serrilhados, perda de detalhe e emendas. Se a alteração puder usar translação inteira sem escala, preserve os pixels dessa forma. Registre escala, deslocamento, recorte e método de amostragem. A operação não cria detalhe.

Em uma máscara binária, o resultado copia a proposta nos pixels brancos e mantém a base nos pretos. Para expressões, o alfa da base pode ser copiado integralmente. Uma correção de silhueta ou de lente exige autorização para mudar também o alfa na região correspondente. O comando compose do kit executa essa substituição quando as imagens já estão alinhadas.

## 8 Produção de novas imagens

Para cada tarefa, escolha uma única saída principal: uma pose, uma expressão, uma vista ou um quadro. Pranchas conceituais ajudam a planejar, mas recortar uma prancha grande e ampliá-la não cria detalhe novo. Para qualidade individual, prefira gerar a peça com enquadramento e espaço suficientes, preservando o arquivo original recebido.

Anexe a folha mestra, a base operacional e, se necessário, um guia de gesto. Explique o papel de cada imagem. O prompt deve declarar identidade, vista, enquadramento, roupa, atuação, luz, tratamento das bordas, transparência e alterações permitidas. Use prompts/03_VARIACAO_CONTROLADA.md como base.

### Ciclo de geração e revisão

1. Defina a diferença pretendida e as regiões que podem mudar.
2. Gere ou edite uma proposta com as referências corretas.
3. Compare com a folha mestra e a base; avalie rosto, proporção, mãos e acessórios.
4. Se o problema for local, peça somente o reparo local e preserve a versão anterior.
5. Se o gerador alterar outras áreas, componha a parte útil por máscara ou descarte a proposta.
6. Registre a fonte selecionada, o preparo aplicado e o estado de revisão.

Quando for necessário mudar câmera ou silhueta, permita alterações correspondentes em vez de exigir igualdade impossível de pixels. A direção visual decide se uma nova cabeça é necessária; a base operacional não deve ser colada sobre uma perspectiva incompatível.

Defina um limite de tentativas por lote para detectar quando a abordagem falhou. Como recomendação operacional, após três tentativas com o mesmo desvio, volte ao briefing, ao enquadramento ou à base em vez de repetir o mesmo prompt. Esse número não é uma regra do gerador.

Peça fundo realmente transparente. Um quadriculado desenhado não é transparência. Confira o canal alfa e visualize a imagem sobre fundos claro, escuro e saturado. Tratamentos de limpeza devem preservar as bordas e nunca transformar automaticamente lentes, pele ou reflexos em buracos.

## 9 Expressões e fala visual

Produza expressões sobre uma base estável. Separe boca, olhos e sobrancelhas em regiões de edição quando possível. A máscara da boca pode incluir uma pequena transição de pele, barba ou bigode; não deve alcançar nariz, queixo ou silhueta facial sem necessidade declarada. A anatomia e a intensidade emocional precisam ser conferidas depois da composição.

Para montar uma variante, alinhe a proposta ao mesmo canvas da base, delimite a região autorizada e substitua os pixels dessa região. Máscaras binárias preservam a aparência de pixel art. Máscaras suaves podem ser úteis em alguns estilos, mas devem ser aprovadas porque introduzem mistura de cores. Sempre compare a imagem final, não apenas a intenção do prompt.

No projeto Felipe, seis formas de fala foram preparadas sobre o mesmo busto: fechada M B P, A, E I, O U, F V e L. Esse agrupamento é um repertório visual simplificado e não constitui um sistema fonético completo. F V e L exigem avaliação de leitura; nem todos os sons de uma língua são distinguidos apenas pela boca.

### Progressão recomendada

| Nível | Entrega | Condição para avançar |
| --- | --- | --- |
| Expressões estáticas | Neutro, sorriso, sério, surpresa e pensativo | Semelhança e intensidade aceitas |
| Piscar | Aberto, intermediário se necessário e fechado | Pálpebras coerentes, sem salto de rosto |
| Fala demonstrativa | Sequência de bocas sem áudio | Identificada como demonstração |
| Fala sincronizada | Áudio, tempos e associação de bocas | Conferência audiovisual na língua alvo |

Não chame uma sequência repetida de bocas de sincronização labial. Para sincronizar, é necessário fornecer áudio ou marcação temporal, idioma, duração e um critério de revisão. Um conjunto de PNGs também não é um rig facial.

Ao reutilizar patches com alfa parcial, limpe a área de destino e substitua o recorte, ou faça substituição de pixels em um editor apropriado. Desenhar o patch repetidamente por cima pode aumentar a opacidade de lentes e bordas. Guarde base, proposta, máscara, posição e resultado para reconstrução.

## 10 Poses e reações expressivas

Comece com poses que preservem a leitura da pessoa: repouso, aceno, apontar, apresentar, joinha, explicar, braços cruzados e comemorar. A quantidade é modular. Uma primeira biblioteca pequena e aprovada vale mais como referência que dezenas de propostas divergentes.

Descreva o gesto em termos concretos: braço que atua, mão de apoio, direção do olhar e enquadramento. “Apontar à esquerda” deve indicar a esquerda do observador; “relógio no pulso esquerdo” indica o lado anatômico do personagem. Use os dois referenciais explicitamente.

Gere poses opostas individualmente quando houver assimetrias de rosto, cabelo ou acessórios. Espelhamento pode ser um recurso de composição se houver autorização e correção dos elementos assimétricos. No lote 05 de Felipe, o leste foi refeito a partir do corpo oeste espelhado, preservando a cabeça leste e corrigindo o relógio; essa exceção exigiu fontes, máscaras e receita de reconstrução.

### Revisão de uma pose

- Confira dedos visíveis, polegares, articulações e sobreposição de braços.
- Verifique se mangas, gola, botões e acessórios acompanham o gesto.
- Confira se o recorte inclui mão, cabelo e detalhes necessários à leitura.
- Compare tamanho e ângulo da cabeça com a referência apropriada.
- Avalie a expressão em relação ao gesto, em tamanho de uso.

Reações como facepalm, dar de ombros, incredulidade e comemoração podem ampliar o repertório. Referências de memes como This is fine, Turn down for what, Mind blown, I give up e Drake devem orientar apenas a atuação corporal e facial solicitada. O avatar continua isolado, sem cenário, texto, fogo, objetos ou efeitos independentes nesta distro.

Não copie a identidade do personagem do meme. Descreva a intenção, o gesto e a expressão a serem reinterpretados pelo avatar validado. Se a pose esconder o rosto, preserve cabelo, silhueta, acessórios e roupa; a reconhecibilidade pode depender dessas pistas.

## 11 Guarda roupa e troca de cores

Separe mudanças de cor de mudanças de geometria. Camisa azul e camisa verde com o mesmo corte podem compartilhar uma base. Camisa social e polo possuem gola, botões, mangas e dobras diferentes e precisam de versões geométricas próprias. Cada versão deve manter a identidade e receber suas próprias máscaras nas poses necessárias.

O projeto trouxe uma prova de conceito que identifica azuis e cinzas por regras de cor. Esse método serve para experimentar, mas pode recolorir óculos, sombras, pele ou acessórios que compartilhem tons. Para produção, use máscaras semânticas revisadas por peça e por quadro.

### Máscaras mínimas de personalização

| Região | Deve incluir | Deve excluir |
| --- | --- | --- |
| Camisa ou polo | Tecido e suas sombras | Pele, relógio, botões e frisos preservados |
| Calça | Tecido e suas sombras | Mãos, cinto e calçados |
| Cinto | Correia | Fivela, camisa e pele |
| Sapatos | Material definido para troca | Calça, solado ou detalhes preservados |

Defina branco como região editável e preto como protegida. O kit usa máscara PNG em tons de cinza com valores somente 0 e 255, no mesmo tamanho do arquivo. Regiões editáveis de peças diferentes não podem se sobrepor. Pixels totalmente transparentes não devem ser selecionados.

A troca deve preservar RGBA fora da união das máscaras e preservar o alfa em toda a imagem. Para pixel art com paleta controlada, mapeie cada cor de origem para uma cor de destino correspondente. Para fontes com muitos tons, use uma rampa calibrada de sombra, base e luz, com os mesmos pontos de luminância em toda a série. Calcular percentis novos a cada quadro pode criar oscilação de cor durante o movimento.

Não trate a cor HEX escolhida como a média obrigatória do tecido renderizado. A luz e a sombra modificam a aparência. Aprove a rampa completa em fundos diferentes e na animação. Mudança para tecido branco, preto ou muito saturado exige conferir separação de volumes e contorno.

O script tools/avatar_tools.py recolor implementa remapeamento exato e rampa compartilhada. Ele não encontra automaticamente as peças nem cria máscaras. É uma generalização técnica incluída nesta distro, testada com imagens sintéticas; precisa das máscaras e cores calibradas do novo avatar.

## 12 Acessórios e personalizações estruturais

Considere acessórios usados no corpo, como óculos, relógio, brincos, chapéu e colar. Defina quais fazem parte da identidade e quais são opcionais. Óculos característicos podem exigir nova versão de identidade ao serem removidos; um chapéu opcional pode ser apenas uma variante de aparência.

Para cada acessório, registre dimensões relativas, lado anatômico, ponto de encaixe, partes que ficam na frente ou atrás e vistas em que ele se torna invisível. O comando accessories aplica camadas preparadas, em ordem, com posição inteira e máscara opcional de oclusão. Ele verifica preservação fora da área visível da camada; não desenha nem encaixa anatomicamente o acessório. A cor pode usar recolor com uma máscara específica, inclusive de armação ou brinco. Para retirar uma camada opcional, volte à base sem ela. A remoção de um item fundido à base pode exigir reparar a região escondida. A simples translação de um PNG frontal não resolve uma vista lateral. São necessárias vistas próprias ou uma composição compatível com a perspectiva.

### Regras de encaixe e oclusão

| Situação | Tratamento |
| --- | --- |
| Óculos com lente além da silhueta do rosto | Conferir alfa da parte externa sem apagar armação e reflexos |
| Relógio no braço distante | Respeitar a parte visível e a oclusão pelo corpo |
| Chapéu sobre cabelo | Definir cobertura e preservar o cabelo original no arquivo base |
| Brinco em um único lado | Manter lateralidade ao trocar a vista |
| Manga sobre pulseira | Resolver ordem de camadas na pose correspondente |

As lentes exigem cuidado: lente sobre o rosto deve permitir a leitura da face; lente que ultrapassa a silhueta pode expor o fundo com alfa parcial ou total, conforme o estilo aprovado. No avatar Felipe, uma correção específica tornou transparente a área externa escolhida. Essa decisão não deve ser aplicada como preenchimento ou apagamento universal em outros avatares.

Guarde as variantes com e sem acessório quando isso fizer parte do briefing. Registre incompatibilidades, como chapéu que não serve em um penteado alternativo ou relógio oculto por manga longa. Uma configuração só está disponível quando seus arquivos e encaixes foram produzidos e verificados.

Customizações que mudam cabelo, barba ou silhueta facial devem ser apresentadas ao titular como versões de aparência, com nova aprovação visual. Não afirme que uma máscara de roupa permite qualquer transformação de identidade.

## 13 Preparação para animação

Um avatar animável precisa de continuidade entre quadros, canvas comum, ponto de ancoragem, fases e durações. A existência de poses diferentes não constitui uma animação pronta. Defina previamente câmera, direções, enquadramento e movimento desejado, sem depender de uma mecânica de jogo.

Para um repertório polivalente, a sequência sugerida é piscar e fala demonstrativa em busto, respiração ou repouso em corpo inteiro, aceno e caminhada. Outros movimentos podem ser acrescentados conforme a aplicação. Quedas, saltos e corridas não são requisitos universais.

### Contrato técnico de uma sequência

| Campo | Definição |
| --- | --- |
| Canvas | Mesma largura e altura em todos os quadros |
| Origem | Canto superior esquerdo, x cresce à direita e y para baixo |
| Pivô | Ponto lógico comum, como centro de apoio entre os pés |
| Direção | Sul frontal, norte costas, oeste esquerda e leste direita nesta convenção |
| Fase | Pose e apoio identificados em cada quadro |
| Duração | Tempo individual em milissegundos |
| Movimento | No lugar ou com deslocamento de raiz declarado |
| Loop | Relação entre último e primeiro quadro |

As coordenadas do kit são inteiras, com retângulos no formato x, y, largura, altura. As caixas de recorte seguem limites superiores exclusivos. Um contato inferior definido em y=1488 significa último pixel em y=1487, caso a convenção seja limite exclusivo. Especifique a convenção em vez de usar “pé em 1488” de modo ambíguo.

Escolha a dimensão pelo maior alcance da sequência e uma margem de segurança. Não recorte automaticamente cada quadro pela silhueta: isso muda o enquadramento e causa saltos. Um busto pode usar uma âncora no tronco; um corpo inteiro pode usar o apoio dos pés. O pivô não precisa ser um pixel visível em todos os quadros, especialmente em movimentos com fase aérea.

Se houver várias direções, valide primeiro as bases estáticas sob a mesma câmera. Normalizar altura e pés por código não corrige perspectiva ou anatomia incompatíveis. Trate cada vista como uma representação coerente da mesma pessoa.

## 14 Construção dos ciclos de movimento

Planeje as fases antes de gerar. Uma caminhada de oito quadros pode distribuir contato, apoio, passagem e alcance nas duas metades do ciclo. Essa organização foi usada nos pacotes, mas os nomes das fases não provam que a anatomia esteja correta. O pé de apoio, a trajetória e as sobreposições devem ser vistos em sequência.

Comece pela direção que permita avaliar melhor o movimento. No projeto, o sul foi refinado e aprovado antes da consolidação das quatro direções. Use uma base por direção, guias de fase e, quando necessário, propostas individuais. A ordem final deve seguir o movimento observado, não necessariamente a ordem em que os arquivos foram gerados.

Preserve a cabeça por composição quando a orientação for compatível. Deixe-a acompanhar o movimento com translações inteiras. O tronco e os ombros podem receber articulação ou deformação controlada. Confira a junção do pescoço e da gola; mistura de duas camisas pode duplicar botões ou criar uma faixa semitransparente.

### Parâmetros do caso Felipe e sua interpretação

| Registro histórico | Interpretação replicável |
| --- | --- |
| Oito quadros por direção, 125 ms cada | Ciclo de 1 s a 8 quadros por segundo |
| Canvas final 960 por 1568 px e pivô 480,1488 | Configuração do lote 05, sem valor universal |
| Cabeça com balanço vertical de menos 12 a mais 12 px | Ajuste artístico proporcional à escala daquela fonte |
| Sul preservado com margem lateral adicionada | Alterar canvas não exige redimensionar o desenho |
| Leste derivado do oeste com correções locais | Espelhamento exige tratar assimetrias e revisar |

Os ciclos norte, oeste e leste constam como estudos sujeitos à revisão visual no lote 05; o sul da revisão 02 do lote 04 tem aceite registrado. Não declare todos como aprovados por terem passado em testes de arquivo.

Avalie a animação em velocidade normal, lenta e quadro a quadro. Observe cabeça flutuando, ombros rígidos, deslizamento dos pés, volume variável, cintilação de textura e descontinuidade na emenda. Uma cabeça perfeitamente copiada pode continuar parecendo colada se não acompanhar a dinâmica do corpo.

Para caminhar no lugar, mantenha o pivô do conjunto estável, mas permita que os pés avancem e recuem dentro do canvas conforme as fases. Deslocamento no espaço e sincronização com o passo pertencem à integração de destino, que precisa de teste próprio.

## 15 Resolução transparência e formatos

Guarde o original recebido do gerador e a versão preparada. Resolução do arquivo, dimensão visível do personagem e densidade aparente de pixel são grandezas diferentes. Ampliar de 1x para 4x por vizinho mais próximo deixa os blocos maiores e nítidos, sem criar informação. Regerar em maior dimensão pode produzir detalhe novo, mas exige nova avaliação de fidelidade.

Não reduza ou quantize automaticamente o master HD para fazê-lo parecer pixel art. Se uma versão de menor resolução for desejada, exporte uma derivação identificada e compare olhos, boca, barba, acessórios e contorno. Quantização pode destruir tons e alfa. Uma versão reduzida aceita não substitui o original.

### Formatos de entrega

| Formato | Uso adequado | Limite relevante |
| --- | --- | --- |
| PNG RGBA | Masters e quadros individuais | Não contém estrutura de rig |
| Atlas PNG e JSON | Sequências e recortes documentados | Conferir limite de textura do destino |
| APNG | Prévia e animação com alfa | Testar o suporte no aplicativo de uso |
| GIF | Prévia simples de ampla circulação | Paleta limitada e transparência restrita |
| WebM ou outro vídeo | Vídeo conforme o destino | Alfa depende de codec e suporte real |
| SVG | Apenas vetor efetivamente construído | Incorporar PNG não o transforma em vetor |

No navegador, prefira image-rendering pixelated quando adequado ao estilo e evite interpolação suave entre quadros raster. Transições de opacidade entre duas poses podem produzir rostos duplicados. A escala final ainda precisa ser conferida no dispositivo de destino.

Memória de textura descomprimida pode ser estimada por largura vezes altura vezes 4 bytes para RGBA de 8 bits. O atlas histórico de 7680 por 6272 px consome cerca de 184 MiB apenas para uma cópia decodificada. Exportações menores ou separadas por sequência podem ser mais adequadas; preserve os HD independentemente da otimização.

Adicione borda clara para fundo escuro apenas como derivação explícita e aprovada. Ela altera a silhueta e pode ficar espessa demais em tamanhos pequenos. Verifique contorno, lentes e mãos sobre branco, preto e uma cor saturada, além do fundo real de destino.

## 16 Verificação e aceite

Mantenha quatro estados independentes: identidade, revisão artística, preparação técnica e integração no destino. Use pendente, aprovado, reprovado ou não aplicável. “Novo para revisão visual” significa que a imagem existe, não que tenha sido aceita.

### Critérios por etapa

| Etapa | Evidência mínima para avançar |
| --- | --- |
| Entrada | Referências legíveis, aparência escolhida e lados confirmados |
| Folha mestra | Aceite do titular com versão e arquivos identificados |
| Expressões e poses | Comparação com a folha, anatomia e enquadramento revisados |
| Cor | Máscaras revisadas, alfa e pixels externos preservados |
| Movimento | Canvas, pivô, fases, durações e revisão visual do ciclo |
| Exportação | Decodificação integral, hashes e comparação das derivações |
| Destino | Reprodução e transparência vistas no aplicativo real |

O teste de edição localizada exige zero diferenças fora da máscara autorizada, comparando canais RGBA na mesma resolução. Se houver uma correção de alfa, ela deve estar explicitamente autorizada e registrada em máscara própria. Para cabeça transladada, alinhe as regiões antes de comparar. Um arquivo que tem hash diferente pode conter os mesmos pixels com compressão diferente; distinga integridade de bytes de igualdade visual ou RGBA.

Decodifique todos os quadros de um APNG, confira quantidade, duração e igualdade com os PNGs de origem. Testar apenas o primeiro quadro é insuficiente. Em um HTML com imagens incorporadas, verifique o PNG inteiro e sua correspondência com a fonte. Um cabeçalho válido não garante um arquivo completo.

O preview precisa ser aberto em um navegador real. Teste reprodução, pausa, quadro manual, direção, fundo, download, tamanho de uso e funcionamento sem rede se prometido. Testes de lógica simulada não comprovam renderização. Os pacotes antigos registram essa limitação; não a transforme em aprovação retrospectiva.

Os scripts desta distro verificam propriedades declaradas de arquivos, máscaras e sequências. Eles não detectam automaticamente todos os erros de anatomia, semelhança, perspectiva, fases ou acessórios. Registre quem fez a revisão visual e qual foi seu resultado.

## 17 Falhas frequentes e reparos

Corrija primeiro a causa que afeta a identidade e depois refine a atuação. Um resultado com rosto diferente não deve virar base só porque tem uma mão bem desenhada. Preserve o componente útil se ele puder ser composto de modo coerente.

| Problema observado | Causa provável | Ação de reparo |
| --- | --- | --- |
| Rosto muda a cada expressão | Geração integral e referências fracas | Usar base aceita e máscaras faciais |
| Cabeça aumenta ao trocar de pose | Recortes e escalas independentes | Registrar marcos e conferir escala antes de compor |
| Aparência fica lisa | Densidade ou textura diferente | Ajustar direção visual e aprovar derivação sem destruir HD |
| Relógio troca de braço | Espelhamento sem correção | Recuperar lateralidade anatômica e revisar oclusão |
| Lente cria mancha no fundo | Alfa preenchido ou composição acumulada | Revisar máscara de lente e substituir pixels corretamente |
| Roupa colore pele ou armação | Seleção global por cor | Usar máscara semântica por peça |
| Cor pulsa durante a animação | Normalização independente por quadro | Aplicar a mesma rampa calibrada em toda a série |
| Personagem salta no canvas | Recorte por quadro ou pivô inconsistente | Restaurar canvas e âncora comuns |
| Gola fica dupla | Transição entre fontes sobrepostas | Reconstruir junção sem misturar silhuetas duplicadas |
| Movimento parece travar | Fase repetida, ordem ou duração inadequada | Revisar sequência e emenda em velocidade normal |
| APNG ou imagem incorporada falha | Arquivo incompleto | Reexportar, decodificar integralmente e renovar os testes |

Não reutilize um relatório de aprovação depois de alterar arquivos ou detectar falhas. Gere um novo relatório ligado à versão e aos hashes atuais. Uma correção local pode exigir revisar também atlas, APNG e preview, pois essas cópias podem continuar contendo a versão antiga.

Se um componente não puder ser preservado com perspectiva ou anatomia coerentes, gere novamente apenas o necessário e registre que houve nova arte. “Determinístico” descreve uma composição efetivamente reprodutível a partir de arquivos, máscaras e parâmetros, não a expectativa de que o gerador obedeça ao prompt.

## 18 Organização e distribuição por avatar

Cada avatar deve ter sua própria pasta e seu identificador. Use nomes sem espaços ou acentos para caminhos técnicos. Mantenha identidade, roupa, vista, ação, quadro e versão no manifesto; o nome do arquivo pode resumir esses campos sem se tornar excessivamente longo.

Exemplo de nome: pessoa01_social_andar_leste_f03_v1.png. O índice f03 identifica a ordem final da animação, enquanto o registro de origem aponta qual tentativa gerada foi selecionada. Nunca altere a origem para fazê-la coincidir artificialmente com a ordem final.

### Estrutura recomendada para um novo avatar

| Pasta | Conteúdo |
| --- | --- |
| privado | Fotos e registros de entrada com acesso controlado |
| ref | Folha mestra aceita, bases e guias identificados |
| gen | Propostas originais e registro de prompts |
| src | Imagens preparadas, componentes e máscaras |
| dist | PNGs, atlas e animações destinados ao uso |
| docs | Ficha, decisões, aprovação, método e relatórios |
| tools | Receitas e scripts necessários à reconstrução |

O pacote de uso não precisa conter fotos pessoais ou propostas descartadas. O pacote de manutenção pode guardá-las separadamente quando necessário e autorizado. O pacote desta metodologia contém apenas instruções, modelos e ferramentas genéricas, sem imagens pessoais do caso de referência.

Registre no manifesto dimensões, cor, alfa, pivô, duração, versão mestre, origem, transformações e SHA-256. Dados desconhecidos devem permanecer nulos ou pendentes. Confira se uma alteração de canvas também atualizou pivô e retângulos do atlas.

Uma alteração de identidade pode justificar uma versão principal; adicionar uma pose pode justificar uma versão secundária; corrigir um PNG incompleto pode justificar uma revisão de correção. Esse esquema de versionamento é uma convenção proposta. O histórico deve explicar a mudança independentemente do número escolhido.

Antes de entregar, confira links relativos, ausência de arquivos privados, instruções de abertura, dependências e estados pendentes. Uma distro reutilizável precisa permitir que outra pessoa descubra o que fornecer e como verificar o resultado sem conhecer a conversa original.

## 19 Roteiro de replicação

O percurso abaixo organiza a execução por dependência, sem prometer duração fixa ou quantidade de gerações. Cada pessoa e cada estilo exigem um número diferente de revisões. Registre tempo e tentativas reais para estimar projetos futuros.

### Primeira entrega de identidade

1. Copie os modelos e crie o identificador do novo avatar.
2. Selecione as fotos e preencha a aparência desejada no briefing.
3. Peça o diagnóstico visual, corrija divergências e confirme a lateralidade.
4. Valide busto neutro, corpo e vistas; monte a folha mestra com os escolhidos.
5. Registre a aprovação e congele a versão mestre.

### Primeira biblioteca versátil

1. Aprove um pequeno conjunto de expressões e poses úteis.
2. Escolha roupas geométricas e delimite as máscaras de cada peça.
3. Teste duas combinações de cor com o mesmo arquivo base, sem regenerá-lo.
4. Produza piscar, uma fala demonstrativa e um movimento simples.
5. Revise tamanhos de uso, transparência, mãos e acessórios.

### Expansão e animação

1. Aprove as bases nas direções realmente necessárias.
2. Construa e revise uma caminhada antes de replicar para outras direções.
3. Exporte quadros, manifesto, APNG e preview; faça a conferência no destino.
4. Registre pendências e só então planeje novos movimentos ou aparências.

Para iniciar ou transferir o trabalho a outra conversa, anexe INICIAR_AVATAR.md, a ficha preenchida, a folha mestra e a base operacional do lote. Inclua o registro de decisões e informe a última aprovação. Reenviar só o prompt não transmite a identidade visual nem o histórico de aceite.

O piloto de replicação desta distro deve ser realizado com uma segunda pessoa antes de classificá-la como validada em múltiplos avatares. Verifique se o operador conseguiu seguir o método, se as máscaras funcionaram no estilo escolhido e se a pessoa reconheceu sua representação em todas as saídas. Esta versão documenta e generaliza o caso Felipe; não declara esse piloto concluído.

## 20 Uso das ferramentas incluídas

As ferramentas não chamam serviços de geração. Elas auditam PNGs, comparam edições, compõem propostas alinhadas, trocam cores, aplicam acessórios preparados, auxiliam na triagem técnica de fotos e empacotam sequências de quadros. O código foi preparado para ser lido e adaptado, com testes sintéticos que verificam invariantes de preservação e exportação.

### Instalação e comandos

Crie um ambiente Python e instale tools/requirements.txt. No Windows, o comando inicial pode ser py em vez de python. Os comandos completos estão em tools/LEIA-ME.md e devem ser executados na raiz da distro. Use cópias dos arquivos e caminhos de saída novos.

| Comando | Função |
| --- | --- |
| audit | Decodificar PNGs e registrar dimensões, alfa e hashes |
| compare | Contar alterações dentro e fora de uma máscara |
| compose | Substituir pixels de uma proposta alinhada somente na máscara |
| recolor | Aplicar cores somente nas máscaras declaradas |
| accessories | Aplicar camadas preparadas com posição e oclusão |
| photo-audit | Ler fotos e registrar indicadores para revisão visual |
| pack | Exportar atlas, APNG, JSON e preview de uma sequência |

O pack recebe um JSON com lista ordenada de PNGs, duração por quadro e pivô. Ele recusa quadros idênticos, pois um codificador pode fundir repetições e alterar a estrutura esperada. Um repouso estático deve ser entregue como PNG; uma pausa mais longa dentro de um ciclo deve ser representada pela duração do quadro correspondente. A exportação de várias direções deve usar uma configuração por direção.

O preview produzido pelo pack incorpora as imagens e oferece reprodução, pausa, seleção manual e troca de fundo. Ele é um instrumento de inspeção, não uma integração certificada. Abra-o no navegador real e registre o resultado. A distro não inclui um jogo ou aplicativo de avatar completo.

Os relatórios em testes/RELATORIO_VALIDACAO.md registram o que foi executado nesta entrega. Eles não validam automaticamente o conjunto de arquivos que outra pessoa produzirá. Execute os testes de novo após adaptar o código ou alterar as regras de exportação.

## 21 Limites e manutenção da metodologia

A fidelidade pode variar com novos modelos, interfaces e estilos. Mantenha um pequeno conjunto de imagens de teste e compare mudanças de ferramenta antes de migrar uma biblioteca inteira. Preservar as referências e os originais permite voltar a uma versão aceita.

As operações determinísticas exigem componentes compatíveis. Colar uma cabeça frontal em corpo de perfil, transportar uma máscara para outra pose sem alinhamento ou reaproveitar um relógio sem resolver oclusão pode produzir erros mesmo que o código execute sem falhar. O operador continua responsável por escolher transformações coerentes.

Esta distro prepara avatares raster em duas dimensões. Ela não gera automaticamente um modelo 3D, um rig esquelético, uma topologia vetorial ou animação facial completa. Essas saídas exigiriam outro contrato técnico e outra produção. A variedade de poses e quadros amplia a utilidade do avatar dentro das capacidades efetivamente entregues.

Para melhorar o método após cada aplicação, registre qual etapa exigiu intervenção, qual instrução foi ambígua e qual diferença visual escapou aos testes. Acrescente uma regra somente quando ela resolver um problema observado e puder ser explicada para o próximo operador. Evite transformar particularidades de uma pessoa em exigências universais.

## Anexo A Fontes internas consultadas

Os nomes abaixo identificam os pacotes do projeto usados como evidência. Eles não são dependências de execução desta distro e suas imagens não foram redistribuídas.

| Pacote | Documentos principais e contribuição |
| --- | --- |
| avatar-felipe_especificacao-fidelidade-v1.zip | Especificação 002, medidas e limitações do QA por cor; status de proposta |
| avatar-felipe_fiel-v1.zip | Ficha 001, manifesto e organização das referências fiéis |
| avatar-felipe_onda1_fundacao.zip | Ficha consolidada, prancha matriz e fundação como origem de identidade |
| avatar-felipe_onda2_referencia.zip | Ficha, manifesto e referência de olhos e vistas |
| avatar-felipe_onda2F_prancha2-expressoesA.zip | README, v2 aprovada, v3 reprovada e limitações de métricas |
| avatar-felipe_poc-palette-swap.zip | Código de recoloração experimental e comparação de cores |
| avatar_felipe_lote01_hd.zip | Critérios, edição por máscaras, alfa de lentes e decodificação integral |
| avatar_felipe_lote02_poses_hd.zip | Poses individuais, lateralidade, reparo localizado e margens |
| avatar_felipe_lote03_amigaveis_rpg.zip | Complementos faciais e estudos estáticos em quatro direções |
| avatar_felipe_lote04_caminhada_sul (1).zip | Revisão 02, articulação de cabeça e ombros e preservação de regiões |
| avatar_felipe_lote05_caminhada_4direcoes (1).zip | Revisão 02, manifestos, reconstrução, espelhamento corrigido e limites |

A etapa inicial no Claude é atribuída ao relato do titular na solicitação de 28 de outubro de 2026. As recomendações sobre quantidade de fotos, sequência de validação, novos modelos de ficha e ferramentas genéricas são propostas desta distro.

## Anexo B Referências técnicas externas

Consultadas em 28 de outubro de 2026. As referências fundamentam somente as observações sobre uso e limites do gerador; as regras de produção são a síntese operacional desta distro.

E1. OpenAI. Image generation. https://developers.openai.com/api/docs/guides/image-generation

E2. OpenAI. Image prompting. https://developers.openai.com/api/docs/guides/image-prompting

As instruções locais da skill imagegen foram consultadas para orientar o uso de referências, a declaração de invariantes, as iterações locais e a verificação de transparência. A versão 1.2 incorpora o snapshot integral da skill imagegen e seu código, licença e referências no módulo skills/avatar-imagens. O upload não instala automaticamente uma skill nem concede acesso ao motor generativo.

## Anexo C Vocabulário operacional

| Termo | Significado nesta distro |
| --- | --- |
| Folha mestra | Conjunto visual aceito que define a identidade estilizada |
| Base operacional | Arquivo de trabalho aceito para um enquadramento ou direção |
| Deriva | Alteração acumulada de aparência entre gerações |
| Máscara | Imagem que delimita a região autorizada de edição |
| Patch | Recorte de substituição com posição e regra de composição |
| Alfa | Canal que controla a transparência de cada pixel |
| Palette swap | Troca controlada de cores preservando a geometria |
| Atlas | Imagem que reúne quadros em células documentadas |
| Pivô | Âncora lógica para posicionar um quadro ou sequência |
| Visema | Representação visual simplificada associada a sons de fala |
| Fonte original | Arquivo recebido antes de recorte e preparo |
| Reconstrução | Reexecução de operações registradas sobre fontes guardadas |
| Aceite | Registro explícito da avaliação por pessoa responsável |


## Anexo D Módulo de imagem incluído

O módulo embutido reúne SKILL.md, procedimentos completos, snapshot integral do provedor, requisitos de Python, diagnóstico sem rede, preparação de pedidos e scripts locais. Resize ajusta dimensões e encaixe; resample escolhe a amostragem. Nearest é o padrão de pixel art e é obrigatório para máscaras binárias. Outros filtros usam alfa pré-multiplicado. Os relatórios registram escala, deslocamento e recorte, para atualizar pivôs e máscaras.

O procedimento de edição por texto usa geração nativa ou a CLI original, se a rota API for explicitamente escolhida. Composição por máscara e comparação asseguram a preservação externa quando aplicáveis. Um arquivo de instrução não contém pesos de modelo, licença de uso de conta ou credenciais. As dependências estão declaradas e há um preparador opcional de ambiente; elas não são bibliotecas binárias embarcadas.
