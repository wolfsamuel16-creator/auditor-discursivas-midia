# Fila de publicação — @auditor_discursivas

Imagens dos posts que o Metricool publica no Instagram. Repositório público de propósito: o Metricool só aceita imagens com endereço público.

## Estrutura
posts/AAAA-MM-DD-<slug>/
- slide_01.png, slide_02.png, ... (ordem do carrossel)
- legenda.txt — legenda final, pronta para publicar
- post.json — {"publicar_em": "AAAA-MM-DDTHH:MM:SS", "tipo": "carrossel", "origem": "<agente>", "primeiro_comentario": "", "status": "aguardando | agendado | publicado | descartado", "metricool_id": null}

## Fluxo
1. Os agentes de produção (Série Semanal, Radar dos Concursos, Parágrafo da Semana, Radar D-10) gravam a pasta com status "aguardando".
2. O Samuel diz na Central de Marketing: "agenda os posts da semana".
3. A Central agenda no Metricool (URL das imagens: https://raw.githubusercontent.com/wolfsamuel16-creator/auditor-discursivas-midia/main/posts/<pasta>/slide_NN.png) e muda o status para "agendado".
