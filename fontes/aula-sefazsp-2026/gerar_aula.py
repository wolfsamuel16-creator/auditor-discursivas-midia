# -*- coding: utf-8 -*-
"""Gera Aula SEFAZ-SP 2026 (HTML + PDF). Uso: python3 gerar_aula.py"""
import base64, pathlib, textwrap, asyncio, html as H
from conteudo import RODADAS

BASE = pathlib.Path(__file__).parent
FONTS = BASE / 'fonts'
FOTO = base64.b64encode((BASE / 'foto.jpg').read_bytes()).decode()
CPL = 68  # caracteres por linha manuscrita (simulação)

def ff():
    out = []
    for fam, w, st, f in [('Poppins',500,'normal','Poppins-Medium.ttf'),('Poppins',600,'normal','Poppins-SemiBold.ttf'),
                          ('Poppins',700,'normal','Poppins-Bold.ttf'),('Poppins',800,'normal','Poppins-ExtraBold.ttf'),
                          ('Lato',400,'normal','Lato-Regular.ttf'),('Lato',400,'italic','Lato-Italic.ttf'),
                          ('Lato',700,'normal','Lato-Bold.ttf'),('Lato',900,'normal','Lato-Black.ttf')]:
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url('file://{FONTS/f}')}}")
    return '\n'.join(out)

CSS = """
:root{--navy:#2A3544;--lar:#F04E23;--cre:#F6F2EC;--cre2:#EFE8DD;--tx:#26303d;--mu:#6b7380;--ok:#2f7d4f}
*{box-sizing:border-box}
@page{size:A4;margin:22mm 18mm 20mm 18mm}
body{font-family:Lato;color:var(--tx);font-size:10.4pt;line-height:1.5;margin:0}
h1,h2,h3,h4{font-family:Poppins;color:var(--navy);margin:0}
p{margin:0 0 7pt}
b,strong{font-weight:700;color:var(--navy)}
.pb{break-before:page}
.eyebrow{font-family:Poppins;font-weight:600;font-size:7.6pt;letter-spacing:.28em;text-transform:uppercase;color:var(--lar)}
h2.sec{font-size:17pt;font-weight:700;margin:2pt 0 10pt;line-height:1.2}
h2.sec .num{color:var(--lar);margin-right:8pt}
h3{font-size:12.5pt;font-weight:700;margin:14pt 0 6pt}
.lead{font-size:11pt;color:#3a4452}
table{width:100%;border-collapse:collapse;margin:6pt 0 11pt;font-size:9.4pt;break-inside:auto}
th{font-family:Poppins;font-weight:600;font-size:8pt;text-align:left;color:#fff;background:var(--navy);padding:6pt 7pt;letter-spacing:.02em}
td{padding:6pt 7pt;border-bottom:1px solid #e3ddd3;vertical-align:top}
tr{break-inside:avoid}
tbody tr:nth-child(even) td{background:#faf7f2}
td.k{font-weight:700;color:var(--navy);width:28%}
.box{border-radius:7pt;padding:10pt 13pt;margin:9pt 0 11pt;break-inside:avoid}
.box .eyebrow{display:block;margin-bottom:4pt}
.box.cre{background:var(--cre)}
.box.nv{background:var(--navy);color:#e9edf2}.box.nv b{color:#fff}.box.nv .eyebrow{color:#ffb39e}
.box.lr{background:#fff3ee;border-left:4pt solid var(--lar)}
.box.bad{background:#fbecea;border-left:4pt solid #c0392b}
.box.good{background:#eaf5ee;border-left:4pt solid var(--ok)}
.stats{display:flex;gap:7pt;margin:8pt 0 12pt}
.stat{flex:1;background:var(--cre);border-radius:7pt;padding:9pt 6pt;text-align:center}
.stat .v{font-family:Poppins;font-weight:800;font-size:19pt;color:var(--lar);line-height:1.1}
.stat .l{font-family:Poppins;font-weight:600;font-size:6.8pt;letter-spacing:.14em;text-transform:uppercase;color:var(--navy)}
ul{margin:3pt 0 8pt;padding-left:15pt}li{margin-bottom:3pt}
/* capa */
.capa{height:253mm;background:var(--navy);color:#fff;border-radius:10pt;padding:26mm 18mm 16mm;display:flex;flex-direction:column;position:relative;overflow:hidden}
.capa .wm{font-family:Poppins;font-weight:800;color:var(--lar);letter-spacing:.18em;font-size:10pt}
.capa h1{color:#fff;font-size:38pt;line-height:1.05;font-weight:800;margin:22mm 0 8mm}
.capa h1 span{color:var(--lar)}
.capa .sub{font-size:13pt;line-height:1.5;color:#dfe5ec;max-width:150mm}
.capa .tag{font-family:Poppins;font-weight:600;letter-spacing:.26em;font-size:8.5pt;color:#ffb39e;margin-top:auto}
.capa .data{font-family:Poppins;font-weight:800;font-size:15pt;letter-spacing:.06em;margin-top:5pt}
.capa .rod{display:flex;justify-content:space-between;border-top:1px solid #4a5668;padding-top:9pt;margin-top:12mm;font-size:9pt;color:#b9c2cd}
.capa .barra{position:absolute;right:-30mm;top:-30mm;width:110mm;height:110mm;border-radius:50%;border:16mm solid rgba(240,78,35,.14)}
/* autor */
.autor{display:flex;gap:14pt;align-items:center;background:var(--cre);border-radius:9pt;padding:13pt;margin:8pt 0 12pt}
.foto{width:84pt;height:84pt;border-radius:50%;border:3.5pt solid var(--lar);background-size:cover;background-position:center;flex:none}
.autor .nm{font-family:Poppins;font-weight:700;font-size:14pt;color:var(--navy)}
.autor .at{color:var(--lar);font-family:Poppins;font-weight:600;font-size:9pt;margin-bottom:4pt}
.autor ul{margin:0;padding-left:13pt;font-size:9.5pt}
/* parte */
.parte{background:var(--navy);color:#fff;border-radius:9pt;padding:16pt 18pt;margin-bottom:14pt}
.parte h2{color:#fff;font-size:21pt;font-weight:800}
.parte p{color:#cfd7e1;margin:5pt 0 0}
.parte .eyebrow{color:#ffb39e}
/* sumário */
.sum{width:100%;font-size:10pt}.sum td{border:0;padding:3pt 0}.sum td.n{width:30pt;font-family:Poppins;font-weight:700;color:var(--lar)}
.sum tr.pt td{padding-top:11pt;font-family:Poppins;font-weight:600;font-size:7.6pt;letter-spacing:.24em;color:var(--mu);text-transform:uppercase}
.sum tbody tr:nth-child(even) td{background:none}
/* roteiro */
.passo{display:flex;gap:11pt;margin:0 0 8pt;break-inside:avoid}
.passo .bn{flex:none;width:24pt;height:24pt;border-radius:50%;background:var(--lar);color:#fff;font-family:Poppins;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:11pt}
.passo h4{font-size:10.5pt;margin-bottom:1pt}
.formula{font-family:Poppins;font-weight:700;color:var(--navy);text-align:center;font-size:12pt;background:var(--cre);border-radius:7pt;padding:10pt;margin:8pt 0}
.formula span{color:var(--lar)}
/* rodada */
.rod-h .eyebrow{font-size:7.2pt}
.rod-h h2{font-size:19pt;font-weight:800;margin:3pt 0 4pt;line-height:1.15}
.rod-h .rn{color:var(--lar)}
.eixo{font-size:9pt;color:var(--mu);margin-bottom:9pt}
.enun{border:1.4pt solid var(--navy);border-radius:8pt;padding:12pt 14pt;margin:6pt 0 10pt;break-inside:auto}
.enun .eyebrow{display:block;margin-bottom:6pt}
.enun p{font-size:10.2pt}
.enun ol{margin:6pt 0 0;padding-left:0;list-style:none}
.enun ol li{display:flex;gap:9pt;margin-bottom:5pt}
.enun ol li .i{font-family:Poppins;font-weight:700;color:var(--lar);flex:none;width:12pt}
.enun .val{color:var(--mu);font-size:9pt;white-space:nowrap}
.pare{background:var(--cre);border-radius:7pt;padding:9pt 12pt;font-size:9.6pt;font-style:italic}
.esq td.k{width:30%}
.esp td:last-child{width:11%;text-align:right;font-family:Poppins;font-weight:700;color:var(--navy)}
.esp td.q{font-weight:700;color:var(--navy);width:28%}
.esp .c{font-size:8.9pt;margin:0 0 2pt}
.tot td{background:var(--cre)!important;font-family:Poppins;font-weight:700;color:var(--navy)}
/* folha */
.folha{border:1px solid #cfc6b8;border-radius:6pt;background:#fffdf9;padding:6pt 10pt 8pt;margin:6pt 0 6pt;break-inside:avoid}
.folha .eyebrow{display:block;margin:2pt 0 5pt}
.ln{display:flex;border-bottom:1px solid #e6ded1;font-size:9.6pt;line-height:1.62}
.ln .nr{width:20pt;flex:none;color:#a39b8f;font-family:Poppins;font-size:7.6pt;padding-top:2pt}
.ln .t{white-space:pre;font-family:Lato}
.nota{font-size:8.4pt;color:var(--mu);font-style:italic}
.tri{display:flex;gap:7pt;margin:9pt 0;break-inside:avoid}
.tri>div{flex:1;border-radius:7pt;padding:9pt 10pt;font-size:9pt}
.tri .eyebrow{display:block;margin-bottom:4pt;font-size:6.8pt}
.tri ul{padding-left:12pt;margin:0}
.t1{background:#fff3ee}.t2{background:#fbecea}.t3{background:#eaf5ee}
.t2 .eyebrow{color:#c0392b}.t3 .eyebrow{color:var(--ok)}
.fontes{font-size:8.8pt}.fontes li{margin-bottom:4pt;word-break:break-word}
.cta{background:var(--lar);color:#fff;border-radius:9pt;padding:13pt 16pt;margin-top:10pt}
.cta b{color:#fff}.cta .eyebrow{color:#fff;opacity:.85;display:block;margin-bottom:3pt}
"""

def e(s):  # texto já com <b> permitido
    return s

def wrap_paragrafos(pars):
    linhas = []
    for p in pars:
        w = textwrap.wrap(p, width=CPL, initial_indent='     ', subsequent_indent='', break_long_words=False, break_on_hyphens=False)
        linhas += w
    return linhas

def folha(pars, total=30, rot='TEXTO DEFINITIVO · ESTUDO DE CASO · 30 LINHAS'):
    ls = wrap_paragrafos(pars)
    assert len(ls) <= total, f'{len(ls)} linhas > {total}'
    out = [f'<div class="folha"><span class="eyebrow">{rot}</span>']
    for i in range(total):
        t = H.escape(ls[i]) if i < len(ls) else ''
        out.append(f'<div class="ln"><span class="nr">{i+1}</span><span class="t">{t}</span></div>')
    out.append('</div>')
    return '\n'.join(out), len(ls)

def stat(v, l): return f'<div class="stat"><div class="v">{v}</div><div class="l">{l}</div></div>'

AUTOR = f"""<div class="autor"><div class="foto" style="background-image:url(data:image/jpeg;base64,{FOTO})"></div>
<div><div class="nm">Samuel Wolf</div><div class="at">@auditor_discursivas</div><ul>
<li>Auditor de Controle Externo do TCE-RJ</li><li>Engenheiro de Infraestrutura Aeronáutica formado pelo ITA</li>
<li>Nomeado Auditor Fiscal da SEFAZ-RS e da SEFIN Manaus</li><li>Trabalha com discursivas há mais de 6 anos</li></ul></div></div>"""

def rodada(r):
    soma = sum(v for _, v in r['itens'])
    itens = ''.join(f'<li><span class="i">{i+1}</span><span>{t} <span class="val">[valor: {v} pontos]</span></span></li>' for i, (t, v) in enumerate(r['itens']))
    caso = ''.join(f'<p>{p}</p>' for p in r['caso'])
    esq = ''.join(f'<tr><td class="k">{a}</td><td>{b}</td></tr>' for a, b in r['esqueleto'])
    pad = ''.join('<tr><td class="k">{}</td><td><ul>{}</ul></td></tr>'.format(a, ''.join(f'<li>{x}</li>' for x in bs)) for a, bs in r['padrao'])
    esp = ''.join('<tr><td class="q">{}</td><td>{}</td><td>{}</td></tr>'.format(q, ''.join(f'<p class="c">Conceito {c}</p>' for c in cs), f'{v:.2f}'.replace('.', ',')) for q, cs, v in r['espelho'])
    fl, nl = folha(r['proposta'])
    tri = lambda cls, tit, xs: f'<div class="{cls}"><span class="eyebrow">{tit}</span><ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul></div>'
    return f"""
<section class="pb rod-h"><span class="eyebrow">Rodada {r['n']} · Estudo de caso · 30 linhas · {soma} pontos</span>
<h2><span class="rn">{r['n']}.</span> {r['titulo']}</h2>
<div class="eixo"><b>Eixo do edital:</b> {r['eixo']}. Caso inédito, elaborado no padrão FCC para treino.</div>
<div class="enun"><span class="eyebrow">Estudo de caso · inédito · padrão FCC · até 30 linhas · 120 pontos</span>
{caso}<p>{r['comando']}</p><ol>{itens}</ol>
<p class="nota" style="margin-top:6pt">Situação hipotética: entes e fatos são fictícios. A distribuição de pontos entre os aspectos é do curso; o edital não a fixa.</p></div>
<div class="pare">Pare aqui. Planeje e escreva a sua resposta em até 30 linhas, cronometrando cerca de 70 minutos, antes de virar a página. A solução começa na próxima página.</div>
</section>
<section class="pb"><h3 style="margin-top:0">Como montar o esqueleto</h3>
<table class="esq"><thead><tr><th>Parágrafo</th><th>Palavras-chave do rascunho</th></tr></thead><tbody>{esq}</tbody></table>
<h3>Padrão de resposta</h3>
<table><thead><tr><th>Aspecto</th><th>O que a resposta deve conter</th></tr></thead><tbody>{pad}</tbody></table>
</section>
<section class="pb"><h3 style="margin-top:0">Espelho de correção (do curso, no modelo de grade da FCC)</h3>
<table class="esp"><thead><tr><th>Quesito</th><th>O que o corretor procura</th><th>Pontos</th></tr></thead><tbody>{esp}
<tr class="tot"><td>Nota máxima</td><td>Erros de língua portuguesa, abordagem tangencial e divagação reduzem a nota (edital, itens 9.7 e 9.8)</td><td>{soma:.2f}</td></tr></tbody></table>
<div class="tri">{tri('t1','Armadilhas do enunciado',r['armadilhas'])}{tri('t2','Erros mais comuns',r['erros'])}{tri('t3','Dicas estratégicas',r['dicas'])}</div>
</section><section class="pb"><h3 style="margin-top:0">Proposta de redação definitiva · {nl} de 30 linhas</h3>
{fl}
<p class="nota">Contagem simulada com cerca de {CPL} caracteres por linha manuscrita. Na sua letra, o número pode variar: treine na folha.</p>
</section>"""

def montar():
    temas = ''.join(f"<tr><td class='k'>{r['n']} · {r['titulo']}</td><td>{r['eixo']}</td><td>{r['porque']}</td></tr>" for r in RODADAS)
    rods = ''.join(rodada(r) for r in RODADAS)
    sum_rod = ''.join(f"<tr><td class='n'>▸</td><td>Rodada {r['n']} · {r['titulo']}</td></tr>" for r in RODADAS)
    html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Discursiva SEFAZ-SP 2026 · Auditor Discursivas</title>
<style>{ff()}{CSS}</style></head><body>

<section class="capa"><div class="barra"></div><div class="wm">AUDITOR DISCURSIVAS</div>
<div class="eyebrow" style="color:#ffb39e;margin-top:30mm">Aula especial · FCC · Temas propostos</div>
<h1 style="margin-top:6mm">Discursiva da<br><span>SEFAZ-SP</span> 2026</h1>
<div class="sub">O estudo de caso interdisciplinar de 30 linhas: o que a FCC avalia, planejamento, estrutura do parágrafo e cinco rodadas com temas inéditos, espelho e resposta completa.</div>
<div class="tag">ANALISTA EM PLANEJAMENTO, ORÇAMENTO E FINANÇAS PÚBLICAS · APOFP</div>
<div class="data">PROVA EM 20 DE DEZEMBRO DE 2026</div>
<div class="rod"><span>Banca FCC · SEFAZ-SP 2026 · Edital n.º 01/2026, retificado pelo Edital n.º 02/2026</span><span>@auditor_discursivas</span></div></section>

<section class="pb"><span class="eyebrow">Antes de começar</span><h2 class="sec">Por que fiz esta aula gratuita</h2>
{AUTOR}
<p>Eu sou o Samuel. Antes de chegar ao controle externo, passei por concursos da área fiscal, e sei na prática o quanto a discursiva pesa — e o quanto ela assusta. Hoje, além do trabalho de auditor, ajudo concurseiros a escrever melhor na prova, com aulas, correções e recursos contra a nota da discursiva.</p>
<p>Fiz esta aula de graça por um motivo simples: quero ajudar. Na SEFAZ-SP, a discursiva vale 120 pontos — o mesmo que a P2 inteira —, elimina quem fizer menos de 48 e é o primeiro critério técnico de desempate. E é um texto só, de 30 linhas: cada parágrafo conta muito.</p>
<p>Aqui está o mesmo jeito que eu uso para corrigir provas e preparar recursos: olhar o que a banca realmente cobra, planejar antes de escrever e responder exatamente ao comando, com a norma aplicada ao caso e uma solução no fim de cada parágrafo. Nada de fórmula mágica — método e treino.</p>
<div class="box lr"><span class="eyebrow">Combinado?</span>Leia com calma, faça as rodadas antes de olhar as soluções e, se tiver dúvida ou quiser compartilhar o que achou, me chama no <b>@auditor_discursivas</b>. Bons estudos!</div>
</section>

<section class="pb"><span class="eyebrow">Palavra inicial</span><h2 class="sec">Um caso, várias disciplinas, uma solução</h2>
<p class="lead">A P3 da SEFAZ-SP é um único estudo de caso interdisciplinar, de até 30 linhas, sobre os Conhecimentos Básicos — o mesmo para as três áreas (Orçamento e Finanças Públicas, Contabilidade Pública e Ciência de Dados e TI). O edital é explícito: a banca avalia a interpretação do caso e a proposta de solução, e a mera citação de lei ou de definição não pontua por si só.</p>
<p>A aula segue essa lógica. A Parte 1 mostra a prova, o que o edital pede, como a FCC corrige, os temas escolhidos, o roteiro de planejamento e o parágrafo que pontua. A Parte 2 traz cinco rodadas completas, cada uma cruzando duas ou três disciplinas. A Parte 3 fecha com o dia da prova e o checklist.</p>
<div class="box nv"><span class="eyebrow">Regra de ouro</span>Um parágrafo para cada aspecto do comando, na ordem do enunciado, aberto pelo diagnóstico (tópico frasal), com o fundamento, o fato do caso e — sempre — a <b>solução</b>. Na FCC, a conclusão de cada parágrafo é uma recomendação, não um resumo.</div>
<h3>Sumário</h3>
<table class="sum"><tbody>
<tr class="pt"><td colspan="2">Parte 1 · Visão geral da prova</td></tr>
<tr><td class="n">01</td><td>A prova discursiva da SEFAZ-SP 2026</td></tr>
<tr><td class="n">02</td><td>O que o edital pede (e o que não pontua)</td></tr>
<tr><td class="n">03</td><td>Como a FCC corrige o estudo de caso</td></tr>
<tr><td class="n">04</td><td>Os temas desta aula</td></tr>
<tr><td class="n">05</td><td>Roteiro de planejamento em cinco passos</td></tr>
<tr><td class="n">06</td><td>O parágrafo que pontua na FCC</td></tr>
<tr class="pt"><td colspan="2">Parte 2 · O estudo de caso de 30 linhas</td></tr>
<tr><td class="n">07</td><td>A estrutura do estudo de caso</td></tr>{sum_rod}
<tr class="pt"><td colspan="2">Parte 3 · O dia da prova</td></tr>
<tr><td class="n">08</td><td>A tarde da prova</td></tr>
<tr><td class="n">09</td><td>Checklist e recurso</td></tr>
</tbody></table>
<p class="nota">Fontes: Edital n.º 01/2026 – SEFAZ-SP/APOFP (DOE-SP de 02/10/2026) e Edital n.º 02/2026 de retificação (DOE-SP de 22/10/2026); legislação citada em cada rodada. Os casos e as resoluções desta aula são material do curso e não constituem padrão oficial da banca.</p>
</section>

<section class="pb"><div class="parte"><span class="eyebrow">Parte 1</span><h2>Visão geral da prova</h2><p>Formato, critérios do edital, correção da FCC, temas, planejamento e parágrafo.</p></div>
<span class="eyebrow">01</span><h2 class="sec">A prova discursiva da SEFAZ-SP 2026</h2>
<div class="stats">{stat('1','estudo de caso')}{stat('120','pontos')}{stat('48','nota mínima')}{stat('30','linhas máximas')}{stat('200','corrigidas por área')}</div>
<p>A P3 – Estudo de Caso é aplicada em <b>20 de dezembro de 2026</b>, à tarde, no mesmo período da P2 (data alterada pelo Edital n.º 02/2026; era 13/12). É uma questão interdisciplinar, sobre os Conhecimentos Básicos, avaliada de 0 a 120 pontos, com habilitação a partir de 48 (itens 9.1, 9.2, 9.5 e 9.6).</p>
<table><thead><tr><th>Ponto do edital</th><th>O que isso significa para você</th></tr></thead><tbody>
<tr><td class="k">Peso na nota final</td><td>P1 vale 112 pontos, P2 vale 120 e a P3 vale 120: a discursiva é cerca de um terço das provas. A nota final soma P1, P2, P3 e títulos (item 12.1).</td></tr>
<tr><td class="k">Desempate</td><td>Depois do critério de idade, o primeiro desempate é a maior nota na discursiva (item 13.1, b).</td></tr>
<tr><td class="k">Quem tem a P3 corrigida</td><td>Só os habilitados nas objetivas e mais bem classificados até o limite do quadro do item 8.3 — 200 por área, respeitados os empates —, além de todos os candidatos com deficiência habilitados.</td></tr>
<tr><td class="k">Limite de 30 linhas</td><td>Deve ser \"rigorosamente observado\", sob pena de perda de pontos (item 9.12). O rascunho não é corrigido (item 9.13).</td></tr>
<tr><td class="k">Caneta</td><td>Esferográfica de material transparente, tinta preta ou azul, letra legível (item 10.15).</td></tr>
</tbody></table>
<div class="box bad"><span class="eyebrow">Nota zero ou redução drástica</span>Zero por fuga ao tema, texto não articulado (só números ou palavras soltas), texto fora do local, assinatura fora do local, marca de identificação, prova em branco, letra ilegível ou desatendimento da grade de correção (item 9.9). Cópia do texto motivador, das questões ou de fontes públicas pode gerar redução drástica (item 9.10).</div>
</section>

<section class="pb"><span class="eyebrow">02</span><h2 class="sec">O que o edital pede (e o que não pontua)</h2>
<div class="box nv"><span class="eyebrow">Item 7.4 do edital — o mais importante desta aula</span>Será avaliada a capacidade de <b>interpretação</b> e de <b>proposta de solução</b> ao caso prático. A mera citação de legislação ou de definições específicas não é objeto de valoração por si só.</div>
<p>Somado aos itens 9.3 (domínio do conteúdo, experiência e adequação às atribuições do cargo) e 9.7 (nota prejudicada por abordagem tangencial, parcial ou diluída em divagações), o recado é claro: <b>quem só define e cita lei perde para quem aplica a lei ao fato e diz o que fazer</b>.</p>
<table><thead><tr><th>Critério do edital</th><th>Onde você atende</th></tr></thead><tbody>
<tr><td class="k">Interpretação do caso</td><td>Tópico frasal com o diagnóstico do fato (regular? irregular? viável?), usando os dados do enunciado</td></tr>
<tr><td class="k">Proposta de solução</td><td>Última frase de cada parágrafo: \"recomenda-se...\", \"deve-se...\"</td></tr>
<tr><td class="k">Domínio do conteúdo</td><td>Fundamento correto, com o vocabulário técnico da disciplina</td></tr>
<tr><td class="k">Correção gramatical (item 9.8)</td><td>Períodos curtos, ordem direta, revisão final</td></tr>
<tr><td class="k">Sem divagação (item 9.7)</td><td>Nada de introdução genérica nem de \"importância do tema\"</td></tr>
</tbody></table>
<h3>O conteúdo que alimenta o estudo de caso</h3>
<p>A P3 sai dos Conhecimentos Básicos (item 9.2), as mesmas dez disciplinas da P1. As quatro de peso 2 na P1 são as candidatas naturais ao caso, e as atribuições do cargo — programação financeira, execução orçamentária, garantias e obrigações do Tesouro, auditoria, despesas de pessoal, política creditícia — indicam o tipo de situação.</p>
<table><thead><tr><th>Disciplina (P1)</th><th>Questões · peso</th><th>O que mais rende num caso</th></tr></thead><tbody>
<tr><td class="k">Administração Financeira e Orçamentária</td><td>8 · peso 2</td><td>Créditos adicionais, contingenciamento, execução da despesa, restos a pagar, DEA, PPA/LDO/LOA</td></tr>
<tr><td class="k">Direito Financeiro e Finanças Públicas</td><td>8 · peso 2</td><td>LRF (metas, renúncia, pessoal, fim de mandato), operações de crédito, regra de ouro, dívida, federalismo fiscal</td></tr>
<tr><td class="k">Contabilidade Geral e Pública</td><td>8 · peso 2</td><td>Enfoques orçamentário e patrimonial, PCASP, DCASP, competência</td></tr>
<tr><td class="k">Fluência de Dados</td><td>8 · peso 2</td><td>Qualidade e governança de dados, LGPD, análise e anomalias, IA</td></tr>
<tr><td class="k">Administração Geral, Pública e Auditoria</td><td>8 · peso 1</td><td>Três Linhas, COSO, auditoria, políticas públicas, indicadores</td></tr>
<tr><td class="k">Direito Administrativo e Constitucional</td><td>10 + 10 · peso 1</td><td>Lei n.º 14.133/2021, LAI, improbidade; finanças públicas (arts. 163 a 169) e sistema tributário com a EC n.º 132/2023</td></tr>
<tr><td class="k">Economia · Matemática Financeira e Estatística</td><td>4 + 6 · peso 1</td><td>Avaliação de projetos (VPL, TIR, sensibilidade), efeitos macro sobre receita e dívida</td></tr>
</tbody></table>
<p class="nota">Quadro de questões e pesos: Edital n.º 01/2026, item 7.1. Língua Portuguesa (10 questões, peso 1) não entra como conteúdo do caso, mas é avaliada no texto.</p>
</section>

<section class="pb"><span class="eyebrow">03</span><h2 class="sec">Como a FCC corrige o estudo de caso</h2>
<p>O edital da SEFAZ-SP não publica pesos por quesito. Ele prevê uma <b>grade de correção (máscara de critérios)</b> com a abordagem e os requisitos de resposta definidos pela banca, divulgada junto com a resposta e a nota de cada candidato na vista da prova (item 9.15). Desatender a grade é causa de nota zero (item 9.9.7).</p>
<div class="box cre"><span class="eyebrow">Como ler isso</span>Na prática, a grade funciona como uma lista do que precisa aparecer em cada aspecto. O corretor procura o elemento; se ele estiver na primeira frase do parágrafo, com o fato do caso, você recebe o ponto mais rápido — e fica mais fácil fundamentar o recurso se ele não vier.</div>
<table><thead><tr><th>Etapa</th><th>Regra do edital</th></tr></thead><tbody>
<tr><td class="k">Resultado preliminar</td><td>Previsto para 03/03/2027 no cronograma retificado (pode mudar)</td></tr>
<tr><td class="k">Vista da prova</td><td>Concedida a todos no período recursal do resultado preliminar (item 14.7)</td></tr>
<tr><td class="k">Prazo do recurso</td><td>2 dias úteis, a partir do 1.º dia útil após a publicação, sem efeito suspensivo (item 14.2)</td></tr>
<tr><td class="k">Forma</td><td>Só pelo site da FCC, com o campo \"Fundamentação\" obrigatório, claro e objetivo, sem juntar documentos (item 14.4) e sem qualquer identificação nas razões (item 14.1.1)</td></tr>
<tr><td class="k">Quantidade</td><td>Um único recurso por candidato para cada evento; recurso de igual teor é desconsiderado (item 14.14)</td></tr>
</tbody></table>
<div class="box lr"><span class="eyebrow">Por que isso importa agora</span>Vista e recurso caem na mesma janela curta. Quem chega a ela sabendo como a grade funciona compara sua resposta item por item e escreve a fundamentação no prazo. Guarde esta página.</div>
</section>

<section class="pb"><span class="eyebrow">04</span><h2 class="sec">Os temas desta aula</h2>
<p>Os cinco casos foram escolhidos por três critérios: estão nos Conhecimentos Básicos, cruzam disciplinas como pede o item 7.3 e conversam com o momento — 2026 é o último ano dos mandatos estaduais, a reforma tributária muda a principal receita do Estado, e o edital trouxe Fluência de Dados com peso 2.</p>
<table><thead><tr><th>Rodada</th><th>Disciplinas cruzadas</th><th>Por que este tema</th></tr></thead><tbody>{temas}</tbody></table>
<div class="box cre"><span class="eyebrow">Como usar as rodadas</span>Leia só o enunciado, cronometre e escreva antes de olhar o resto. Depois, corrija-se com o espelho: atribua o conceito de cada quesito e compare com a proposta de redação. Os espelhos seguem a lógica de grade da FCC, para treino; a grade real só será conhecida na vista da prova.</div>
</section>

<section class="pb"><span class="eyebrow">05</span><h2 class="sec">Roteiro de planejamento em cinco passos</h2>
<p>A prova da tarde divide o tempo entre 40 questões da P2 e o estudo de caso. O roteiro leva cerca de 20 minutos e devolve esse tempo no texto definitivo, sem rasuras e sem linha desperdiçada.</p>
<div class="passo"><div class="bn">1</div><div><h4>Comando antes do caso</h4>Leia primeiro o que é pedido. Numere os aspectos, sublinhe o verbo (\"analise\", \"proponha\", \"indique\") e circule normas citadas e quantificadores.</div></div>
<div class="passo"><div class="bn">2</div><div><h4>Tipo de cada aspecto</h4>Conceito, regularidade de um fato, cálculo/interpretação ou recomendação. O tipo decide como o tópico frasal começa.</div></div>
<div class="passo"><div class="bn">3</div><div><h4>Linhas por aspecto</h4>30 linhas divididas pelo número de aspectos (veja a seção 07). Anote a cota ao lado de cada item no rascunho.</div></div>
<div class="passo"><div class="bn">4</div><div><h4>Caso marcado</h4>Só agora leia o caso. Marque cada dado (datas, percentuais, valores, \"sem\", \"inclusive\") e ligue-o ao aspecto que ele responde. Dado que você não usou é ponto que você deixou na mesa.</div></div>
<div class="passo"><div class="bn">5</div><div><h4>Esqueleto em palavras-chave</h4>Para cada parágrafo: diagnóstico · fundamento · fato · solução. Nada de rascunho integral: 30 linhas passadas a limpo custam tempo que falta na P2.</div></div>
<h3>Texto técnico × redação escolar</h3>
<table><thead><tr><th>Critério</th><th>Redação escolar</th><th>Estudo de caso (FCC)</th></tr></thead><tbody>
<tr><td class="k">Objetivo</td><td>Defender uma tese</td><td>Interpretar o caso e propor solução</td></tr>
<tr><td class="k">Abertura</td><td>Longa, com contextualização</td><td>Nenhuma, ou 1–2 linhas com o diagnóstico</td></tr>
<tr><td class="k">Repertório</td><td>Cultural e histórico</td><td>Normas, conceitos e dados do caso</td></tr>
<tr><td class="k">Estrutura</td><td>Livre</td><td>Um parágrafo por aspecto, na ordem do comando</td></tr>
<tr><td class="k">Fechamento</td><td>Proposta de intervenção geral</td><td>Solução no fim de cada parágrafo</td></tr>
</tbody></table>
</section>

<section class="pb"><span class="eyebrow">06</span><h2 class="sec">O parágrafo que pontua na FCC</h2>
<p>Se cada parágrafo seguir a mesma sequência, o corretor encontra o quesito na primeira frase e confere o resto em segundos. Na SEFAZ-SP, o quarto passo é o que o item 7.4 manda valorizar.</p>
<div class="formula">Diagnóstico <span>+</span> Fundamento <span>+</span> Fato do caso <span>+</span> Solução</div>
<table><thead><tr><th>Parte</th><th>O que é</th><th>Exemplo</th></tr></thead><tbody>
<tr><td class="k">1. Diagnóstico (tópico frasal)</td><td>Responde ao aspecto já na 1.ª frase</td><td>\"O contrato de reforma das escolas é irregular.\"</td></tr>
<tr><td class="k">2. Fundamento</td><td>A norma ou o conceito, aberto por recurso de autoridade</td><td>\"O art. 42 da LRF veda, nos dois últimos quadrimestres do mandato, obrigação com parcelas no exercício seguinte sem caixa.\"</td></tr>
<tr><td class="k">3. Fato do caso</td><td>O dado do enunciado que se encaixa na norma</td><td>\"Assinado em setembro, com parcelas em 2027 e sem saldo...\"</td></tr>
<tr><td class="k">4. Solução</td><td>O que fazer, em uma frase</td><td>\"...o ajuste deve ser reduzido ao que couber no caixa ou adiado.\"</td></tr>
</tbody></table>
<div class="box bad"><span class="eyebrow">Assim não pontua</span>\"A Lei de Responsabilidade Fiscal é um marco da gestão fiscal responsável no Brasil, tendo grande importância para o equilíbrio das contas públicas. O art. 42 trata do fim do mandato.\"</div>
<div class="box good"><span class="eyebrow">Assim pontua</span>\"O contrato é irregular. O art. 42 da LRF veda, nos dois últimos quadrimestres do mandato, obrigação com parcelas no exercício seguinte sem caixa. Assinado em setembro, com parcelas em 2027 e sem saldo, o ajuste deve ser reduzido ao que couber no caixa ou adiado.\"</div>
<h3>Como citar normas</h3>
<ul><li>Primeira menção completa (\"Lei n.º 14.133/2021\"); depois, \"a mesma lei\".</li>
<li>Artigo só com certeza. Número errado tira mais credibilidade do que número ausente — e, pelo item 7.4, a citação sozinha não dá ponto.</li>
<li>Normas paulistas pelo nome, se souber (\"Constituição do Estado de São Paulo\", \"Lei estadual n.º 10.261/1968\").</li></ul>
<p><b>Conectivos que organizam:</b> fundamentar — \"Nos termos do...\", \"Conforme o...\"; aplicar ao caso — \"No caso,...\"; propor solução — \"Recomenda-se...\", \"Deve-se...\"; passar ao aspecto seguinte — \"Além disso,...\", \"Quanto ao fato 2,...\", \"Por fim,...\".</p>
</section>

<section class="pb"><div class="parte"><span class="eyebrow">Parte 2</span><h2>O estudo de caso de 30 linhas</h2><p>Uma questão · Conhecimentos Básicos · 120 pontos · até 30 linhas</p></div>
<span class="eyebrow">07</span><h2 class="sec">A estrutura do estudo de caso</h2>
<p>O estudo de caso é um texto dissertativo em prosa, que responde aos aspectos do comando aplicados ao caso. Não é peça oficial: não leva cabeçalho, título, vocativo nem assinatura.</p>
<div class="tri"><div class="t3"><span class="eyebrow">O estudo de caso tem</span><ul><li>Um parágrafo por aspecto, na ordem do comando</li><li>Diagnóstico na 1.ª frase de cada parágrafo</li><li>Fundamento e dado do caso em cada parágrafo</li><li>Solução no fim de cada parágrafo</li><li>Abertura opcional de 1–2 linhas com o diagnóstico geral</li></ul></div>
<div class="t2"><span class="eyebrow">O estudo de caso não tem</span><ul><li>Título, cabeçalho, vocativo ou assinatura</li><li>Introdução genérica ou conclusão que só repete</li><li>Tópicos, setas ou tabelas</li><li>Cópia do enunciado (item 9.10)</li><li>Seu nome ou qualquer marca (item 9.9.4)</li></ul></div></div>
<h3>Calibragem das 30 linhas</h3>
<table><thead><tr><th>Comando com</th><th>Linhas por parágrafo</th><th>Total alvo</th></tr></thead><tbody>
<tr><td class="k">3 aspectos</td><td>(1–2 de abertura) + 9 + 9 + 9</td><td>28–30</td></tr>
<tr><td class="k">4 aspectos</td><td>7 + 7 + 7 + 7</td><td>28–30</td></tr>
<tr><td class="k">5 aspectos</td><td>6 + 6 + 6 + 5 + 5</td><td>28–30</td></tr>
</tbody></table>
<p>Escreva perto do limite, mas nunca além dele: o item 9.12 tira pontos de quem passa das 30 linhas. Se o comando der valores diferentes por aspecto, as linhas acompanham os valores.</p>
<div class="box cre"><span class="eyebrow">E a introdução?</span>Com 30 linhas e quatro aspectos, ela é luxo. Com três aspectos, uma frase de abertura que já dá o diagnóstico (\"As três medidas tratam do fim do mandato, mas apenas parte delas pode ser adotada\") ajuda o corretor e custa duas linhas. Nunca abra com contexto genérico.</div>
</section>

{rods}

<section class="pb"><div class="parte"><span class="eyebrow">Parte 3</span><h2>O dia da prova</h2><p>Gestão da tarde e conferência final</p></div>
<span class="eyebrow">08</span><h2 class="sec">A tarde da prova</h2>
<p>Pela manhã, a P1 tem 80 questões. À tarde, no mesmo período, vêm a P2 (40 questões de peso 3) e a P3. O edital de convocação, previsto para 08/12/2026, confirma horários e local. Vale decidir antes de entrar na sala como dividir a tarde. Uma sugestão:</p>
<table><thead><tr><th>Tempo</th><th>Etapa</th></tr></thead><tbody>
<tr><td class="k">10 min</td><td>Ler o comando e o caso da P3, numerar os aspectos e marcar os dados</td></tr>
<tr><td class="k">15 min</td><td>Esqueleto em palavras-chave e linhas por parágrafo</td></tr>
<tr><td class="k">35–40 min</td><td>Texto definitivo</td></tr>
<tr><td class="k">5–10 min</td><td>Revisão: um parágrafo por aspecto, solução em cada um, acentos, crases, concordância, linha 30</td></tr>
<tr><td class="k">Restante</td><td>P2, com reserva para transcrever o gabarito</td></tr>
</tbody></table>
<div class="box lr"><span class="eyebrow">Por onde começar</span>A P3 vale 120 pontos e exige a cabeça mais descansada. Se a ordem for livre, há bom argumento para fazê-la antes da P2. Se preferir aquecer com a objetiva, fixe um horário-limite para parar e começar o caso.</div>
<h3>Sete erros que custam a vaga</h3>
<ul><li>Só definir e citar lei, sem aplicar ao caso e sem propor solução (item 7.4).</li>
<li>Pular um aspecto do comando: cada aspecto é um quesito da grade.</li>
<li>Abrir com contexto genérico (\"o tema é de grande relevância...\").</li>
<li>Ignorar os números e datas do caso: estão ali para serem usados.</li>
<li>Copiar trechos do enunciado (item 9.10).</li>
<li>Passar da 30.ª linha (item 9.12) ou escrever fora do espaço (item 9.9.2).</li>
<li>Assinar ou deixar qualquer marca que identifique (item 9.9.4).</li></ul>
</section>

<section class="pb"><span class="eyebrow">09</span><h2 class="sec">Checklist do dia da prova</h2>
<div class="tri"><div class="t1"><span class="eyebrow">Antes de passar a limpo</span><ul><li>Cada aspecto tem um parágrafo?</li><li>Aspectos duplos (\"conceito e espécies\", \"requisitos e garantia\") estão completos?</li><li>Todos os dados do caso foram usados?</li><li>Cada parágrafo abre com o diagnóstico?</li><li>Cada parágrafo fecha com uma solução?</li></ul></div>
<div class="t3"><span class="eyebrow">Depois de passar a limpo</span><ul><li>Nada além da linha 30 nem fora do espaço.</li><li>Nenhuma assinatura, nome ou marca.</li><li>Letra legível, caneta preta ou azul.</li><li>Acentos, crases e concordâncias revisados.</li><li>Nenhuma frase copiada do enunciado.</li></ul></div></div>
<div class="box nv"><span class="eyebrow">Última palavra</span>A diferença entre 48 e 90 pontos raramente está no conhecimento. Está em responder a tudo o que foi perguntado, na ordem em que foi perguntado, aplicando a norma ao fato e dizendo o que fazer. Treine até isso ficar automático.</div>
<h3>Fontes</h3>
<ul class="fontes">
<li>SEFAZ-SP. Edital n.º 01/2026, de 1.º/10/2026, Concurso Público para Analista em Planejamento, Orçamento e Finanças Públicas – APOFP (DOE-SP de 02/10/2026), itens 7, 8, 9, 10, 12, 13 e 14.</li>
<li>SEFAZ-SP. Edital n.º 02/2026, de 21/10/2026, retificação do cronograma (DOE-SP de 22/10/2026): provas em 20/12/2026; resultado preliminar previsto para 03/03/2027 (conferido por fontes secundárias: Gran Cursos, Notícias Concursos, Folha Dirigida/Qconcursos).</li>
<li>Constituição Federal; ADCT; EC n.º 132/2023; LC n.º 101/2000 (LRF); Lei n.º 4.320/1964; Lei n.º 14.133/2021; Lei n.º 12.527/2011 (LAI); Lei n.º 13.709/2018 (LGPD); Código Penal; STF, Tema 483 da repercussão geral; MCASP (STN); IIA, Modelo das Três Linhas (2020).</li>
</ul>
<p class="nota">O edital prevalece sobre qualquer resumo, inclusive este. Confira datas e regras no texto oficial e no site da FCC.</p>
</section>

<section class="pb"><span class="eyebrow">Uma palavra final</span><h2 class="sec">Obrigado por ter lido até aqui</h2>
{AUTOR}
<p>Eu sou o Samuel. Passei pelos dois lados da discursiva: como candidato, em concursos da área fiscal e de controle, e hoje como auditor que escreve relatórios técnicos todos os dias. Há mais de seis anos ajudo concurseiros a escrever melhor na prova — com aulas, correções e recursos contra a nota da discursiva.</p>
<p>Montei esta aula do mesmo jeito que corrijo uma prova: olhando o que a banca realmente cobra e o que faz um texto ganhar ou perder pontos. Se ela te ajudou a enxergar a P3 da SEFAZ-SP com mais clareza, já valeu.</p>
<div class="box lr"><span class="eyebrow">Gostou do material?</span>Comenta lá no <b>@auditor_discursivas</b> o que você achou. Parece pouco, mas cada comentário ajuda muito o meu trabalho e faz este material chegar a mais gente que está na mesma luta que você. Por lá eu sempre posto conteúdo sobre discursivas: estrutura, análise de provas e padrões das bancas.</div>
<p>Eu torço muito por você. Estude com método, treine na folha, cronometre os textos e chegue ao dia 20 de dezembro confiando no que você construiu.</p>
<div class="cta"><span class="eyebrow">E se a nota não vier como você esperava?</span>Não aceite a nota de cara. Na FCC, a vista da prova — com a grade de correção e a pontuação de cada critério — e o recurso acontecem juntos, em <b>apenas 2 dias úteis</b>. Um recurso bem fundamentado aponta, critério por critério, o que a sua resposta já trazia e não foi pontuado. Com nota mínima de 48 e desempate pela discursiva, isso pode ser a diferença entre a eliminação e a nomeação.<br><br><b>Me chama no direct do @auditor_discursivas</b> que a gente analisa a sua prova juntos e prepara o recurso. A análise de viabilidade é gratuita.</div>
<p style="margin-top:12pt">Um abraço e boa prova,<br><b>Samuel Wolf</b></p>
</section>
</body></html>"""
    return html

HEADER = """<div style="width:100%;font-family:Lato,sans-serif;font-size:7.5pt;color:#8a8f98;padding:0 18mm;display:flex;justify-content:space-between">
<span style="font-weight:700;color:#F04E23;letter-spacing:.14em">AUDITOR DISCURSIVAS</span><span>Discursiva SEFAZ-SP 2026</span></div>"""
FOOTER = """<div style="width:100%;font-family:Lato,sans-serif;font-size:7.5pt;color:#8a8f98;padding:0 18mm;text-align:right">
@auditor_discursivas · Página <span class="pageNumber"></span></div>"""

async def pdf(html_path, pdf_path):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.goto('file://' + str(html_path)); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
        await pg.pdf(path=str(pdf_path), format='A4', print_background=True, display_header_footer=True,
                     header_template=HEADER, footer_template=FOOTER,
                     margin={'top': '22mm', 'bottom': '20mm', 'left': '18mm', 'right': '18mm'})
        await b.close()

if __name__ == '__main__':
    out = BASE / 'saida'; out.mkdir(exist_ok=True)
    for r in RODADAS:
        _, n = folha(r['proposta']); print(f"Rodada {r['n']}: {n} linhas")
    hp = out / 'Aula SEFAZ-SP 2026 - Discursiva do APOFP.html'
    hp.write_text(montar(), encoding='utf-8')
    pp = out / 'Aula SEFAZ-SP 2026 - Discursiva do APOFP - Temas inéditos.pdf'
    asyncio.run(pdf(hp, pp)); print('ok', pp)
