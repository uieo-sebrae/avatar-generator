# Entrada do operador de IA

Versão 1.2. Leia INICIAR_AVATAR.md e inicie a condução descrita ali. O usuário não precisa preencher formulários, escolher prompts ou executar comandos para começar.

Use os prompts como apoio e docs/REFERENCIA_TECNICA.html como consulta. Registre estado em modelos/estado_projeto.json quando houver execução de arquivos. Este método não instala uma skill nem adiciona ferramentas ausentes.

Se o usuário anexou somente INICIAR_AVATAR.md, conduza briefing, avaliação visual das fotos e validação do rosto. Solicite os scripts do ZIP apenas quando uma operação técnica os exigir.

Ler também skills/avatar-imagens/SKILL.md. O módulo integral fornecido inclui geração, edição por texto, resize, resample e o snapshot completo do provedor. Não depender de uma skill de imagem instalada fora do pacote. A ferramenta nativa ou o acesso autorizado à API ainda pertencem ao ambiente.
