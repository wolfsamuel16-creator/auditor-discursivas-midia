"""Gera as 3 campanhas de recurso do TCE-PE (D-7, D-1, D) no layout aprovado do perfil."""
import pathlib

CSS = pathlib.Path(__file__).with_name('base.css').read_text(encoding='utf-8')
ROD = '<div class="rod"><span>@auditor_discursivas</span><span class="sv">{}</span></div>'
CTA_SMALL = 'ou mande <b>TCEPE</b> no direct. A análise de viabilidade é gratuita.'
AUTOR = ('<div class="autor" style="margin-top:0;align-items:center"><div class="foto" style="flex:0 0 190px;width:190px;height:190px"></div>'
         '<div><b>Samuel Wolf</b><span style="display:block;color:var(--lar);opacity:1;font-weight:700;margin:4px 0 14px">Recursos de provas discursivas</span>'
         '<ul class="cred"><li>✔ Engenheiro pelo ITA</li><li>✔ Auditor de Controle Externo do TCE-RJ</li>'
         '<li>✔ Nomeado Auditor Fiscal da SEFAZ-RS</li><li>✔ Nomeado Auditor Fiscal da SEFIN Manaus</li></ul></div></div>')
AUTOR_ST = '<div class="autor"><div class="foto"></div><div><b>Samuel Wolf</b><span>Recursos de provas discursivas</span></div></div>'


def top(i, n):
    return f'<div class="top"><span class="wm">AUDITOR DISCURSIVAS</span><span class="ct">{i:02d} / {n:02d}</span></div>'


def capa(i, n, h1, chips, p):
    ch = ''.join(f'<span class="chip">{c}</span>' for c in chips)
    return (f'<section class="s navy">{top(i, n)}<div class="sp"></div><div class="selo">RECURSO DE DISCURSIVA</div>'
            f'<h1>{h1}</h1><div class="chips">{ch}</div><p class="big">{p}</p><div class="sp"></div>{ROD.format("Arraste →")}</section>')


def lista(i, n, h2, itens, card):
    li = ''.join(f'<li><span class="num">{k}</span><span>{t}</span></li>' for k, t in enumerate(itens, 1))
    return (f'<section class="s claro" style="justify-content:center">{top(i, n)}<h2>{h2}</h2><ul class="lista">{li}</ul>'
            f'<div class="card">{card}</div>{ROD.format("Salvar →")}</section>')


def linha(i, n, h2, eventos, card):
    ev = ''.join(f'<div class="ev{" d" if d else ""}"><span class="k">{k}</span><span>{t}</span></div>' for k, t, d in eventos)
    return (f'<section class="s claro" style="justify-content:center">{top(i, n)}<h2>{h2}</h2><div class="tl">{ev}</div>'
            f'<div class="card">{card}</div>{ROD.format("Salvar →")}</section>')


def fecho(i, n, h2, p):
    return (f'<section class="s claro">{top(i, n)}<div class="sp"></div><h2>{h2}</h2><p class="big" style="margin:44px 0 52px">{p}</p>'
            f'<div class="box">Comente TCEPE<small>{CTA_SMALL}</small></div><div class="sp"></div>{AUTOR}'
            f'<div class="rod"><span>@auditor_discursivas</span><span></span></div></section>')


def story(corpo, tom='claro'):
    return f'<section class="st {tom}"><div class="wm">AUDITOR DISCURSIVAS</div>{corpo}</section>'


BOX_ST = '<div class="box">Mande TCEPE no direct.<small>A análise de viabilidade é gratuita.</small></div>'
CHIPS = ['TCE-PE', 'FGV', 'Cargos reaplicados']

CAMP = {
 'd7': dict(slides=[
    capa(1, 4, 'TCE-PE: a nota da discursiva sai em <em>7 dias.</em>', CHIPS,
         'E o recurso só vale de <b>13 a 16/11</b>. Quem se prepara agora chega pronto.'),
    linha(2, 4, 'Na FGV, a janela de recurso é <em>uma só.</em>',
          [('12/11', '<b>Resultado preliminar</b> da discursiva', False),
           ('13 a 16/11', '<b>Recurso</b> contra a nota da discursiva', True),
           ('08/12', '<b>Resultado definitivo</b> e resultado final', False)],
          'Não há padrão preliminar com recurso próprio, como no Cebraspe. <b>Você vê a nota e recorre no mesmo prazo curto.</b>'),
    lista(3, 4, 'Use esta semana para <em>adiantar o recurso</em>',
          ['<b>Reconstrua sua resposta</b> enquanto ainda lembra, item por item',
           'Liste as <b>normas, artigos e acórdãos</b> que você citou',
           'Leia no edital as <b>regras do recurso</b>'],
          '<b>Ponto recuperado no recurso vale tanto quanto questão acertada na objetiva.</b>'),
    fecho(4, 4, 'Quer chegar ao dia 13 <em>com o recurso encaminhado?</em>', 'Eu leio a sua resposta contra o espelho e digo se o recurso tem fundamento.'),
 ], stories=[
    story('<div class="selo">RECURSO DE DISCURSIVA</div><p class="big">Discursiva do TCE-PE</p><div class="big-n">7 dias</div>'
          '<p class="big" style="margin:30px 0 60px">para a nota sair (12/11). O recurso é só de <b>13 a 16/11</b>.</p>' + BOX_ST),
    story('<h1 style="font-size:96px">Como você acha que foi na <em>discursiva do TCE-PE?</em></h1>'
          '<div class="opt"><div class="op a">💪 Fui bem</div><div class="op b">😬 Posso precisar de recurso</div></div>'
          '<p class="mid" style="margin-top:60px">Responda no direct com a sua opção. Se for a segunda, mande <b>TCEPE</b>.</p>'),
    story('<h1 style="font-size:92px">Adiante o recurso <em>nesta semana</em></h1>'
          '<ul class="lista"><li><span class="num">1</span><span>Reconstrua a resposta</span></li><li><span class="num">2</span><span>Liste as normas citadas</span></li>'
          '<li><span class="num">3</span><span>Reserve 13 a 16/11</span></li></ul><div class="sp"></div>' + BOX_ST + AUTOR_ST),
 ]),
 'd1': dict(slides=[
    capa(1, 4, 'TCE-PE: a nota da discursiva sai <em>amanhã.</em>', ['TCE-PE', 'FGV', 'Recurso 13 a 16/11'],
         'São só 4 dias de prazo. <b>Deixe tudo pronto hoje.</b>'),
    lista(2, 4, 'Checklist para <em>hoje</em>',
          ['A <b>reconstrução da sua resposta</b>, item por item',
           'As <b>normas e fundamentos</b> que você usou',
           '<b>13 a 16/11</b> reservados na agenda'],
          'Quando a nota sair, compare <b>item por item</b> com o espelho da banca.'),
    lista(3, 4, 'Onde o recurso <em>tem argumento</em>',
          ['Você <b>abordou o item</b> e ele veio zerado ou parcial',
           'Você usou <b>fundamento equivalente</b> ao do espelho',
           'Houve desconto de forma <b>sem erro identificável</b>'],
          'Recurso bom não reclama da nota: <b>aponta a linha da sua folha que atende ao critério.</b>'),
    fecho(4, 4, 'Saiu e não concordou? <em>Fala comigo.</em>', 'A análise começa assim que você me mandar a sua nota.'),
 ], stories=[
    story('<div class="selo">RECURSO DE DISCURSIVA</div><h1 style="font-size:110px">Amanhã sai a nota da discursiva do <em>TCE-PE.</em></h1>'
          '<p class="big" style="margin:50px 0 60px">Recurso: <b>13 a 16/11</b>.</p>' + BOX_ST),
    story('<h1 style="font-size:96px">Checklist para <em>hoje</em></h1><ul class="lista"><li><span class="num">1</span><span>Resposta reconstruída</span></li>'
          '<li><span class="num">2</span><span>Normas e fundamentos listados</span></li><li><span class="num">3</span><span>13 a 16/11 na agenda</span></li></ul>'),
    story('<h1 style="font-size:92px">Não concordou com a nota? <em>Fala comigo.</em></h1><p class="big" style="margin:50px 0 60px">Eu leio a sua resposta contra o espelho e digo se o recurso tem fundamento.</p>'
          + BOX_ST + AUTOR_ST),
 ]),
 'd': dict(slides=[
    capa(1, 4, 'Não concorda com a nota da sua discursiva do <em>TCE-PE?</em>', ['TCE-PE', 'FGV', 'Recurso 13 a 16/11'],
         '<b>Você ainda tem chance.</b> O recurso vai de 13 a 16/11.'),
    lista(2, 4, 'Como funciona <em>comigo</em>',
          ['Você me manda <b>TCEPE</b>, o cargo e a sua nota de cada item',
           'Faço a <b>análise de viabilidade gratuita</b>: sua resposta × espelho',
           'Se houver fundamento, eu <b>redijo o recurso</b> item por item, dentro do prazo'],
          'Questão discursiva: <b>R$ 350</b> · Peça técnica: <b>R$ 700</b>. A análise de viabilidade é gratuita.'),
    linha(3, 4, '4 dias, com <em>fim de semana</em> no meio',
          [('sex 13/11', 'Abre o recurso', False), ('sáb 14 e dom 15', 'Prazo correndo', False), ('seg 16/11', '<b>Último dia</b>', True)],
          '<b>Quanto antes você mandar, mais tempo para fundamentar.</b> Depois de 16/11, essa correção não se discute mais.'),
    fecho(4, 4, 'Ponto recuperado é <em>ponto na classificação.</em>', 'Mande agora e eu te digo se o seu recurso tem fundamento.'),
 ], stories=[
    story('<div class="selo">RECURSO DE DISCURSIVA</div><h1 style="font-size:104px">Dia de resultado: discursiva do <em>TCE-PE.</em></h1>'
          '<p class="big" style="margin:50px 0 60px">Não concordou com a nota? O recurso é de <b>13 a 16/11</b>.</p>' + BOX_ST + AUTOR_ST),
    story('<div class="selo">RECURSO TCE-PE</div><p class="big">Recurso aberto até segunda</p><div class="big-n">16/11</div>'
          '<p class="big" style="margin:30px 0 60px">Quanto antes, mais tempo para fundamentar.</p>' + BOX_ST),
    story('<div class="selo">RECURSO TCE-PE</div><p class="big">Faltam</p><div class="big-n">3 dias</div>'
          '<p class="big" style="margin:30px 0 60px">O prazo termina segunda, 16/11.</p>' + BOX_ST),
    story('<div class="selo">RECURSO TCE-PE</div><p class="big">Faltam</p><div class="big-n">2 dias</div>'
          '<p class="big" style="margin:30px 0 60px">Recurso bom aponta a linha da sua folha que atende ao critério do espelho.</p>' + BOX_ST),
    story('<div class="selo">RECURSO TCE-PE</div><div class="big-n" style="font-size:200px">Último dia</div>'
          '<p class="big" style="margin:30px 0 60px">O recurso da discursiva do TCE-PE termina <b>hoje</b>.</p>' + BOX_ST + AUTOR_ST),
 ]),
}

for k, c in CAMP.items():
    html = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            + ''.join(c['slides']) + ''.join([c['stories'][0].replace('class="st claro"','class="st navy"',1)] + c['stories'][1:]) + '</body></html>')
    pathlib.Path(f'carrossel_{k}.html').write_text(html, encoding='utf-8')
    print(k, len(c['slides']), 'slides', len(c['stories']), 'stories')
