# -*- coding: utf-8 -*-
AREA = 'fiscal'
N_AREA = 1          # rodada da trilha (1 a 5)
N_GERAL = 2         # rodada da série (1 a 15)
DATA = '20 de novembro de 2026'
PROXIMA = ('Policial', '27/11/2026')

TEMAS = [
dict(
curto='Reforma tributária do consumo',
titulo='Reforma tributária do consumo: IBS, CBS e imposto seletivo',
eixo='reforma tributária do consumo (Emenda Constitucional n.º 132/2023)',
linhas=30, minutos=55,
motivadores=[
("<p>Em novembro de 2026, o governador do estado Alfa anunciou que, para atrair uma fábrica de máquinas agrícolas, enviará à assembleia legislativa projeto de lei que concede à empresa redução de 80% do imposto sobre bens e serviços (IBS) devido nas vendas que ela fizer a partir de 2033, “nos moldes do crédito presumido de ICMS que o estado concede hoje”. Segundo o plano de negócios, cerca de 90% da produção será vendida a compradores de outros estados.</p>"
 "<p>Na sessão seguinte, um deputado estadual afirmou que a medida, além de inconstitucional, seria inútil para o estado.</p>",
 "Situação hipotética. Ente, empresa e números são fictícios."),
],
comando='Considerando a situação hipotética apresentada, redija um texto dissertativo acerca da reforma tributária do consumo, respondendo, necessariamente, aos seguintes questionamentos:',
aspectos=[
('Quais tributos sobre o consumo a Emenda Constitucional n.º 132/2023 criou, de quem é a competência de cada um e quais tributos eles substituem?', '9,00'),
('Que princípios o sistema tributário nacional passou a observar e quais características do IBS concretizam ao menos dois deles?', '9,00'),
('O deputado tem razão ao dizer que a medida é inconstitucional e inútil para o estado Alfa? Que alternativa o estado tem para disputar o investimento?', '10,00'),
],
esqueleto=[
('§1 · item 1 · 9 linhas', 'TF: IVA dual + imposto seletivo · IBS: estados, DF e municípios (art. 156-A) → substitui ICMS e ISS · CBS: União (art. 195, V) → substitui PIS e Cofins · IS: União (art. 153, VIII), extrafiscal → bens e serviços prejudiciais à saúde ou ao meio ambiente · IPI com alíquota zero, salvo Zona Franca de Manaus.'),
('§2 · item 2 · 8 linhas', 'TF: art. 145, § 3.º · simplicidade, transparência, justiça tributária, cooperação, meio ambiente · simplicidade → legislação única, alíquota uniforme por ente · transparência → imposto “por fora” e destacado no documento fiscal · justiça → não cumulatividade e devolução a pessoas físicas (§ 4.º: atenuar regressividade).'),
('§3 · item 3 · 10 linhas', 'TF: sim, nos dois pontos · inconstitucional: vedação de benefícios do IBS (art. 156-A, § 1.º, X) + ICMS extinto em 2033 (ADCT, art. 129) · inútil: destino (art. 156-A, § 1.º, VII) → 90% das vendas geram receita para outros estados · solução: infraestrutura, logística, mão de obra, Fundo Nacional de Desenvolvimento Regional.'),
('Fecho · 1 linha', 'A reforma troca a guerra fiscal pela tributação no destino.'),
],
padrao=[
('1. Tributos, competência e substituição', [
 'Modelo de IVA dual: o imposto sobre bens e serviços (IBS), de competência compartilhada entre estados, Distrito Federal e municípios (CF, art. 156-A), substituirá o ICMS e o ISS, extintos a partir de 2033 (ADCT, art. 129).',
 'A contribuição sobre bens e serviços (CBS), da União (CF, art. 195, V), substitui o PIS e a Cofins, extintos a partir de 2027 (ADCT, art. 126).',
 'O imposto seletivo (IS), da União (CF, art. 153, VIII), incide sobre a produção, extração, comercialização ou importação de bens e serviços prejudiciais à saúde ou ao meio ambiente; o IPI passa a ter alíquota zero a partir de 2027, salvo para produtos com industrialização incentivada na Zona Franca de Manaus (ADCT, art. 126, III). Plus: os três foram instituídos pela Lei Complementar n.º 214/2025.']),
('2. Princípios e características do IBS', [
 'O sistema tributário nacional deve observar os princípios da simplicidade, da transparência, da justiça tributária, da cooperação e da defesa do meio ambiente (CF, art. 145, § 3.º); as alterações da legislação devem buscar atenuar efeitos regressivos (§ 4.º).',
 'Características do IBS que os concretizam (CF, art. 156-A, § 1.º): legislação única e uniforme (IV); alíquota própria de cada ente, a mesma para todas as operações (V e VI); não cumulatividade (VIII); não integra a própria base (IX); valor informado no documento fiscal (XIII). Aceita-se a devolução a pessoas físicas (§ 5.º, VIII).']),
('3. Benefício prometido e alternativa', [
 'Inconstitucional: o IBS não pode ser objeto de concessão de incentivos e benefícios financeiros ou fiscais, ressalvadas as hipóteses da própria Constituição (art. 156-A, § 1.º, X); além disso, o ICMS e seus créditos presumidos deixam de existir em 2033 (ADCT, art. 129).',
 'Inútil: o IBS é cobrado pelo somatório das alíquotas do estado e do município de destino (art. 156-A, § 1.º, VII); como 90% das vendas irão a outros estados, a receita dessas operações pertence aos estados de destino, e não a Alfa.',
 'Solução esperada: competir por fatores não tributários (infraestrutura, logística, qualificação de mão de obra, segurança jurídica), inclusive com recursos do Fundo Nacional de Desenvolvimento Regional (CF, art. 159-A).']),
],
apresentacao='2,00',
espelho=[
('Tributos criados, competência e substituição', [
 'Conceito 0 — não abordou ou atribuiu o IBS à União.',
 'Conceito 1 (3,00) — indicou corretamente um dos tributos, com competência e tributo substituído.',
 'Conceito 2 (6,00) — indicou corretamente dois tributos.',
 'Conceito 3 (9,00) — indicou corretamente o IBS, a CBS e o imposto seletivo, com competência e substituição (ou o papel do IS em relação ao IPI).'], '9,00'),
('Princípios e características do IBS', [
 'Conceito 0 — não abordou o aspecto.',
 'Conceito 1 (3,00) — citou princípios do art. 145, § 3.º, sem ligá-los a características do IBS.',
 'Conceito 2 (6,00) — ligou um princípio a uma característica do IBS.',
 'Conceito 3 (9,00) — ligou ao menos dois princípios a características do IBS.'], '9,00'),
('Validade e utilidade da medida e alternativa', [
 'Conceito 0 — não abordou ou afirmou que o benefício é válido.',
 'Conceito 1 (2,50) — afirmou a inconstitucionalidade, sem fundamento.',
 'Conceito 2 (5,00) — fundamentou a inconstitucionalidade na vedação de benefícios do IBS.',
 'Conceito 3 (7,50) — fez isso e explicou a inutilidade pelo princípio do destino, com os dados do caso.',
 'Conceito 4 (10,00) — fez tudo isso e propôs alternativa não tributária para atrair o investimento.'], '10,00'),
],
total='30,00',
texto=[
'A Emenda Constitucional n.º 132/2023 criou um IVA dual e um imposto seletivo. O IBS, de competência compartilhada entre estados, Distrito Federal e municípios (CF, art. 156-A), substituirá o ICMS e o ISS. A CBS, da União (art. 195, V), substitui o PIS e a Cofins. O imposto seletivo, também federal (art. 153, VIII), incide sobre bens e serviços prejudiciais à saúde ou ao meio ambiente e assume o papel extrafiscal do IPI, que terá alíquota zero, salvo na Zona Franca de Manaus.',
'O sistema passou a observar a simplicidade, a transparência, a justiça tributária, a cooperação e a defesa do meio ambiente (art. 145, § 3.º). A simplicidade aparece na legislação única do IBS, com uma alíquota por ente, igual para todas as operações; a transparência, no imposto que não integra a própria base e vem informado no documento fiscal; a justiça, na não cumulatividade e na devolução a pessoas físicas.',
'O deputado tem razão nos dois pontos. A medida é inconstitucional, pois o IBS não pode ser objeto de incentivos ou benefícios fiscais, salvo as exceções constitucionais (art. 156-A, § 1.º, X), e o ICMS será extinto em 2033. Seria também inútil: o IBS pertence ao destino (art. 156-A, § 1.º, VII), e, como 90% das vendas irão para outros estados, essa receita não seria de Alfa. Recomenda-se disputar o investimento com infraestrutura, logística e mão de obra qualificada, inclusive com o Fundo Nacional de Desenvolvimento Regional.',
'Assim, a reforma substitui a guerra fiscal pela tributação no destino.',
],
tri=(
 ['O item 3 é triplo: “inconstitucional”, “inútil” e “alternativa”. A alternativa é a parte mais esquecida — e vale o conceito máximo.', 'O dado “90% para outros estados” está no caso por um motivo: é ele que prova a inutilidade pelo destino.'],
 ['Atribuir o IBS à União ou dizer que a CBS substitui o ICMS.', 'Defender a medida “porque gera empregos”: o comando pede análise jurídica, e a Constituição veda o benefício.'],
 ['Decore o trio “IBS: estados, DF e municípios · CBS: União · IS: União” — ele resolve metade das questões de reforma.', 'Se não lembrar o inciso do art. 156-A, escreva a regra (“o IBS não admite benefícios fiscais”): a regra vale mais que o número.'],
),
),
dict(
curto='Planejamento × evasão',
titulo='Planejamento tributário, evasão e a norma do art. 116 do CTN',
eixo='planejamento tributário e evasão fiscal (CTN, art. 116, parágrafo único)',
linhas=30, minutos=55,
motivadores=[
("<p>Em fiscalização de IRPJ e CSLL na empresa Gama Ltda., o auditor-fiscal identificou três fatos:</p>"
 "<p>I – no início do ano-calendário, antes de qualquer operação, a empresa optou pela tributação com base no lucro presumido, que, pelas projeções do contador, resultaria em carga menor do que a do lucro real;</p>"
 "<p>II – em março, a Gama integralizou um imóvel, pelo valor contábil, no capital da Delta Ltda., empresa de um comprador que vinha negociando o bem; sete dias depois, a Gama retirou-se da sociedade e recebeu em dinheiro o valor de mercado do imóvel. A Delta não exerceu nenhuma atividade no período;</p>"
 "<p>III – durante todo o ano, parte das vendas foi registrada em notas fiscais com valores inferiores aos efetivamente cobrados dos clientes, e a diferença foi recebida em conta bancária de terceiro.</p>",
 "Situação hipotética. Empresas e fatos são fictícios."),
],
comando='Considerando a situação hipotética apresentada, redija um texto dissertativo acerca dos limites do planejamento tributário, respondendo, necessariamente, aos seguintes questionamentos:',
aspectos=[
('O que distingue o planejamento tributário (elisão) da evasão fiscal? Como se classificam os fatos I e III?', '9,00'),
('O que dispõe o parágrafo único do art. 116 do CTN, como o STF o interpretou e como ele se aplica ao fato II?', '10,00'),
('Quais as consequências do fato III para a Gama, quanto ao lançamento, à multa e à esfera penal?', '9,00'),
],
esqueleto=[
('§1 · item 1 · 8 linhas', 'TF: licitude dos meios (+ momento) · elisão: meio lícito, em regra antes do fato gerador · evasão: sonegação, fraude ou simulação, em regra no momento ou depois · I = planejamento (opção legal, antes) · III = evasão (oculta receita já ocorrida).'),
('§2 · item 2 · 11 linhas', 'TF: norma antidissimulação · LC 104/2001: desconsiderar atos para dissimular fato gerador ou elementos da obrigação, com procedimento em lei ordinária · STF, ADI 2.446: constitucional, não proíbe planejamento lícito · II: integraliza + sai em 7 dias + Delta sem atividade = compra e venda dissimulada · solução: desconsiderar e tributar o ganho de capital.'),
('§3 · item 3 · 9 linhas', 'TF: três consequências · lançamento de ofício (art. 149, VII) · decadência pelo art. 173, I, sem homologação tácita (art. 150, § 4.º) · multa qualificada: 100%, 150% na reincidência (Lei 14.689/2023; STF, Tema 863) · representação fiscal para fins penais (Lei 8.137/1990), após decisão administrativa final.'),
('Fecho · 1 linha', 'Economizar é lícito; esconder, não.'),
],
padrao=[
('1. Elisão × evasão e classificação', [
 'Planejamento tributário (elisão): economia de tributo por meios lícitos, em regra adotados antes da ocorrência do fato gerador, escolhendo entre alternativas que a lei oferece.',
 'Evasão: supressão ou redução do tributo por meios ilícitos — sonegação, fraude, conluio ou simulação —, em regra no momento ou depois da ocorrência do fato gerador.',
 'Fato I: planejamento legítimo — a opção pelo lucro presumido é alternativa prevista em lei, feita antes das operações. Fato III: evasão — o subfaturamento oculta do fisco receita já auferida.',
 ]),
('2. Art. 116, parágrafo único, ADI 2.446 e fato II', [
 'Incluído pela Lei Complementar n.º 104/2001: a autoridade administrativa poderá desconsiderar atos ou negócios jurídicos praticados com a finalidade de dissimular a ocorrência do fato gerador do tributo ou a natureza dos elementos constitutivos da obrigação tributária, observados os procedimentos a serem estabelecidos em lei ordinária.',
 'STF, ADI n.º 2.446 (2022): a norma é constitucional; não proíbe o contribuinte de buscar, por vias legítimas, economia fiscal; alcança atos de dissimulação de fato gerador previsto em lei e efetivamente ocorrido.',
 'Fato II: a integralização seguida, em sete dias, da retirada com recebimento em dinheiro, numa sociedade sem atividade, dissimula uma compra e venda do imóvel e o ganho de capital correspondente.',
 'Solução: desconsiderar a forma adotada e lançar o tributo segundo a operação real, com o devido procedimento.']),
('3. Consequências do fato III', [
 'Lançamento de ofício, pois houve dolo, fraude ou simulação (CTN, art. 149, VII); afastada a homologação tácita do art. 150, § 4.º, a decadência passa a contar pelo art. 173, I.',
 'Multa de ofício qualificada por sonegação, fraude ou conluio (Lei n.º 9.430/1996, art. 44, § 1.º): limitada a 100% do tributo, podendo chegar a 150% na reincidência, após a Lei n.º 14.689/2023; o STF fixou o mesmo limite no Tema 863 da repercussão geral.',
 'Esfera penal: a conduta pode configurar crime contra a ordem tributária (Lei n.º 8.137/1990, art. 1.º); a representação fiscal para fins penais é encaminhada após a decisão final na esfera administrativa (Lei n.º 9.430/1996, art. 83).']),
],
apresentacao='2,00',
espelho=[
('Elisão × evasão e classificação dos fatos I e III', [
 'Conceito 0 — não abordou ou classificou o fato I como evasão.',
 'Conceito 1 (3,00) — distinguiu elisão e evasão, sem classificar os fatos.',
 'Conceito 2 (6,00) — distinguiu e classificou corretamente um dos fatos.',
 'Conceito 3 (9,00) — distinguiu pela licitude dos meios e classificou corretamente os fatos I e III.'], '9,00'),
('Art. 116, parágrafo único, STF e fato II', [
 'Conceito 0 — não abordou o aspecto.',
 'Conceito 1 (2,50) — explicou a norma, sem o entendimento do STF nem a aplicação ao caso.',
 'Conceito 2 (5,00) — explicou a norma e o entendimento do STF, sem aplicá-la ao fato II.',
 'Conceito 3 (7,50) — explicou a norma e a aplicou ao fato II, sem o entendimento do STF.',
 'Conceito 4 (10,00) — explicou a norma, o entendimento do STF e a aplicou ao fato II, com a consequência (desconsideração e lançamento).'], '10,00'),
('Consequências do fato III', [
 'Conceito 0 — não abordou o aspecto.',
 'Conceito 1 (3,00) — indicou uma consequência correta.',
 'Conceito 2 (6,00) — indicou duas consequências corretas.',
 'Conceito 3 (9,00) — indicou o lançamento de ofício, a multa qualificada com o limite atual e a repercussão penal.'], '9,00'),
],
total='30,00',
texto=[
'O planejamento tributário e a evasão distinguem-se pela licitude dos meios. A elisão é a economia obtida por alternativa permitida em lei, em regra antes do fato gerador; a evasão reduz o tributo por sonegação, fraude ou simulação, em geral depois dele. Assim, o fato I é planejamento legítimo, pois a opção pelo lucro presumido é prevista em lei e foi feita antes das operações. O fato III é evasão: o subfaturamento esconde do fisco receita já auferida.',
'O parágrafo único do art. 116 do CTN, incluído pela Lei Complementar n.º 104/2001, permite à autoridade desconsiderar atos praticados para dissimular o fato gerador, observado procedimento em lei ordinária. Na ADI n.º 2.446, o STF declarou a norma constitucional e afirmou que ela não proíbe o planejamento lícito, mas só a dissimulação. O fato II enquadra-se nela: a saída da sociedade sete dias após a integralização, numa empresa sem atividade, dissimula a venda do imóvel. Cabe desconsiderar a forma e tributar o ganho de capital.',
'O fato III gera três consequências. Haverá lançamento de ofício, por fraude (CTN, art. 149, VII), com decadência contada pelo art. 173, I. A multa será qualificada, limitada a 100% do tributo, ou 150% na reincidência (Lei n.º 14.689/2023 e STF, Tema 863). Por fim, a conduta pode ser crime contra a ordem tributária (Lei n.º 8.137/1990), objeto de representação fiscal após a decisão administrativa final.',
'Em síntese, economizar tributo é lícito; esconder o fato gerador, não.',
],
tri=(
 ['O fato I é a “pegadinha”: pagar menos não é, por si, ilícito. Classificá-lo como evasão zera o conceito do item 1.', 'No item 2, o STF é parte do quesito: explicar a norma sem dizer que ela não proíbe o planejamento lícito vale meio item.'],
 ['Usar só o critério temporal (“antes” ou “depois” do fato gerador) e esquecer a licitude dos meios.', 'Citar a multa de 150% como regra geral: desde a Lei n.º 14.689/2023, ela é de 100%, e 150% só na reincidência.'],
 ['Os dados “sete dias” e “sem atividade” provam a dissimulação: use-os na resposta.', 'Plus que enriquece: a Lei Complementar n.º 225/2026 (Código de Defesa do Contribuinte) presume a boa-fé do contribuinte, sem impedir auditorias — o planejamento lícito continua protegido.'],
),
),
]

FONTES = [
 'CF/1988, arts. 145, §§ 3.º e 4.º; 153, VIII; 156-A, § 1.º e § 5.º, VIII; 159-A; e 195, V (redação da EC n.º 132/2023); ADCT, arts. 126 e 129. Lei Complementar n.º 214/2025.',
 'CTN, arts. 116, parágrafo único (LC n.º 104/2001), 149, VII, 150, § 4.º, e 173, I. Lei n.º 9.430/1996, arts. 44, § 1.º, e 83; Lei n.º 14.689/2023; Lei n.º 8.137/1990, art. 1.º; LC n.º 225/2026.',
 'STF, ADI n.º 2.446 (2022), rel. Min. Cármen Lúcia; STF, Tema 863 da repercussão geral.',
 'Aulas gratuitas SEFAZ-SP 2026 (FCC) e SEFAZ-AL 2026 (Cebraspe) do @auditor_discursivas; Edital n.º 1 – SEFAZ/AL, de 24/8/2026.',
]
