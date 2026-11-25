# -*- coding: utf-8 -*-
AREA = 'policial'
N_AREA = 1          # rodada da trilha (1 a 5)
N_GERAL = 3         # rodada da série (1 a 15)
DATA = '27 de novembro de 2026'
PROXIMA = ('Controle', '04/12/2026')

TEMAS = [
dict(
curto='Medidas protetivas: do papel à proteção',
titulo='Desafios para a efetividade das medidas protetivas de urgência',
eixo='violência contra a mulher e atuação policial (Lei n.º 11.340/2006 — Lei Maria da Penha)',
linhas=30, minutos=60,
motivadores=[
("<p><b>Texto I.</b> Segundo o Anuário Brasileiro de Segurança Pública 2026, o Brasil registrou 1.571 feminicídios em 2025, aumento de 4% em relação aos 1.504 casos de 2024. No mesmo ano, foram registrados 132.025 descumprimentos de medidas protetivas de urgência, alta de 16,7% — em média, 362 por dia. Nos 18 estados que informaram o dado, 70 mulheres foram mortas enquanto tinham medida protetiva ativa.</p>",
 "Elaborado com base no Anuário Brasileiro de Segurança Pública 2026 (Fórum Brasileiro de Segurança Pública), conforme divulgado pela imprensa em julho de 2026."),
("<p><b>Texto II.</b> Desde 2024, descumprir medida protetiva de urgência é punido com reclusão de 2 a 5 anos, e multa (Lei n.º 11.340/2006, art. 24-A). Em 2025, a Lei n.º 15.125 passou a permitir que a medida protetiva seja cumulada com a monitoração eletrônica do agressor, “disponibilizando-se à vítima dispositivo de segurança que alerte sobre sua eventual aproximação”.</p>",
 "Elaborado com base nas Leis n.º 14.994/2024 e n.º 15.125/2025."),
],
comando='Considerando que os textos acima têm caráter unicamente motivador, redija um texto dissertativo-argumentativo, de 20 a 30 linhas, sobre o tema <b>Desafios para a efetividade das medidas protetivas de urgência no enfrentamento da violência contra a mulher</b>. Em seu texto, contemple, necessariamente, os seguintes aspectos:',
aspectos=[
('por que a concessão da medida protetiva, por si só, não garante a proteção da vítima;', '6,00'),
('o papel das forças de segurança na fiscalização das medidas e na resposta ao descumprimento;', '6,00'),
('proposta de intervenção, com agente, ação, meio e finalidade.', '6,00'),
],
esqueleto=[
('Introdução · 6 linhas', 'Dado: 1.571 feminicídios em 2025, recorde · medida protetiva é a principal ferramenta da Lei Maria da Penha · TESE: só protege se for fiscalizada e se o descumprimento tiver resposta rápida.'),
('Desenvolvimento 1 · 8 linhas', 'Medida é ordem judicial: sem vigilância, depende do agressor obedecer · 132.025 descumprimentos (≈ 362/dia) · 70 mulheres mortas com medida ativa · vítima com medo ou dependência não denuncia.'),
('Desenvolvimento 2 · 8 linhas', 'Polícia transforma a ordem em proteção · patrulhas especializadas visitam a vítima · descumprir é crime (art. 24-A: reclusão de 2 a 5 anos) → prisão em flagrante · Lei 15.125/2025: tornozeleira + alerta à vítima.'),
('Conclusão · 6 linhas', 'Retoma a tese · proposta: governos estaduais + Judiciário · ampliar patrulhas e monitoração eletrônica · centrais integradas de alerta · a fim de que a resposta chegue antes da agressão.'),
],
padrao=[
('Atendimento ao tema e tese', [
 'Tese que responde ao recorte (“desafios para a efetividade”), e não só ao assunto: a medida protetiva existe, mas não protege sozinha.',
 'Uso crítico de dado dos textos motivadores (recorde de feminicídios, descumprimentos), reescrito com as palavras do candidato.']),
('1. Por que a medida, sozinha, não basta', [
 'A medida protetiva é uma ordem judicial: sem fiscalização, sua eficácia depende da obediência do próprio agressor.',
 'Dados do descumprimento (132.025 casos em 2025) e mortes de mulheres com medida ativa como prova do argumento.',
 'Plus: medo, dependência financeira ou emocional e subnotificação dificultam a denúncia do descumprimento.']),
('2. Papel das forças de segurança', [
 'Fiscalização ativa: patrulhas especializadas que visitam e acompanham as vítimas com medida protetiva.',
 'Resposta ao descumprimento: é crime (Lei n.º 11.340/2006, art. 24-A, com pena de reclusão de 2 a 5 anos, e multa, desde a Lei n.º 14.994/2024), o que permite a prisão em flagrante.',
 'Monitoração eletrônica do agressor com dispositivo de alerta para a vítima (art. 22, § 5.º, incluído pela Lei n.º 15.125/2025).']),
('3. Proposta de intervenção', [
 'Agente (governos estaduais, polícias, Judiciário), ação (ampliar patrulhas e monitoração), meio (recursos e centrais integradas de monitoramento) e finalidade (resposta antes da nova agressão).',
 'Proposta ligada aos argumentos do texto, não genérica (“conscientizar a sociedade”).']),
],
apresentacao='2,00',
espelho=[
('Por que a medida, sozinha, não garante proteção', [
 'Conceito 0 — não abordou ou fugiu ao recorte (texto só sobre violência em geral).',
 'Conceito 1 (2,00) — afirmou a insuficiência, sem explicar por quê.',
 'Conceito 2 (4,00) — explicou a dependência de fiscalização, sem dado ou fundamento.',
 'Conceito 3 (6,00) — explicou a insuficiência com dado ou fundamento, integrado ao argumento.'], '6,00'),
('Papel das forças de segurança', [
 'Conceito 0 — não abordou o aspecto.',
 'Conceito 1 (2,00) — citou a atuação policial de forma genérica.',
 'Conceito 2 (4,00) — tratou da fiscalização ou da resposta ao descumprimento, com fundamento.',
 'Conceito 3 (6,00) — tratou da fiscalização e da resposta ao descumprimento, com fundamento legal correto.'], '6,00'),
('Proposta de intervenção', [
 'Conceito 0 — não apresentou proposta.',
 'Conceito 1 (2,00) — proposta vaga, sem agente ou sem meio.',
 'Conceito 2 (4,00) — proposta com agente e ação, sem meio ou finalidade.',
 'Conceito 3 (6,00) — proposta completa (agente, ação, meio e finalidade), ligada aos argumentos.'], '6,00'),
],
total='20,00',
texto=[
'Em 2025, o Brasil registrou 1.571 feminicídios, o maior número da série. A medida protetiva de urgência, principal ferramenta da Lei Maria da Penha, deveria interromper esse ciclo. Na prática, porém, muitas decisões não chegam a proteger quem as pediu. Torná-la efetiva exige superar dois desafios: a falta de fiscalização e a demora da resposta ao descumprimento.',
'Em primeiro lugar, a medida protetiva é uma ordem judicial e, sem vigilância, depende de o agressor obedecê-la. Prova disso são os 132.025 descumprimentos registrados em 2025, cerca de 362 por dia, e as mulheres mortas enquanto tinham medida ativa. Além disso, muitas vítimas, por medo ou dependência financeira, não denunciam a violação, e a ordem fica só no papel. Assim, sem quem a acompanhe, a medida protege menos justamente quem corre mais risco.',
'Por outro lado, as forças de segurança podem transformar a decisão em proteção real. Patrulhas especializadas que visitam as vítimas identificam o risco antes da nova agressão. Ademais, descumprir a medida é crime punido com reclusão de dois a cinco anos, o que permite a prisão em flagrante, e a Lei n.º 15.125/2025 autorizou a monitoração eletrônica do agressor, com alerta à vítima quando ele se aproxima. Esses instrumentos, porém, só funcionam com efetivo treinado e resposta imediata.',
'Portanto, a medida protetiva só protege quando é fiscalizada. Cabe aos governos estaduais, em parceria com o Judiciário, ampliar as patrulhas especializadas e a monitoração eletrônica, por meio de centrais integradas de alerta, a fim de que a polícia chegue antes do agressor.',
],
tri=(
 ['O recorte é “efetividade das medidas protetivas”: um texto só sobre as causas da violência contra a mulher fala do assunto e foge do tema.', 'Copiar os números do Texto I sem ligá-los a um argumento não pontua: o dado tem de provar a tese.'],
 ['Proposta vaga (“conscientizar a sociedade”), sem agente nem meio.', 'Tratar o descumprimento como simples infração administrativa: desde 2018 é crime (art. 24-A), e a pena subiu em 2024.'],
 ['Termine a conclusão com a finalidade (“a fim de que...”): é a parte mais esquecida da proposta.', 'Se não lembrar o artigo, cite a lei: “a Lei Maria da Penha pune o descumprimento com reclusão” já fundamenta.'],
),
),
dict(
curto='Câmeras corporais: transparência e proteção',
titulo='A câmera corporal como instrumento de transparência e de proteção do policial',
eixo='câmeras corporais na atividade policial (Portaria MJSP n.º 648/2024)',
linhas=30, minutos=60,
motivadores=[
("<p><b>Texto I.</b> Em 28 de maio de 2024, o Ministério da Justiça e Segurança Pública publicou a Portaria n.º 648, com diretrizes nacionais sobre o uso de câmeras corporais pelas polícias. Entre as regras, estão o acionamento automático, remoto ou pelo próprio policial. Os estados que quiserem comprar os equipamentos com recursos do Fundo Nacional de Segurança Pública devem seguir essas diretrizes.</p>",
 "Elaborado com base em informações da Agência Gov (dezembro de 2024)."),
("<p><b>Texto II.</b> Em 2024, ao julgar a Suspensão de Liminar n.º 1.696, o presidente do Supremo Tribunal Federal determinou que o governo de São Paulo cumprisse a Portaria n.º 648/2024 e mantivesse o compromisso de usar câmeras corporais em operações policiais. Em 2025, no julgamento da ADPF n.º 635, o STF determinou que o Rio de Janeiro comprovasse a instalação de câmeras nas viaturas das polícias Militar e Civil.</p>",
 "Elaborado com base em notícias do STF (junho de 2024) e da Agência Brasil (outubro de 2025)."),
],
comando='Considerando que os textos acima têm caráter unicamente motivador, redija um texto dissertativo-argumentativo, de 20 a 30 linhas, sobre o tema <b>A câmera corporal como instrumento de transparência e de proteção do policial</b>. Em seu texto, contemple, necessariamente, os seguintes aspectos:',
aspectos=[
('a câmera corporal como instrumento de transparência e de controle da atividade policial;', '6,00'),
('a câmera corporal como instrumento de proteção do próprio policial;', '6,00'),
('condições para que o uso seja eficaz, com proposta de intervenção (agente, ação, meio e finalidade).', '6,00'),
],
esqueleto=[
('Introdução · 6 linhas', 'Segurança pública: dever do Estado (CF, art. 144) → exige legitimidade · Portaria MJSP 648/2024: diretrizes nacionais · TESE: câmera serve à sociedade (transparência) e ao policial (prova), se houver regras.'),
('Desenvolvimento 1 · 8 linhas', 'Transparência: registro objetivo da abordagem e do uso da força · facilita o controle externo do MP (CF, art. 129, VII) e das corregedorias · STF exigiu câmeras em SP (SL 1.696) e no RJ (ADPF 635).'),
('Desenvolvimento 2 · 7 linhas', 'Proteção do policial: prova da legalidade da atuação · contra acusações falsas · palavra do agente deixa de ser a única versão · inibe agressões e desacato.'),
('Conclusão · 7 linhas', 'Condição: acionamento automático ou remoto + custódia segura das imagens · proposta: governos estaduais + MJSP · aderir às diretrizes e regulamentar acesso · capacitação · a fim de que a imagem proteja cidadão e policial.'),
],
padrao=[
('Atendimento ao tema e tese', [
 'Tese que contempla os dois lados do recorte: transparência para a sociedade e proteção para o policial. Texto só “contra” ou só “a favor” da polícia foge do recorte.',
 'Uso de fundamento (CF, art. 144; Portaria MJSP n.º 648/2024) e dos textos motivadores com as palavras do candidato.']),
('1. Transparência e controle', [
 'A gravação cria registro objetivo das abordagens e do uso da força, o que reforça a legitimidade da polícia perante a comunidade.',
 'Facilita o controle externo da atividade policial pelo Ministério Público (CF, art. 129, VII) e o controle interno das corregedorias.',
 'Plus: as decisões do STF sobre São Paulo (SL n.º 1.696) e Rio de Janeiro (ADPF n.º 635), dos textos motivadores.']),
('2. Proteção do policial', [
 'A imagem prova a legalidade da atuação e protege o agente contra acusações infundadas.',
 'A presença da câmera tende a inibir agressões e desacatos — argumento válido se apresentado como tendência, sem número inventado.']),
('3. Condições e proposta', [
 'Condições: acionamento que não dependa só da vontade do policial (automático ou remoto), custódia segura e acesso regulado às imagens, treinamento.',
 'Proposta com agente (governos estaduais, MJSP, polícias), ação, meio e finalidade.']),
],
apresentacao='2,00',
espelho=[
('Transparência e controle da atividade policial', [
 'Conceito 0 — não abordou o aspecto.',
 'Conceito 1 (2,00) — mencionou a transparência de forma genérica.',
 'Conceito 2 (4,00) — explicou como a gravação permite o controle, sem fundamento.',
 'Conceito 3 (6,00) — explicou o controle com fundamento (controle externo do MP, corregedorias ou decisões do STF).'], '6,00'),
('Proteção do policial', [
 'Conceito 0 — não abordou ou tratou a câmera só como vigilância contra o policial.',
 'Conceito 1 (2,00) — afirmou que a câmera protege o policial, sem explicar.',
 'Conceito 2 (4,00) — explicou a câmera como prova da legalidade da atuação.',
 'Conceito 3 (6,00) — explicou a proteção com consequência concreta (prova, defesa contra acusações, efeito inibidor).'], '6,00'),
('Condições de eficácia e proposta', [
 'Conceito 0 — não apresentou condição nem proposta.',
 'Conceito 1 (2,00) — proposta vaga.',
 'Conceito 2 (4,00) — indicou condição de eficácia ou proposta completa.',
 'Conceito 3 (6,00) — indicou condição de eficácia e proposta completa (agente, ação, meio e finalidade).'], '6,00'),
],
total='20,00',
texto=[
'A Constituição Federal define a segurança pública como dever do Estado, e a força desse dever depende da confiança da sociedade na polícia. Nesse contexto, a câmera corporal, que ganhou diretrizes nacionais com a Portaria MJSP n.º 648/2024, pode servir tanto à transparência quanto à proteção do próprio policial, desde que seu uso siga regras claras.',
'Em primeiro lugar, a gravação cria um registro objetivo das abordagens e do uso da força. Isso fortalece o controle externo da atividade policial, atribuído ao Ministério Público, e o trabalho das corregedorias, que passam a decidir com base em imagens. Não por acaso, o Supremo Tribunal Federal exigiu câmeras em São Paulo e nas viaturas do Rio de Janeiro.',
'Além disso, a câmera protege o policial. A imagem comprova a legalidade da atuação e afasta acusações infundadas, de modo que a palavra do agente deixa de ser a única versão. A presença do equipamento também tende a inibir agressões e desacatos durante a ocorrência. Assim, a gravação favorece o bom policial, que passa a ter a prova do próprio trabalho, e reduz a desconfiança que costuma cercar a atuação nas ruas.',
'Portanto, a câmera beneficia o cidadão e o policial, desde que o acionamento não dependa apenas da vontade do agente e as imagens tenham custódia segura. Cabe aos governos estaduais aderir às diretrizes nacionais, com recursos do Fundo Nacional de Segurança Pública, regulamentar o acesso às gravações e capacitar o efetivo para o uso correto dos equipamentos, a fim de que a tecnologia fortaleça a confiança na polícia.',
],
tri=(
 ['O recorte tem dois lados: transparência e proteção do policial. Tratar só um deles atende metade do tema.', 'Não transforme o texto em ataque à polícia nem em defesa corporativa: o tom esperado é institucional e equilibrado.'],
 ['Inventar percentuais de queda da letalidade: sem fonte segura, use “tende a” e o argumento continua válido.', 'Proposta sem agente (“é preciso investir em câmeras”).'],
 ['A condição de eficácia (acionamento automático ou remoto, custódia das imagens) é o que mostra domínio do tema.', 'Use os casos do STF do texto motivador com suas palavras: eles provam que a câmera já é política pública cobrada.'],
),
),
]

FONTES = [
 'CF/1988, arts. 129, VII, e 144. Lei n.º 11.340/2006 (Lei Maria da Penha), arts. 22, § 5.º (incluído pela Lei n.º 15.125/2025), e 24-A (pena alterada pela Lei n.º 14.994/2024). Leis n.º 13.675/2018 e n.º 14.751/2023.',
 'Anuário Brasileiro de Segurança Pública 2026 (Fórum Brasileiro de Segurança Pública), conforme Correio Braziliense (24/7/2026) e CNN Brasil (23/7/2026).',
 'Portaria MJSP n.º 648, de 28/5/2024; Agência Gov (26/12/2024). STF, SL n.º 1.696 (notícia STF de 10/6/2024); STF, ADPF n.º 635 (Agência Brasil, 30/10/2025).',
 'Aula gratuita PM-SC 2026 (Instituto AOCP) do @auditor_discursivas; Edital n.º 002/CCP/2026 – CFP.',
]
