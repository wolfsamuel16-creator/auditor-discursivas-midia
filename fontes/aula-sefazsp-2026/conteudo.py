# -*- coding: utf-8 -*-
"""Conteúdo das cinco rodadas da aula SEFAZ-SP 2026 (APOFP · FCC), no formato de estudo de caso da FCC."""

RODADAS = [{'n': 1,
  'titulo': 'Frustração de receita no último ano de mandato',
  'eixo': 'Administração Financeira e Orçamentária · Direito Financeiro (LRF) · Contabilidade Pública',
  'porque': '2026 é o último ano dos mandatos estaduais, e a prova cai em 20 de dezembro, às vésperas do encerramento do exercício.',
  'caso': ['O Estado Alfa vive em 2026 o último ano do mandato do governador. O relatório do 4.º bimestre mostrou que a receita realizada, abaixo da prevista, pode não comportar a meta de resultado '
           'primário fixada na Lei de Diretrizes Orçamentárias (LDO). Para enfrentar a situação, a Secretaria da Fazenda e Planejamento do Estado elaborou três propostas.',
           '<b>Proposta 1</b> — limitar empenho de forma linear em todas as despesas do Poder Executivo, inclusive nos repasses constitucionais aos municípios e no pagamento de juros e amortizações '
           'da dívida.',
           '<b>Proposta 2</b> — assinar, em setembro de 2026, contrato de reforma de 200 escolas estaduais, com três parcelas, duas delas a serem pagas em 2027, embora o fluxo de caixa projetado '
           'para 31/12/2026 não tenha saldo para cobri-las.',
           '<b>Proposta 3</b> — inscrever em restos a pagar, no encerramento do exercício, todo o saldo empenhado e não pago, sem verificar a disponibilidade de caixa de cada fonte de recursos.'],
  'comando': 'Tendo em vista a situação narrada, na condição de Analista em Planejamento, Orçamento e Finanças Públicas, responda, justificadamente:',
  'itens': ['A Proposta 1 pode ser adotada? Em que termos a limitação de empenho deve ser feita?',
            'A Proposta 2 é regular? Que solução você propõe?',
            'O que são restos a pagar e quais são suas espécies? Em que condições a inscrição pretendida na Proposta 3 pode ser feita?'],
  'esqueleto': [('a) · N linhas',
                 'Resposta: sim, mas não linear · LRF, art. 9.º: 30 dias após o bimestre, critérios da LDO · § 2.º: obrigações constitucionais e legais e serviço da dívida ficam fora · solução: '
                 'preservar repasses e dívida; cortar discricionárias.'),
                ('b) · N linhas',
                 'Resposta: não, é irregular · LRF, art. 42: dois últimos quadrimestres + parcelas sem caixa · fato: setembro, parcelas em 2027, sem saldo · solução: ajustar ao caixa ou adiar · CP, '
                 'art. 359-C.'),
                ('c) · N linhas',
                 'Resposta: conceito + espécies; só com lastro · Lei n.º 4.320/1964, art. 36: processados × não processados · LRF, arts. 50, I, e 55, III, b: caixa por fonte · solução: cancelar '
                 'empenhos não liquidados sem caixa.')],
  'padrao': [('a) Proposta 1',
              ['Se a realização da receita puder não comportar o cumprimento das metas de resultado primário ou nominal, os Poderes e o Ministério Público promovem, por ato próprio e nos trinta dias '
               'subsequentes, limitação de empenho e movimentação financeira, segundo os critérios fixados pela LDO (LC n.º 101/2000, art. 9.º).',
               'Não são objeto de limitação as despesas que constituam obrigações constitucionais e legais do ente, inclusive as destinadas ao serviço da dívida, e as ressalvadas pela LDO (art. 9.º, '
               '§ 2.º).',
               'Solução: a limitação é cabível, mas não linear. Repasses constitucionais aos municípios e serviço da dívida devem ser preservados; o corte recai sobre despesas discricionárias. '
               'Recuperada a receita, a recomposição das dotações é proporcional às reduções (art. 9.º, § 1.º).']),
             ('b) Proposta 2',
              ['É vedado ao titular de Poder ou órgão, nos dois últimos quadrimestres do mandato, contrair obrigação de despesa que não possa ser cumprida integralmente dentro dele, ou que tenha '
               'parcelas a pagar no exercício seguinte sem suficiente disponibilidade de caixa (LRF, art. 42).',
               'Na apuração do caixa, consideram-se os encargos e as despesas compromissadas a pagar até o final do exercício (art. 42, parágrafo único).',
               'Solução: se firmado em setembro (dentro do período) e com parcelas em 2027 sem saldo, o contrato não pode ser firmado como proposto: deve ser reduzido ao que couber no caixa do '
               'exercício ou adiado. Correlato penal: Código Penal, art. 359-C.']),
             ('c) Proposta 3',
              ['Restos a pagar são as despesas empenhadas e não pagas até 31 de dezembro, distinguindo-se as processadas (já liquidadas) das não processadas (pendentes de liquidação) (Lei n.º '
               '4.320/1964, art. 36).',
               'A disponibilidade de caixa é registrada por fonte, de modo que os recursos vinculados fiquem identificados (LRF, art. 50, I), e recurso vinculado só atende ao seu objeto (art. 8.º, '
               'parágrafo único).',
               'Solução: os restos a pagar não processados só podem ser inscritos até o limite do saldo de caixa de cada fonte, demonstrado no Relatório de Gestão Fiscal (RGF) do último '
               'quadrimestre (LRF, art. 55, III, b), regra que o art. 42 reforça no último ano de mandato. Empenhos não liquidados sem cobertura devem ser cancelados; os processados, que já são obrigação do ente, têm '
               'prioridade.'])],
  'espelho': [('a) Limitação de empenho',
               40,
               [('Gatilho: a receita pode não comportar as metas fiscais; limitação nos 30 dias seguintes ao bimestre, por ato próprio, pelos critérios da LDO', 15),
                ('Despesas protegidas: obrigações constitucionais e legais e serviço da dívida (repasses aos municípios, juros e amortizações)', 15),
                ('Solução: corte nas discricionárias, sem linearidade; recomposição proporcional se a receita se recuperar', 10)]),
              ('b) Contrato de reforma',
               40,
               [('Vedação do art. 42: dois últimos quadrimestres, obrigação não cumprida no mandato ou com parcelas no exercício seguinte sem caixa', 20),
                ('Enquadramento do fato: setembro de 2026, parcelas em 2027, sem saldo — irregular', 10),
                ('Solução: reduzir ao que couber no caixa ou adiar (crime do CP, art. 359-C)', 10)]),
              ('c) Restos a pagar',
               40,
               [('Conceito: despesas empenhadas e não pagas até 31/12', 10),
                ('Espécies: processados (liquidados) e não processados', 10),
                ('Condição: não processados só até o saldo de caixa de cada fonte (reforçada pelo art. 42 no último ano)', 10),
                ('Solução: cancelar empenhos não liquidados sem cobertura; priorizar processados', 10)])],
  'proposta': ['A Proposta 1 só pode ser adotada se a limitação não for linear. Pelo art. 9.º da LRF, se a receita puder não comportar as metas, os Poderes e o Ministério Público limitam empenho '
               'e movimentação financeira nos trinta dias seguintes ao fim do bimestre, pelos critérios da LDO; no caso, logo após o 4.º bimestre. O § 2.º exclui as obrigações constitucionais e '
               'legais e o serviço da dívida: repasses aos municípios, juros e amortizações devem ser preservados, e o corte deve recair sobre despesas discricionárias, recompostas se a receita se '
               'recuperar (§ 1.º).',
               'A Proposta 2 é irregular. O art. 42 da LRF veda ao titular de Poder, nos dois últimos quadrimestres do mandato, contrair obrigação que não possa ser cumprida integralmente dentro '
               'dele ou que tenha parcelas no exercício seguinte sem caixa, computadas as despesas compromissadas até o fim do exercício. Se firmado em setembro, com parcelas em 2027 e sem saldo, o '
               'ajuste deve ser reduzido ao que couber no caixa ou adiado, sob pena de configurar o crime do art. 359-C do Código Penal.',
               'Restos a pagar são as despesas empenhadas e não pagas até 31 de dezembro: processados, se liquidados, ou não processados, se pendentes de liquidação (Lei n.º 4.320/1964, art. 36). '
               'A Proposta 3 não pode ser adotada como está: os não processados só podem ser inscritos até o saldo de caixa de cada fonte (LRF, arts. 50, I, e 55, III, b), exigência reforçada pelo art. 42 no último ano de mandato. '
               'Recomenda-se cancelar os empenhos não liquidados sem cobertura e priorizar os processados, que já são obrigação do ente.'],
  'armadilhas': ['O enunciado lista repasses aos municípios e dívida de propósito: é exatamente o que o § 2.º do art. 9.º protege.',
                 '"Setembro" está no texto para você enquadrar o período do art. 42 (a partir de 1.º de maio).'],
  'erros': ['Concluir que a LRF proíbe qualquer despesa no fim do mandato: proíbe a obrigação sem caixa.',
            'Tratar restos a pagar como uma espécie só. Processados e não processados têm tratamento diferente na hora de cancelar.'],
  'dicas': ['Comece cada item respondendo à pergunta ("A Proposta 2 é irregular.") e feche com a solução: o edital avalia a proposta de solução, não só o conceito.',
            'O item c tem três perguntas dentro dele (conceito, espécies e condição): responda às três, na ordem.']},
 {'n': 2,
  'titulo': 'Operação de crédito para uma linha de metrô',
  'eixo': 'Direito Financeiro (operações de crédito, regra de ouro) · AFO (PPA) · Economia (avaliação de projetos)',
  'porque': 'Junta três disciplinas de peso no edital e dialoga com a atribuição do cargo de cuidar de garantias, obrigações do Tesouro e política creditícia.',
  'caso': ['O Estado Beta pretende contratar operação de crédito externa, com garantia da União, para financiar a construção de uma nova linha de metrô, com obras previstas de 2027 a 2031. O projeto '
           'não consta do Plano Plurianual (PPA) vigente.',
           'O estudo de viabilidade, feito com taxa mínima de atratividade de 8% ao ano, apresentou valor presente líquido (VPL) positivo no cenário-base, mas negativo no cenário em que a demanda de '
           'passageiros fica 20% abaixo da projetada.',
           'Em reunião, um assessor sugeriu destinar parte do empréstimo ao pagamento da folha de dezembro, "já que o dinheiro estará em caixa".'],
  'comando': 'Tendo em vista a situação narrada, na condição de Analista em Planejamento, Orçamento e Finanças Públicas, responda, justificadamente:',
  'itens': ['Que requisitos devem ser cumpridos para contratar a operação e obter a garantia da União?',
            'Que consequência tem o fato de o projeto não constar do PPA, e o que deve ser feito?',
            'A sugestão do assessor pode ser acolhida?',
            'Como deve ser interpretado o estudo de viabilidade, e qual é a recomendação técnica?'],
  'esqueleto': [('a) · N linhas',
                 'Resposta: contratação possível, cumpridos os requisitos · LRF, art. 32: Ministério da Fazenda, parecer de custo-benefício, autorização em lei, inclusão no orçamento, limites do '
                 'Senado, autorização específica do Senado (externa) · art. 40: contragarantia e adimplência.'),
                ('b) · N linhas',
                 'Resposta: incluir antes de iniciar · CF, art. 167, § 1.º: investimento plurianual sem PPA = crime de responsabilidade · solução: revisão do PPA ou lei que autorize a inclusão.'),
                ('c) · N linhas', 'Resposta: não · recurso vinculado ao objeto (LRF, art. 8.º, parágrafo único) · regra de ouro (CF, art. 167, III) e sua razão · folha com receita corrente.'),
                ('d) · N linhas', 'Resposta: viável, mas sensível à demanda · VPL > 0 à TMA · sensibilidade = risco · solução: revisar demanda, cenários, benefícios sociais.')],
  'padrao': [('a) Requisitos e garantia',
              ['O Ministério da Fazenda verifica os limites e condições da operação (LRF, art. 32). O pleito vem instruído com parecer técnico e jurídico que demonstre a relação custo-benefício e o '
               'interesse econômico e social da operação, e exigem-se prévia e expressa autorização na lei orçamentária, em créditos adicionais ou em lei específica; inclusão dos recursos no '
               'orçamento; observância dos limites e condições do Senado; autorização específica do Senado, na operação externa; e respeito à regra de ouro (art. 32, § 1.º, I a V; CF, art. 52, V).',
               'A garantia da União depende de contragarantia em valor igual ou superior ao da garantia e da adimplência do Estado com o garantidor (LRF, art. 40, § 1.º). O Estado pode vincular '
               'receitas próprias e transferências como contragarantia (CF, art. 167, § 4.º).']),
             ('b) Ausência no PPA',
              ['Nenhum investimento cuja execução ultrapasse um exercício financeiro pode ser iniciado sem prévia inclusão no PPA, ou sem lei que autorize a inclusão, sob pena de crime de '
               'responsabilidade (CF, art. 167, § 1.º).',
               'Solução: as obras vão de 2027 a 2031; antes do início, o Estado deve rever o PPA ou aprovar lei que autorize a inclusão do projeto.']),
             ('c) Recursos na folha',
              ['A Constituição veda operações de crédito que excedam as despesas de capital, ressalvadas as autorizadas por créditos suplementares ou especiais com finalidade precisa, aprovados por '
               'maioria absoluta (CF, art. 167, III — regra de ouro; LRF, art. 32, § 1.º, V). É um limite agregado do exercício, cuja razão é impedir que o endividamento financie despesa corrente.',
               'O que impede este uso específico é a vinculação: os recursos da operação estão vinculados ao objeto autorizado em lei e no contrato e só podem atendê-lo (LRF, art. 8.º, parágrafo '
               'único). A sugestão deve ser rejeitada.']),
             ('d) Estudo de viabilidade',
              ['VPL positivo à taxa mínima de atratividade indica que o projeto cria valor no cenário-base; a análise de sensibilidade mostra que a viabilidade depende da demanda, que é o risco '
               'central.',
               'Recomendação: revisar as premissas de demanda, montar cenários com probabilidades, incorporar os benefícios sociais (tempo de viagem, emissões, acidentes) numa análise '
               'custo-benefício e prever medidas de mitigação antes de decidir.'])],
  'espelho': [('a) Requisitos e garantia',
               30,
               [('Requisitos do art. 32 da LRF (verificação pelo Ministério da Fazenda, autorização legislativa, inclusão no orçamento, limites do Senado, parecer de custo-benefício)', 15),
                ('Autorização específica do Senado, por ser operação externa', 5),
                ('Garantia: contragarantia suficiente e adimplência (art. 40, § 1.º)', 10)]),
              ('b) Ausência no PPA',
               30,
               [('Vedação de iniciar investimento plurianual sem inclusão no PPA (CF, art. 167, § 1.º)', 15),
                ('Consequência: crime de responsabilidade', 5),
                ('Solução: revisão do PPA ou lei que autorize a inclusão antes das obras', 10)]),
              ('c) Uso na folha',
               30,
               [('Rejeição da sugestão', 5), ('Vinculação dos recursos ao objeto da operação', 15), ('Regra de ouro e sua finalidade (endividamento não financia despesa corrente)', 10)]),
              ('d) Viabilidade',
               30,
               [('VPL positivo à TMA de 8%: o projeto cria valor no cenário-base', 10),
                ('Sensibilidade: com demanda 20% menor o VPL fica negativo — risco central', 10),
                ('Recomendação concreta (revisar demanda, cenários, benefícios sociais)', 10)])],
  'proposta': ['A operação pode ser contratada, cumpridos os requisitos legais. Pelo art. 32 da LRF, o Ministério da Fazenda verifica limites e condições, e exigem-se parecer com a relação '
               'custo-benefício, autorização em lei, inclusão no orçamento, limites do Senado e, por ser externa, autorização específica do Senado. A garantia da União exige contragarantia '
               'suficiente, que pode vincular receitas próprias e transferências, e adimplência do Estado (LRF, art. 40, § 1.º; CF, art. 167, § 4.º).',
               'Enquanto o projeto não constar do PPA, as obras não podem ser iniciadas. O art. 167, § 1.º, da Constituição veda iniciar investimento que ultrapasse um exercício sem prévia inclusão no plano, '
               'sob pena de crime de responsabilidade. Como as obras vão de 2027 a 2031, o Estado deve rever o PPA ou aprovar lei que autorize a inclusão antes de iniciá-las.',
               'A sugestão do assessor deve ser rejeitada. Os recursos da operação estão vinculados ao objeto autorizado e só podem atendê-lo (LRF, art. 8.º, parágrafo único), e a regra de ouro '
               '(CF, art. 167, III) existe justamente para que o endividamento não financie despesa corrente. Os recursos devem ser aplicados nas obras, e a folha deve ser coberta por receitas '
               'correntes ou pela limitação de outras despesas.',
               'O estudo indica viabilidade, mas com risco relevante. O VPL positivo à taxa mínima de atratividade de 8% mostra que o projeto cria valor no cenário-base, mas basta a demanda cair '
               '20% para o VPL ficar negativo. Recomenda-se revisar essa premissa, calcular a demanda de equilíbrio, simular cenários com probabilidades e incluir os benefícios sociais antes da '
               'contratação.'],
  'armadilhas': ['"Externa" e "com garantia da União" acrescentam dois requisitos: autorização específica do Senado e contragarantia.',
                 'O cenário de demanda 20% menor não manda rejeitar o projeto: manda tratar o risco.'],
  'erros': ['Dizer que o projeto é inviável porque um cenário deu VPL negativo.', 'Confundir regra de ouro com limite de endividamento do Senado.'],
  'dicas': ['Em Economia, o edital quer raciocínio, não fórmula: explique o que o VPL e a sensibilidade significam para a decisão.',
            'Quatro itens em 30 linhas: 5 a 8 linhas por item, conforme o que cada pergunta exige.']},
 {'n': 3,
  'titulo': 'Renúncia de ICMS e projeção de receita na reforma tributária',
  'eixo': 'Direito Financeiro (LRF) · Direito Constitucional (sistema tributário e EC n.º 132/2023) · Economia',
  'porque': 'A reforma tributária está no programa (EC n.º 132/2023) e muda a principal receita do Estado; a LDO de 2027 já precisa refleti-la.',
  'caso': ['Em 2026, o Estado Gama elabora o projeto da LDO para 2027. Dois fatos chamaram a atenção da equipe técnica da Secretaria da Fazenda e Planejamento.',
           '<b>Fato 1</b> — a Assembleia aprovou projeto de lei, de iniciativa parlamentar e ainda pendente de sanção, que prorroga por cinco anos a redução da base de cálculo do ICMS para um setor '
           'industrial, sem estimativa de impacto orçamentário-financeiro, sem medida de compensação e sem convênio celebrado no âmbito do Confaz.',
           '<b>Fato 2</b> — a projeção da receita de ICMS que alimenta o anexo de metas fiscais (2027 a 2029) e o cenário fiscal de médio prazo do Estado (até 2034) repete o crescimento médio dos '
           'últimos dez anos e não considera a substituição gradual do ICMS pelo Imposto sobre Bens e Serviços (IBS).',
           'Questionado, o secretário afirmou que "como o ICMS vai acabar, perder arrecadação agora não faz diferença".'],
  'comando': 'Tendo em vista a situação narrada, na condição de Analista em Planejamento, Orçamento e Finanças Públicas, responda, justificadamente:',
  'itens': ['O benefício do fato 1 atende aos requisitos legais e constitucionais para a sua concessão?',
            'A projeção de receita do fato 2 está adequada às regras da reforma tributária? O que deve ser feito?',
            'A afirmação do secretário está correta? Qual é a recomendação técnica?'],
  'esqueleto': [('a) · N linhas',
                 'Resposta: não; benefício irregular · LRF, art. 14: estimativa no exercício e nos dois seguintes + LDO + não afetar metas ou compensação · ADCT, art. 113 · CF, art. 155, § 2.º, XII, '
                 'g: deliberação dos Estados (Confaz).'),
                ('b) · N linhas',
                 'Resposta: não; projeção inadequada · LRF, art. 12: efeitos das alterações na legislação · EC n.º 132/2023: IBS compartilhado, no destino; ICMS reduzido de 2029 a 2032, extinto em '
                 '2033 · solução: refazer com cenários e memória de cálculo.'),
                ('c) · N linhas',
                 'Resposta: não; afirmação errada · ICMS financia o Estado até 2032 · renúncia = gasto tributário, avaliar custo-benefício · elasticidade da receita · solução: não sancionar/rever, '
                 'monitorar.')],
  'padrao': [('a) Requisitos da renúncia',
              ['A concessão ou ampliação de benefício tributário que implique renúncia deve vir com estimativa do impacto no exercício de início de vigência e nos dois seguintes, atender à LDO e '
               'demonstrar que a renúncia foi considerada na estimativa da receita e não afeta as metas fiscais, ou vir acompanhada de medidas de compensação por aumento de receita (LRF, art. 14).',
               'A proposição legislativa que crie ou altere renúncia deve trazer estimativa de impacto (ADCT, art. 113, aplicado pelo STF a todos os entes).',
               'Benefício de ICMS depende de deliberação dos Estados e do Distrito Federal, na forma de lei complementar (CF, art. 155, § 2.º, XII, g — convênio no Confaz).']),
             ('b) Projeção na reforma',
              ['As previsões de receita devem considerar os efeitos das alterações na legislação, da variação de preços e do crescimento econômico, com metodologia de cálculo e premissas (LRF, art. '
               '12); no anexo de metas fiscais, exige-se memória e metodologia de cálculo (art. 4.º, § 2.º, II).',
               'A EC n.º 132/2023 cria o IBS, de competência compartilhada entre Estados, Distrito Federal e municípios (CF, art. 156-A), cobrado no destino, e reduz o ICMS gradualmente de 2029 a '
               '2032, até sua extinção em 2033.',
               'Solução: refazer a projeção de 2029 em diante com a transição e com cenários, explicitando a metodologia no anexo de metas fiscais.']),
             ('c) Afirmação do secretário',
              ['O ICMS continua sendo a principal receita própria do Estado até o fim da transição; a renúncia reduz recursos já nos próximos exercícios e pressiona as metas.',
               'Renúncia é gasto tributário: deve ser avaliada pela relação custo-benefício e pela elasticidade da receita em relação à atividade econômica, não presumida neutra.',
               'Recomendação: apontar os vícios, propor a revisão ou o veto da prorrogação e monitorar o benefício com indicadores de resultado.'])],
  'espelho': [('a) Requisitos da renúncia',
               40,
               [('Requisitos do art. 14 da LRF (estimativa no exercício e nos dois seguintes, compatibilidade com a LDO, não afetar metas ou compensação)', 20),
                ('Estimativa de impacto na proposição (ADCT, art. 113)', 5),
                ('Benefício de ICMS depende de deliberação dos Estados e do DF (Confaz)', 10),
                ('Conclusão aplicada: faltam estimativa, compensação e convênio', 5)]),
              ('b) Projeção de receita',
               40,
               [('Previsão deve considerar alterações na legislação (LRF, art. 12)', 10),
                ('Transição: ICMS reduzido de 2029 a 2032, extinto em 2033; IBS compartilhado e no destino', 20),
                ('Solução: refazer com cenários, memória e metodologia de cálculo', 10)]),
              ('c) Afirmação do secretário',
               40,
               [('ICMS segue como principal receita própria na transição; a renúncia reduz recursos já', 15),
                ('Renúncia como gasto tributário: avaliação de custo-benefício e elasticidade da receita', 15),
                ('Recomendação concreta (apontar vícios, rever a prorrogação, monitorar)', 10)])],
  'proposta': ['O benefício do fato 1 não atende aos requisitos e é irregular. Nos termos do art. 14 da LRF, a renúncia de receita exige estimativa do impacto no exercício e nos dois seguintes, '
               'compatibilidade com a LDO e demonstração de que não afeta as metas fiscais, ou medidas de compensação por aumento de receita. O art. 113 do ADCT também exige estimativa de impacto na '
               'proposição. Além disso, benefício de ICMS depende de deliberação dos Estados e do Distrito Federal, por convênio no Confaz (CF, art. 155, § 2.º, XII, g). No caso, não há estimativa, '
               'compensação nem convênio, o que vicia a renúncia e expõe as metas fiscais.',
               'A projeção do fato 2 não está adequada. O art. 12 da LRF manda considerar os efeitos das alterações na legislação. Pela EC n.º 132/2023, o ICMS será reduzido de 2029 a 2032 e '
               'extinto em 2033, substituído pelo IBS, compartilhado com os municípios e cobrado no destino. Repetir a média histórica ignora essa transição, que começa em 2029, último ano do anexo, '
               'e atravessa todo o horizonte até 2034. A projeção deve ser refeita com cenários de transição, com a memória e a metodologia de cálculo exigidas para o anexo de metas fiscais (LRF, '
               'art. 4.º, § 2.º, II).',
               'A afirmação do secretário está errada. Até 2032, o ICMS segue como principal receita própria, e a renúncia reduz recursos já nos próximos exercícios. Por ser gasto tributário, a '
               'renúncia deve ser avaliada pela relação custo-benefício, considerando a elasticidade da receita em relação à atividade econômica: o benefício só se justifica se o retorno superar o '
               'custo. Recomenda-se apontar os vícios, propor a revisão da prorrogação e monitorar o benefício por indicadores.'],
  'armadilhas': ['"Iniciativa parlamentar" não afasta o art. 14: a LRF vale para a renúncia, venha de quem vier.',
                 'O fato 2 vai até 2034: o horizonte atravessa toda a transição e o primeiro ano sem ICMS; já em 2029, último ano do anexo de metas, começa a redução.'],
  'erros': ['Dizer que o ICMS já foi extinto ou que o IBS é estadual: ele é compartilhado entre Estados, Distrito Federal e municípios.',
            'Responder ao secretário só com a lei: ele errou no raciocínio econômico, e o edital avalia a proposta de solução.'],
  'dicas': ['Datas da reforma são o tipo de dado que o corretor confere: 2029 a 2032 de redução, extinção em 2033.',
            'Se não lembrar o número do inciso, cite o dispositivo pelo conteúdo: "a Constituição exige deliberação dos Estados".']},
 {'n': 4,
  'titulo': 'Painel de dados, fracionamento de despesa e LGPD',
  'eixo': 'Fluência de Dados · Administração Pública e Auditoria Governamental · Direito Administrativo (Lei n.º 14.133/2021, LAI e LGPD)',
  'porque': 'Fluência de Dados tem 8 questões de peso 2 na P1 (item 7.1), o mesmo peso de AFO, Contabilidade e Direito Financeiro, e o cargo inclui auditoria e controle; o caso cruza dados e norma, '
            'como pede o item 7.3.',
  'caso': ['A Secretaria da Fazenda e Planejamento do Estado Delta implantou um painel que cruza dados de empenhos, contratos e fornecedores. Na primeira análise, foram identificados três achados.',
           '<b>Achado 1</b> — cerca de 8% dos registros de empenho têm o CPF ou o CNPJ do credor em branco, e há empenhos duplicados, com o mesmo número e valores diferentes.',
           '<b>Achado 2</b> — uma mesma unidade gestora realizou, em 2026, onze contratações diretas por dispensa em razão do valor para serviços de manutenção predial, cada uma abaixo do limite '
           'legal, mas que, somadas, o superam com folga.',
           '<b>Achado 3</b> — a área de comunicação pretende publicar, como dados abertos, a lista de servidores com nome, CPF completo e remuneração.',
           'O secretário pediu orientação sobre quem deve agir em cada achado.'],
  'comando': 'Tendo em vista a situação narrada, na condição de Analista em Planejamento, Orçamento e Finanças Públicas, responda, justificadamente (não há necessidade de mencionar dispositivo '
             'legal):',
  'itens': ['Que dimensões de qualidade de dados o achado 1 compromete, e que cuidado se deve ter antes de tirar conclusões do painel?',
            'As contratações do achado 2 são regulares?',
            'A publicação pretendida no achado 3 pode ser feita? Em que termos?',
            'No Modelo das Três Linhas, quem deve agir em relação aos achados, e como?'],
  'esqueleto': [('a) · N linhas', 'Resposta: completude, unicidade · também consistência · tratar antes de concluir · alerta = indício, não prova.'),
                ('b) · N linhas',
                 'Resposta: não; indício de fracionamento · Lei n.º 14.133/2021, art. 75, § 1.º: soma no exercício, por unidade gestora, mesmo ramo · solução: apurar e contratação única por '
                 'licitação.'),
                ('c) · N linhas', 'Resposta: em parte — nome e remuneração, sim; CPF completo, não · LAI + STF (Tema 483) · LGPD: necessidade e finalidade · mascarar o CPF.'),
                ('d) · N linhas', 'Resposta: cada linha tem um papel · 1.ª: gestão corrige · 2.ª: riscos/conformidade monitora e cria alertas · 3.ª: auditoria interna avalia com independência.')],
  'padrao': [('a) Qualidade de dados',
              ['Campos em branco afetam a completude; empenhos duplicados afetam a unicidade; mesmo número com valores diferentes afeta a consistência.',
               'Antes de concluir, os dados devem ser limpos e tratados (pré-processamento), e o resultado do painel deve ser lido como indício a confirmar nos documentos, não como prova de '
               'irregularidade.']),
             ('b) Fracionamento',
              ['Para aferir os valores da dispensa, considera-se o somatório do que for despendido no exercício pela respectiva unidade gestora e o somatório da despesa com objetos de mesma '
               'natureza, isto é, do mesmo ramo de atividade (Lei n.º 14.133/2021, art. 75, § 1.º).',
               'Onze contratações do mesmo objeto, na mesma unidade e no mesmo exercício, que, somadas, superam o limite, indicam fracionamento. Solução: apurar responsabilidades e planejar '
               'contratação única, por licitação.']),
             ('c) Publicação de dados',
              ['É legítima a publicação, inclusive em sítio eletrônico, do nome do servidor e da remuneração correspondente (STF, Tema 483 da repercussão geral); a transparência ativa decorre da LAI '
               '(Lei n.º 12.527/2011).',
               'O CPF completo é dado pessoal desnecessário à finalidade de transparência: a LGPD exige finalidade e necessidade (art. 6.º) e rege o tratamento pelo poder público (art. 23). Solução: '
               'publicar com CPF mascarado ou omitido.']),
             ('d) Três Linhas',
              ['Primeira linha: a gestão, que executa e corrige — saneia os registros, revê as contratações, ajusta a lista a publicar e responde pelo controle do dia a dia.',
               'Segunda linha: funções de gestão de riscos e conformidade, que apoiam e monitoram — transformam os achados em alertas permanentes no painel.',
               'Terceira linha: auditoria interna (órgão central de controle interno), que presta avaliação e assessoria independentes e objetivas sobre os controles e se reporta ao órgão de '
               'governança, sem subordinação à gestão. O Tribunal de Contas faz avaliação externa, fora das três linhas.'])],
  'espelho': [('a) Qualidade de dados',
               30,
               [('Dimensões: completude (8% sem CPF/CNPJ), unicidade (duplicados) e consistência (mesmo número, valores diferentes)', 18),
                ('Cautela: tratar os dados antes; alerta é indício a confirmar, não prova', 12)]),
              ('b) Fracionamento',
               30,
               [('Limite aferido pela soma no exercício, por unidade gestora, para objetos do mesmo ramo', 15),
                ('Aplicação: onze contratações somadas superam o limite — fracionamento', 8),
                ('Solução: apurar responsabilidade; contratação única por licitação', 7)]),
              ('c) Publicação',
               30,
               [('Nome e remuneração podem ser publicados (transparência; entendimento do STF)', 12),
                ('CPF completo não: excede a finalidade e fere a necessidade (proteção de dados)', 12),
                ('Solução: publicar com o CPF mascarado ou omitido', 6)]),
              ('d) Três Linhas',
               30,
               [('1.ª linha (gestão): corrige registros, contratações e a lista', 10),
                ('2.ª linha (riscos e conformidade): alertas permanentes e orientação sobre dados', 10),
                ('3.ª linha (auditoria interna): avaliação independente, reporta à governança', 10)])],
  'proposta': ['O achado 1 compromete a completude, a unicidade e a consistência dos dados: os cerca de 8% de registros sem CPF ou CNPJ afetam a completude; os empenhos duplicados, a unicidade; e o mesmo número com valores '
               'diferentes, a consistência. Por isso, os dados devem ser tratados antes da análise, e os alertas do painel devem ser lidos como indícios a confirmar nos documentos, não como prova.',
               'As contratações do achado 2 não são regulares: indicam fracionamento de despesa. Pela Lei n.º 14.133/2021, o limite da dispensa é aferido pela soma do que a '
               'unidade gestora gasta no exercício com objetos do mesmo ramo. No caso, as onze contratações, somadas, superam o limite. Essa divisão artificial afasta a licitação; deve-se apurar a '
               'responsabilidade e realizar contratação única, por licitação, prevista no plano de contratações anual.',
               'A publicação do achado 3 só pode ser feita em parte: nome e remuneração podem ser publicados, conforme a LAI e o entendimento do STF. O CPF completo, contudo, excede a finalidade de transparência '
               'e fere o princípio da necessidade da LGPD. A lista deve ser publicada com o CPF mascarado ou omitido.',
               'No Modelo das Três Linhas, cada linha tem papel próprio. A gestão, primeira linha, saneia os registros, revê as contratações e ajusta a lista a publicar. A segunda linha, de '
               'riscos, conformidade e proteção de dados, transforma os achados em alertas permanentes e orienta o tratamento de dados pessoais. A auditoria interna, terceira linha, avalia com '
               'independência os controles e se reporta ao órgão de governança.'],
  'armadilhas': ['"Cada uma abaixo do limite" é a isca: o limite é aferido pela soma, não por contratação.',
                 'O achado 3 não pede "pode ou não pode": pede o limite. Parte pode ser publicada, parte não.'],
  'erros': ['Tratar o alerta do painel como prova de fraude.', 'Colocar a auditoria interna corrigindo registros: corrigir é da gestão; a auditoria avalia.'],
  'dicas': ['Use os nomes técnicos das dimensões de qualidade: completude, unicidade, consistência, acurácia, validade.',
            'Quando o enunciado dispensa citar dispositivo, cite a regra pelo conteúdo ("a soma do que a unidade gasta no exercício"); o número do artigo é opcional.']},
 {'n': 5,
  'titulo': 'Serviço prestado sem empenho e despesa de exercícios anteriores',
  'eixo': 'Administração Financeira e Orçamentária · Contabilidade Aplicada ao Setor Público (MCASP) · Direito Financeiro',
  'porque': 'AFO e Contabilidade Pública têm peso 2 na P1 e são a base das três áreas; o caso cruza os enfoques orçamentário e patrimonial.',
  'caso': ['Em fevereiro de 2026, uma secretaria do Estado Épsilon recebeu faturas de serviços de manutenção predial efetivamente prestados em novembro e dezembro de 2025, sem prévio empenho, porque '
           'o contrato havia vencido e a renovação não havia sido formalizada.',
           'A contabilidade não registrou nenhum valor relativo a esses serviços nas demonstrações de 2025. Em 2026, o órgão pretende pagar as faturas como despesa de exercícios anteriores, "sem '
           'necessidade de qualquer outro registro".'],
  'comando': 'Tendo em vista a situação narrada, na condição de Analista em Planejamento, Orçamento e Finanças Públicas, responda, justificadamente:',
  'itens': ['A despesa foi realizada de forma regular? A Administração deve pagar pelos serviços?',
            'O pagamento pode ser feito como despesa de exercícios anteriores? Em que condições?',
            'Como o caso deve ser tratado nos enfoques orçamentário e patrimonial, e quais são os efeitos nas demonstrações de 2025?',
            'Que providências de correção e de controle devem ser adotadas?'],
  'esqueleto': [('a) · N linhas',
                 'Resposta: não; mas deve indenizar · Lei n.º 4.320/1964, art. 60: vedada despesa sem prévio empenho · estágios: empenho, liquidação, pagamento · mas o serviço foi prestado: vedação '
                 'ao enriquecimento sem causa.'),
                ('b) · N linhas', 'Resposta: sim, como DEA · art. 37: compromisso reconhecido após o encerramento · condições: reconhecimento pela autoridade, dotação própria em 2026.'),
                ('c) · N linhas',
                 'Resposta: tratamento distinto · orçamentário: despesa de 2026 (art. 35, II) · patrimonial: VPD e passivo em 2025 (competência) · efeito: passivo e VPD subavaliados.'),
                ('d) · N linhas', 'Resposta: corrigir e controlar · ajuste de exercícios anteriores no PL · apuração de responsabilidade · controle de vigência de contratos.')],
  'padrao': [('a) Despesa sem empenho',
              ['É vedada a realização de despesa sem prévio empenho (Lei n.º 4.320/1964, art. 60). A despesa percorre empenho, liquidação e pagamento (arts. 58 a 65).',
               'Como os serviços foram efetivamente prestados, a Administração deve indenizar o que foi executado, para não enriquecer sem causa (Lei n.º 14.133/2021, art. 149; o contrato verbal é '
               'vedado pelo art. 95, § 2.º), sem prejuízo da apuração de responsabilidade de quem deu causa à irregularidade.']),
             ('b) Despesa de exercícios anteriores',
              ['Podem ser pagos à conta de dotação específica, discriminada por elementos, os compromissos reconhecidos após o encerramento do exercício correspondente, entre outras hipóteses (Lei '
               'n.º 4.320/1964, art. 37).',
               'Condições: reconhecimento da dívida pela autoridade competente, comprovação da prestação (liquidação) e dotação própria no orçamento de 2026.']),
             ('c) Enfoques orçamentário e patrimonial',
              ['No enfoque orçamentário, pertencem ao exercício as despesas nele legalmente empenhadas (Lei n.º 4.320/1964, art. 35, II): a despesa é de 2026.',
               'No enfoque patrimonial, a variação patrimonial diminutiva e o passivo devem ser reconhecidos em 2025, quando o serviço foi prestado (regime de competência — MCASP), mesmo sem '
               'empenho.',
               'Efeito: o Balanço Patrimonial de 2025 subavaliou o passivo, e a Demonstração das Variações Patrimoniais subavaliou as VPD.']),
             ('d) Correção e controle',
              ['Correção do erro de exercício anterior por ajuste de exercícios anteriores no patrimônio líquido, com evidenciação em notas explicativas.',
               'Apuração de responsabilidade e controle preventivo: monitoramento da vigência dos contratos e alerta antes do vencimento.'])],
  'espelho': [('a) Despesa sem empenho',
               30,
               [('Irregular: vedada despesa sem prévio empenho (Lei n.º 4.320/1964, art. 60)', 12),
                ('Dever de indenizar o serviço prestado (vedação ao enriquecimento sem causa)', 12),
                ('Apuração de responsabilidade', 6)]),
              ('b) DEA',
               30,
               [('Enquadramento: compromisso reconhecido após o encerramento do exercício (art. 37)', 15),
                ('Condições: reconhecimento pela autoridade, comprovação do serviço, dotação própria em 2026', 15)]),
              ('c) Dois enfoques',
               30,
               [('Orçamentário: despesa de 2026, exercício do empenho (art. 35, II)', 10),
                ('Patrimonial: VPD e passivo em 2025, pela competência', 10),
                ('Efeitos: passivo e VPD subavaliados nas demonstrações de 2025', 10)]),
              ('d) Providências',
               30,
               [('Correção por ajuste de exercícios anteriores no PL, com nota explicativa', 12), ('Apuração de responsabilidade', 9), ('Controle preventivo de vigência dos contratos', 9)])],
  'proposta': ['A despesa foi irregular, mas os serviços devem ser pagos. O art. 60 da Lei n.º 4.320/1964 veda despesa sem prévio empenho, primeiro estágio da despesa, anterior à liquidação e ao '
               'pagamento: é o empenho que reserva a dotação e cria a obrigação de pagar. Como os serviços foram prestados, porém, a Administração deve indenizá-los para não enriquecer sem causa '
               '(Lei n.º 14.133/2021, art. 149), sem prejuízo da apuração de responsabilidade.',
               'O pagamento pode ser feito como despesa de exercícios anteriores. O art. 37 da Lei n.º 4.320/1964 admite pagar, à conta de dotação específica, compromissos reconhecidos após o '
               'encerramento do exercício. Exigem-se o reconhecimento da dívida pela autoridade competente, a comprovação documental do serviço, com preço compatível com o de mercado, e a dotação '
               'própria em 2026, com empenho no elemento de despesa de exercícios anteriores.',
               'Os enfoques orçamentário e patrimonial tratam o caso de forma diferente. No orçamentário, a despesa é de 2026, ano do empenho (art. 35, II). No patrimonial, a variação patrimonial '
               'diminutiva (VPD) e o passivo deveriam ter sido reconhecidos em 2025, pela competência, ainda que sem execução orçamentária. Assim, o Balanço Patrimonial de 2025 subavaliou o passivo, '
               'e a DVP, as VPD, distorcendo o resultado patrimonial do exercício.',
               'Recomenda-se corrigir o erro por ajuste de exercícios anteriores no patrimônio líquido, com nota explicativa sobre a natureza e o valor do erro, apurar a responsabilidade de quem '
               'deu causa à despesa sem empenho e instituir controle de vigência dos contratos, com alerta antes do vencimento.'],
  'armadilhas': ['"Sem necessidade de qualquer outro registro" é a armadilha: a DEA resolve o orçamento, mas não o erro patrimonial de 2025.',
                 'O serviço foi prestado: negar o pagamento seria enriquecimento sem causa.'],
  'erros': ['Dizer que a despesa pertence a 2025 também no orçamento: pelo art. 35, II, ela é do exercício do empenho.', 'Esquecer os efeitos nas demonstrações, que o item c pede expressamente.'],
  'dicas': ['Separe os enfoques com conectivos claros: "no enfoque orçamentário...", "no patrimonial...".',
            'Use as siglas só depois de escrever por extenso uma vez, salvo as consagradas (DVP, VPD, PL).']}]
