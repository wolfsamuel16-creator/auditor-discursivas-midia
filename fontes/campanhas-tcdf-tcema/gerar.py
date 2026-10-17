"""Gera os HTML dos carrosséis (1080x1350) e stories (1080x1920) das campanhas TCDF e TCE-MA."""
import pathlib, json

OUT = pathlib.Path('/home/claude/carrossel/out'); OUT.mkdir(exist_ok=True)

CSS = """
:root{--navy:#2A3544;--laranja:#F04E23;--texto:#2B3644;--verde:#00897B;--cinza:#8A929B;--cinza-claro:#B8C2CC;
--filete:#CFD6DD;--cx-verde:#D9F0EC;--cx-azul:#F4FAFB;--cx-laranja:#FFE7D6;--cx-navy:#E6EAF0}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#E8EBEE;font-family:'Lato',sans-serif;padding:40px;display:flex;flex-direction:column;align-items:center;gap:40px}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#fff;flex-shrink:0}
.story{width:1080px;height:1920px;position:relative;overflow:hidden;flex-shrink:0;background:var(--navy)}
.pad{padding:84px}
.dark{background:var(--navy);display:flex;flex-direction:column;justify-content:space-between}
.marca{font-family:'Poppins';font-weight:600;font-size:22px;letter-spacing:3px;text-transform:uppercase;color:var(--laranja)}
.contador{font-family:'Poppins';font-weight:600;font-size:22px;letter-spacing:2px;color:var(--cinza)}
.rule{width:120px;height:8px;background:var(--laranja)}
.eyebrow{font-family:'Poppins';font-weight:600;font-size:24px;letter-spacing:4px;text-transform:uppercase;color:var(--cinza-claro)}
.h1{font-family:'Poppins';font-weight:800;font-size:96px;line-height:1.04;color:#fff;letter-spacing:-2px}
.h1 em{font-style:normal;color:var(--laranja)}
.sub{font-size:34px;line-height:1.45;color:var(--cinza-claro);max-width:880px}
.sub b{color:#fff}
.selo{display:flex;gap:14px;flex-wrap:wrap}
.selo span{font-family:'Poppins';font-weight:600;font-size:22px;letter-spacing:1.5px;text-transform:uppercase;color:#fff;border:2px solid var(--cinza);border-radius:40px;padding:10px 22px}
.selo span.on{background:var(--laranja);border-color:var(--laranja)}
.rodape{display:flex;justify-content:space-between;align-items:flex-end;font-size:24px;letter-spacing:1.5px;color:var(--cinza)}
.rodape .seta{color:var(--laranja);font-family:'Poppins';font-weight:600}
.cta{background:var(--laranja);border-radius:16px;padding:34px 40px}
.cta .a{font-family:'Poppins';font-weight:700;font-size:40px;color:#fff;line-height:1.25}
.cta .a b{background:#fff;color:var(--laranja);padding:0 14px;border-radius:8px}
.cta .b{font-size:28px;color:#FFE7D6;margin-top:12px;line-height:1.4}
.faixa-navy{background:var(--navy);padding:24px 84px;font-family:'Poppins';font-weight:600;font-size:22px;letter-spacing:3px;text-transform:uppercase;color:#fff;display:flex;justify-content:space-between}
.faixa-navy .n{color:var(--cinza-claro)}
.faixa-laranja{background:var(--laranja);padding:28px 84px;font-family:'Poppins';font-weight:700;font-size:46px;line-height:1.15;color:#fff;letter-spacing:-.5px}
.corpo{padding:60px 84px 0}
.txt{font-size:38px;line-height:1.45;color:var(--texto)}
.txt b{color:var(--navy)}
.nums{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-bottom:34px}
.num{background:var(--cx-navy);border-radius:14px;padding:30px 34px}
.num .v{font-family:'Poppins';font-weight:800;font-size:66px;line-height:1;color:var(--navy)}
.num .v small{font-size:34px;font-weight:700}
.num .l{font-size:28px;line-height:1.35;color:var(--texto);margin-top:10px}
.num.dest{background:var(--cx-laranja)} .num.dest .v{color:var(--laranja)}
.dica{margin-top:30px;padding-top:36px;border-top:2px solid var(--filete);display:flex;gap:22px;align-items:flex-start}
.dica-rot{font-family:'Poppins';font-weight:700;font-size:21px;letter-spacing:2px;color:var(--laranja);text-transform:uppercase;padding-top:6px;white-space:nowrap}
.dica-txt{font-size:35px;line-height:1.42;color:var(--texto)}
.dica-txt b{color:var(--navy)}
.lista div{display:flex;gap:24px;align-items:flex-start;padding:30px 0;border-bottom:1px solid var(--filete)}
.lista div:last-child{border-bottom:none}
.lista .ok{font-family:'Poppins';font-weight:800;color:var(--verde);font-size:34px;min-width:40px}
.lista .q{font-size:35px;line-height:1.38;color:var(--texto)}
.lista .q b{color:var(--navy)}
.lista .q small{display:block;font-size:27px;color:var(--cinza);margin-top:4px}
.rod{display:flex;gap:26px;align-items:flex-start;padding:28px 0;border-bottom:1px solid var(--filete)}
.rod:last-child{border-bottom:none}
.rod .k{font-family:'Poppins';font-weight:800;font-size:28px;color:#fff;background:var(--laranja);min-width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.rod .k.p{background:var(--navy)}
.rod .t{font-size:34px;line-height:1.3;color:var(--texto)}
.rod .t b{color:var(--navy)}
.rod .t small{display:block;font-family:'Poppins';font-weight:600;font-size:20px;letter-spacing:2px;text-transform:uppercase;color:var(--cinza);margin-bottom:4px}
.folha{background:#FFFDF8;border:2px solid var(--filete);border-radius:14px;padding:40px 44px;font-size:33px;line-height:1.62;color:var(--texto)}
.folha .r{text-align:right} .folha .c{text-align:center} .folha .i{padding-left:56px}
.folha .hl{background:var(--cx-laranja);box-shadow:inset 0 -4px 0 var(--laranja);padding:1px 0}
.folha .g{color:var(--cinza)}
.bloco{display:flex;gap:24px;align-items:stretch;margin-bottom:20px}
.bloco .lado{min-width:12px;border-radius:6px;background:var(--laranja)}
.bloco .c{flex:1;background:var(--cx-azul);border:2px solid var(--filete);border-radius:14px;padding:22px 30px}
.bloco .c .h{font-family:'Poppins';font-weight:700;font-size:30px;color:var(--navy)}
.bloco .c .h span{color:var(--laranja)}
.bloco .c .d{font-size:29px;line-height:1.38;color:var(--texto);margin-top:4px}
.rod-claro{position:absolute;bottom:0;left:0;right:0;padding:30px 84px;display:flex;justify-content:space-between;font-size:22px;letter-spacing:1.5px;color:var(--cinza)}
.rod-claro .seta{color:var(--laranja);font-family:'Poppins';font-weight:700}
.foto{width:132px;height:132px;border-radius:50%;border:5px solid var(--laranja);background:#1c2735 center/cover no-repeat;display:flex;align-items:center;justify-content:center;font-family:'Poppins';font-weight:800;font-size:44px;color:var(--laranja)}
/* stories: 250px livres no topo, 340px na base */
.st-in{position:absolute;top:250px;bottom:340px;left:84px;right:84px;display:flex;flex-direction:column;justify-content:center;gap:44px}
.st-h{font-family:'Poppins';font-weight:800;font-size:92px;line-height:1.05;color:#fff;letter-spacing:-2px}
.st-h em{font-style:normal;color:var(--laranja)}
.st-p{font-size:48px;line-height:1.45;color:var(--cinza-claro)}
.st-p b{color:#fff}
.st-box{background:#fff;border-radius:22px;padding:44px 48px}
.st-box .q{font-family:'Poppins';font-weight:700;font-size:46px;color:var(--navy);line-height:1.2}
.st-box .r{font-size:38px;color:var(--texto);margin-top:16px;line-height:1.4}
.kw{display:inline-block;background:var(--laranja);color:#fff;font-family:'Poppins';font-weight:800;font-size:110px;letter-spacing:4px;border-radius:20px;padding:6px 44px}
.tag{display:inline-flex;align-items:center;gap:18px;background:var(--laranja);color:#fff;font-family:'Poppins';font-weight:800;font-size:54px;letter-spacing:3px;text-transform:uppercase;border-radius:16px;padding:14px 34px 10px;line-height:1.1}
.tag small{font-family:'Lato';font-weight:700;font-size:26px;letter-spacing:1px;text-transform:none;color:#FFE7D6;border-left:3px solid #FFB89C;padding-left:18px}
.st-marca{position:absolute;top:140px;left:84px;right:84px;display:flex;justify-content:space-between}
"""

def head(title):
    return f'<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<title>{title}</title>\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Lato:wght@400;700;900&display=swap" rel="stylesheet">\n<style>{CSS}</style>\n</head>\n<body>\n'

def capa(n, tot, eyebrow, titulo, sub, selos, kw):
    s = ''.join(f'<span class="{"on" if i==0 else ""}">{x}</span>' for i, x in enumerate(selos))
    return f'''<div class="slide dark pad" data-n="{n:02d}">
  <div style="display:flex;justify-content:space-between"><div class="marca">Auditor Discursivas</div><div class="contador">{n:02d} / {tot:02d}</div></div>
  <div>
    <div class="tag" style="margin-bottom:46px">Aula gratuita<small>{eyebrow}</small></div>
    <div class="h1">{titulo}</div>
    <div class="sub" style="margin-top:36px">{sub}</div>
    <div class="selo" style="margin-top:40px">{s}</div>
    <div class="cta" style="margin-top:54px"><div class="a">Comente <b>{kw}</b> que eu te mando a aula grátis no direct.</div></div>
  </div>
  <div class="rodape"><div>@auditor_discursivas</div><div class="seta">Arraste →</div></div>
</div>
'''

def conteudo(n, tot, faixa, titulo, corpo, rodape='@auditor_discursivas'):
    return f'''<div class="slide" data-n="{n:02d}">
  <div class="faixa-navy"><span>{faixa}</span><span class="n">{n:02d} / {tot:02d}</span></div>
  <div class="faixa-laranja">{titulo}</div>
  <div class="corpo">{corpo}</div>
  <div class="rod-claro"><div>{rodape}</div><div class="seta">→</div></div>
</div>
'''

def fecho(n, tot, frase, kw, linha_recurso):
    return f'''<div class="slide dark pad" data-n="{n:02d}">
  <div style="display:flex;justify-content:space-between"><div class="marca">Auditor Discursivas</div><div class="contador">{n:02d} / {tot:02d}</div></div>
  <div>
    <div class="tag" style="margin-bottom:44px">Aula gratuita<small>em PDF, no seu direct</small></div>
    <div class="h1" style="font-size:76px">{frase}</div>
    <div class="cta" style="margin-top:54px">
      <div class="a">Comente <b>{kw}</b> aqui embaixo e a aula gratuita chega no seu direct.</div>
      <div class="b">{linha_recurso}</div>
    </div>
    <div style="display:flex;align-items:center;gap:28px;margin-top:54px">
      <div class="foto">SW</div>
      <div><div style="font-family:'Poppins';font-weight:700;font-size:38px;color:#fff">Samuel Wolf</div>
      <div style="font-size:28px;color:var(--cinza-claro);margin-top:6px">Recursos de provas discursivas</div>
      <div style="font-size:23px;color:var(--cinza);margin-top:8px;line-height:1.4">Engenheiro pelo ITA · Auditor de Controle Externo do TCE-RJ ·<br>Nomeado Auditor Fiscal da SEFAZ-RS e da SEFIN Manaus</div></div>
    </div>
  </div>
  <div class="rodape"><div>@auditor_discursivas</div><div class="seta">↑ Salvar</div></div>
</div>
'''

def story(n, corpo):
    return f'''<div class="story" data-n="st{n:02d}">
  <div class="st-marca"><div class="marca">Auditor Discursivas</div><div class="contador">@auditor_discursivas</div></div>
  <div class="st-in">{corpo}</div>
</div>
'''

# =================== TCDF ===================
T = 7
tcdf = head('Campanha TCDF 2026 — carrossel') + capa(1, T,
    'PDF · Cebraspe',
    'Discursiva do <em>TCDF 2026</em>',
    'Analista Administrativo de Controle Externo. A questão de 20 linhas e a <b>Informação de 50 linhas</b>, no padrão do Manual do TCDF.',
    ['Prova 22/11', '40 páginas', '5 rodadas com espelho'], 'TCDF')

tcdf += conteudo(2, T, 'A prova da tarde', 'Dois textos, 50 pontos, uma linha de corte', '''
<div class="nums">
  <div class="num"><div class="v">20 <small>linhas</small></div><div class="l">Questão dissertativa · <b>15 pontos</b></div></div>
  <div class="num"><div class="v">50 <small>linhas</small></div><div class="l">Peça técnica: a <b>Informação</b> · <b>35 pontos</b></div></div>
  <div class="num"><div class="v">4 h</div><div class="l">Para os dois textos, à mão, no turno da tarde</div></div>
  <div class="num dest"><div class="v">30 <small>/ 50</small></div><div class="l">Abaixo disso, <b>eliminado</b></div></div>
</div>
<div class="txt">Os dois textos saem dos <b>conhecimentos especializados</b>: Gestão de Contratos, Direito Administrativo, AFO, Regime Jurídico dos Servidores do DF e Administração Pública.</div>
<div class="dica"><div class="dica-rot">Fonte</div><div class="dica-txt">Edital n.º 1 – TCDF/ANACE, de 2026.</div></div>
''')

tcdf += conteudo(3, T, 'O que pouca gente aproveita', 'A forma da Informação vale ponto', '''
<div class="txt" style="margin-bottom:30px">Só a peça segue o <b>Manual de Redação Oficial do TCDF</b>. E a moldura é fixa: dá para decorar.</div>
<div class="nums">
  <div class="num dest"><div class="v">0 a 6</div><div class="l">Quesito só para os <b>dados do processo</b> no espelho de 2023</div></div>
  <div class="num dest"><div class="v">0 a 3</div><div class="l">Quesito só para o <b>desfecho</b>: sugestões, fecho e signatário</div></div>
</div>
<div class="dica"><div class="dica-rot">Atenção</div><div class="dica-txt">O signatário é <b>“NOME”</b> e <b>“CARGO”</b>, escritos assim. Seu nome no texto definitivo é marca de identificação e <b>anula a prova</b>.</div></div>
<div class="dica" style="margin-top:20px;border-top:none;padding-top:0"><div class="dica-rot">Fonte</div><div class="dica-txt">Padrão de resposta definitivo do Cebraspe, TCDF 2023, Analista. Mesmo cargo, mesma peça.</div></div>
''')

tcdf += conteudo(4, T, 'Prévia da aula gratuita', 'A moldura da Informação, na ordem', '''
<div class="folha">
  <div><span class="hl">Informação n.º ......./..... – (sigla)</span></div>
  <div class="r"><span class="hl">Brasília, 22 de novembro de 2026.</span></div>
  <div><span class="hl">Processo n.º</span> · <span class="hl">Jurisdicionado</span> · <span class="hl">Assunto</span> · <span class="hl">Ementa</span></div>
  <div class="i">Senhor Diretor,</div>
  <div class="c">Relatório (dispensado)</div>
  <div class="i">Em relação ao fato 1, ... <span class="g">(sem número)</span></div>
  <div class="i">2. No que diz respeito a ...</div>
  <div class="i">3. Diante do exposto, ... sugestões:</div>
  <div class="i">I – ...; II – ...; e III – ....</div>
  <div class="i">À consideração superior,</div>
  <div class="c">NOME<br>CARGO</div>
</div>
<div class="txt" style="font-size:30px;margin-top:22px;color:var(--cinza)">Na aula, cada elemento vem explicado, com o que vale ponto no espelho.</div>
''')

tcdf += conteudo(5, T, 'Na aula gratuita · 40 páginas', 'Do edital ao checklist do dia', '''
<div class="lista">
  <div><span class="ok">✓</span><span class="q"><b>Raio-X do edital</b> e de como o Cebraspe corrige<small>Fórmula, descontos de língua e o que zera ou anula</small></span></div>
  <div><span class="ok">✓</span><span class="q">O que a banca <b>já cobrou no TCDF</b><small>Provas e padrões de 2021, 2023 e 2024</small></span></div>
  <div><span class="ok">✓</span><span class="q"><b>Roteiro de planejamento</b> em cinco passos<small>E o parágrafo de desenvolvimento que pontua</small></span></div>
  <div><span class="ok">✓</span><span class="q">O <b>formato exato da Informação</b>, pelo padrão da banca</span></div>
  <div><span class="ok">✓</span><span class="q"><b>5 rodadas</b> com espelho e resposta completa<small>3 questões de 20 linhas + 2 Informações de 50</small></span></div>
  <div><span class="ok">✓</span><span class="q">Gestão das <b>quatro horas</b> e checklist do dia</span></div>
</div>
''')

tcdf += conteudo(6, T, 'As cinco rodadas', 'Temas inéditos, escolhidos a dedo', '''
<div class="rod"><span class="k">1</span><span class="t"><small>Questão · AFO</small><b>As restrições da LRF no fim do mandato</b></span></div>
<div class="rod"><span class="k">2</span><span class="t"><small>Questão · LC distrital n.º 840/2011</small><b>Acumulação de cargos públicos</b></span></div>
<div class="rod"><span class="k">3</span><span class="t"><small>Questão · Gestão de Contratos</small><b>Reajuste, repactuação e revisão</b></span></div>
<div class="rod"><span class="k p">4</span><span class="t"><small>Informação · Licitações</small><b>Representação contra edital de pregão eletrônico</b></span></div>
<div class="rod"><span class="k p">5</span><span class="t"><small>Informação · AFO</small><b>Créditos adicionais na execução orçamentária</b></span></div>
<div class="dica"><div class="dica-rot">Por quê</div><div class="dica-txt">2026 é o último ano do mandato no DF, e a Lei n.º 14.133/2021 é hoje a maior fonte de casos de contratação.</div></div>
''')

tcdf += fecho(7, T, 'Moldura decorada.<br>Um parágrafo por item.<br><em>Nota acima de 30.</em>', 'TCDF',
    'Depois da prova, se a nota não vier, me manda <b style="color:#fff">RECURSO</b> no direct. A análise de viabilidade é gratuita.')
tcdf += '</body>\n</html>\n'
(OUT / 'carrossel_tcdf.html').write_text(tcdf, encoding='utf-8')

st_tcdf = head('Campanha TCDF 2026 — stories')
st_tcdf += story(1, '''<div><span class="tag">Aula gratuita<small>TCDF 2026</small></span></div>
<div class="st-h">Vai fazer a discursiva do <em>TCDF</em>?</div>
<div class="st-p">Preparei uma aula <b>grátis</b>, em PDF, de <b>40 páginas</b> para o Analista: a questão de 20 linhas, a <b>Informação de 50</b> e <b>5 rodadas</b> com espelho e resposta completa.</div>''')
st_tcdf += story(2, '''<div class="st-h">É só mandar no <em>direct</em></div>
<div><span class="kw">TCDF</span></div>
<div class="st-p">Manda <b>TCDF</b> numa mensagem para o <b>@auditor_discursivas</b> e a <b>aula gratuita</b> chega na hora.</div>
<div class="st-box"><div class="q">Prefere comentar?</div><div class="r">Comente <b>TCDF</b> no post da aula do TCDF que eu também te mando.</div></div>''')
st_tcdf += story(3, '''<div class="eyebrow">Você sabia?</div>
<div class="st-h">A forma da Informação <em>vale ponto</em>.</div>
<div class="st-p">No espelho do TCDF 2023, os dados do processo tiveram um quesito de <b>0 a 6</b> só para eles. A moldura é fixa: dá para decorar.</div>
<div class="st-box"><div class="q">Mande TCDF no direct</div><div class="r">e receba grátis a aula com a moldura completa, elemento por elemento.</div></div>''')
st_tcdf += '</body>\n</html>\n'
(OUT / 'stories_tcdf.html').write_text(st_tcdf, encoding='utf-8')

# =================== TCE-MA ===================
T = 7
ma = head('Campanha TCE-MA 2026 — carrossel') + capa(1, T,
    'PDF · Cebraspe',
    'Discursiva do <em style="white-space:nowrap">TCE&#8209;MA 2026</em>',
    'Auditor Estadual de Controle Externo. A <b>peça técnica de 60 linhas</b> e as duas situações-problema de 30 linhas.',
    ['Prova 29/11', '46 páginas', '6 rodadas com espelho'], 'TCEMA')

ma += conteudo(2, T, 'A prova da tarde', 'Três textos, 40 pontos, quatro horas', '''
<div class="nums">
  <div class="num"><div class="v">60 <small>linhas</small></div><div class="l">Peça de natureza técnica · <b>20 pontos</b></div></div>
  <div class="num"><div class="v">2 × 30</div><div class="l">Situações-problema · <b>10 pontos</b> cada</div></div>
  <div class="num"><div class="v">4 h</div><div class="l">Para os três textos, depois de <b>5 h</b> de objetiva</div></div>
  <div class="num dest"><div class="v">20 <small>/ 40</small></div><div class="l">Abaixo disso, <b>eliminado</b></div></div>
</div>
<div class="txt">Cada ponto da discursiva vale o mesmo que um da objetiva. A peça sozinha equivale a <b>dez questões de conhecimentos específicos</b>.</div>
<div class="dica"><div class="dica-rot">Fonte</div><div class="dica-txt">Edital n.º 1 – TCE/MA, de 6/7/2026 (subitens 9.2 e 11.1).</div></div>
''')

ma += conteudo(3, T, 'Primeira discursiva do Cebraspe no TCE-MA', 'Sem prova anterior. E agora?', '''
<div class="txt" style="margin-bottom:28px">A aula cruza <b>12 provas de controle</b> do Cebraspe com as atribuições do cargo no edital. O formato mais parecido é o do <b>TCE-PR 2024</b>: Auditor, peça de 60 linhas.</div>
<div class="lista">
  <div><span class="ok">1</span><span class="q"><b>Contas</b><small>De governo e de gestão, parecer prévio</small></span></div>
  <div><span class="ok">2</span><span class="q"><b>Achados</b><small>Condição, critério, causa, efeito e matriz de responsabilização</small></span></div>
  <div><span class="ok">3</span><span class="q"><b>Encaminhamentos</b><small>Cada medida com destinatário e fundamento</small></span></div>
</div>
<div class="dica" style="margin-top:12px"><div class="dica-rot">O recado</div><div class="dica-txt">É daí que tende a sair a peça.</div></div>
''')

ma += conteudo(4, T, 'O que está quente no Maranhão', 'Seis temas no radar do TCE-MA', '''
<div class="rod"><span class="k">1</span><span class="t"><b>Emendas Pix nos municípios</b><small style="margin:4px 0 0">Força-tarefa do TCE-MA em 2026 · ADPF 854</small></span></div>
<div class="rod"><span class="k">2</span><span class="t"><b>Contas do prefeito ordenador de despesas</b><small style="margin:4px 0 0">ADPF 982 (2025)</small></span></div>
<div class="rod"><span class="k">3</span><span class="t"><b>Registro de aposentadoria</b><small style="margin:4px 0 0">Prazo de 5 anos do Tema 445</small></span></div>
<div class="rod"><span class="k">4</span><span class="t"><b>Transporte escolar: achado e responsabilização</b><small style="margin:4px 0 0">Matriz de achados e de responsabilização</small></span></div>
<div class="rod"><span class="k p">5</span><span class="t"><b>Parecer sobre contratação emergencial</b><small style="margin:4px 0 0">Peça · Lei n.º 14.133/2021</small></span></div>
<div class="rod"><span class="k p">6</span><span class="t"><b>Contas de governo com parecer prévio</b><small style="margin:4px 0 0">Peça · LRF e mínimos constitucionais</small></span></div>
<div class="txt" style="font-size:28px;color:var(--cinza);margin-top:16px">Cada um vira uma rodada completa na aula.</div>
''')

ma += conteudo(5, T, 'Prévia da aula gratuita', 'A peça de 60 linhas em quatro blocos', '''
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">1 · Introdução <span>“Trata-se de...”</span></div><div class="d">Objeto, fatos centrais e o que cumpre examinar · 4 a 7 linhas</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">2 · Análise <span>“Quanto ao...”</span></div><div class="d">Um parágrafo por item, com veredito, norma, fato e consequência · cerca de 70%</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">3 · Conclusão <span>“Em conclusão,...”</span></div><div class="d">Retoma cada análise em meia linha. Nada novo · 3 a 5 linhas</div></div></div>
<div class="bloco"><div class="lado"></div><div class="c"><div class="h">4 · Encaminhamentos <span>I, II, III</span></div><div class="d">Cautelares primeiro, mérito depois. Todo item com destinatário · 8 a 14 linhas</div></div></div>
<div class="dica" style="margin-top:14px"><div class="dica-rot">Regra</div><div class="dica-txt">Nunca invente prazo: <b>“no prazo a ser fixado pelo Tribunal”</b>.</div></div>
''')

ma += conteudo(6, T, 'Na aula gratuita · 46 páginas', 'Do edital ao checklist do dia', '''
<div class="lista">
  <div><span class="ok">✓</span><span class="q"><b>Raio-X do edital</b> e de como o Cebraspe corrige<small>Fórmula, descontos de língua e quem tem a prova corrigida</small></span></div>
  <div><span class="ok">✓</span><span class="q">O que a banca <b>já cobrou em controle</b><small>12 provas, de TCU 2015 a TCE-MS 2025</small></span></div>
  <div><span class="ok">✓</span><span class="q"><b>Roteiro de planejamento</b> em cinco passos<small>E o parágrafo de desenvolvimento que pontua</small></span></div>
  <div><span class="ok">✓</span><span class="q"><b>6 rodadas</b> com espelho e resposta completa<small>4 situações-problema de 30 linhas + 2 peças de 60</small></span></div>
  <div><span class="ok">✓</span><span class="q">Gestão das <b>quatro horas</b> e checklist do dia</span></div>
</div>
''')

ma += fecho(7, T, 'Quatro blocos.<br>Um parágrafo por item.<br><em>Nota acima de 20.</em>', 'TCEMA',
    'Depois da prova, se a nota não vier, me manda <b style="color:#fff">RECURSO</b> no direct. A análise de viabilidade é gratuita.')
ma += '</body>\n</html>\n'
(OUT / 'carrossel_tcema.html').write_text(ma, encoding='utf-8')

st_ma = head('Campanha TCE-MA 2026 — stories')
st_ma += story(1, '''<div><span class="tag">Aula gratuita<small>TCE-MA 2026</small></span></div>
<div class="st-h">Vai fazer a discursiva do <em style="white-space:nowrap">TCE&#8209;MA</em>?</div>
<div class="st-p">Preparei uma aula <b>grátis</b>, em PDF, de <b>46 páginas</b> para o Auditor: a <b>peça de 60 linhas</b>, as duas situações-problema e <b>6 rodadas</b> com espelho e resposta completa.</div>''')
st_ma += story(2, '''<div class="st-h">É só mandar no <em>direct</em></div>
<div><span class="kw">TCEMA</span></div>
<div class="st-p">Manda <b>TCEMA</b> numa mensagem para o <b>@auditor_discursivas</b> e a <b>aula gratuita</b> chega na hora.</div>
<div class="st-box"><div class="q">Prefere comentar?</div><div class="r">Comente <b>TCEMA</b> no post da aula do TCE-MA que eu também te mando.</div></div>''')
st_ma += story(3, '''<div class="eyebrow">Você sabia?</div>
<div class="st-h">A peça vale <em>metade</em> da discursiva.</div>
<div class="st-p">São <b>20 dos 40 pontos</b>, o mesmo que dez questões de conhecimentos específicos. E ela tem esqueleto: quatro blocos que dá para treinar.</div>
<div class="st-box"><div class="q">Mande TCEMA no direct</div><div class="r">e receba grátis a aula com as 6 rodadas.</div></div>''')
st_ma += '</body>\n</html>\n'
(OUT / 'stories_tcema.html').write_text(st_ma, encoding='utf-8')
print('ok')
