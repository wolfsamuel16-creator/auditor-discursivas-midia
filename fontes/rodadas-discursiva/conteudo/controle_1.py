# -*- coding: utf-8 -*-
AREA = 'controle'
N_AREA = 1          # rodada da trilha (1 a 5)
N_GERAL = 1         # rodada da série (1 a 15)
DATA = '13 de novembro de 2026'
PROXIMA = ('Fiscal', '20/11/2026')

TEMAS = [
dict(
curto='Controle externo',
titulo='Controle externo e controle interno na Constituição',
eixo='controle da administração pública (CF, arts. 70 a 75)',
linhas=30, minutos=55,
motivadores=[
("<p>“A fiscalização contábil, financeira, orçamentária, operacional e patrimonial da União e das entidades da administração direta e indireta, quanto à legalidade, legitimidade, economicidade, aplicação das subvenções e renúncia de receitas, será exercida pelo Congresso Nacional, mediante controle externo, e pelo sistema de controle interno de cada Poder.”</p>",
 "Constituição Federal de 1988, art. 70, caput."),
],
comando='Considerando que o texto apresentado tem caráter unicamente motivador, redija um texto dissertativo acerca do controle da administração pública. Ao elaborar seu texto, aborde, necessariamente, os seguintes aspectos:',
aspectos=[
('titularidade do controle externo e posição do tribunal de contas na estrutura constitucional;', '9,00'),
('diferença entre apreciar as contas anuais do chefe do Poder Executivo e julgar as contas dos administradores públicos;', '10,00'),
('relação entre o controle interno e o controle externo, conforme o art. 74 da Constituição Federal.', '9,00'),
],
esqueleto=[
('Abertura · 2 linhas', 'Controle externo = de fora do órgão · complementa o interno de cada Poder.'),
('§1 · aspecto 1 · 7 linhas', 'TF: titular = Legislativo · art. 71: Congresso com auxílio do TCU · auxílio ≠ subordinação: órgão autônomo, competências da própria CF · art. 75: simetria (TCEs × assembleias).'),
('§2 · aspecto 2 · 9 linhas', 'TF: apreciar ≠ julgar · contas do Presidente: parecer prévio em 60 dias (art. 71, I), julgamento do Congresso (art. 49, IX) = juízo político · contas dos administradores: julgamento do próprio TCU (art. 71, II) = juízo técnico · débito ou multa = título executivo (§ 3.º).'),
('§3 · aspecto 3 · 9 linhas', 'TF: complementares · art. 74: sistema integrado · finalidades + inciso IV: apoiar o controle externo · § 1.º: ciência ao TCU sob pena de responsabilidade solidária · interno contínuo, por dentro; externo independente, por fora.'),
('Fecho · 2 linhas', 'Síntese: controle político, técnico e interno somados.'),
],
padrao=[
('1. Titularidade e posição do TC', [
 'O controle externo é titularizado pelo Poder Legislativo: no âmbito federal, pelo Congresso Nacional, com o auxílio do Tribunal de Contas da União (CF, arts. 70 e 71).',
 'O tribunal de contas não é subordinado ao Legislativo: é órgão autônomo, com competências próprias fixadas diretamente na Constituição.',
 'Pelo art. 75, o modelo aplica-se aos tribunais de contas dos estados e do DF e aos tribunais e conselhos de contas dos municípios, onde houver.']),
('2. Apreciar × julgar', [
 'Contas anuais do Presidente da República: o TCU as aprecia mediante parecer prévio, elaborado em sessenta dias a contar do recebimento (art. 71, I); o julgamento compete ao Congresso Nacional (art. 49, IX).',
 'Contas dos administradores e demais responsáveis por dinheiros, bens e valores públicos, e de quem der causa a perda, extravio ou irregularidade com prejuízo ao erário: o TCU julga (art. 71, II).',
 'As decisões do tribunal de que resulte imputação de débito ou multa têm eficácia de título executivo (art. 71, § 3.º).',
 'Plus: nos municípios, o parecer prévio sobre as contas do prefeito só deixa de prevalecer por decisão de dois terços da Câmara Municipal (art. 31, § 2.º).']),
('3. Interno × externo (art. 74)', [
 'Os Poderes mantêm, de forma integrada, sistema de controle interno com finalidades de avaliar metas e programas, comprovar a legalidade e avaliar resultados da gestão, controlar operações de crédito e apoiar o controle externo (incisos I a IV).',
 'Os responsáveis pelo controle interno, ao tomarem conhecimento de irregularidade, dela darão ciência ao TCU, sob pena de responsabilidade solidária (§ 1.º).',
 'Ideia-chave esperada: os controles são complementares — o interno atua de dentro e de forma contínua; o externo, de fora e com independência.']),
],
apresentacao='2,00',
espelho=[
('Titularidade do controle externo e posição do tribunal de contas', [
 'Conceito 0 — não abordou ou afirmou que o tribunal é órgão do Legislativo subordinado a ele.',
 'Conceito 1 (3,00) — indicou o Legislativo como titular, sem tratar do tribunal.',
 'Conceito 2 (6,00) — indicou o titular e o auxílio do tribunal, sem tratar da autonomia.',
 'Conceito 3 (9,00) — indicou o titular, o auxílio e a autonomia do tribunal (com ou sem a simetria do art. 75).'], '9,00'),
('Apreciar × julgar contas', [
 'Conceito 0 — não abordou ou confundiu as competências.',
 'Conceito 1 (2,50) — tratou de apenas uma das competências, sem diferenciá-las.',
 'Conceito 2 (5,00) — diferenciou parecer prévio e julgamento, sem indicar quem julga as contas do chefe do Executivo.',
 'Conceito 3 (7,50) — diferenciou e indicou o Legislativo como julgador das contas do chefe do Executivo.',
 'Conceito 4 (10,00) — fez tudo isso e mencionou o julgamento técnico pelo tribunal, com eficácia de título executivo para débito ou multa.'], '10,00'),
('Relação entre controle interno e externo', [
 'Conceito 0 — não abordou o aspecto.',
 'Conceito 1 (3,00) — afirmou que os controles se complementam, sem fundamento.',
 'Conceito 2 (6,00) — mencionou o dever de apoio ao controle externo (art. 74, IV) OU a ciência obrigatória ao tribunal (§ 1.º).',
 'Conceito 3 (9,00) — mencionou o apoio e a ciência obrigatória, sob pena de responsabilidade solidária.'], '9,00'),
],
total='30,00',
texto=[
'O controle externo é exercido de fora da estrutura fiscalizada e complementa o controle interno de cada Poder.',
'A titularidade do controle externo pertence ao Poder Legislativo. No âmbito federal, o art. 71 da Constituição Federal atribui essa função ao Congresso Nacional, com o auxílio do Tribunal de Contas da União. Esse auxílio não significa subordinação: o tribunal é órgão autônomo, com competências fixadas diretamente na Constituição. Pelo art. 75, o modelo aplica-se também aos tribunais de contas dos estados.',
'Apreciar e julgar contas são competências distintas. As contas anuais do Presidente da República são apenas apreciadas pelo TCU, que emite parecer prévio em sessenta dias (art. 71, I); o julgamento cabe ao Congresso Nacional (art. 49, IX), em juízo político. Já as contas dos administradores e demais responsáveis por recursos públicos são julgadas pelo próprio tribunal (art. 71, II), em juízo técnico, e a decisão que imputa débito ou multa tem eficácia de título executivo.',
'Os dois controles são complementares. O art. 74 exige que os Poderes mantenham sistema integrado de controle interno, que, além de avaliar metas e resultados da gestão, deve apoiar o controle externo (inciso IV). Por isso, quem atua no controle interno e toma conhecimento de irregularidade deve dar ciência ao TCU, sob pena de responsabilidade solidária (§ 1.º). Assim, o controle interno atua de dentro e de forma contínua; o externo, de fora e com independência.',
'Conclui-se que o modelo constitucional soma controle político, técnico e interno.',
],
tri=(
 ['“Auxílio” do tribunal ao Legislativo é a palavra que derruba candidatos: auxiliar não é ser subordinado.', 'O aspecto 2 pede diferença: dizer só o que o TCU faz com as contas do Presidente vale meio quesito.'],
 ['Dizer que o TCU “julga” as contas do Presidente da República.', 'Gastar 6 linhas de introdução histórica sobre o controle e não chegar ao art. 74.'],
 ['Use as palavras do comando no tópico frasal (“titularidade”, “apreciar”, “julgar”).', 'Se sobrar linha, o art. 31, § 2.º (contas do prefeito, dois terços da Câmara) é um bom plus no aspecto 2.'],
),
),
dict(
curto='Governança pública',
titulo='Governança pública e governança das contratações',
eixo='governança pública (Decreto n.º 9.203/2017) e governança das contratações (Lei n.º 14.133/2021)',
linhas=30, minutos=55,
motivadores=[
("<p>“Governança pública – conjunto de mecanismos de liderança, estratégia e controle postos em prática para avaliar, direcionar e monitorar a gestão, com vistas à condução de políticas públicas e à prestação de serviços de interesse da sociedade.”</p>",
 "Decreto n.º 9.203/2017, art. 2.º, I."),
],
comando='Considerando que o fragmento de texto apresentado tem caráter unicamente motivador, redija um texto dissertativo acerca da governança no setor público. Ao elaborar seu texto, aborde, necessariamente, os seguintes aspectos:',
aspectos=[
('conceito de governança pública e seus três mecanismos, com a distinção entre governança e gestão;', '10,00'),
('três princípios da governança pública previstos no Decreto n.º 9.203/2017, com breve explicação de cada um;', '8,00'),
('responsabilidade da alta administração pela governança das contratações, conforme a Lei n.º 14.133/2021.', '10,00'),
],
esqueleto=[
('Abertura · 1 linha', 'Governança orienta o Estado para resultados · decreto federal e nova lei de licitações.'),
('§1 · aspecto 1 · 10 linhas', 'TF: conceito (art. 2.º, I) · liderança (integridade, competência, responsabilidade nos cargos de topo) · estratégia (diretrizes, objetivos, prioridades) · controle (processos que mitigam riscos) · governança direciona e supervisiona; gestão executa.'),
('§2 · aspecto 2 · 7 linhas', 'TF: art. 3.º · integridade · transparência · prestação de contas e responsabilidade · fecho: compromissos verificáveis.'),
('§3 · aspecto 3 · 8 linhas', 'TF: alta administração responde (art. 11, parágrafo único) · processos e estruturas, inclusive gestão de riscos e controles internos · avaliar, direcionar, monitorar licitações e contratos · ambiente íntegro, alinhamento ao planejamento e às leis orçamentárias, eficiência, efetividade e eficácia.'),
('Fecho · 1 linha', 'Do rito ao resultado.'),
],
padrao=[
('1. Conceito, mecanismos e distinção', [
 'Conceito do art. 2.º, I, do Decreto n.º 9.203/2017: mecanismos de liderança, estratégia e controle para avaliar, direcionar e monitorar a gestão.',
 'Mecanismos (art. 5.º): liderança — práticas de natureza humana ou comportamental nos principais cargos (integridade, competência, responsabilidade, motivação); estratégia — diretrizes, objetivos, planos, ações e priorização; controle — processos estruturados para mitigar riscos e garantir a execução ordenada, ética, econômica, eficiente e eficaz.',
 'Distinção: a governança avalia, direciona e monitora; a gestão planeja, executa e controla as operações (Referencial Básico de Governança do TCU).']),
('2. Três princípios (art. 3.º)', [
 'Rol do decreto: capacidade de resposta; integridade; confiabilidade; melhoria regulatória; prestação de contas e responsabilidade; transparência.',
 'Pontua quem cita três deles e explica cada um com coerência (ex.: integridade = conduta ética e prioridade ao interesse público; transparência = acesso da sociedade às informações; prestação de contas e responsabilidade = justificar os atos e responder por eles).']),
('3. Governança das contratações', [
 'A alta administração do órgão ou entidade é responsável pela governança das contratações (Lei n.º 14.133/2021, art. 11, parágrafo único).',
 'Deve implementar processos e estruturas, inclusive de gestão de riscos e controles internos, para avaliar, direcionar e monitorar os processos licitatórios e os contratos.',
 'Finalidades: alcançar os objetivos do art. 11 (resultado mais vantajoso, isonomia e justa competição, evitar sobrepreço e superfaturamento, incentivar inovação e desenvolvimento sustentável), promover ambiente íntegro e confiável, alinhar as contratações ao planejamento estratégico e às leis orçamentárias e promover eficiência, efetividade e eficácia.']),
],
apresentacao='2,00',
espelho=[
('Conceito, mecanismos e distinção governança × gestão', [
 'Conceito 0 — não abordou o aspecto ou confundiu governança com gestão.',
 'Conceito 1 (2,50) — conceituou governança de forma genérica, sem os mecanismos.',
 'Conceito 2 (5,00) — conceituou e citou os mecanismos, sem explicá-los.',
 'Conceito 3 (7,50) — conceituou e explicou os três mecanismos, sem a distinção.',
 'Conceito 4 (10,00) — conceituou, explicou os mecanismos e distinguiu governança de gestão.'], '10,00'),
('Três princípios do decreto', [
 'Conceito 0 — não citou princípio do decreto.',
 'Conceito 1 (2,00) — citou um princípio, com explicação.',
 'Conceito 2 (5,00) — citou dois princípios, com explicação.',
 'Conceito 3 (8,00) — citou e explicou três princípios.'], '8,00'),
('Governança das contratações na Lei n.º 14.133/2021', [
 'Conceito 0 — não abordou o aspecto.',
 'Conceito 1 (3,00) — afirmou a responsabilidade da alta administração, sem dizer o que ela deve fazer.',
 'Conceito 2 (6,00) — indicou o dever de implementar processos e estruturas (riscos e controles internos), sem as finalidades.',
 'Conceito 3 (10,00) — indicou o dever e ao menos duas finalidades (ambiente íntegro, alinhamento ao planejamento e às leis orçamentárias, eficiência, efetividade e eficácia).'], '10,00'),
],
total='30,00',
texto=[
'A governança orienta a atuação estatal para resultados à sociedade.',
'Segundo o Decreto n.º 9.203/2017, governança pública é o conjunto de mecanismos de liderança, estratégia e controle para avaliar, direcionar e monitorar a gestão. A liderança reúne práticas de integridade, competência e responsabilidade nos principais cargos; a estratégia define diretrizes, objetivos e prioridades; e o controle estrutura processos para mitigar riscos e garantir a execução eficiente das atividades. Assim, governança não se confunde com gestão: aquela direciona e supervisiona, esta executa.',
'Entre os princípios do decreto, destacam-se a integridade, que exige conduta ética e prioridade ao interesse público; a transparência, que garante à sociedade o acesso às informações; e a prestação de contas e responsabilidade, que obriga os agentes a justificar seus atos e a responder por eles. Esses princípios tornam a governança verificável pela sociedade e pelos órgãos de controle.',
'Nas contratações, a Lei n.º 14.133/2021 atribui à alta administração a responsabilidade pela governança (art. 11, parágrafo único). Cabe-lhe implementar processos e estruturas, inclusive de gestão de riscos e controles internos, para avaliar, direcionar e monitorar licitações e contratos, a fim de promover ambiente íntegro e confiável, alinhar as contratações ao planejamento estratégico e às leis orçamentárias e buscar eficiência, efetividade e eficácia.',
'Portanto, a governança desloca o foco do mero rito para o resultado.',
],
tri=(
 ['O comando pede a distinção entre governança e gestão: sem ela, o aspecto 1 não chega ao conceito máximo.', '“Três princípios” significa três, cada um com explicação; listar os seis sem explicar rende menos.'],
 ['Citar princípios do art. 37 da CF (legalidade, impessoalidade...) no lugar dos princípios do decreto.', 'Tratar a governança das contratações como tarefa do agente de contratação, e não da alta administração.'],
 ['Os três mecanismos (liderança, estratégia, controle) servem para qualquer tema de governança: memorize.', 'No aspecto 3, os verbos “avaliar, direcionar e monitorar” ligam a lei de licitações ao conceito do decreto: use-os.'],
),
),
]

FONTES = [
 'Constituição Federal de 1988, arts. 31, § 2.º; 49, IX; 70; 71, I, II e § 3.º; 74, IV e § 1.º; e 75.',
 'Decreto n.º 9.203/2017 (política de governança da administração pública federal), arts. 2.º, I; 3.º; e 5.º.',
 'Lei n.º 14.133/2021, art. 11, caput e parágrafo único.',
 'TCU. Referencial Básico de Governança Organizacional (3.ª ed., 2020).',
 'Cadernos de prova e padrões de resposta do Cebraspe (TCE-RJ 2021, TCDF 2021, TCE-PB 2018, CGE-RJ 2024, TCE-MS 2025); Edital n.º 1 – CGU – AFFC, de 8/10/2026 (fórmula de desconto da questão de 30 linhas).',
]
