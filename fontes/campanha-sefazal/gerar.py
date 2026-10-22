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
T = 6

c = head('Campanha SEFAZ-AL 2026 — carrossel') + capa(1, T,
    'PDF · 40 páginas',
    'Discursiva da <em style="white-space:nowrap">SEFAZ&#8209;AL</em> 2026',
    'Uma aula completa para o <b>Auditor Fiscal</b>: método, os quatro eixos do edital e <b>6 rodadas inéditas</b> com espelho e resposta linha a linha.',
    ['40 páginas', '6 rodadas', 'Espelho + resposta'], KW)

c += conteudo(2, T, 'Na aula gratuita · 40 páginas', 'O que você recebe no PDF', """
<div class="lista">
  <div><span class="ok">✓</span><span class="q"><b>Raio-X do edital</b> e de como o Cebraspe corrige<small>Fórmula da nota, correção dupla, o que zera ou anula</small></span></div>
  <div><span class="ok">✓</span><span class="q">O que o edital pede em <b>cada um dos quatro eixos</b><small>Os tópicos do edital que mais rendem uma questão de 30 linhas</small></span></div>
  <div><span class="ok">✓</span><span class="q">O que a banca <b>já cobrou na área fiscal</b><small>SEFAZ-AL 2021, SEFAZ-SE 2021, SEFAZ-AC 2024</small></span></div>
  <div><span class="ok">✓</span><span class="q"><b>O que está quente</b> para a SEFAZ-AL<small>Split payment, transição do ICMS, fiscalização por dados</small></span></div>
  <div><span class="ok">✓</span><span class="q"><b>Roteiro de planejamento</b> em cinco passos<small>E a calibragem das 30 linhas por item</small></span></div>
  <div><span class="ok">✓</span><span class="q">Gestão das <b>4h30</b> e checklist do dia da prova</span></div>
</div>
""")

c += conteudo(3, T, 'O coração da aula', 'Seis rodadas inéditas, um caso por eixo', """
<div class="rod"><span class="k">1</span><span class="t"><small>Ciência de dados</small><b>Seleção de contribuintes com aprendizado de máquina</b></span></div>
<div class="rod"><span class="k">2</span><span class="t"><small>Ciência de dados</small><b>BI e modelagem dimensional da arrecadação</b></span></div>
<div class="rod"><span class="k">3</span><span class="t"><small>Auditoria fiscal</small><b>Cruzamento NF-e × EFD ICMS/IPI</b></span></div>
<div class="rod"><span class="k">4</span><span class="t"><small>Finanças públicas</small><b>Renúncia de receita e incentivo de ICMS</b></span></div>
<div class="rod"><span class="k">5</span><span class="t"><small>Reforma tributária</small><b>Split payment, crédito e apuração assistida</b></span></div>
<div class="rod"><span class="k">6</span><span class="t"><small>Reforma tributária</small><b>Princípio do destino, transição e Comitê Gestor</b></span></div>
<div class="txt" style="font-size:28px;color:var(--cinza);margin-top:14px">Questões no padrão Cebraspe: 30 linhas, 10 pontos, itens com valor.</div>
""")

c += conteudo(4, T, 'Como cada rodada funciona', 'Você escreve. Depois, a aula corrige.', """
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">1 · Questão inédita</div><div class="d">Leia o enunciado e escreva em <b>60 minutos</b>, cronometrados</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">2 · Orientação de solução</div><div class="d">O esqueleto: linhas por item, tópico frasal e dado do caso</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">3 · Padrão de resposta e espelho</div><div class="d">O que o corretor procura, com <b>conceitos graduados</b> por quesito</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">4 · Resposta definitiva</div><div class="d">O texto pronto, <b>linha a linha</b>, dentro das 30 linhas</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">5 · Armadilhas e dicas</div><div class="d">Os erros mais comuns e o que o enunciado esconde</div></div></div>
""")

c += conteudo(5, T, 'Prévia da aula gratuita', 'O parágrafo que pontua, em quatro partes', """
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">1 · Tópico frasal</div><div class="d">“O crédito relativo ao material de uso e consumo é indevido.”</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">2 · Fundamento</div><div class="d">“...pois o art. 33, I, da LC n.º 87/1996 só admite esse crédito a partir de 2033.”</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">3 · Aplicação ao caso</div><div class="d">“No caso, a empresa creditou R$ 45 mil de NF-e com CFOP 1.556.”</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">4 · Fechamento</div><div class="d">“Assim, o valor deve ser estornado, com multa.”</div></div></div>
<div class="dica" style="margin-top:14px"><div class="dica-rot">E em dados?</div><div class="dica-txt">O fundamento é o <b>conceito técnico</b>, com o nome técnico, aplicado à SEFAZ.</div></div>
""")

c += fecho(6, T, 'Seis rodadas.<br>Espelho e resposta.<br><em>Grátis no seu direct.</em>', KW,
    'Depois da prova, se a nota não vier como você esperava, me manda <b style="color:#fff">RECURSO</b> no direct. A análise de viabilidade é gratuita.')
c += '</body>\n</html>\n'
(OUT / 'carrossel_sefazal.html').write_text(c, encoding='utf-8')

st = head('Campanha SEFAZ-AL 2026 — stories')
st += story(1, """<div><span class="tag">Aula gratuita<small>SEFAZ-AL 2026</small></span></div>
<div class="st-h">A aula da discursiva da <em style="white-space:nowrap">SEFAZ&#8209;AL</em> chegou.</div>
<div class="st-p"><b>40 páginas</b>, grátis, em PDF, para o Auditor Fiscal:</div>
<div class="st-box"><div class="r" style="margin-top:0;line-height:1.6">✓ Raio-X do edital e da correção<br>✓ Os quatro eixos, um a um<br>✓ Roteiro de planejamento<br>✓ <b>6 rodadas inéditas</b> com espelho<br>✓ Checklist do dia da prova</div></div>""")
st += story(2, """<div class="eyebrow">Como cada rodada funciona</div>
<div class="st-h">Você escreve. A aula <em>corrige</em>.</div>
<div class="st-box"><div class="r" style="margin-top:0;line-height:1.6"><b>1.</b> Questão inédita, 60 min<br><b>2.</b> Orientação de solução<br><b>3.</b> Padrão de resposta e espelho<br><b>4.</b> Resposta definitiva, linha a linha<br><b>5.</b> Armadilhas e dicas</div></div>
<div class="st-p">Seis rodadas nos quatro eixos: <b>dados, auditoria fiscal, finanças e reforma tributária</b>.</div>""")
st += story(3, """<div class="st-h">É só mandar no <em>direct</em></div>
<div><span class="kw">SEFAZAL</span></div>
<div class="st-p">Manda <b>SEFAZAL</b> numa mensagem para o <b>@auditor_discursivas</b> e a <b>aula gratuita</b> chega na hora.</div>
<div class="st-box"><div class="q">Prefere comentar?</div><div class="r">Comente <b>SEFAZAL</b> no post da aula da SEFAZ-AL que eu também te mando.</div></div>""")
st += '</body>\n</html>\n'
(OUT / 'stories_sefazal.html').write_text(st, encoding='utf-8')
print('ok')
