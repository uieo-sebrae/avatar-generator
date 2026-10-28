# Operações complementares do avatar

Usar scripts/avatar_tools.py. Ele contém os comandos audit, compare, compose, recolor, accessories, photo-audit e pack com as mesmas regras da distro.

Manter máscaras binárias opacas no mesmo canvas. Recolorir somente regiões semanticamente revisadas; nomes de peças e acessórios são livres. Não inferir automaticamente uma camisa apenas por ser azul. Preservar alfa e pixels externos.

Aplicar acessórios somente depois de preparar vista, escala e encaixe; usar máscara de oclusão para cabelo ou corpo que deve aparecer à frente. Voltar à base limpa para remover uma camada opcional. Não recuperar como originais partes ocultas que nunca foram desenhadas.

Antes de iniciar a geração, usar photo-audit como auxílio técnico e examinar fotos visualmente. O script não detecta rostos nem aprova identidade, gênero, idade ou anatomia. Registrar suficiência para o enquadramento pretendido.

Ao empacotar animação, manter canvas comum, pivô, ordem e duração. Não recortar cada quadro automaticamente. Decodificar atlas e APNG integralmente. Aprovação de fluidez exige ver o ciclo.
