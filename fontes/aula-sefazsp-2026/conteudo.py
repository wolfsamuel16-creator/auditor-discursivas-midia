# -*- coding: utf-8 -*-
"""Conteúdo das cinco rodadas da aula SEFAZ-SP 2026 (APOFP · FCC)."""

RODADAS = [
# ---------------------------------------------------------------- 1
dict(
 n=1,
 titulo="Frustração de receita no último ano de mandato",
 eixo="Administração Financeira e Orçamentária · Direito Financeiro (LRF) · Contabilidade Pública",
 porque="2026 é o último ano dos mandatos estaduais, e a prova cai em 20 de dezembro, às vésperas do encerramento do exercício.",
 caso=[
  "O Estado Alfa vive em 2026 o último ano do mandato do governador. O relatório do 4.º bimestre mostrou que a receita realizada, abaixo da prevista, pode não comportar a meta de resultado primário fixada na Lei de Diretrizes Orçamentárias (LDO). Para enfrentar a situação, a Secretaria da Fazenda e Planejamento do Estado elaborou três propostas.",
  "<b>Proposta 1</b> — limitar empenho de forma linear em todas as despesas do Poder Executivo, inclusive nos repasses constitucionais aos municípios e no pagamento de juros e amortizações da dívida.",
  "<b>Proposta 2</b> — assinar, em setembro de 2026, contrato de reforma de 200 escolas estaduais, com três parcelas, duas delas a serem pagas em 2027, embora o fluxo de caixa projetado para 31/12/2026 não tenha saldo para cobri-las.",
  "<b>Proposta 3</b> — inscrever em restos a pagar, no encerramento do exercício, todo o saldo empenhado e não pago, sem verificar a disponibilidade de caixa de cada fonte de recursos.",
 ],
 comando="Considerando a situação hipotética, na condição de Analista em Planejamento, Orçamento e Finanças Públicas, analise as três propostas e indique a solução tecnicamente adequada para cada uma, abordando, necessariamente, os seguintes aspectos:",
 itens=[
  ("os requisitos e os limites da limitação de empenho, aplicados à proposta 1;", 40),
  ("a regularidade da proposta 2;", 40),
  ("o conceito e as espécies de restos a pagar e as condições para a inscrição pretendida na proposta 3.", 40),
 ],
 esqueleto=[
  ("Abertura · 2 linhas", "Diagnóstico: as três medidas mexem no fim do mandato; duas precisam de ajuste."),
  ("§1 · aspecto 1 · 8 linhas", "TF: limitar, sim; linear, não · LRF, art. 9.º: 30 dias após o bimestre, critérios da LDO · § 2.º: obrigações constitucionais e legais e serviço da dívida ficam fora · solução: preservar repasses e dívida; cortar discricionárias."),
  ("§2 · aspecto 2 · 8 linhas", "TF: contrato irregular · LRF, art. 42: dois últimos quadrimestres + parcelas sem caixa · fato: setembro, parcelas em 2027, sem saldo · solução: ajustar ao caixa ou adiar · CP, art. 359-C."),
  ("§3 · aspecto 3 · 10 linhas", "TF: inscrição só com lastro · Lei n.º 4.320/1964, art. 36: processados × não processados · LRF, arts. 50, I, e 55, III, b: caixa por fonte · solução: cancelar empenhos não liquidados sem caixa."),
 ],
 padrao=[
  ("1. Limitação de empenho", [
   "Se a realização da receita puder não comportar o cumprimento das metas de resultado primário ou nominal, os Poderes e o Ministério Público promovem, por ato próprio e nos trinta dias subsequentes, limitação de empenho e movimentação financeira, segundo os critérios fixados pela LDO (LC n.º 101/2000, art. 9.º).",
   "Não são objeto de limitação as despesas que constituam obrigações constitucionais e legais do ente, inclusive as destinadas ao serviço da dívida, e as ressalvadas pela LDO (art. 9.º, § 2.º).",
   "Solução: a limitação é cabível, mas não linear. Repasses constitucionais aos municípios e serviço da dívida devem ser preservados; o corte recai sobre despesas discricionárias. Recuperada a receita, a recomposição das dotações é proporcional às reduções (art. 9.º, § 1.º).",
  ]),
  ("2. Contrato no fim do mandato", [
   "É vedado ao titular de Poder ou órgão, nos dois últimos quadrimestres do mandato, contrair obrigação de despesa que não possa ser cumprida integralmente dentro dele, ou que tenha parcelas a pagar no exercício seguinte sem suficiente disponibilidade de caixa (LRF, art. 42).",
   "Na apuração do caixa, consideram-se os encargos e as despesas compromissadas a pagar até o final do exercício (art. 42, parágrafo único).",
   "Solução: assinado em setembro (dentro do período) e com parcelas em 2027 sem saldo, o contrato não pode ser firmado como proposto: deve ser reduzido ao que couber no caixa do exercício ou adiado. Correlato penal: Código Penal, art. 359-C.",
  ]),
  ("3. Restos a pagar", [
   "Restos a pagar são as despesas empenhadas e não pagas até 31 de dezembro, distinguindo-se as processadas (já liquidadas) das não processadas (pendentes de liquidação) (Lei n.º 4.320/1964, art. 36).",
   "A disponibilidade de caixa é registrada por fonte, de modo que os recursos vinculados fiquem identificados (LRF, art. 50, I), e recurso vinculado só atende ao seu objeto (art. 8.º, parágrafo único).",
   "Solução: no último ano de mandato, os restos a pagar não processados só podem ser inscritos até o limite do saldo de caixa, demonstrado no RGF do último quadrimestre (LRF, art. 55, III, b), em coerência com o art. 42. Empenhos não liquidados sem cobertura devem ser cancelados; os processados, que já são obrigação do ente, têm prioridade.",
  ]),
 ],
 espelho=[
  ("2.1 Limitação de empenho", [
   "0 — não abordou ou abordou de forma equivocada.",
   "1 (13,3) — afirmou que cabe limitar empenho, sem requisitos.",
   "2 (26,7) — indicou gatilho, prazo de 30 dias e critérios da LDO OU as despesas protegidas.",
   "3 (40,0) — gatilho, prazo, critérios da LDO, despesas protegidas (§ 2.º) e solução aplicada ao caso.",
  ], 40),
  ("2.2 Contrato de reforma", [
   "0 — não abordou ou abordou de forma equivocada.",
   "1 (13,3) — citou o art. 42 sem aplicá-lo.",
   "2 (26,7) — indicou o período e a vedação de parcelas sem caixa.",
   "3 (40,0) — período, vedação, enquadramento do fato (setembro, parcelas em 2027, sem saldo) e solução.",
  ], 40),
  ("2.3 Restos a pagar", [
   "0 — não abordou ou abordou de forma equivocada.",
   "1 (13,3) — conceituou restos a pagar sem as espécies.",
   "2 (26,7) — conceito e espécies (processados × não processados).",
   "3 (40,0) — conceito, espécies, limite do saldo de caixa por fonte (art. 55, III, b) e solução (cancelar empenhos sem lastro).",
  ], 40),
 ],
 proposta=[
  "As três medidas tratam do fim do mandato, mas apenas parte delas pode ser adotada como proposta.",
  "A limitação de empenho é cabível, mas não de forma linear. Nos termos do art. 9.º da LRF, se a receita puder não comportar as metas fiscais, os Poderes devem limitar empenho e movimentação financeira nos trinta dias seguintes ao fim do bimestre, segundo os critérios da LDO. O § 2.º, porém, exclui as obrigações constitucionais e legais, inclusive o serviço da dívida. Assim, os repasses aos municípios e os juros e as amortizações devem ser preservados, e o corte deve recair sobre despesas discricionárias. Se a receita se recuperar, as dotações devem ser recompostas de forma proporcional às reduções (§ 1.º).",
  "O contrato de reforma das escolas, por sua vez, é irregular. O art. 42 da LRF veda ao titular de Poder, nos dois últimos quadrimestres do mandato, contrair obrigação que não possa ser cumprida nele ou que tenha parcelas no exercício seguinte sem caixa, computadas as despesas compromissadas até o fim do exercício. Assinado em setembro, com parcelas em 2027 e sem saldo, o ajuste deve ser reduzido ao que couber no caixa ou adiado, sob pena do crime do art. 359-C do Código Penal.",
  "Por fim, a inscrição em restos a pagar exige lastro. Eles são as despesas empenhadas e não pagas até 31 de dezembro: processados, se liquidados, ou não processados, se pendentes de liquidação (Lei n.º 4.320/1964, art. 36). No último ano de mandato, os não processados só podem ser inscritos até o saldo de caixa de cada fonte (LRF, arts. 50, I, e 55, III, b). Recomenda-se cancelar os empenhos não liquidados sem cobertura e priorizar os processados.",
 ],
 armadilhas=["O enunciado lista repasses aos municípios e dívida de propósito: é exatamente o que o § 2.º do art. 9.º protege.", "\"Setembro\" está no texto para você enquadrar o período do art. 42 (a partir de 1.º de maio)."],
 erros=["Concluir que a LRF proíbe qualquer despesa no fim do mandato: proíbe a obrigação sem caixa.", "Tratar restos a pagar como uma espécie só. Processados e não processados têm tratamento diferente na hora de cancelar."],
 dicas=["Feche cada parágrafo com a solução (\"recomenda-se...\"): o edital avalia a proposta de solução, não só o conceito.", "Use o vocabulário da lei: \"limitação de empenho e movimentação financeira\", \"disponibilidade de caixa\", \"fonte de recursos\"."],
),
# ---------------------------------------------------------------- 2
dict(
 n=2,
 titulo="Operação de crédito para uma linha de metrô",
 eixo="Direito Financeiro (operações de crédito, regra de ouro) · AFO (PPA) · Economia (avaliação de projetos)",
 porque="Junta três disciplinas de peso no edital e a atribuição do cargo de cuidar de garantias, obrigações do Tesouro e política creditícia.",
 caso=[
  "O Estado Beta pretende contratar operação de crédito externa, com garantia da União, para financiar a construção de uma nova linha de metrô, com obras previstas de 2027 a 2031. O projeto não consta do Plano Plurianual (PPA) vigente.",
  "O estudo de viabilidade, feito com taxa mínima de atratividade de 8% ao ano, apresentou valor presente líquido (VPL) positivo no cenário-base, mas negativo no cenário em que a demanda de passageiros fica 20% abaixo da projetada.",
  "Em reunião, um assessor sugeriu destinar parte do empréstimo ao pagamento da folha de dezembro, \"já que o dinheiro estará em caixa\".",
 ],
 comando="Considerando a situação hipotética, na condição de Analista em Planejamento, Orçamento e Finanças Públicas, elabore parecer sobre a operação, abordando, necessariamente, os seguintes aspectos:",
 itens=[
  ("os requisitos legais para a contratação da operação e para a concessão da garantia da União;", 30),
  ("a consequência de o projeto não constar do PPA;", 30),
  ("a sugestão de usar os recursos do empréstimo na folha de pagamento;", 30),
  ("a interpretação do estudo de viabilidade e a recomendação técnica.", 30),
 ],
 esqueleto=[
  ("§1 · aspecto 1 · 8 linhas", "TF: contratação possível, cumpridos os requisitos · LRF, art. 32: verificação pelo Ministério da Fazenda, autorização legislativa, inclusão no orçamento, limites do Senado, autorização específica do Senado (externa) · art. 40: contragarantia e adimplência."),
  ("§2 · aspecto 2 · 6 linhas", "TF: incluir antes · CF, art. 167, § 1.º: investimento plurianual sem PPA = crime de responsabilidade · solução: revisão do PPA ou lei que autorize a inclusão."),
  ("§3 · aspecto 3 · 6 linhas", "TF: vedado · recurso vinculado ao objeto (LRF, art. 8.º, parágrafo único) · regra de ouro (CF, art. 167, III) e sua razão."),
  ("§4 · aspecto 4 · 8 linhas", "TF: viável, mas sensível à demanda · VPL > 0 cria valor à TMA · sensibilidade = risco · solução: cenários, revisão da demanda, benefícios sociais, mitigação."),
 ],
 padrao=[
  ("1. Requisitos e garantia", [
   "O Ministério da Fazenda verifica os limites e condições da operação (LRF, art. 32). O pleito vem instruído com parecer técnico e jurídico que demonstre a relação custo-benefício e o interesse econômico e social da operação, e exigem-se prévia e expressa autorização na lei orçamentária, em créditos adicionais ou em lei específica; inclusão dos recursos no orçamento; observância dos limites e condições do Senado; autorização específica do Senado, na operação externa; e respeito à regra de ouro (art. 32, § 1.º, I a V; CF, art. 52, V).",
   "A garantia da União depende de contragarantia em valor igual ou superior e da adimplência do Estado com o garantidor (LRF, art. 40, § 1.º). O Estado pode vincular receitas próprias e transferências como contragarantia (CF, art. 167, § 4.º).",
  ]),
  ("2. Ausência no PPA", [
   "Nenhum investimento cuja execução ultrapasse um exercício financeiro pode ser iniciado sem prévia inclusão no PPA, ou sem lei que autorize a inclusão, sob pena de crime de responsabilidade (CF, art. 167, § 1.º).",
   "Solução: as obras vão de 2027 a 2031; antes do início, o Estado deve rever o PPA ou aprovar lei que autorize a inclusão do projeto.",
  ]),
  ("3. Recursos na folha", [
   "A Constituição veda operações de crédito que excedam as despesas de capital, ressalvadas as autorizadas por créditos suplementares ou especiais com finalidade precisa, aprovados por maioria absoluta (CF, art. 167, III — regra de ouro; LRF, art. 32, § 1.º, V). É um limite agregado do exercício, cuja razão é impedir que o endividamento financie despesa corrente.",
   "O que impede este uso específico é a vinculação: os recursos da operação estão vinculados ao objeto autorizado em lei e no contrato e só podem atendê-lo (LRF, art. 8.º, parágrafo único). A sugestão deve ser rejeitada.",
  ]),
  ("4. Estudo de viabilidade", [
   "VPL positivo à taxa mínima de atratividade indica que o projeto cria valor no cenário-base; a análise de sensibilidade mostra que a viabilidade depende da demanda, que é o risco central.",
   "Recomendação: revisar as premissas de demanda, montar cenários com probabilidades, incorporar os benefícios sociais (tempo de viagem, emissões, acidentes) numa análise custo-benefício e prever medidas de mitigação antes de decidir.",
  ]),
 ],
 espelho=[
  ("2.1 Requisitos e garantia", ["0 — não abordou ou abordou de forma equivocada.", "1 (10) — citou requisitos genéricos.", "2 (20) — indicou ao menos três requisitos do art. 32.", "3 (30) — requisitos do art. 32, inclusive a autorização do Senado para a operação externa, e condições da garantia (contragarantia e adimplência)."], 30),
  ("2.2 PPA", ["0 — não abordou ou abordou de forma equivocada.", "1 (10) — disse que o PPA é necessário, sem fundamento.", "2 (20) — indicou a vedação do art. 167, § 1.º.", "3 (30) — vedação, consequência (crime de responsabilidade) e solução (revisão do PPA ou lei)."], 30),
  ("2.3 Uso na folha", ["0 — não abordou ou aceitou a sugestão.", "1 (10) — rejeitou sem fundamento.", "2 (20) — fundamentou na regra de ouro.", "3 (30) — vinculação dos recursos ao objeto, regra de ouro e sua finalidade (não financiar despesa corrente)."], 30),
  ("2.4 Viabilidade", ["0 — não abordou ou abordou de forma equivocada.", "1 (10) — interpretou o VPL sem a sensibilidade.", "2 (20) — interpretou VPL e sensibilidade.", "3 (30) — VPL, sensibilidade como risco e recomendação concreta (cenários, demanda, benefícios sociais)."], 30),
 ],
 proposta=[
  "A operação pode ser contratada, desde que cumpridos os requisitos legais. Nos termos do art. 32 da LRF, cabe ao Ministério da Fazenda verificar limites e condições, e exigem-se parecer que demonstre o custo-benefício, autorização prévia em lei, inclusão dos recursos no orçamento e observância dos limites do Senado. Por ser externa, a operação depende ainda de autorização específica do Senado. A garantia da União exige contragarantia de valor igual ou superior e adimplência do Estado (art. 40, § 1.º), e a contragarantia pode vincular receitas próprias e transferências (CF, art. 167, § 4.º).",
  "Além disso, o projeto precisa entrar no PPA antes do início das obras. O art. 167, § 1.º, da Constituição veda iniciar investimento que ultrapasse um exercício sem prévia inclusão no plano, sob pena de crime de responsabilidade. Como as obras vão de 2027 a 2031, o Estado deve rever o PPA ou aprovar lei que autorize a inclusão.",
  "A sugestão de pagar a folha com o empréstimo deve ser rejeitada. Os recursos da operação estão vinculados ao objeto autorizado e só podem atendê-lo (LRF, art. 8.º, parágrafo único), e a regra de ouro (CF, art. 167, III) existe justamente para que o endividamento não financie despesa corrente. Os recursos devem ir para as obras, e a folha deve ser coberta por receitas correntes ou pela limitação de outras despesas.",
  "Por fim, o estudo indica viabilidade, mas com risco relevante. O VPL positivo mostra que o projeto cria valor à taxa mínima de 8%, porém a sensibilidade revela que tudo depende da demanda. Recomenda-se revisar essa premissa, simular cenários com probabilidades, incluir os benefícios sociais em análise custo-benefício e prever medidas que reduzam o risco de demanda antes da contratação.",
 ],
 armadilhas=["\"Externa\" e \"com garantia da União\" acrescentam dois requisitos: autorização específica do Senado e contragarantia.", "O cenário de demanda 20% menor não manda rejeitar o projeto: manda tratar o risco."],
 erros=["Dizer que o projeto é inviável porque um cenário deu VPL negativo.", "Confundir regra de ouro com limite de endividamento do Senado."],
 dicas=["Em Economia, o edital quer raciocínio, não fórmula: explique o que o VPL e a sensibilidade significam para a decisão.", "Quatro aspectos em 30 linhas: 7 a 8 linhas por parágrafo, sem abertura."],
),
# ---------------------------------------------------------------- 3
dict(
 n=3,
 titulo="Renúncia de ICMS e projeção de receita na reforma tributária",
 eixo="Direito Financeiro (LRF) · Direito Constitucional (sistema tributário e EC n.º 132/2023) · Economia",
 porque="A reforma tributária está no programa (EC n.º 132/2023) e muda a principal receita do Estado; a LDO de 2027 já precisa refleti-la.",
 caso=[
  "Em 2026, o Estado Gama elabora o projeto da LDO para 2027. Dois fatos chamaram a atenção da equipe técnica da Secretaria da Fazenda e Planejamento.",
  "<b>Fato 1</b> — a Assembleia aprovou lei, de iniciativa parlamentar, que prorroga por cinco anos redução da base de cálculo do ICMS para um setor industrial, sem estimativa de impacto orçamentário-financeiro, sem medida de compensação e sem convênio celebrado no âmbito do Confaz.",
  "<b>Fato 2</b> — a projeção da receita de ICMS para 2027 a 2034, que alimenta o anexo de metas fiscais, repete o crescimento médio dos últimos dez anos e não considera a substituição gradual do ICMS pelo Imposto sobre Bens e Serviços (IBS).",
  "Questionado, o secretário afirmou que \"como o ICMS vai acabar, perder arrecadação agora não faz diferença\".",
 ],
 comando="Considerando a situação hipotética, na condição de Analista em Planejamento, Orçamento e Finanças Públicas, analise os fatos e a afirmação do secretário, propondo as providências cabíveis e abordando, necessariamente, os seguintes aspectos:",
 itens=[
  ("os requisitos legais e constitucionais para a concessão do benefício descrito no fato 1;", 40),
  ("a adequação da projeção de receita do fato 2 diante das regras da reforma tributária;", 40),
  ("o equívoco da afirmação do secretário e a recomendação técnica.", 40),
 ],
 esqueleto=[
  ("§1 · aspecto 1 · 10 linhas", "TF: benefício irregular · LRF, art. 14: estimativa no exercício e nos dois seguintes + LDO + não afetar metas ou compensação · ADCT, art. 113 · CF, art. 155, § 2.º, XII, g: deliberação dos Estados (Confaz)."),
  ("§2 · aspecto 2 · 10 linhas", "TF: projeção inadequada · LRF, art. 12: efeitos das alterações na legislação · EC n.º 132/2023: IBS compartilhado, no destino; ICMS reduzido de 2029 a 2032, extinto em 2033 · solução: refazer com cenários e memória de cálculo."),
  ("§3 · aspecto 3 · 8 linhas", "TF: afirmação errada · ICMS financia o Estado até 2032 · renúncia = gasto tributário, avaliar custo-benefício · elasticidade da receita · solução: não sancionar/rever, monitorar."),
 ],
 padrao=[
  ("1. Requisitos da renúncia", [
   "A concessão ou ampliação de benefício tributário que implique renúncia deve vir com estimativa do impacto no exercício de início de vigência e nos dois seguintes, atender à LDO e demonstrar que a renúncia foi considerada na estimativa da receita e não afeta as metas fiscais, ou vir acompanhada de medidas de compensação por aumento de receita (LRF, art. 14).",
   "A proposição legislativa que crie ou altere renúncia deve trazer estimativa de impacto (ADCT, art. 113, aplicado pelo STF a todos os entes).",
   "Benefício de ICMS depende de deliberação dos Estados, na forma de lei complementar (CF, art. 155, § 2.º, XII, g — convênio no Confaz).",
  ]),
  ("2. Projeção na reforma", [
   "As previsões de receita devem considerar os efeitos das alterações na legislação, da variação de preços e do crescimento econômico, com metodologia de cálculo e premissas (LRF, art. 12); no anexo de metas fiscais, exige-se memória e metodologia de cálculo (art. 4.º, § 2.º, II).",
   "A EC n.º 132/2023 cria o IBS, de competência compartilhada entre Estados, Distrito Federal e municípios (CF, art. 156-A), cobrado no destino, e reduz o ICMS gradualmente de 2029 a 2032, até sua extinção em 2033.",
   "Solução: refazer a projeção de 2029 em diante com a transição e com cenários, explicitando a metodologia no anexo de metas fiscais.",
  ]),
  ("3. Afirmação do secretário", [
   "O ICMS continua sendo a principal receita própria do Estado até o fim da transição; a renúncia reduz recursos já nos próximos exercícios e pressiona as metas.",
   "Renúncia é gasto tributário: deve ser avaliada pela relação custo-benefício e pela elasticidade da receita em relação à atividade econômica, não presumida neutra.",
   "Recomendação: apontar os vícios, propor a revisão ou o veto da prorrogação e monitorar o benefício com indicadores de resultado.",
  ]),
 ],
 espelho=[
  ("2.1 Requisitos da renúncia", ["0 — não abordou ou abordou de forma equivocada.", "1 (13,3) — citou a necessidade de estimativa de impacto.", "2 (26,7) — requisitos do art. 14 (estimativa, LDO e metas ou compensação).", "3 (40,0) — art. 14 completo, ADCT, art. 113 OU exigência de deliberação dos Estados (Confaz), aplicados ao fato 1."], 40),
  ("2.2 Projeção de receita", ["0 — não abordou ou abordou de forma equivocada.", "1 (13,3) — disse que a projeção deve considerar a reforma, sem fundamento.", "2 (26,7) — art. 12 da LRF e regra de transição do ICMS.", "3 (40,0) — art. 12, transição (2029–2032, extinção em 2033), IBS no destino e solução (cenários e metodologia)."], 40),
  ("2.3 Afirmação e recomendação", ["0 — não abordou ou concordou com o secretário.", "1 (13,3) — discordou sem fundamento.", "2 (26,7) — mostrou que o ICMS financia o Estado na transição.", "3 (40,0) — ICMS na transição, renúncia como gasto tributário (custo-benefício) e recomendação concreta."], 40),
 ],
 proposta=[
  "O benefício do fato 1 é irregular. Nos termos do art. 14 da LRF, a renúncia de receita exige estimativa do impacto no exercício e nos dois seguintes, compatibilidade com a LDO e demonstração de que não afeta as metas fiscais, ou medidas de compensação por aumento de receita. O art. 113 do ADCT também exige estimativa de impacto na proposição. Além disso, benefício de ICMS depende de deliberação dos Estados, por convênio no Confaz (CF, art. 155, § 2.º, XII, g). No caso, faltam todos esses requisitos, o que torna a renúncia irregular e expõe as metas fiscais.",
  "A projeção do fato 2 também é inadequada. O art. 12 da LRF manda considerar os efeitos das alterações na legislação. Pela EC n.º 132/2023, o ICMS será reduzido de 2029 a 2032 e extinto em 2033, substituído pelo IBS, compartilhado com os municípios e cobrado no destino. Repetir a média histórica até 2034 ignora essa transição. A projeção deve ser refeita com cenários de transição, com a memória e a metodologia de cálculo exigidas para o anexo de metas fiscais (LRF, art. 4.º, § 2.º, II).",
  "Por fim, a afirmação do secretário é equivocada. Até 2032, o ICMS segue como principal receita própria, e a renúncia reduz recursos já nos próximos exercícios. Por ser gasto tributário, deve ser avaliada por custo-benefício, considerando a elasticidade da receita em relação à atividade econômica: o benefício só se justifica se o retorno superar o custo. Recomenda-se apontar os vícios, propor a revisão da prorrogação e monitorar o benefício por indicadores.",
 ],
 armadilhas=["\"Iniciativa parlamentar\" não afasta o art. 14: a LRF vale para a renúncia, venha de quem vier.", "O fato 2 pede projeção até 2034: o período atravessa toda a transição e o primeiro ano sem ICMS."],
 erros=["Dizer que o ICMS já foi extinto ou que o IBS é estadual: ele é compartilhado entre Estados e municípios.", "Responder ao secretário só com a lei: ele errou no raciocínio econômico, e o edital avalia a proposta de solução."],
 dicas=["Datas da reforma são o tipo de dado que o corretor confere: 2029 a 2032 de redução, extinção em 2033.", "Se não lembrar o número do inciso, cite o dispositivo pelo conteúdo: \"a Constituição exige deliberação dos Estados\"."],
),
# ---------------------------------------------------------------- 4
dict(
 n=4,
 titulo="Painel de dados, fracionamento de despesa e LGPD",
 eixo="Fluência de Dados · Administração Pública e Auditoria Governamental · Direito Administrativo (Lei n.º 14.133/2021, LAI e LGPD)",
 porque="Fluência de Dados é disciplina nova, com peso 2 na P1, e o cargo inclui auditoria e controle; a FCC gosta de casos que cruzam dados e norma.",
 caso=[
  "A Secretaria da Fazenda e Planejamento do Estado Delta implantou um painel que cruza dados de empenhos, contratos e fornecedores. Na primeira análise, foram identificados três achados.",
  "<b>Achado 1</b> — cerca de 8% dos registros de empenho têm o CPF ou o CNPJ do credor em branco, e há empenhos duplicados, com o mesmo número e valores diferentes.",
  "<b>Achado 2</b> — uma mesma unidade gestora realizou, em 2026, onze contratações diretas por dispensa em razão do valor para serviços de manutenção predial, cada uma abaixo do limite legal, mas que, somadas, o superam com folga.",
  "<b>Achado 3</b> — a área de comunicação pretende publicar, como dados abertos, a lista de servidores com nome, CPF completo e remuneração.",
  "O secretário pediu orientação sobre quem deve agir em cada achado.",
 ],
 comando="Considerando a situação hipotética, na condição de Analista em Planejamento, Orçamento e Finanças Públicas, analise os achados e proponha as providências, abordando, necessariamente, os seguintes aspectos:",
 itens=[
  ("as dimensões de qualidade de dados afetadas no achado 1 e o cuidado antes de tirar conclusões do painel;", 30),
  ("a regularidade das contratações do achado 2;", 30),
  ("os limites legais da publicação pretendida no achado 3;", 30),
  ("a atuação de cada linha do Modelo das Três Linhas no tratamento dos achados.", 30),
 ],
 esqueleto=[
  ("§1 · aspecto 1 · 7 linhas", "TF: completude e unicidade comprometidas · também consistência · tratar antes de concluir · alerta = indício, não prova."),
  ("§2 · aspecto 2 · 7 linhas", "TF: indício de fracionamento · Lei n.º 14.133/2021, art. 75, § 1.º: soma no exercício, por unidade gestora, mesmo ramo · solução: apurar e planejar contratação única."),
  ("§3 · aspecto 3 · 7 linhas", "TF: nome e remuneração, sim; CPF completo, não · LAI + STF (Tema 483) · LGPD: necessidade e finalidade · mascarar o CPF."),
  ("§4 · aspecto 4 · 8 linhas", "TF: cada linha tem um papel · 1.ª: gestão corrige · 2.ª: riscos/conformidade monitora e cria alertas · 3.ª: auditoria interna avalia com independência."),
 ],
 padrao=[
  ("1. Qualidade de dados", [
   "Campos em branco afetam a completude; empenhos duplicados afetam a unicidade; mesmo número com valores diferentes afeta a consistência.",
   "Antes de concluir, os dados devem ser limpos e tratados (pré-processamento), e o resultado do painel deve ser lido como indício a confirmar nos documentos, não como prova de irregularidade.",
  ]),
  ("2. Fracionamento", [
   "Para aferir os valores da dispensa, considera-se o somatório do que for despendido no exercício pela respectiva unidade gestora e o somatório da despesa com objetos de mesma natureza, isto é, do mesmo ramo de atividade (Lei n.º 14.133/2021, art. 75, § 1.º).",
   "Onze contratações do mesmo objeto, na mesma unidade e no mesmo exercício, que somadas superam o limite, indicam fracionamento. Solução: apurar responsabilidades e planejar contratação única, por licitação.",
  ]),
  ("3. Publicação de dados", [
   "É legítima a publicação, inclusive em sítio eletrônico, do nome do servidor e da remuneração correspondente (STF, Tema 483 da repercussão geral); a transparência ativa decorre da LAI (Lei n.º 12.527/2011).",
   "O CPF completo é dado pessoal desnecessário à finalidade de transparência: a LGPD exige finalidade e necessidade (art. 6.º) e rege o tratamento pelo poder público (art. 23). Solução: publicar com CPF mascarado ou omitido.",
  ]),
  ("4. Três Linhas", [
   "Primeira linha: a gestão, que executa e corrige — saneia os registros, revê as contratações e responde pelo controle do dia a dia.",
   "Segunda linha: funções de gestão de riscos e conformidade, que apoiam e monitoram — transformam os achados em alertas permanentes no painel.",
   "Terceira linha: auditoria interna (órgão central de controle interno), que presta avaliação e assessoria independentes e objetivas sobre os controles e reporta ao órgão de governança, com independência em relação à gestão.",
  ]),
 ],
 espelho=[
  ("2.1 Qualidade de dados", ["0 — não abordou ou abordou de forma equivocada.", "1 (10) — citou problema de qualidade sem nomear dimensões.", "2 (20) — nomeou duas dimensões (completude, unicidade ou consistência).", "3 (30) — dimensões e cautela (tratamento prévio; alerta como indício)."], 30),
  ("2.2 Fracionamento", ["0 — não abordou ou considerou regular.", "1 (10) — apontou fracionamento sem fundamento.", "2 (20) — fundamentou na regra do somatório.", "3 (30) — regra do art. 75, § 1.º (exercício, unidade gestora, mesmo ramo), aplicação ao caso e solução."], 30),
  ("2.3 Publicação", ["0 — não abordou ou aprovou a publicação integral.", "1 (10) — vedou toda a publicação.", "2 (20) — admitiu nome e remuneração, com fundamento.", "3 (30) — nome e remuneração (Tema 483/LAI), vedação do CPF completo (LGPD) e solução (mascaramento)."], 30),
  ("2.4 Três Linhas", ["0 — não abordou ou abordou de forma equivocada.", "1 (10) — descreveu uma linha.", "2 (20) — descreveu duas linhas.", "3 (30) — as três linhas, cada uma com sua providência no caso."], 30),
 ],
 proposta=[
  "O achado 1 compromete a qualidade dos dados. Campos de CPF ou CNPJ em branco afetam a completude; empenhos duplicados, a unicidade; e o mesmo número com valores diferentes, a consistência. Por isso, os dados devem ser tratados antes da análise, e os alertas do painel devem ser lidos como indícios a confirmar nos documentos, não como prova. Convém ainda validar os CPF e CNPJ informados.",
  "O achado 2 indica fracionamento de despesa. Pelo art. 75, § 1.º, da Lei n.º 14.133/2021, o limite da dispensa considera a soma do que a unidade gestora gasta no exercício com objetos do mesmo ramo. No caso, as onze contratações, somadas, superam o limite. Esse parcelamento artificial afasta indevidamente a licitação. Deve-se apurar a responsabilidade e planejar contratação única, com base no planejamento anual de contratações.",
  "Quanto ao achado 3, nome e remuneração podem ser publicados, conforme a LAI e o Tema 483 do STF. O CPF completo, contudo, excede a finalidade de transparência e fere o princípio da necessidade da LGPD (art. 6.º). A própria LAI restringe o acesso a informações pessoais (art. 31). A lista deve sair com o CPF mascarado ou omitido.",
  "Por fim, cada linha tem papel próprio. A gestão, primeira linha, saneia os registros e revê as contratações. A segunda linha, de riscos e conformidade, transforma os achados em alertas permanentes. A auditoria interna, terceira linha, avalia com independência os controles e reporta ao órgão de governança. Essa divisão evita que quem executa avalie a si mesmo.",
 ],
 armadilhas=["\"Cada uma abaixo do limite\" é a isca: o limite é aferido pela soma, não por contratação.", "O achado 3 não pede \"pode ou não pode\": pede o limite. Parte pode ser publicada, parte não."],
 erros=["Tratar o alerta do painel como prova de fraude.", "Colocar a auditoria interna corrigindo registros: corrigir é da gestão; a auditoria avalia."],
 dicas=["Use os nomes técnicos das dimensões de qualidade: completude, unicidade, consistência, acurácia, validade.", "Não arrisque valor de dispensa: os limites são atualizados por decreto todo ano. A regra do somatório basta."],
),
# ---------------------------------------------------------------- 5
dict(
 n=5,
 titulo="Serviço prestado sem empenho e despesa de exercícios anteriores",
 eixo="Administração Financeira e Orçamentária · Contabilidade Aplicada ao Setor Público (MCASP) · Direito Financeiro",
 porque="AFO e Contabilidade Pública têm peso 2 na P1 e são a base das três áreas; o caso cruza os enfoques orçamentário e patrimonial.",
 caso=[
  "Em fevereiro de 2026, uma secretaria do Estado Épsilon recebeu faturas de serviços de manutenção predial efetivamente prestados em novembro e dezembro de 2025, sem prévio empenho, porque o contrato havia vencido e a renovação não foi formalizada.",
  "A contabilidade não registrou nenhum valor relativo a esses serviços nas demonstrações de 2025. Em 2026, o órgão pretende pagar as faturas como despesa de exercícios anteriores, \"sem necessidade de qualquer outro registro\".",
 ],
 comando="Considerando a situação hipotética, na condição de Analista em Planejamento, Orçamento e Finanças Públicas, analise o caso e proponha as providências, abordando, necessariamente, os seguintes aspectos:",
 itens=[
  ("a regularidade da realização da despesa sem prévio empenho;", 30),
  ("o enquadramento do pagamento como despesa de exercícios anteriores e as condições para ele;", 30),
  ("o tratamento sob os enfoques orçamentário e patrimonial, com os efeitos nas demonstrações de 2025;", 30),
  ("as providências de correção e de controle.", 30),
 ],
 esqueleto=[
  ("§1 · aspecto 1 · 7 linhas", "TF: irregular · Lei n.º 4.320/1964, art. 60: vedada despesa sem prévio empenho · estágios: empenho, liquidação, pagamento · mas o serviço foi prestado: vedação ao enriquecimento sem causa."),
  ("§2 · aspecto 2 · 7 linhas", "TF: cabe DEA · art. 37: compromisso reconhecido após o encerramento · condições: reconhecimento pela autoridade, dotação própria em 2026."),
  ("§3 · aspecto 3 · 9 linhas", "TF: dois enfoques · orçamentário: despesa de 2026 (art. 35, II) · patrimonial: VPD e passivo em 2025 (competência) · efeito: passivo e VPD subavaliados."),
  ("§4 · aspecto 4 · 7 linhas", "TF: corrigir e controlar · ajuste de exercícios anteriores no PL · apuração de responsabilidade · controle de vigência de contratos."),
 ],
 padrao=[
  ("1. Despesa sem empenho", [
   "É vedada a realização de despesa sem prévio empenho (Lei n.º 4.320/1964, art. 60). A despesa percorre empenho, liquidação e pagamento (arts. 58 a 65).",
   "Como os serviços foram efetivamente prestados, a Administração deve indenizar o que foi executado, para não enriquecer sem causa (Lei n.º 14.133/2021, art. 149; o contrato verbal é vedado pelo art. 95, § 2.º), sem prejuízo da apuração de responsabilidade de quem deu causa à irregularidade.",
  ]),
  ("2. Despesa de exercícios anteriores", [
   "Podem ser pagos à conta de dotação específica, discriminada por elementos, os compromissos reconhecidos após o encerramento do exercício correspondente, entre outras hipóteses (Lei n.º 4.320/1964, art. 37).",
   "Condições: reconhecimento da dívida pela autoridade competente, comprovação da prestação (liquidação) e dotação própria no orçamento de 2026.",
  ]),
  ("3. Enfoques orçamentário e patrimonial", [
   "No enfoque orçamentário, pertencem ao exercício as despesas nele legalmente empenhadas (Lei n.º 4.320/1964, art. 35, II): a despesa é de 2026.",
   "No enfoque patrimonial, a variação patrimonial diminutiva e o passivo devem ser reconhecidos em 2025, quando o serviço foi prestado (regime de competência — MCASP), mesmo sem empenho.",
   "Efeito: o Balanço Patrimonial de 2025 subavaliou o passivo, e a Demonstração das Variações Patrimoniais subavaliou as VPD.",
  ]),
  ("4. Correção e controle", [
   "Correção do erro de exercício anterior por ajuste de exercícios anteriores no patrimônio líquido, com evidenciação em notas explicativas.",
   "Apuração de responsabilidade e controle preventivo: monitoramento da vigência dos contratos e alerta antes do vencimento.",
  ]),
 ],
 espelho=[
  ("2.1 Despesa sem empenho", ["0 — não abordou ou considerou regular.", "1 (10) — apontou a irregularidade sem fundamento.", "2 (20) — fundamentou no art. 60.", "3 (30) — art. 60, estágios da despesa e dever de pagar o serviço prestado, com apuração de responsabilidade."], 30),
  ("2.2 DEA", ["0 — não abordou ou abordou de forma equivocada.", "1 (10) — admitiu a DEA sem enquadramento.", "2 (20) — enquadrou no art. 37.", "3 (30) — enquadramento e condições (reconhecimento, liquidação, dotação própria)."], 30),
  ("2.3 Dois enfoques", ["0 — não abordou ou abordou de forma equivocada.", "1 (10) — tratou de um enfoque.", "2 (20) — tratou dos dois enfoques.", "3 (30) — dois enfoques e efeitos nas demonstrações de 2025."], 30),
  ("2.4 Providências", ["0 — não abordou.", "1 (10) — uma providência.", "2 (20) — duas providências.", "3 (30) — correção contábil (ajuste no PL), responsabilização e controle preventivo."], 30),
 ],
 proposta=[
  "A despesa foi realizada de forma irregular. O art. 60 da Lei n.º 4.320/1964 veda despesa sem prévio empenho, primeiro estágio antes da liquidação e do pagamento: é o empenho que reserva a dotação e cria a obrigação de pagar. Como os serviços foram prestados, porém, a Administração deve pagá-los para não enriquecer sem causa, sem prejuízo da apuração de responsabilidade.",
  "O pagamento cabe como despesa de exercícios anteriores. O art. 37 da mesma lei admite pagar, à conta de dotação específica, compromissos reconhecidos após o encerramento do exercício. Exige-se o reconhecimento da dívida pela autoridade competente, a comprovação documental do serviço, com preço compatível com o de mercado, e dotação própria em 2026, com empenho no elemento de despesa de exercícios anteriores.",
  "Nos enfoques, o tratamento é diferente. No orçamentário, a despesa é de 2026, ano do empenho (art. 35, II). No patrimonial, a VPD e o passivo deveriam ter sido reconhecidos em 2025, pela competência, ainda que sem execução orçamentária. Assim, o Balanço Patrimonial de 2025 subavaliou o passivo, e a DVP, as VPD, distorcendo o resultado patrimonial do exercício.",
  "Diante disso, recomenda-se corrigir o erro por ajuste de exercícios anteriores no patrimônio líquido, com nota explicativa sobre sua natureza e seu valor, apurar a responsabilidade de quem deu causa à despesa sem empenho e instituir controle de vigência dos contratos, com alerta antes do vencimento.",
 ],
 armadilhas=["\"Sem necessidade de qualquer outro registro\" é a armadilha: a DEA resolve o orçamento, mas não o erro patrimonial de 2025.", "O serviço foi prestado: negar o pagamento seria enriquecimento sem causa."],
 erros=["Dizer que a despesa pertence a 2025 também no orçamento: pelo art. 35, II, ela é do exercício do empenho.", "Esquecer os efeitos nas demonstrações, que o comando pede expressamente."],
 dicas=["Separe os enfoques com conectivos claros: \"no enfoque orçamentário...\", \"no patrimonial...\".", "Use as siglas só depois de escrever por extenso uma vez, salvo as consagradas (DVP, VPD, PL)."],
),
]
