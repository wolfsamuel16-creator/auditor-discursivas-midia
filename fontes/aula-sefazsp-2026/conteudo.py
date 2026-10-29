# -*- coding: utf-8 -*-
"""Conteúdo das cinco rodadas da aula SEFAZ-SP 2026 (APOFP · FCC), no formato de estudo de caso da FCC."""

RODADAS = [{'n': 1,
  'titulo': 'Frustração de receita no último ano de mandato',
  'eixo': 'Administração Financeira e Orçamentária · Direito Financeiro (LRF) · Contabilidade Pública',
  'porque': '2026 é o último ano dos mandatos estaduais, e a prova cai em 20 de dezembro, às vésperas do '
            'encerramento do exercício.',
  'caso': ['O Estado Alfa vive em 2026 o último ano do mandato do governador. O relatório do 4.º bimestre '
           'mostrou que a receita realizada, abaixo da prevista, pode não comportar a meta de resultado '
           'primário fixada na Lei de Diretrizes Orçamentárias (LDO). Para enfrentar a situação, a '
           'Secretaria da Fazenda e Planejamento do Estado elaborou três propostas.',
           '<b>Proposta 1</b> — limitar empenho de forma linear em todas as despesas do Poder Executivo, '
           'inclusive nos repasses constitucionais aos municípios e no pagamento de juros e amortizações da '
           'dívida.',
           '<b>Proposta 2</b> — assinar, em setembro de 2026, contrato de reforma de 200 escolas estaduais, '
           'a ser integralmente executado até dezembro de 2026, com pagamento em três parcelas, duas delas '
           'em 2027, embora o fluxo de caixa projetado para 31/12/2026, já deduzidas as despesas '
           'compromissadas, não tenha saldo para cobri-las.',
           '<b>Proposta 3</b> — inscrever em restos a pagar, no encerramento do exercício, todo o saldo '
           'empenhado e não pago, sem verificar a disponibilidade de caixa de cada fonte de recursos.'],
  'comando': 'Tendo em vista a situação narrada, na condição de Analista em Planejamento, Orçamento e '
             'Finanças Públicas, responda, justificadamente:',
  'itens': ['A Proposta 1 pode ser adotada? Em que termos a limitação de empenho deve ser feita?',
            'A Proposta 2 é regular? Que solução você propõe?',
            'A Proposta 3 pode ser adotada? Distinga as espécies de restos a pagar envolvidas e indique a '
            'solução.'],
  'esqueleto': [('a) · N linhas',
                 'Resposta: não como formulada · LRF, art. 9.º: todos os Poderes e o MP, 30 dias após o '
                 'bimestre, critérios da LDO · § 2.º: obrigações constitucionais e legais e serviço da '
                 'dívida ficam fora · solução: cortar discricionárias; recompor se a receita voltar.'),
                ('b) · N linhas',
                 'Resposta: não, é irregular · LRF, art. 42: dois últimos quadrimestres + parcelas sem '
                 'caixa, deduzidas as compromissadas · fato: setembro, parcelas em 2027, sem saldo · '
                 'solução: só a etapa paga em 2026, com caixa reservado · CP, art. 359-C.'),
                ('c) · N linhas',
                 'Resposta: só em parte · Lei n.º 4.320/1964, art. 36: processados × não processados · '
                 'processados: inscrever · não processados: até o caixa de cada fonte (LRF, arts. 8.º, 50, '
                 'I, e 55, III, b) · solução: cancelar os não liquidados sem caixa.')],
  'padrao': [('a) Proposta 1',
              ['Se a realização da receita puder não comportar o cumprimento das metas de resultado primário '
               'ou nominal, os Poderes e o Ministério Público promovem, por ato próprio e nos trinta dias '
               'subsequentes, limitação de empenho e movimentação financeira, segundo os critérios fixados '
               'pela LDO (LC n.º 101/2000, art. 9.º).',
               'Não são objeto de limitação as despesas que constituam obrigações constitucionais e legais '
               'do ente, inclusive as destinadas ao serviço da dívida, e as ressalvadas pela LDO (art. 9.º, '
               '§ 2.º).',
               'Solução: a Proposta 1 não pode ser adotada como formulada. A limitação cabe a cada Poder e '
               'ao Ministério Público, não só ao Executivo, e deve preservar os repasses constitucionais aos '
               'municípios e o serviço da dívida; o corte recai sobre despesas discricionárias. Recuperada a '
               'receita, a recomposição das dotações é proporcional às reduções (art. 9.º, § 1.º).']),
             ('b) Proposta 2',
              ['É vedado ao titular de Poder ou órgão, nos dois últimos quadrimestres do mandato, contrair '
               'obrigação de despesa que não possa ser cumprida integralmente dentro dele, ou que tenha '
               'parcelas a pagar no exercício seguinte sem suficiente disponibilidade de caixa (LRF, art. '
               '42).',
               'Na apuração do caixa, consideram-se os encargos e as despesas compromissadas a pagar até o '
               'final do exercício (art. 42, parágrafo único).',
               'Solução: firmado em setembro (dentro do período) e com parcelas em 2027 sem saldo, o '
               'contrato não pode ser assinado como proposto. Deve-se contratar apenas a etapa executável e '
               'paga em 2026, com caixa reservado, e deixar o restante ao próximo mandato. Correlato penal: '
               'Código Penal, art. 359-C.']),
             ('c) Proposta 3',
              ['Restos a pagar são as despesas empenhadas e não pagas até 31 de dezembro, distinguindo-se as '
               'processadas (já liquidadas) das não processadas (pendentes de liquidação) (Lei n.º '
               '4.320/1964, art. 36).',
               'A disponibilidade de caixa é registrada por fonte, de modo que os recursos vinculados fiquem '
               'identificados (LRF, art. 50, I), e recurso vinculado só atende ao seu objeto (art. 8.º, '
               'parágrafo único).',
               'Solução: a Proposta 3 só pode ser adotada em parte. Os restos a pagar processados, já '
               'liquidados, devem ser inscritos, pois o credor cumpriu sua parte; os não processados, só até '
               'o saldo de caixa de cada fonte, demonstrado no Relatório de Gestão Fiscal (RGF) do último '
               'quadrimestre (LRF, art. 55, III, b), regra que o art. 42 reforça no último ano de mandato. '
               'Empenhos não liquidados sem cobertura devem ser cancelados.'])],
  'espelho': [('a) Limitação de empenho',
               40,
               [('Gatilho e alcance: cada Poder e o MP limitam empenho nos 30 dias seguintes ao bimestre, '
                 'pelos critérios da LDO',
                 15),
                ('Despesas protegidas: obrigações constitucionais e legais e serviço da dívida (repasses aos '
                 'municípios, juros e amortizações)',
                 15),
                ('Solução: corte nas discricionárias; recomposição proporcional se a receita se recuperar',
                 10)]),
              ('b) Contrato de reforma',
               40,
               [('Vedação do art. 42: dois últimos quadrimestres, parcelas no exercício seguinte sem caixa, '
                 'deduzidas as despesas compromissadas',
                 20),
                ('Enquadramento do fato: setembro de 2026, parcelas em 2027, sem saldo — irregular', 10),
                ('Solução: contratar só a etapa executável e paga em 2026, com caixa reservado (crime do CP, '
                 'art. 359-C)',
                 10)]),
              ('c) Restos a pagar',
               40,
               [('Conceito: despesas empenhadas e não pagas até 31/12', 8),
                ('Espécies: processados (liquidados) e não processados', 10),
                ('Processados devem ser inscritos; não processados só até o caixa de cada fonte (vinculação)',
                 14),
                ('Solução: apurar o caixa por fonte e cancelar empenhos não liquidados sem cobertura', 8)])],
  'proposta': ['A Proposta 1 não pode ser adotada como formulada. Pelo art. 9.º da LRF, se a receita puder '
               'não comportar a meta, cada Poder e o Ministério Público, não só o Executivo, devem limitar '
               'empenho e movimentação financeira nos trinta dias seguintes ao fim do bimestre, pelos '
               'critérios da LDO. O § 2.º, porém, exclui as obrigações constitucionais e legais e o serviço '
               'da dívida; logo, repasses aos municípios, juros e amortizações devem ser preservados, e o '
               'corte deve recair sobre despesas discricionárias, recompostas se a receita se recuperar (§ '
               '1.º).',
               'A Proposta 2, por sua vez, é irregular. O art. 42 da LRF veda ao titular de Poder, nos dois '
               'últimos quadrimestres do mandato, contrair obrigação que não possa ser cumprida nele ou que '
               'tenha parcelas no exercício seguinte sem caixa suficiente, deduzidas as despesas '
               'compromissadas até o fim do ano. Setembro está nesse período, e as parcelas de 2027 não têm '
               'cobertura. Propõe-se contratar só a etapa executável e paga em 2026, com caixa reservado, e '
               'deixar o restante ao próximo mandato, sob pena de configurar o crime do art. 359-C do Código '
               'Penal.',
               'Por fim, restos a pagar são as despesas empenhadas e não pagas até 31 de dezembro (Lei n.º '
               '4.320/1964, art. 36): processados, se liquidados, e não processados, se pendentes de '
               'liquidação. A inscrição pretendida, contudo, só é possível em parte. Os processados devem '
               'ser inscritos, pois o credor já cumpriu sua parte; os não processados, só até o caixa de '
               'cada fonte, já que recurso vinculado não custeia outra despesa (LRF, arts. 8.º, parágrafo '
               'único, 50, I, e 55, III, b). Cabe apurar o caixa por fonte e cancelar os empenhos não '
               'liquidados sem cobertura.'],
  'armadilhas': ['"Poder Executivo", repasses e dívida estão no texto de propósito: a limitação cabe a cada '
                 'Poder e ao MP e não atinge o que o § 2.º do art. 9.º protege.',
                 '"Setembro" está no texto para você enquadrar o período do art. 42 (a partir de 1.º de '
                 'maio).'],
  'erros': ['Dizer que a LRF proíbe o corte linear: o que ela proíbe é atingir as despesas ressalvadas no § '
            '2.º.',
            'Mandar cancelar restos a pagar processados: o credor já cumpriu sua parte, e a despesa já foi '
            'liquidada.'],
  'dicas': ['Comece cada item respondendo à pergunta ("A Proposta 2 é irregular.") e feche com a solução: o '
            'edital avalia a proposta de solução, não só o conceito.',
            'O item c pede duas coisas (espécies e solução): distinga processados de não processados e diga '
            'o que fazer com cada um.']},
 {'n': 2,
  'titulo': 'Operação de crédito para uma linha de metrô',
  'eixo': 'Direito Financeiro (operações de crédito, regra de ouro) · AFO (PPA) · Economia (avaliação de '
          'projetos)',
  'porque': 'Junta três disciplinas de peso no edital e dialoga com a atribuição do cargo de cuidar de '
            'garantias, obrigações do Tesouro e política creditícia.',
  'caso': ['O Estado Beta pretende contratar em 2027 operação de crédito externa, em dólares, com garantia '
           'da União, para financiar a construção de uma nova linha de metrô, com obras previstas de 2027 a '
           '2031. O projeto não consta do Plano Plurianual (PPA) vigente.',
           'O estudo de viabilidade, feito com taxa mínima de atratividade de 8% ao ano, apresentou valor '
           'presente líquido (VPL) positivo no cenário-base, mas negativo no cenário em que a demanda de '
           'passageiros fica 20% abaixo da projetada.',
           'Em reunião, um assessor sugeriu destinar parte do empréstimo ao pagamento da folha de dezembro, '
           '"já que o dinheiro estará em caixa".'],
  'comando': 'Tendo em vista a situação narrada, na condição de Analista em Planejamento, Orçamento e '
             'Finanças Públicas, responda, justificadamente:',
  'itens': ['Quais são os principais requisitos da LRF para contratar a operação e obter a garantia da '
            'União?',
            'Que consequência tem o fato de o projeto não constar do PPA, e o que deve ser feito?',
            'A sugestão do assessor pode ser acolhida?',
            'Como deve ser interpretado o estudo de viabilidade, e qual é a recomendação técnica?'],
  'esqueleto': [('a) · N linhas',
                 'Resposta: os requisitos · LRF, art. 32: Ministério da Fazenda, parecer de custo-benefício '
                 'e interesse social, autorização em lei, recursos no orçamento, limites do Senado, regra de '
                 'ouro · externa: Senado (CF, art. 52, V) · art. 40: contragarantia de valor igual ou '
                 'superior e adimplência.'),
                ('b) · N linhas',
                 'Resposta: não iniciar sem inclusão · CF, art. 167, § 1.º: investimento plurianual sem PPA '
                 '= crime de responsabilidade · LRF, art. 5.º, § 5.º: sem dotação na LOA · solução: lei que '
                 'inclua no PPA, depois LDO e LOA, antes de contratar.'),
                ('c) · N linhas',
                 'Resposta: não · recurso vinculado ao objeto (LRF, art. 8.º, parágrafo único) · regra de '
                 'ouro: crédito limitado às despesas de capital (CF, art. 167, III) · folha com receita '
                 'corrente e corte de outros gastos.'),
                ('d) · N linhas',
                 'Resposta: viável, mas com alto risco de demanda · VPL > 0 à TMA · cenário negativo ≠ '
                 'inviabilidade automática · solução: demanda de equilíbrio, cenários com probabilidades, '
                 'benefícios sociais, risco cambial.')],
  'padrao': [('a) Requisitos e garantia',
              ['O Ministério da Fazenda verifica os limites e condições da operação (LRF, art. 32). '
               'Exigem-se parecer técnico e jurídico que demonstre a relação custo-benefício e o interesse '
               'econômico e social; prévia e expressa autorização legislativa; inclusão dos recursos no '
               'orçamento; observância dos limites e condições do Senado; autorização específica do Senado, '
               'na operação externa; e respeito à regra de ouro (art. 32, § 1.º, I a V; CF, art. 52, V).',
               'A garantia da União depende de contragarantia em valor igual ou superior ao da garantia e da '
               'adimplência do Estado com o garantidor (LRF, art. 40, § 1.º). O Estado pode vincular '
               'receitas próprias e transferências como contragarantia (CF, art. 167, § 4.º).']),
             ('b) Ausência no PPA',
              ['Nenhum investimento cuja execução ultrapasse um exercício pode ser iniciado sem prévia '
               'inclusão no PPA, ou sem lei que a autorize, sob pena de crime de responsabilidade (CF, art. '
               '167, § 1.º); a LOA também não pode consignar dotação para ele (LRF, art. 5.º, § 5.º).',
               'Solução: as obras vão de 2027 a 2031; antes de contratar, aprovar lei que inclua o projeto '
               'no PPA e prevê-lo na LDO e na LOA.']),
             ('c) Recursos na folha',
              ['A Constituição veda operações de crédito que excedam as despesas de capital, ressalvadas as '
               'autorizadas por créditos suplementares ou especiais com finalidade precisa, aprovados por '
               'maioria absoluta (CF, art. 167, III — regra de ouro; LRF, art. 32, § 1.º, V). É um limite '
               'agregado do exercício, cuja razão é impedir que o endividamento financie despesa corrente.',
               'O que impede este uso específico é a vinculação: os recursos da operação estão vinculados ao '
               'objeto autorizado em lei e no contrato e só podem atendê-lo (LRF, art. 8.º, parágrafo '
               'único). A sugestão deve ser rejeitada.']),
             ('d) Estudo de viabilidade',
              ['VPL positivo à taxa mínima de atratividade indica que o projeto cria valor no cenário-base; '
               'a análise de sensibilidade mostra que a viabilidade depende da demanda, que é o risco '
               'central. Um cenário negativo não torna o projeto inviável por si só: importa a sua '
               'probabilidade.',
               'Recomendação: revisar as premissas de demanda, calcular a demanda de equilíbrio (VPL igual a '
               'zero), montar cenários com probabilidades, considerar os benefícios sociais (tempo de '
               'viagem, emissões, acidentes), avaliar o risco cambial de uma dívida em dólares e prever '
               'medidas de mitigação antes de decidir.'])],
  'espelho': [('a) Requisitos e garantia',
               35,
               [('Ministério da Fazenda; parecer com custo-benefício e interesse social', 10),
                ('Autorização legislativa e recursos no orçamento', 5),
                ('Limites do Senado e regra de ouro', 5),
                ('Externa: autorização específica do Senado', 5),
                ('Garantia: contragarantia de valor igual ou superior e adimplência', 10)]),
              ('b) Ausência no PPA',
               25,
               [('Vedação do art. 167, § 1.º, da CF (crime de responsabilidade)', 10),
                ('Caso: obras de 2027 a 2031; sem PPA, sem dotação', 5),
                ('Solução: lei de inclusão no PPA e previsão na LDO e na LOA', 10)]),
              ('c) Uso na folha',
               30,
               [('Rejeição da sugestão', 5),
                ('Vinculação dos recursos ao objeto', 15),
                ('Regra de ouro; folha é despesa corrente', 5),
                ('Solução: receitas correntes e ajuste da programação', 5)]),
              ('d) Viabilidade',
               30,
               [('VPL positivo à TMA: cria valor no cenário-base', 8),
                ('Sensibilidade: risco alto, não inviabilidade automática', 7),
                ('Recomendação concreta (equilíbrio, cenários, benefícios sociais, câmbio)', 15)])],
  'proposta': ['Para contratar a operação, o Estado precisa ter limites e condições verificados pelo '
               'Ministério da Fazenda, com parecer técnico e jurídico que demonstre custo-benefício e '
               'interesse social, autorização legislativa, inclusão no orçamento, respeito aos limites do '
               'Senado e à regra de ouro e, por ser externa, autorização específica do Senado (LRF, art. 32; '
               'CF, art. 52, V). A garantia da União exige adimplência e contragarantia de valor igual ou '
               'superior, que pode vincular impostos e transferências (LRF, art. 40, § 1.º; CF, art. 167, § '
               '4.º).',
               'Além disso, sem inclusão no PPA, as obras não podem ser iniciadas. A Constituição veda '
               'iniciar investimento plurianual sem prévia inclusão no plano ou lei que a autorize, sob pena '
               'de crime de responsabilidade (art. 167, § 1.º), e a LOA não pode prever dotação para ele '
               '(LRF, art. 5.º, § 5.º). Assim, deve-se aprovar lei que inclua o projeto no PPA e prevê-lo na '
               'LDO e na LOA antes de contratar.',
               'A sugestão do assessor, por sua vez, deve ser rejeitada. Os recursos do empréstimo '
               'vinculam-se ao objeto autorizado (LRF, art. 8.º, parágrafo único), e a regra de ouro limita '
               'o crédito às despesas de capital (CF, art. 167, III). A folha deve ser paga com receitas '
               'correntes e, se faltar caixa, com corte de outros gastos.',
               'Por fim, o estudo indica viabilidade, mas com alto risco de demanda. O VPL positivo à taxa '
               'de 8% mostra que o projeto cria valor no cenário-base, porém a queda de 20% na demanda o '
               'torna negativo. Antes de contratar, convém revisar a demanda projetada, calcular a de '
               'equilíbrio, simular cenários com probabilidades e incluir benefícios sociais e o risco '
               'cambial.'],
  'armadilhas': ['"Externa", "em dólares" e "com garantia da União" pedem autorização específica do Senado, '
                 'contragarantia e atenção ao risco cambial.',
                 'O cenário de demanda 20% menor não manda rejeitar o projeto: manda tratar o risco.'],
  'erros': ['Dizer que o projeto é inviável porque um cenário deu VPL negativo.',
            'Confundir regra de ouro com limite de endividamento do Senado.'],
  'dicas': ['Em Economia, o edital quer raciocínio, não fórmula: explique o que o VPL e a sensibilidade '
            'significam para a decisão.',
            'Quatro itens em 30 linhas: 5 a 8 linhas por item, conforme o que cada pergunta exige.']},
 {'n': 3,
  'titulo': 'Renúncia de ICMS e projeção de receita na reforma tributária',
  'eixo': 'Direito Financeiro (LRF) · Direito Constitucional (sistema tributário e EC n.º 132/2023) · '
          'Economia',
  'porque': 'A reforma tributária está no programa (EC n.º 132/2023) e muda a principal receita do Estado; a '
            'LDO de 2027 já precisa refleti-la.',
  'caso': ['Em 2026, o Estado Gama elabora o projeto da LDO para 2027. Dois fatos chamaram a atenção da '
           'equipe técnica da Secretaria da Fazenda e Planejamento.',
           '<b>Fato 1</b> — a Assembleia aprovou projeto de lei, de iniciativa parlamentar e ainda pendente '
           'de sanção, que prorroga por cinco anos a redução da base de cálculo do ICMS para um setor '
           'industrial, benefício não amparado em convênio do Confaz nem convalidado nos termos da LC n.º '
           '160/2017, sem estimativa de impacto orçamentário-financeiro e sem medida de compensação.',
           '<b>Fato 2</b> — a projeção da receita de ICMS que alimenta o anexo de metas fiscais (2027 a '
           '2029) e o cenário fiscal de médio prazo do Estado (até 2034) repete o crescimento médio dos '
           'últimos dez anos e não considera a substituição gradual do ICMS pelo Imposto sobre Bens e '
           'Serviços (IBS).',
           'Questionado, o secretário afirmou que "como o ICMS vai acabar, perder arrecadação agora não faz '
           'diferença".'],
  'comando': 'Tendo em vista a situação narrada, na condição de Analista em Planejamento, Orçamento e '
             'Finanças Públicas, responda, justificadamente:',
  'itens': ['O benefício do fato 1 atende aos requisitos legais e constitucionais para a sua concessão? Que '
            'providência cabe ao Poder Executivo?',
            'A projeção de receita do fato 2 está adequada às normas de projeção de receita e à transição da '
            'reforma tributária? O que deve ser feito?',
            'A afirmação do secretário está correta? Qual é a recomendação técnica?'],
  'esqueleto': [('a) · N linhas',
                 'Resposta: não; vetar · LRF, art. 14: estimativa no exercício e nos dois seguintes + LDO + '
                 'metas ou compensação · ADCT, art. 113 (STF: vale para os Estados) · CF, art. 155, § 2.º, '
                 'XII, g: convênio no Confaz · providência: veto.'),
                ('b) · N linhas',
                 'Resposta: não; refazer · LRF, art. 12 · EC n.º 132/2023: ICMS a 90%, 80%, 70% e 60% de '
                 '2029 a 2032, extinto em 2033; IBS compartilhado, no destino · solução: separar ICMS e IBS, '
                 'com cenários e memória de cálculo.'),
                ('c) · N linhas',
                 'Resposta: não; afirmação errada · ICMS é a principal receita até 2032 · efeitos: caixa, '
                 'cota-parte, mínimos de saúde e educação · gasto tributário: custo-benefício · solução: '
                 'veto; nova proposta com requisitos, prazo e indicadores.')],
  'padrao': [('a) Requisitos da renúncia',
              ['A concessão ou ampliação de benefício tributário que implique renúncia deve vir com '
               'estimativa do impacto no exercício de início de vigência e nos dois seguintes, atender à LDO '
               'e demonstrar que a renúncia foi considerada na estimativa da receita e não afeta as metas '
               'fiscais, ou vir acompanhada de medidas de compensação por aumento de receita (LRF, art. 14).',
               'A proposição legislativa que crie ou altere renúncia deve trazer estimativa de impacto '
               '(ADCT, art. 113, aplicado pelo STF a todos os entes).',
               'Benefício de ICMS depende de deliberação dos Estados e do Distrito Federal, na forma de lei '
               'complementar (CF, art. 155, § 2.º, XII, g — convênio no Confaz).',
               'Solução: faltam estimativa, compensação e convênio. Cabe à Secretaria propor ao governador o '
               'veto, por inconstitucionalidade e por contrariedade ao interesse público.']),
             ('b) Projeção na reforma',
              ['As previsões de receita devem considerar os efeitos das alterações na legislação, da '
               'variação de preços e do crescimento econômico, com metodologia de cálculo e premissas (LRF, '
               'art. 12); no anexo de metas fiscais, exige-se memória e metodologia de cálculo (art. 4.º, § '
               '2.º, II).',
               'A EC n.º 132/2023 cria o IBS, de competência compartilhada entre Estados, Distrito Federal e '
               'municípios (CF, art. 156-A), cobrado no destino, e fixa as alíquotas do ICMS em 9/10, 8/10, '
               '7/10 e 6/10 das vigentes de 2029 a 2032 (ADCT, art. 128), até sua extinção em 2033.',
               'Solução: a média histórica ignora a transição, que já alcança 2029 (último ano do anexo) e '
               'todo o cenário até 2034. A projeção deve ser refeita separando ICMS e IBS, com cenários e '
               'com memória e metodologia de cálculo no anexo de metas fiscais.']),
             ('c) Afirmação do secretário',
              ['O ICMS continua sendo a principal receita própria do Estado até 2032; a renúncia reduz, já '
               'nos próximos exercícios, o caixa, a cota-parte dos municípios (CF, art. 158, IV) e a base '
               'dos mínimos constitucionais de saúde e educação.',
               'Renúncia é gasto tributário: só se justifica se o retorno econômico e social superar o '
               'custo, o que deve ser demonstrado e avaliado com indicadores.',
               'Recomendação: veto da prorrogação; em eventual nova proposta, exigir estimativa, '
               'compensação, convênio, prazo e indicadores de avaliação.'])],
  'espelho': [('a) Requisitos da renúncia',
               40,
               [('Requisitos do art. 14 da LRF (estimativa no exercício e nos dois seguintes, '
                 'compatibilidade com a LDO, não afetar metas ou compensação)',
                 15),
                ('Estimativa de impacto na proposição (ADCT, art. 113, aplicável aos Estados)', 5),
                ('Benefício de ICMS depende de convênio no Confaz', 10),
                ('Aplicação e providência: faltam estimativa, compensação e convênio; veto', 10)]),
              ('b) Projeção de receita',
               40,
               [('Previsão deve considerar alterações na legislação (LRF, art. 12) e trazer memória de '
                 'cálculo',
                 10),
                ('Transição: alíquotas do ICMS reduzidas de 2029 a 2032, extinção em 2033; IBS compartilhado '
                 'e no destino',
                 20),
                ('Solução: refazer separando ICMS e IBS, com cenários e metodologia', 10)]),
              ('c) Afirmação do secretário',
               40,
               [('ICMS segue como principal receita até 2032; efeitos da renúncia (caixa, cota-parte, '
                 'mínimos de saúde e educação)',
                 15),
                ('Renúncia como gasto tributário: justificar e avaliar o custo-benefício', 10),
                ('Recomendação concreta (veto; nova proposta com requisitos, prazo e indicadores)', 15)])],
  'proposta': ['O benefício do fato 1 não atende aos requisitos legais e constitucionais, e o projeto deve '
               'ser vetado. A LRF, art. 14, exige estimativa do impacto no ano de início e nos dois '
               'seguintes, compatibilidade com a LDO e neutralidade nas metas ou compensação por aumento de '
               'receita; o ADCT, art. 113, aplicável aos Estados segundo o STF, exige a estimativa na '
               'própria proposição. Além disso, benefício de ICMS depende de convênio no Confaz (CF, art. '
               '155, § 2.º, XII, g). No caso, faltam estimativa, compensação e convênio; cabe à Secretaria '
               'propor ao governador o veto por inconstitucionalidade e contrariedade ao interesse público.',
               'Da mesma forma, a projeção do fato 2 está inadequada e deve ser refeita. A LRF, art. 12, '
               'manda considerar as alterações na legislação. Pela EC n.º 132/2023, as alíquotas do ICMS '
               'cairão a 90%, 80%, 70% e 60% de 2029 a 2032, e o imposto será extinto em 2033, substituído '
               'pelo IBS, compartilhado com os municípios e cobrado no destino. A média histórica ignora '
               'essa transição, que já atinge 2029, último ano do anexo, e todo o cenário até 2034. A nova '
               'projeção deve separar ICMS e IBS, com cenários, memória e metodologia de cálculo (LRF, art. '
               '4.º, § 2.º, II).',
               'Por fim, a afirmação do secretário está errada, e a recomendação é não prorrogar o '
               'benefício. Até 2032, o ICMS segue como principal receita própria, e a renúncia reduz, nos '
               'próximos exercícios, o caixa, a cota-parte dos municípios e a base dos mínimos de saúde e '
               'educação. Como gasto tributário, o benefício só se justifica se o retorno superar o custo. '
               'Assim, recomenda-se o veto e, em nova proposta, exigir estimativa, compensação, convênio, '
               'prazo e indicadores de avaliação.'],
  'armadilhas': ['"Iniciativa parlamentar" não afasta o art. 14, e "pendente de sanção" pede a providência '
                 'do Executivo: o veto.',
                 'O fato 2 vai até 2034: o horizonte atravessa toda a transição e o primeiro ano sem ICMS; '
                 'já em 2029, último ano do anexo de metas, começa a redução.'],
  'erros': ['Dizer que o ICMS já foi extinto ou que o IBS é estadual: ele é compartilhado entre Estados, '
            'Distrito Federal e municípios.',
            'Responder ao secretário só com a lei: ele errou no raciocínio econômico, e o edital avalia a '
            'proposta de solução.'],
  'dicas': ['Datas da reforma são o tipo de dado que o corretor confere: alíquotas do ICMS a 90%, 80%, 70% e '
            '60% de 2029 a 2032, extinção em 2033.',
            'Se não lembrar o número do inciso, cite o dispositivo pelo conteúdo: "a Constituição exige '
            'deliberação dos Estados".']},
 {'n': 4,
  'titulo': 'Painel de dados, fracionamento de despesa e LGPD',
  'eixo': 'Fluência de Dados · Administração Pública e Auditoria Governamental · Direito Administrativo (Lei '
          'n.º 14.133/2021, LAI e LGPD)',
  'porque': 'Fluência de Dados tem 8 questões de peso 2 na P1 (item 7.1), o mesmo peso de AFO, Contabilidade '
            'e Direito Financeiro, e o cargo inclui auditoria e controle; o caso cruza dados e norma, como '
            'pede o item 7.3.',
  'caso': ['A Secretaria da Fazenda e Planejamento do Estado Delta implantou um painel que cruza dados de '
           'empenhos, contratos e fornecedores. Na primeira análise, foram identificados três achados.',
           '<b>Achado 1</b> — cerca de 8% dos registros de empenho têm o CPF ou o CNPJ do credor em branco, '
           'e há empenhos duplicados, com o mesmo número e valores diferentes.',
           '<b>Achado 2</b> — uma mesma unidade gestora realizou, em 2026, onze contratações diretas por '
           'dispensa em razão do valor para serviços de manutenção predial, cada uma abaixo do limite legal, '
           'mas que, somadas, o superam com folga.',
           '<b>Achado 3</b> — a área de comunicação pretende publicar, como dados abertos, a lista de '
           'servidores com nome, CPF completo e remuneração.',
           'O secretário pediu orientação sobre a regularidade das situações e o papel de cada área.'],
  'comando': 'Tendo em vista a situação narrada, na condição de Analista em Planejamento, Orçamento e '
             'Finanças Públicas, responda, justificadamente (não há necessidade de mencionar dispositivo '
             'legal):',
  'itens': ['Que dimensões de qualidade de dados o achado 1 compromete, e que cuidados devem ser tomados '
            'antes de tirar conclusões do painel?',
            'As contratações do achado 2 são regulares?',
            'A publicação pretendida no achado 3 pode ser feita? Em que termos?',
            'No Modelo das Três Linhas, que papel cabe a cada linha diante dos achados?'],
  'esqueleto': [('a) · N linhas',
                 'Resposta: completude, unicidade · também consistência · tratar antes de concluir · alerta '
                 '= indício, não prova.'),
                ('b) · N linhas',
                 'Resposta: não; fracionamento · Lei n.º 14.133/2021, art. 75, § 1.º: soma no exercício, por '
                 'unidade gestora, mesmo ramo · solução: apurar, com defesa, e licitar a demanda anual do '
                 'plano de contratações.'),
                ('c) · N linhas',
                 'Resposta: em parte — nome e remuneração, sim; CPF completo, não · LAI + STF (Tema 483) · '
                 'LGPD: necessidade e finalidade · mascarar o CPF, ouvido o encarregado de dados.'),
                ('d) · N linhas',
                 'Resposta: todos agem, cada um no seu papel · 1.ª: gestão corrige · 2.ª: riscos, '
                 'conformidade e dados apoiam, monitoram e questionam · 3.ª: auditoria interna avalia com '
                 'independência e reporta.')],
  'padrao': [('a) Qualidade de dados',
              ['Campos em branco afetam a completude; empenhos duplicados afetam a unicidade; mesmo número '
               'com valores diferentes afeta a consistência.',
               'Antes de concluir, os dados devem ser limpos e tratados (pré-processamento), e o resultado '
               'do painel deve ser lido como indício a confirmar nos documentos, não como prova de '
               'irregularidade.']),
             ('b) Fracionamento',
              ['Para aferir os valores da dispensa, considera-se o somatório do que for despendido no '
               'exercício pela respectiva unidade gestora e o somatório da despesa com objetos de mesma '
               'natureza, isto é, do mesmo ramo de atividade (Lei n.º 14.133/2021, art. 75, § 1.º).',
               'Onze contratações do mesmo objeto, na mesma unidade e no mesmo exercício, que, somadas, '
               'superam o limite, indicam fracionamento. Solução: apurar responsabilidades e planejar '
               'contratação única, por licitação.']),
             ('c) Publicação de dados',
              ['É legítima a publicação, inclusive em sítio eletrônico, do nome do servidor e da remuneração '
               'correspondente (STF, Tema 483 da repercussão geral); a transparência ativa decorre da LAI '
               '(Lei n.º 12.527/2011).',
               'O CPF completo é dado pessoal desnecessário à finalidade de transparência: a LGPD exige '
               'finalidade e necessidade (art. 6.º) e rege o tratamento pelo poder público (art. 23). '
               'Solução: publicar com CPF mascarado ou omitido.']),
             ('d) Três Linhas',
              ['Primeira linha: a gestão, que executa e corrige — saneia os registros, revê as contratações, '
               'ajusta a lista a publicar e responde pelo controle do dia a dia.',
               'Segunda linha: funções de gestão de riscos e conformidade, que apoiam e monitoram — '
               'transformam os achados em alertas permanentes no painel.',
               'Terceira linha: auditoria interna (órgão central de controle interno), que presta avaliação '
               'e assessoria independentes e objetivas sobre os controles e se reporta ao órgão de '
               'governança, sem subordinação à gestão. O Tribunal de Contas faz avaliação externa, fora das '
               'três linhas.'])],
  'espelho': [('a) Qualidade de dados',
               30,
               [('Dimensões: completude (8% sem CPF/CNPJ), unicidade (duplicados) e consistência (mesmo '
                 'número, valores diferentes)',
                 18),
                ('Cautela: tratar os dados antes; alerta é indício a confirmar, não prova', 12)]),
              ('b) Fracionamento',
               30,
               [('Limite aferido pela soma no exercício, por unidade gestora, para objetos do mesmo ramo',
                 15),
                ('Aplicação: onze contratações somadas superam o limite — fracionamento', 8),
                ('Solução: apurar, com defesa dos envolvidos; licitar a demanda anual planejada', 7)]),
              ('c) Publicação',
               30,
               [('Nome e remuneração podem ser publicados (transparência; entendimento do STF)', 12),
                ('CPF completo não: excede a finalidade, fere a necessidade e facilita fraudes', 12),
                ('Solução: publicar com o CPF mascarado, após análise do encarregado de dados', 6)]),
              ('d) Três Linhas',
               30,
               [('1.ª linha (gestão): corrige registros, contratações e a lista', 10),
                ('2.ª linha (riscos, conformidade e proteção de dados): apoia, monitora e questiona; '
                 'transforma achados em controles',
                 10),
                ('3.ª linha (auditoria interna): avalia com independência, sem executar, e reporta à '
                 'governança',
                 10)])],
  'proposta': ['O achado 1 compromete a completude, a unicidade e a consistência dos dados: 8% dos empenhos '
               'sem CPF ou CNPJ não se ligam a nenhum fornecedor, e números repetidos com valores diferentes '
               'impedem saber qual registro vale. Assim, antes de concluir, deve-se sanear os dados na '
               'origem, e os alertas do painel devem ser tratados como indícios a confirmar nos documentos, '
               'não como prova.',
               'Quanto ao achado 2, as contratações são irregulares, pois configuram fracionamento de '
               'despesa. O limite da dispensa é aferido pela soma do que a unidade gestora gasta no '
               'exercício com objetos do mesmo ramo, e as onze contratações de manutenção predial, somadas, '
               'o superam. Deve-se apurar o caso, com defesa dos envolvidos, e licitar a demanda anual '
               'prevista no plano de contratações.',
               'Já a publicação do achado 3 pode ser feita apenas em parte. Nome e remuneração podem ser '
               'divulgados, pois o interesse público no controle do gasto com pessoal prevalece sobre a '
               'privacidade do servidor. O CPF completo, porém, é desnecessário a essa finalidade e facilita '
               'fraudes, sobretudo em dados abertos. A lista deve ser publicada com o CPF mascarado, após '
               'análise do encarregado de dados.',
               'Por fim, no Modelo das Três Linhas, todos agem, cada um no seu papel. A primeira linha, a '
               'gestão, corrige: a área contábil saneia os empenhos; a unidade gestora revê as contratações; '
               'e a comunicação ajusta a lista. A segunda linha, de riscos, conformidade e proteção de '
               'dados, apoia, monitora e questiona, transformando os achados em controles do painel. A '
               'auditoria interna, terceira linha, avalia com independência esses controles, sem '
               'executá-los, e reporta-se ao secretário e ao órgão de governança.'],
  'armadilhas': ['"Cada uma abaixo do limite" é a isca: o limite é aferido pela soma, não por contratação.',
                 'O achado 3 não pede "pode ou não pode": pede o limite. Parte pode ser publicada, parte '
                 'não.'],
  'erros': ['Tratar o alerta do painel como prova de fraude.',
            'Colocar a auditoria interna corrigindo registros: corrigir é da gestão; a auditoria avalia.'],
  'dicas': ['Use os nomes técnicos das dimensões de qualidade: completude, unicidade, consistência, '
            'acurácia, validade.',
            'Quando o enunciado dispensa citar dispositivo, cite a regra pelo conteúdo ("a soma do que a '
            'unidade gasta no exercício"); o número do artigo é opcional.']},
 {'n': 5,
  'titulo': 'Serviço prestado sem empenho e despesa de exercícios anteriores',
  'eixo': 'Administração Financeira e Orçamentária · Contabilidade Aplicada ao Setor Público (MCASP) · '
          'Direito Financeiro',
  'porque': 'AFO e Contabilidade Pública têm peso 2 na P1 e são a base das três áreas; o caso cruza os '
            'enfoques orçamentário e patrimonial.',
  'caso': ['Em fevereiro de 2026, uma secretaria do Estado Épsilon recebeu faturas de serviços de manutenção '
           'predial prestados em novembro e dezembro de 2025, atestados pelo fiscal, sem prévio empenho, '
           'porque o contrato expirara em outubro de 2025 sem prorrogação formalizada durante sua vigência; '
           'não há indício de má-fé da empresa.',
           'As demonstrações contábeis de 2025, já publicadas, não registraram nenhum valor relativo a esses '
           'serviços. Em 2026, o órgão pretende pagar as faturas como despesa de exercícios anteriores, "sem '
           'necessidade de qualquer outro registro".'],
  'comando': 'Tendo em vista a situação narrada, na condição de Analista em Planejamento, Orçamento e '
             'Finanças Públicas, responda, justificadamente:',
  'itens': ['A despesa foi realizada de forma regular? A Administração deve pagar pelos serviços?',
            'O pagamento pode ser feito como despesa de exercícios anteriores? Em que condições?',
            'Como o caso deve ser tratado nos enfoques orçamentário e patrimonial, e quais são os efeitos '
            'nas demonstrações de 2025?',
            'Que providências de correção e de controle devem ser adotadas?'],
  'esqueleto': [('a) · N linhas',
                 'Resposta: irregular, mas indenizar · Lei n.º 4.320/1964, art. 60 · contrato vencido: '
                 'contratação verbal nula (Lei n.º 14.133/2021, art. 95, § 2.º) · art. 149: indenizar o '
                 'executado · responsabilizar quem deu causa.'),
                ('b) · N linhas',
                 'Resposta: sim, mas não "sem outro registro" · art. 37: compromisso reconhecido após o '
                 'encerramento · reconhecimento da dívida, liquidação, dotação em 2026, elemento 92.'),
                ('c) · N linhas',
                 'Resposta: enfoques divergem · orçamentário: 2026 (art. 35, II) · patrimonial: VPD e '
                 'passivo em 2025 · efeitos: passivo subavaliado, PL e resultado superavaliados; Balanço '
                 'Orçamentário intacto.'),
                ('d) · N linhas',
                 'Resposta: retificar e controlar · NBC TSP 23: retificação retrospectiva, ajustes de '
                 'exercícios anteriores, comparativos, nota · sem nova VPD em 2026 · vigência e '
                 'fechamento.')],
  'padrao': [('a) Despesa sem empenho',
              ['É vedada a realização de despesa sem prévio empenho (Lei n.º 4.320/1964, art. 60). A despesa '
               'percorre empenho, liquidação e pagamento (arts. 58 a 65).',
               'O contrato vencido não pode ser prorrogado depois, e a contratação verbal é nula (Lei n.º '
               '14.133/2021, art. 95, § 2.º). Ainda assim, como os serviços foram prestados e atestados, sem '
               'má-fé da empresa, a Administração deve indenizar o executado, vedado o enriquecimento sem '
               'causa (art. 149), sem prejuízo da responsabilização de quem deu causa.']),
             ('b) Despesa de exercícios anteriores',
              ['Podem ser pagos à conta de dotação específica, discriminada por elementos, os compromissos '
               'reconhecidos após o encerramento do exercício correspondente, entre outras hipóteses (Lei '
               'n.º 4.320/1964, art. 37).',
               'Condições: reconhecimento da dívida pela autoridade competente para empenhar, em processo '
               'próprio; liquidação (prova da prestação, valor, credor e preço de mercado — art. 63); '
               'dotação específica em 2026 e empenho no elemento 92. A DEA resolve o orçamento, mas não '
               'dispensa o registro patrimonial.']),
             ('c) Enfoques orçamentário e patrimonial',
              ['No enfoque orçamentário, pertencem ao exercício as despesas nele legalmente empenhadas (Lei '
               'n.º 4.320/1964, art. 35, II): a despesa é de 2026.',
               'No enfoque patrimonial, a variação patrimonial diminutiva e o passivo devem ser reconhecidos '
               'em 2025, quando o serviço foi prestado (regime de competência — MCASP), mesmo sem empenho.',
               'Efeitos em 2025: o Balanço Patrimonial subavaliou o passivo e superavaliou o patrimônio '
               'líquido; a DVP subavaliou as VPD e superavaliou o resultado. O Balanço Orçamentário e o '
               'Balanço Financeiro não foram afetados, pois não houve empenho nem pagamento.']),
             ('d) Correção e controle',
              ['Como as demonstrações de 2025 já foram publicadas, trata-se de erro de exercício anterior: '
               'retificação retrospectiva (NBC TSP 23), com registro do passivo contra ajustes de exercícios '
               'anteriores no patrimônio líquido, reapresentação dos comparativos e nota explicativa.',
               'No empenho e no pagamento de 2026, não se reconhece nova VPD: o passivo apenas é baixado, '
               'sem contar a despesa duas vezes.',
               'Controles: vigência dos contratos com alerta para prorrogar ou licitar a tempo, levantamento '
               'das obrigações sem empenho no fechamento do exercício e responsabilização.'])],
  'espelho': [('a) Despesa sem empenho',
               30,
               [('Irregular: sem prévio empenho (art. 60); contrato vencido não se prorroga, e a contratação '
                 'verbal é nula (art. 95, § 2.º)',
                 12),
                ('Dever de indenizar o executado e comprovado (art. 149), vedado o enriquecimento sem causa',
                 12),
                ('Responsabilização de quem deu causa', 6)]),
              ('b) DEA',
               30,
               [('Enquadramento: compromisso reconhecido após o encerramento do exercício (art. 37)', 10),
                ('Condições: reconhecimento da dívida, liquidação com ateste e preço de mercado, dotação em '
                 '2026, elemento 92',
                 14),
                ('Refutação do "sem qualquer outro registro"', 6)]),
              ('c) Dois enfoques',
               35,
               [('Orçamentário: despesa de 2026, exercício do empenho (art. 35, II)', 8),
                ('Patrimonial: VPD e passivo em 2025, pela competência', 10),
                ('Efeitos: passivo subavaliado; PL e resultado superavaliados', 12),
                ('Balanço Orçamentário não afetado', 5)]),
              ('d) Providências',
               25,
               [('Retificação retrospectiva: ajustes de exercícios anteriores no PL, comparativos e nota '
                 'explicativa',
                 10),
                ('Sem nova VPD no empenho de 2026', 5),
                ('Controles: vigência dos contratos, levantamento no fechamento e responsabilização', 10)])],
  'proposta': ['A despesa foi irregular, mas os serviços devem ser indenizados. O art. 60 da Lei n.º '
               '4.320/1964 veda despesa sem prévio empenho, e o contrato vencido não podia ser prorrogado '
               'depois, o que torna nula a contratação verbal (Lei n.º 14.133/2021, art. 95, § 2.º). Como os '
               'serviços foram prestados, a nulidade não exime o Estado de indenizá-los (art. 149), vedado o '
               'enriquecimento sem causa, e quem deu causa ao vício deve ser responsabilizado.',
               'Por isso, o pagamento pode ser feito como despesa de exercícios anteriores (DEA), mas não '
               '"sem outro registro". Trata-se de compromisso reconhecido após o encerramento do exercício '
               '(art. 37 da Lei n.º 4.320/1964), que exige reconhecimento da dívida pela autoridade '
               'competente, liquidação com ateste do serviço e preço de mercado, dotação específica em 2026 '
               'e empenho no elemento 92.',
               'Além disso, os enfoques orçamentário e patrimonial divergem. No orçamentário, a despesa é de '
               '2026, ano do empenho (art. 35, II). No patrimonial, pela competência, a VPD e o passivo '
               'deveriam ter sido registrados em 2025, ainda sem empenho. Logo, em 2025, o Balanço '
               'Patrimonial subavaliou o passivo e superavaliou o patrimônio líquido, e a DVP superavaliou o '
               'resultado, sem afetar o Balanço Orçamentário.',
               'Diante disso, deve-se corrigir o erro retrospectivamente (NBC TSP 23), registrando o passivo '
               'contra ajustes de exercícios anteriores, no patrimônio líquido, com reapresentação dos '
               'comparativos e nota explicativa; no empenho de 2026, não se reconhece nova VPD. Por fim, '
               'cabe controlar a vigência dos contratos, com alerta para prorrogar ou licitar a tempo, e '
               'levantar obrigações sem empenho no fechamento.'],
  'armadilhas': ['"Sem necessidade de qualquer outro registro" é a isca: a DEA resolve o orçamento, mas não '
                 'o erro de 2025, que, publicado, se corrige retrospectivamente.',
                 'O serviço foi prestado e atestado: negar o pagamento seria enriquecimento sem causa.'],
  'erros': ['Dizer que a despesa pertence a 2025 também no orçamento: pelo art. 35, II, ela é do exercício '
            'do empenho.',
            'Reconhecer nova VPD ao empenhar a DEA em 2026: a despesa seria contada duas vezes.'],
  'dicas': ['Separe os enfoques com conectivos claros: "no enfoque orçamentário...", "no patrimonial...".',
            'Use as siglas só depois de escrever por extenso uma vez, salvo as consagradas (DVP, VPD, PL).']}]
