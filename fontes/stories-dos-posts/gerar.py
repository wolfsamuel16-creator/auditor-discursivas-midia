import pathlib, sys
from playwright.sync_api import sync_playwright
F='/home/claude/fonts'
CSS=f"""
@font-face{{font-family:P;src:url(file://{F}/Poppins-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:P;src:url(file://{F}/Poppins-Bold.ttf);font-weight:700}}
@font-face{{font-family:L;src:url(file://{F}/Lato-Regular.ttf);font-weight:400}}
@font-face{{font-family:L;src:url(file://{F}/Lato-Bold.ttf);font-weight:700}}
body{{margin:0}}
section{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:P;color:#fff;background:#2A3544}}
.glow{{position:absolute;left:140px;right:140px;top:300px;height:760px;background:radial-gradient(closest-side,rgba(240,78,35,.35),rgba(240,78,35,0));}}
.wm{{position:absolute;top:150px;left:80px;font-weight:800;font-size:30px;letter-spacing:4px;color:#F04E23}}
.top{{position:absolute;top:255px;left:0;right:0;text-align:center}}
.pill{{display:inline-block;background:#F04E23;font-weight:700;font-size:36px;letter-spacing:5px;padding:12px 34px;border-radius:50px}}
.wrap{{position:absolute;left:80px;right:80px;top:340px;bottom:340px;display:flex;flex-direction:column;align-items:center;gap:30px}}
.card{{flex:none;transform:rotate(-3deg);margin-top:10px;border-radius:18px;border:6px solid #F04E23;box-shadow:0 22px 50px rgba(0,0,0,.5);object-fit:cover;object-position:top}}
.box{{width:100%}}
.t{{font-weight:800;font-size:66px;line-height:1.06}}
.t span{{color:#F04E23}}
.li{{font-family:L;font-weight:700;font-size:36px;line-height:1.45;margin-top:20px;color:#E6EAF0}}
.li b{{color:#F04E23}}
.cta{{width:100%;box-sizing:border-box;margin-top:auto;background:#F6F2EC;color:#2A3544;border-radius:30px;padding:20px 36px;text-align:center}}
.cta .a{{font-weight:700;font-size:34px}}
.cta .k{{font-weight:800;font-size:76px;color:#F04E23;line-height:1.05}}
.cta .s{{font-family:L;font-size:28px;color:#4A5568}}
.ft{{position:absolute;bottom:200px;left:0;right:0;text-align:center;font-family:L;font-weight:700;font-size:30px;color:#AEB7C4}}
"""
S=[
 dict(img='c1.png',w=330,h=560,pill='REEL NOVO NO PERFIL',
  t='573 notas do TCE-SC: <span>antes e depois</span> do recurso',
  li='<b>›</b> Meus alunos: +1,41 ponto em média<br><b>›</b> Demais candidatos: +1,08<br><b>›</b> Dados oficiais da FGV',
  a='TCE-PE: nota sai em 12/11. Mande',k='TCEPE',s='no direct · análise de viabilidade gratuita'),
 dict(img='c2.png',w=480,h=480,pill='POST NOVO NO PERFIL',
  t='Sabia a resposta e a nota veio parcial? Olhe <span>o esqueleto</span>',
  li='<b>›</b> Um parágrafo por item do comando<br><b>›</b> Tópico frasal · fundamento · conclusão<br><b>›</b> Exemplo com o art. 212 da CF/88',
  a='Toque no meu perfil e',k='SALVE',s='para revisar antes do próximo simulado'),
 dict(img='c3.png',w=420,h=525,pill='POST NOVO NO PERFIL',
  t='TCE-GO 2024: a armadilha do <span>“explique como”</span>',
  li='<b>›</b> Questão inteira de 10 pontos (FGV)<br><b>›</b> As 4 ideias do espelho oficial<br><b>›</b> O parágrafo que pontua, frase a frase',
  a='Toque no meu perfil e',k='SALVE',s='para treinar as questões de “explique”'),
 dict(img='c4.png',w=420,h=525,pill='POST NOVO NO PERFIL',
  t='Saiu a nota da discursiva do <span>TCE-PE</span>',
  li='<b>›</b> Recurso de 13 a 16/11: só 4 dias<br><b>›</b> Análise de viabilidade gratuita<br><b>›</b> Recurso redigido item por item',
  a='Não concordou? Mande',k='TCEPE',s='no direct · vagas limitadas'),
]
h='<html><head><style>'+CSS+'</style></head><body>'
for s in S:
    h+=f"""<section class=st><div class=glow></div><div class=wm>AUDITOR DISCURSIVAS</div>
<div class=top><span class=pill>{s['pill']}</span></div>
<div class=wrap><img class=card src="{s['img']}" style="width:{s['w']}px;height:{s['h']}px">
<div class=box><div class=t>{s['t']}</div><div class=li>{s['li']}</div></div>
<div class=cta><div class=a>{s['a']}</div><div class=k>{s['k']}</div><div class=s>{s['s']}</div></div></div>
<div class=ft>@auditor_discursivas</div></section>"""
h+='</body></html>'
pathlib.Path('stories.html').write_text(h)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto(pathlib.Path('stories.html').resolve().as_uri()); pg.wait_for_timeout(800)
    for i,el in enumerate(pg.query_selector_all('section'),1): el.screenshot(path=f'story_{i:02d}.png')
    print(pg.evaluate("""[...document.querySelectorAll('section')].map(s=>{const w=s.querySelector('.wrap');const b=s.querySelector('.box').getBoundingClientRect(),c=s.querySelector('.cta').getBoundingClientRect(),t=s.getBoundingClientRect();return [Math.round(b.bottom-t.top),Math.round(c.top-t.top),Math.round(c.bottom-t.top),w.scrollHeight>w.clientHeight?'TRANSBORDO':'ok']})"""))
    b.close()
