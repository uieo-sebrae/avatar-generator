# Compatibilidade do módulo de imagem

## Conteúdo fornecido

O módulo inclui procedimentos completos de geração, edição por texto, resize e resample; código de operações locais; preparação de pedidos; diagnóstico; instalação opcional de dependências; e uma cópia integral da skill imagegen e seus scripts, referências, metadados, recursos e licença em providers/openai-imagegen.

Essa cópia é um snapshot do ambiente em 28 de outubro de 2026, preservado sem alterações. O hash por arquivo é registrado na distro. Ela não representa instalação ou acesso ao serviço em outra conta.

## O que o pacote executa

Resize, resample, máscaras, composição e outras operações determinísticas usam Python e bibliotecas. O código está incluído; os interpretadores e bibliotecas de terceiros são dependências de execução. scripts/setup_local.py pode preparar um ambiente isolado quando a instalação for autorizada. Sem --install, ele só explica a ação.

Geração e edição semântica usam uma ferramenta nativa da IA ou a CLI fornecida, com acesso autorizado ao serviço. Pesos de modelos, contas, credenciais e franquias de uso não podem ser incorporados ao ZIP. Sem um motor disponível, a geração permanece pendente, mesmo que os procedimentos estejam integralmente fornecidos.

## Snapshot e modelos atuais

O adaptador original tem suas próprias validações de modelos, dimensões, qualidade e transparência. Não confundir documentação atual de um modelo com suporte implementado no snapshot. Em particular, o script pode recusar combinações que um serviço mais recente já aceite. Não editar silenciosamente o script do provedor nem trocar o modelo para contornar isso.

Preferir geração nativa para o usuário leigo. Se ele optar por API, confirmar modelo, configuração e custos no ambiente de destino e fazer dry-run antes. Se o adaptador não aceitar a combinação necessária, registrar a limitação e usar uma rota compatível explicitamente escolhida.

## Referências oficiais consultadas

- https://developers.openai.com/api/docs/guides/image-generation
- https://developers.openai.com/api/reference/resources/images/methods/edit

A API oferece geração e edição com referências ou máscaras; máscaras orientam o modelo e não garantem preservação exata. Autenticação e acesso pertencem ao ambiente de execução. A biblioteca de composição local cobre a preservação de pixels quando as fontes são compatíveis.
