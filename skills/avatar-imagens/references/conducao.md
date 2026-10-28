# Inicie a criação guiada do meu avatar

Metodologia de avatares hi-bit • Versão 1.1 • 28 de outubro de 2026

Este arquivo orienta a IA que o recebe. Comece a condução assim que o usuário o anexar e pedir para iniciar. Se a intenção do upload não estiver explícita, pergunte se ele quer iniciar ou consultar. Use linguagem simples e uma etapa por vez. Não obrigue a pessoa a estudar o manual, preencher formulários, programar ou escolher prompts.

## Objetivo e abrangência

Ajude uma pessoa leiga a construir um avatar consistente a partir de fotos reais. Valide uma folha mestra e depois crie expressões, poses, roupas, cores, acessórios e movimentos. Produza somente o avatar isolado e seus acessórios usados no corpo. Cenários, objetos independentes, tokens e peças de jogo ficam fora.

O método serve a homens, mulheres e pessoas de qualquer gênero ou idade representada. A aparência e a idade pretendidas são informadas pelo usuário; não infira sua identidade de gênero pelas fotos. Não use um homem adulto como modelo padrão. Preserve as proporções escolhidas, sem adultizar crianças, rejuvenescer pessoas idosas ou acrescentar barba, maquiagem ou formas corporais por estereótipo. O estilo pode ser polivalente sem apagar características pessoais.

## Antes de começar

Confira as capacidades reais do ambiente: ler este arquivo ou o ZIP, ver fotos, gerar e editar imagens e executar código. Não invente acesso ou execução.

Se puder ver fotos e gerar imagens, diga: “Vou ajudar você a criar seu avatar. Primeiro vamos escolher as fotos, depois acertar a aparência e criar as variações”. Pergunte como a pessoa quer ser representada, para que usará o avatar e se já tem fotos. Reaproveite respostas anteriores. Pergunte idade ou faixa etária da representação somente se ela ainda não estiver clara.

Se não houver geração de imagem, explique isso antes de coletar fotos: é possível preparar o briefing, mas a geração exige outra ferramenta. Se não conseguir ver as fotos, não as aprove. Se não abrir ZIP, peça INICIAR_AVATAR.md separado. Se não executar código, avance nas etapas visuais e informe o limite quando chegar à customização técnica. Receber a distro não adiciona essas funções à IA.

## Etapa 1 Entender a aparência desejada

Faça no máximo duas ou três perguntas curtas por rodada. Explique hi-bit como “desenho em pixels com bastante detalhe”, se necessário. Registre aparência, finalidade e roupa inicial com palavras do usuário. Não associe roupas a gênero ou idade.

Preencha você mesmo o briefing. Confirme só as escolhas que afetam o resultado: aparência atual ou antiga, óculos, cabelo e lado de acessórios. Não peça ao leigo termos como máscara, paleta, pivô ou resolução. Escolha os parâmetros técnicos com base no uso e explique o efeito em linguagem comum.

## Etapa 2 Avaliar fotos antes de gerar

Para começar o rosto, peça de quatro a seis fotos: frente natural, frente sorrindo, três quartos de ambos os lados e detalhes importantes. Peça corpo, perfil ou costas quando essas saídas forem necessárias. Evite exigir um acervo completo antes de trabalhar no busto.

Abra e examine cada foto como F01, F02 e assim por diante. Avalie foco no rosto, luz, sombras, cor, filtros, distorção, cortes, partes escondidas, reflexo de lentes, visibilidade do cabelo, aparência de épocas diferentes e possibilidade de espelhamento. Leia dimensões se houver ferramenta; arquivo grande não prova nitidez do rosto.

Devolva por foto uma decisão simples: usar, usar com ressalva ou substituir, com motivo concreto. Exemplo: “F02 serve para o sorriso, mas o reflexo esconde os olhos”. Confira se cabelo, contorno facial, olhos, nariz e boca estão suficientemente visíveis nas referências em conjunto.

Confira a cobertura do conjunto para a próxima saída. Frente e três quartos podem bastar para o primeiro busto; não comprovam automaticamente perfis, costas ou proporções corporais. Não invente um detalhe invisível como se estivesse confirmado. Se faltar informação, peça somente a foto complementar necessária e explique como fazê-la.

Quando os scripts estiverem disponíveis, use photo-audit como apoio de leitura, dimensão e indicadores técnicos. face_bbox é opcional e precisa ser marcado na foto após orientação EXIF; o script não detecta faces. Não transforme indicadores de textura ou luminosidade em aprovação facial automática.

Registre a avaliação em modelos/AVALIACAO_FOTOS.md ou em texto equivalente. Escolha: apto para a primeira proposta; apto só para a vista especificada; ou precisa complementar. Só gere depois de registrar suficiência para a saída atual. Essa avaliação não autentica a identidade real da pessoa.

## Etapa 3 Validar rosto e folha mestra

Resuma os traços a preservar e confirme dúvidas. Gere primeiro um busto neutro em três quartos, com as fotos escolhidas, idade visual e estilo combinados. Use fundo realmente transparente, sem texto ou cenário. Mostre a proposta e peça comentários comuns sobre rosto, cabelo e acessórios.

Corrija um ponto por vez e aguarde o aceite do usuário. Não aprove a semelhança em nome dele. Depois faça corpo e vistas progressivamente. Confirme proporções e peça fotos complementares quando necessário. Não copie a anatomia de outro avatar.

Monte a folha mestra com as imagens aceitas, sem redesenhá-las ao montar a prancha. Inclua rosto, corpo, vistas necessárias, expressões iniciais e detalhes pertinentes. Registre versão, data, aceite e arquivos; calcule hashes reais se houver ferramentas. Sem acesso a hash, registre nomes e o limite.

A folha mestra aceita define a identidade estilizada. Uma geração nova ou base operacional não passa a substituí-la automaticamente. Preserve os originais; não reduza ou quantize o master HD por padrão.

## Etapa 4 Criar expressões e poses

Ofereça um primeiro conjunto pequeno conforme a finalidade, como sorriso, surpresa, pensativo, acenar e apresentar. Deixe a pessoa escolher sem exigir vocabulário técnico. Use a folha mestra e a base da vista correta em toda geração.

Para expressão local, proponha a região de olhos, boca ou sobrancelhas e componha sobre a base. compare e compose podem verificar pixels fora da máscara. Não prometa igualdade de pixels só por escrever uma restrição no prompt.

Confira anatomia, mãos, proporção, estilo, acessórios e transparência. Diferencie lado anatômico de lado da imagem. Não espelhe o avatar inteiro sem autorização e correção das assimetrias. Memes são apenas gestos e expressões do próprio avatar, sem texto, cenário ou efeitos independentes.

## Etapa 5 Customizar sem perder a identidade

Pergunte o que a pessoa quer mudar em palavras comuns e traduza isso para a operação correta.

Se for só cor, use recolor e máscaras por peça ou acessório. Os nomes são livres: camisa, vestido, saia, calça, calçado, armação, brinco ou outro item existente. Preserve alfa, pele, cabelo e regiões protegidas. Use a mesma calibração de cores na animação. Não regenere o personagem para uma troca simples de cor.

Se mudar o modelo da roupa, uma gola, manga ou vestido diferente exige arte própria ou camada já preparada e aceita. O código não desenha a roupa. Gere a geometria necessária, confira a identidade e prepare suas máscaras.

Para um acessório opcional, gere ou obtenha uma camada na vista e escala corretas. Defina posição e quais partes passam na frente ou atrás. accessories aplica camadas preparadas e máscaras de oclusão; não descobre sozinho o pulso ou a orelha. Para retirar o acessório opcional, retorne à base sem ele. Se o acessório já estiver fundido à imagem, remover pode exigir reconstruir uma parte escondida e revisar o resultado.

Se houver execução de código, prepare e rode as configurações para o usuário. Não peça que ele edite JSON ou abra terminal. Se faltar essa capacidade, explique a limitação e forneça o pedido e os arquivos necessários para continuar em ambiente compatível. Não anuncie como concluída uma customização que ficou pendente.

## Etapa 6 Preparar movimentos

Comece por piscar, acenar ou caminhar, conforme o uso. Proponha os parâmetros em vez de perguntar coordenadas ou número de quadros ao leigo. Mostre prévias para ele avaliar.

Mantenha canvas, escala, pivô, fases e duração documentados. Revise uma direção antes de expandir. Preserve a cabeça quando a vista for compatível e permita movimento para evitar rigidez. Não cole uma cabeça frontal num perfil e não recorte cada quadro pela silhueta.

Use pack para exportar quadros, APNG, atlas, manifesto e preview quando houver código. Fala demonstrativa sem áudio não é sincronização labial. O conjunto é raster em duas dimensões, sem promessa de modelo 3D ou rig universal.

## Etapa 7 Conferir e entregar

O usuário aprova identidade e aparência. Você verifica arquivos, alfa, máscaras e encaixes. Mantenha separados identidade, arte, preparação técnica e aplicativo de destino. Não declare teste em navegador sem abri-lo e conferir.

Entregue arquivos de uso, explicação curta e pendências. Guarde um resumo com folha mestra, escolhas, arquivos aceitos e próxima ação. Use modelos/estado_projeto.json quando possível; caso contrário, texto equivalente. Não peça novamente decisões já aprovadas sem motivo.

O material genérico da distro nunca deve incorporar fotos pessoais do projeto individual. O fim de um lote não significa que todos os movimentos ou variações foram feitos.

## Recursos desta skill

Ler SKILL.md na raiz do módulo. Os comandos locais estão em scripts; os procedimentos completos ficam em references. Se houver o restante da distro, os modelos e o guia humano também podem ser usados. Caso contrário, registrar briefing, avaliação das fotos e estado em texto equivalente, sem depender de arquivos externos. A fonte integral do provedor está em assets/imagegen-integral.zip e pode ser extraída por scripts/unpack_provider.py.
