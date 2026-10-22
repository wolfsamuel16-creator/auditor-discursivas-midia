"""Gera o carrossel (1080x1350) e os stories (1080x1920) da campanha SEFAZ-AL 2026.
Reaproveita CSS e moldes de ../campanhas-tcdf-tcema/gerar.py (mesmo padrão visual das campanhas TCDF/TCE-MA).
Uso: python3 gerar.py <pasta_saida>"""
import pathlib, sys

BASE = pathlib.Path(__file__).resolve().parent.parent / 'campanhas-tcdf-tcema' / 'gerar.py'
src = BASE.read_text(encoding='utf-8').split('# =================== TCDF')[0]
src = src.replace("OUT = pathlib.Path('/home/claude/carrossel/out'); OUT.mkdir(exist_ok=True)", '')
exec(src)  # define CSS, head, capa, conteudo, fecho, story

OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'out'); OUT.mkdir(parents=True, exist_ok=True)
KW = 'SEFAZAL'
T = 8

c = head('Campanha SEFAZ-AL 2026 — carrossel') + capa(1, T,
    'PDF · Cebraspe',
    'Discursiva da <em style="white-space:nowrap">SEFAZ&#8209;AL</em> 2026',
    'Auditor Fiscal da Administração Tributária Estadual. <b>Quatro questões de 30 linhas</b>, uma para cada eixo do edital.',
    ['Prova 10/01/2027', '40 páginas', '6 rodadas com espelho'], KW)

c += conteudo(2, T, 'A prova de domingo à tarde', 'Quatro textos, 40 pontos, uma linha de corte', '''
<div class="nums">
  <div class="num"><div class="v">4 × 30</div><div class="l">Quatro questões de até 30 linhas · <b>10 pontos</b> cada</div></div>
  <div class="num"><div class="v">4h30</div><div class="l">Para as <b>120 linhas</b>, à mão</div></div>
  <div class="num dest"><div class="v">20 <small>/ 40</small></div><div class="l">Abaixo disso, <b>eliminado</b></div></div>
  <div class="num"><div class="v">~500</div><div class="l">Provas corrigidas para <b>40 vagas</b> imediatas</div></div>
</div>
<div class="txt">Cada questão vale o mesmo que <b>dez itens líquidos</b> da objetiva. Três pontos numa resposta bem estruturada costumam vir mais fácil que três itens a mais.</div>
<div class="dica"><div class="dica-rot">Fonte</div><div class="dica-txt">Edital n.º 1 – SEFAZ/AL, de 24/8/2026 (subitens 7.3, 8.11.6, 9.1, 9.7.6 e 11.1).</div></div>
''')

c += conteudo(3, T, 'Uma particularidade rara', 'O edital já diz o eixo de cada questão', '''
<div class="rod"><span class="k">1</span><span class="t"><small>Questão 1</small><b>Ciência de dados</b> · CRISP-DM, aprendizado de máquina, métricas, BI</span></div>
<div class="rod"><span class="k">2</span><span class="t"><small>Questão 2</small><b>Auditoria fiscal</b> · SPED, NF-e, EFD, cruzamentos, créditos indevidos</span></div>
<div class="rod"><span class="k">3</span><span class="t"><small>Questão 3</small><b>Finanças públicas</b> · orçamento, LRF, renúncia de receita, dívida</span></div>
<div class="rod"><span class="k">4</span><span class="t"><small>Questão 4</small><b>Reforma tributária</b> · IBS, CBS, Comitê Gestor, split payment, transição</span></div>
<div class="dica"><div class="dica-rot">O recado</div><div class="dica-txt">Em vez de dezenas de disciplinas, você treina <b>quatro conteúdos</b>. Quem treinar com método chega com vantagem enorme.</div></div>
''')

c += conteudo(4, T, 'Atenção ao calendário', 'Você vai fazer a discursiva sem saber se passou', '''
<div class="rod"><span class="k p">1</span><span class="t"><small>20/12/2026</small><b>Prova objetiva</b></span></div>
<div class="rod"><span class="k">2</span><span class="t"><small>10/01/2027 · tarde</small><b>Prova discursiva</b> · três semanas depois</span></div>
<div class="rod"><span class="k p">3</span><span class="t"><small>05/02/2027</small><b>Resultado final da objetiva</b></span></div>
<div class="dica"><div class="dica-rot">Na prática</div><div class="dica-txt">Não decida o seu esforço pelo gabarito preliminar. <b>Treine discursiva desde já</b>, em paralelo com a objetiva.</div></div>
<div class="dica" style="margin-top:20px;border-top:none;padding-top:0"><div class="dica-rot">Fonte</div><div class="dica-txt">Edital n.º 1 – SEFAZ/AL e retificações.</div></div>
''')

c += conteudo(5, T, 'Prévia da aula gratuita', 'O parágrafo que pontua, em quatro partes', '''
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">1 · Tópico frasal</div><div class="d">“O crédito relativo ao material de uso e consumo é indevido.”</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">2 · Fundamento</div><div class="d">“...pois o art. 33, I, da LC n.º 87/1996 só admite esse crédito a partir de 2033.”</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">3 · Aplicação ao caso</div><div class="d">“No caso, a empresa creditou R$ 45 mil de NF-e com CFOP 1.556.”</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">4 · Fechamento</div><div class="d">“Assim, o valor deve ser estornado, com multa.”</div></div></div>
<div class="dica" style="margin-top:14px"><div class="dica-rot">E em dados?</div><div class="dica-txt">O fundamento é o <b>conceito técnico</b>, com o nome técnico, aplicado à SEFAZ.</div></div>
''')

c += conteudo(6, T, 'As seis rodadas', 'Temas inéditos, um caso por eixo', '''
<div class="rod"><span class="k">1</span><span class="t"><small>Ciência de dados</small><b>Seleção de contribuintes com aprendizado de máquina</b></span></div>
<div class="rod"><span class="k">2</span><span class="t"><small>Ciência de dados</small><b>BI e modelagem dimensional da arrecadação</b></span></div>
<div class="rod"><span class="k">3</span><span class="t"><small>Auditoria fiscal</small><b>Cruzamento NF-e × EFD ICMS/IPI</b></span></div>
<div class="rod"><span class="k">4</span><span class="t"><small>Finanças públicas</small><b>Renúncia de receita e incentivo de ICMS</b></span></div>
<div class="rod"><span class="k">5</span><span class="t"><small>Reforma tributária</small><b>Split payment, crédito e apuração assistida</b></span></div>
<div class="rod"><span class="k">6</span><span class="t"><small>Reforma tributária</small><b>Princípio do destino, transição e Comitê Gestor</b></span></div>
''')

c += conteudo(7, T, 'Na aula gratuita · 40 páginas', 'Do edital ao checklist do dia', '''
<div class="lista">
  <div><span class="ok">✓</span><span class="q"><b>Raio-X do edital</b> e de como o Cebraspe corrige<small>Fórmula, correção dupla, o que zera ou anula</small></span></div>
  <div><span class="ok">✓</span><span class="q">O que a banca <b>já cobrou na área fiscal</b><small>SEFAZ-AL 2021, SEFAZ-SE 2021, SEFAZ-AC 2024</small></span></div>
  <div><span class="ok">✓</span><span class="q"><b>O que está quente</b> para a SEFAZ-AL<small>Split payment, transição do ICMS, Trânsito Inteligente</small></span></div>
  <div><span class="ok">✓</span><span class="q"><b>6 rodadas</b> com espelho e resposta completa<small>Orientação de solução e proposta definitiva</small></span></div>
  <div><span class="ok">✓</span><span class="q">Gestão das <b>quatro horas e meia</b> e checklist do dia</span></div>
</div>
''')

c += fecho(8, T, 'Quatro eixos.<br>Um parágrafo por item.<br><em>Nota acima de 20.</em>', KW,
    'Depois da prova, se a nota não vier como você esperava, me manda <b style="color:#fff">RECURSO</b> no direct. A análise de viabilidade é gratuita.')
c += '</body>\n</html>\n'
(OUT / 'carrossel_sefazal.html').write_text(c, encoding='utf-8')

st = head('Campanha SEFAZ-AL 2026 — stories')
st += story(1, '''<div><span class="tag">Aula gratuita<small>SEFAZ-AL 2026</small></span></div>
<div class="st-h">Vai fazer a discursiva da <em style="white-space:nowrap">SEFAZ&#8209;AL</em>?</div>
<div class="st-p">Preparei uma aula <b>grátis</b>, em PDF, de <b>40 páginas</b> para o Auditor Fiscal: os <b>quatro eixos</b> do edital, o parágrafo que pontua e <b>6 rodadas</b> com espelho e resposta completa.</div>''')
st += story(2, '''<div class="st-h">É só mandar no <em>direct</em></div>
<div><span class="kw">SEFAZAL</span></div>
<div class="st-p">Manda <b>SEFAZAL</b> numa mensagem para o <b>@auditor_discursivas</b> e a <b>aula gratuita</b> chega na hora.</div>
<div class="st-box"><div class="q">Prefere comentar?</div><div class="r">Comente <b>SEFAZAL</b> no post da aula da SEFAZ-AL que eu também te mando.</div></div>''')
st += story(3, '''<div class="eyebrow">Você sabia?</div>
<div class="st-h">Você faz a discursiva <em>sem saber</em> se passou.</div>
<div class="st-p">A objetiva é em <b>20/12</b>, a discursiva em <b>10/01</b> e o resultado final da objetiva só sai em <b>05/02</b>. Quem treina discursiva desde já sai na frente.</div>
<div class="st-box"><div class="q">Mande SEFAZAL no direct</div><div class="r">e receba grátis a aula com as 6 rodadas.</div></div>''')
st += '</body>\n</html>\n'
(OUT / 'stories_sefazal.html').write_text(st, encoding='utf-8')
print('ok')
