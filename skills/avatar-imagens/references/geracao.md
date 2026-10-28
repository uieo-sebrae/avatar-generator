# Geração de avatar com referências

## Entradas

Receber instrução, fotos avaliadas ou folha mestra aprovada, enquadramento, vista, roupa e estilo. Identificar cada anexo por papel. Em um avatar novo, seguir conducao.md e obter aceite do rosto antes de ampliar. Em uma variação, a folha mestra é a origem da identidade.

## Execução nativa

1. Ler o módulo fornecido em ../providers/openai-imagegen/SKILL.md. Não depender de uma instalação separada.
2. Inspecionar os arquivos locais na ferramenta de visão antes da geração ou edição.
3. Organizar o prompt com identidade, referência, vista, atuação, estilo, invariantes e fundo.
4. Usar a ferramenta nativa de imagem do agente. Passar as referências pelo mecanismo efetivamente suportado; caminhos no texto não significam que o gerador recebeu os arquivos.
5. Gerar uma imagem por pose ou vista quando a qualidade individual importar. Iterar uma alteração por vez.
6. Inspecionar rosto, mãos, proporção, roupa e acessórios. Verificar alfa real.
7. Guardar original e resultado preparado. Atribuir aprovação somente quando o usuário avaliar.

## Pedido preparado por código

Usar scripts/prepare_request.py com action generate e images identificadas. Ele cria prompt.txt e request.json, sem geração ou envio de fotos. Entregar esses arquivos à ferramenta nativa junto das imagens. Não apresentar a preparação como execução.

## Alternativa API escolhida pelo usuário

Usar a CLI integral fornecida em providers/openai-imagegen/scripts/image_gen.py, seguindo references/cli.md daquela pasta. Configurar a chave fora da conversa. Validar o modelo e os parâmetros na documentação atual. Usar generate quando não houver imagem de entrada e edit para referências ou transformação de imagem. Testar primeiro --dry-run; a simulação não comprova acesso ao modelo.

Exemplo de simulação que não envia imagens nem faz chamada:

```sh
python providers/openai-imagegen/scripts/image_gen.py generate --model gpt-image-2 --prompt "Avatar hi-bit isolado conforme o briefing" --out proposta.png --dry-run
```

O nome do modelo no exemplo corresponde ao snapshot do adaptador, não a uma escolha universal. O fluxo padrão continua nativo. Não mudar de modelo para obter transparência sem decisão explícita.

## Saída

PNG original, prompt efetivamente usado, referências e papéis, fonte da geração, estado artístico e relatório técnico quando executado. Não incluir fotos pessoais no pacote genérico.
