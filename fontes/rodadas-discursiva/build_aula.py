# -*- coding: utf-8 -*-
"""Rodadas de Discursiva — gera o PDF de uma rodada.
Uso: python3 build_aula.py conteudo/controle_1.py   → saida/<area>-<n>.pdf (+ .html)
Estrutura do PDF: capa · por que fiz · mini-aula da área (areas/<area>.py) · Tema 1 e Tema 2
(enunciado → esqueleto + padrão de resposta + espelho → texto definitivo + dicas) · palavra final + CTA · fontes.
"""
import sys, html, base64, pathlib, importlib.util, re
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent

def load(path):
    spec = importlib.util.spec_from_file_location('m', path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

C = load(sys.argv[1])
A_ = load(ROOT / 'areas' / f'{C.AREA}.py')
FOTO = 'data:image/jpeg;base64,' + base64.b64encode((ROOT / 'foto.jpg').read_bytes()).decode()
CSS = (ROOT / 'base.css').read_text().replace("url('fonts/", f"url('file://{ROOT}/fonts/") + """
.texto{border-left:3pt solid var(--lar);background:#fffdf9;padding:6pt 10pt;margin:0 0 8pt;font-size:9.6pt}
.texto p{margin:0 0 4pt}.texto .fonte{font-size:8pt;color:var(--mu);font-style:italic;margin:2pt 0 0}
.comando{margin:8pt 0 0;font-size:10.2pt}
.esp .cc{font-size:8.6pt;color:#3a4452;margin:1pt 0}
.trilha td:first-child{width:14%;font-family:Poppins;font-weight:700;color:var(--lar)}
.capa .rodtag{display:inline-block;background:var(--lar);color:#fff;font-family:Poppins;font-weight:800;font-size:12pt;letter-spacing:.12em;padding:6pt 12pt;border-radius:6pt;margin-top:24mm}
"""

def folha(pars, width=67, total=30):
    lines = []
    for p in pars:
        words = p.split(); cur = ''; first = True; pl = []
        for w in words:
            lim = width - 4 if first else width
            cand = (cur + ' ' + w).strip()
            if len(cand) <= lim: cur = cand
            else: pl.append((cur, first)); first = False; cur = w
        pl.append((cur, first))
        for i, (t, f) in enumerate(pl):
            cls = (['ini'] if f else []) + (['fim'] if i == len(pl) - 1 else [])
            lines.append((t, ' '.join(cls)))
    n = len(lines)
    out = []
    for i in range(total):
        t, c = lines[i] if i < n else (' ', 'fim')
        out.append(f'<div class="ln"><span class="nr">{i+1}</span><span class="t {c}">{html.escape(t)}</span></div>')
    return n, '\n'.join(out)

AUTOR = f'''<div class="autor"><div class="foto" style="background-image:url({FOTO})"></div>
<div><div class="nm">Samuel Wolf</div><div class="at">@auditor_discursivas</div><ul>
<li>Auditor de Controle Externo do TCE-RJ</li><li>Engenheiro de Infraestrutura Aeronáutica formado pelo ITA</li>
<li>Nomeado Auditor Fiscal da SEFAZ-RS e da SEFIN Manaus</li></ul></div></div>'''

P = []; add = P.append
ul = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'

# CAPA
add(f'''<section class="capa"><div class="barra"></div><div class="wm">AUDITOR DISCURSIVAS</div>
<div><span class="rodtag">AULA GRATUITA · RODADA {C.N_AREA} · {A_.NOME.upper()}</span></div>
<h1 style="margin-top:8mm">Rodadas de<br><span>Discursiva</span></h1>
<div class="sub">{A_.SUBTITULO} Uma mini-aula de método e dois temas inéditos, cada um com padrão de resposta, espelho de correção e texto definitivo completo.</div>
<div class="tag">{A_.PUBLICO}</div>
<div class="data">{html.escape(C.TEMAS[0]['curto'])} · {html.escape(C.TEMAS[1]['curto'])}</div>
<div class="rod"><span>Trilha {A_.NOME} · Rodada {C.N_AREA} de 5 · {C.DATA}</span><span>@auditor_discursivas</span></div></section>''')

# POR QUE
add(f'''<section class="pb"><span class="eyebrow">Antes de começar</span><h2 class="sec">Como funcionam as Rodadas</h2>
{AUTOR}
<p>Eu sou o Samuel. Passei por concursos com prova discursiva e hoje, além do trabalho de auditor, ajudo concurseiros a escrever melhor na prova, com aulas e com recursos contra a nota da discursiva.</p>
<p>As <b>Rodadas de Discursiva</b> são um treino semanal e gratuito, em três trilhas: <b>Controle</b>, <b>Fiscal</b> e <b>Policial</b>. Toda semana sai uma rodada nova, alternando as trilhas, com o mesmo formato: uma mini-aula curta de método e <b>dois temas inéditos</b>, cada um com o padrão de resposta, o espelho de correção e um <b>texto definitivo</b> completo para você comparar com o seu.</p>
<table class="trilha"><thead><tr><th>Etapa</th><th>O que fazer</th></tr></thead><tbody>
<tr><td>1</td><td>Leia a mini-aula ({A_.NOME.lower()}): como a banca cobra e o parágrafo que pontua.</td></tr>
<tr><td>2</td><td>Leia só o enunciado do Tema 1, cronometre e escreva à mão, numa folha de {C.TEMAS[0]['linhas']} linhas.</td></tr>
<tr><td>3</td><td>Corrija-se com o espelho: conceito por quesito, conte os erros e só depois leia o texto definitivo.</td></tr>
<tr><td>4</td><td>Repita com o Tema 2. Guarde os textos: na próxima rodada da trilha, compare a evolução.</td></tr>
</tbody></table>
<div class="box lr"><span class="eyebrow">Quer a próxima rodada?</span>Siga o <b>@auditor_discursivas</b>. A próxima rodada é a da trilha <b>{C.PROXIMA[0]}</b>, em <b>{C.PROXIMA[1]}</b>. Para receber esta trilha de novo, comente ou mande <b>{A_.PALAVRA}</b> no direct.</div>
</section>''')

# MINI-AULA
for s in A_.aula():
    add(s)

# TEMAS
for i, t in enumerate(C.TEMAS, 1):
    aspectos = ''.join(f'<li><span class="i">{k}</span><span>{a} <span class="val">[valor: {v} pontos]</span></span></li>' for k, (a, v) in enumerate(t['aspectos'], 1))
    textos = ''.join(f'<div class="texto">{c}<p class="fonte">{f}</p></div>' for c, f in t['motivadores'])
    add(f'''<section class="pb rod-h"><span class="eyebrow">Rodada {C.N_AREA} · Tema {i} · {t['linhas']} linhas · {A_.FORMATO_CURTO}</span>
<h2><span class="rn">{i}.</span> {t['titulo']}</h2>
<div class="eixo"><b>Assunto:</b> {t['eixo']}. Enunciado inédito, elaborado para treino no {A_.PADRAO_BANCA}.</div>
<div class="enun"><span class="eyebrow">Questão · inédita · {A_.PADRAO_BANCA} · {t['linhas']} linhas</span>
{textos}
<p class="comando">{t['comando']}</p><ol>{aspectos}</ol></div>
<div class="pare">Pare aqui. Planeje e escreva a sua resposta em até {t['linhas']} linhas, cronometrando cerca de {t['minutos']} minutos, antes de virar a página. A solução começa na próxima página.</div>
</section>''')
    esq = ''.join(f'<tr><td class="k">{a}</td><td>{b}</td></tr>' for a, b in t['esqueleto'])
    pad = ''.join(f'<tr><td class="k">{a}</td><td>{ul(b)}</td></tr>' for a, b in t['padrao'])
    esp = '<tr><td class="q">1</td><td>Apresentação e estrutura textual: legibilidade, respeito às margens e indicação de parágrafos</td><td>0,00 a ' + t['apresentacao'] + '</td></tr>'
    for q, (desc, conceitos, pts) in enumerate(t['espelho'], 1):
        cc = ''.join(f'<p class="cc">{c}</p>' for c in conceitos)
        esp += f'<tr><td class="q">2.{q}</td><td><b>{desc}</b>{cc}</td><td>{pts}</td></tr>'
    add(f'''<section class="pb sol"><h3 style="margin-top:0">Tema {i} · Como montar o esqueleto</h3>
<table class="esq"><thead><tr><th>Parágrafo</th><th>Palavras-chave do rascunho</th></tr></thead><tbody>{esq}</tbody></table>
<h3>Padrão de resposta (do curso)</h3>
<table class="pad"><thead><tr><th>Item</th><th>O que a resposta deve conter</th></tr></thead><tbody>{pad}</tbody></table>
<h3>Espelho de correção (do curso, {A_.PADRAO_BANCA})</h3>
<table class="esp"><thead><tr><th>Quesito</th><th>O que o corretor procura</th><th>Pontos</th></tr></thead><tbody>{esp}
<tr class="tot"><td>Total</td><td>Nota de conteúdo máxima</td><td>{t['total']}</td></tr></tbody></table>
<p class="nota">{A_.NOTA_DESCONTO}</p>
</section>''')
    nl, fl = folha(t['texto'], total=t['linhas'])
    t1, t2, t3 = t['tri']
    add(f'''<section class="pb"><h3 style="margin-top:0">Tema {i} · Proposta de texto definitivo · {nl} de {t['linhas']} linhas</h3>
<div class="folha"><span class="eyebrow">TEXTO DEFINITIVO · {t['linhas']} LINHAS</span>
{fl}
</div>
<p class="nota">Contagem simulada com cerca de 67 caracteres por linha. Na sua letra, o número muda: treine na folha pautada.</p>
<div class="tri"><div class="t1"><span class="eyebrow">Armadilhas do tema</span>{ul(t1)}</div><div class="t2"><span class="eyebrow">Erros mais comuns</span>{ul(t2)}</div><div class="t3"><span class="eyebrow">Dicas estratégicas</span>{ul(t3)}</div></div>
</section>''')
    print(f'Tema {i}: {nl} linhas')
    assert nl <= t['linhas'], f'Tema {i} passou de {t["linhas"]} linhas'

# PALAVRA FINAL
add(f'''<section class="pb"><span class="eyebrow">Uma palavra final</span><h2 class="sec">Até a próxima rodada</h2>
{AUTOR}
<p>Se você escreveu os dois textos antes de olhar as soluções, já fez a parte mais difícil: treinar como na prova. Compare o seu texto com o espelho com honestidade, quesito por quesito. É assim que o corretor vai ler o seu.</p>
<div class="box lr"><span class="eyebrow">Gostou?</span>Comenta no <b>@auditor_discursivas</b> o que achou e manda esta rodada para quem estuda com você. A próxima é a da trilha <b>{C.PROXIMA[0]}</b>, em <b>{C.PROXIMA[1]}</b>.</div>
<div class="cta"><span class="eyebrow">E se a nota da sua discursiva não vier como você esperava?</span>Não aceite a nota de cara. Depois do resultado, a banca abre um prazo curto de recurso, e um recurso bem fundamentado mostra, quesito por quesito, o que o seu texto já trazia e não foi pontuado — e confere a contagem de erros e de linhas.<br><br><b>Mande RECURSO no direct do @auditor_discursivas.</b> A análise de viabilidade é gratuita: você só decide depois de saber se vale recorrer.</div>
<p style="margin-top:12pt">Um abraço e bons estudos,<br><b>Samuel Wolf</b></p>
<h3>Fontes</h3><ul class="fontes">{''.join(f'<li>{f}</li>' for f in C.FONTES)}</ul>
<p class="nota">Os temas, padrões de resposta, espelhos e textos desta rodada são material do curso, elaborados para treino, e não constituem padrão oficial de nenhuma banca. Confira sempre o edital do seu concurso.</p>
</section>''')

doc = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Rodada {C.N_AREA} {A_.NOME} · Auditor Discursivas</title><style>{CSS}</style></head><body>{"".join(P)}</body></html>'
out = ROOT / 'saida'; out.mkdir(exist_ok=True)
slug = f'{C.AREA}-{C.N_AREA}'
(out / f'{slug}.html').write_text(doc, encoding='utf-8')
head = f'<div style="width:100%;font-family:Poppins;font-size:6.5pt;padding:0 18mm;display:flex;justify-content:space-between;margin-top:6mm"><span style="color:#F04E23;font-weight:700;letter-spacing:.28em">AUDITOR DISCURSIVAS</span><span style="color:#2A3544;letter-spacing:.12em">Rodadas de Discursiva · {A_.NOME} {C.N_AREA}</span></div>'
foot = '<div style="width:100%;font-family:Poppins;font-size:6.5pt;padding:0 18mm;text-align:right;color:#2A3544;margin-bottom:6mm">@auditor_discursivas · Página <span class="pageNumber"></span></div>'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto('file://' + str(out / f'{slug}.html')); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(400)
    pg.pdf(path=str(out / f'{slug}.pdf'), format='A4', print_background=True, display_header_footer=True, header_template=head, footer_template=foot, prefer_css_page_size=True)
    b.close()
print('ok', out / f'{slug}.pdf')
