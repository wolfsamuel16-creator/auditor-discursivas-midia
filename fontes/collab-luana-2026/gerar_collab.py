"""Artes dos posts em collab com @luvicentecoach (Central, 09/11/2026). Uso: python3 gerar_collab.py"""
import html, json, pathlib, subprocess
AQUI = pathlib.Path(__file__).parent
PECAS = json.loads((AQUI / 'collab.json').read_text(encoding='utf-8'))

CSS = """
@font-face{font-family:P;src:url(fonts/Poppins-SemiBold.ttf);font-weight:600}
@font-face{font-family:P;src:url(fonts/Poppins-Bold.ttf);font-weight:700}
@font-face{font-family:P;src:url(fonts/Poppins-ExtraBold.ttf);font-weight:800}
@font-face{font-family:L;src:url(fonts/Lato-Regular.ttf);font-weight:400}
@font-face{font-family:L;src:url(fonts/Lato-Bold.ttf);font-weight:700}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#999;display:flex;flex-direction:column;gap:40px;padding:40px}
:root{--navy:#2A3544;--lar:#F04E23;--creme:#F6F2EC;--txt:#2B3644;--cinza:#8A929B}
.s{position:relative;overflow:hidden;background:var(--creme);color:var(--navy);font-family:L;display:flex;flex-direction:column;flex-shrink:0}
.feed{width:1080px;height:1350px;padding:60px 76px 56px;gap:26px}
.story{width:1080px;height:1920px;padding:250px 80px 340px;gap:30px}
.topo{display:flex;justify-content:space-between;align-items:center;font-family:P}
.wm{color:var(--lar);font-weight:700;letter-spacing:3px;font-size:24px}
.selo{background:var(--lar);color:#fff;font-weight:800;letter-spacing:2px;border-radius:10px;font-size:22px;padding:9px 18px}
.card{background:var(--navy);color:#fff;border-radius:26px;padding:34px 40px;display:flex;flex-direction:column;gap:8px}
.card .sig{font-family:P;font-weight:800;font-size:76px;line-height:1;letter-spacing:-1px}
.card .org{font-family:P;font-weight:700;font-size:30px;line-height:1.2}
.card .car{font-size:27px;opacity:.9;line-height:1.3}
.card .ban{font-size:24px;opacity:.7}
.faixa{align-self:flex-start;margin-top:10px;background:var(--lar);color:#fff;font-family:P;font-weight:700;font-size:25px;padding:8px 22px;border-radius:40px}
h1{font-family:P;font-weight:800;font-size:58px;line-height:1.08;letter-spacing:-.5px}
h1 em{font-style:normal;color:var(--lar)}
.sub{font-size:29px;line-height:1.4;color:var(--txt)}
.grat{background:#fff;border:4px solid var(--lar);border-radius:22px;padding:26px 32px;position:relative}
.grat .tag{position:absolute;top:-20px;left:28px;background:var(--lar);color:#fff;font-family:P;font-weight:800;font-size:20px;letter-spacing:2px;padding:6px 16px;border-radius:10px}
.grat b{font-family:P;font-weight:800;font-size:34px;display:block}
.grat span{font-size:26px;line-height:1.35;color:var(--txt)}
.autor{display:flex;gap:26px;align-items:center;margin-top:auto}
.autor img{width:130px;height:130px;border-radius:50%;border:7px solid var(--lar);object-fit:cover;flex-shrink:0}
.autor b{font-family:P;font-weight:800;font-size:34px;display:block}
.autor .cr{font-size:23px;line-height:1.4;color:var(--txt)}
.parc{display:flex;align-items:center;gap:14px;font-family:P;font-weight:700;font-size:26px;color:var(--navy)}
.parc .x{color:var(--lar)}
.cta{background:var(--navy);color:#fff;text-align:center;font-family:P;font-weight:700;font-size:32px;border-radius:22px;padding:22px}
.cta b{color:var(--lar);font-weight:800}
.story .card .sig{font-size:90px} .story h1{font-size:66px} .story .sub{font-size:32px} .story .cta{font-size:36px;padding:26px}
"""

def bloco(c, cls):
    e = {k: html.escape(str(v)) for k, v in c.items()}
    if c['momento'] == 'prova':
        faixa = f'PROVA DISCURSIVA · {e["data"]}'
        h1 = f'Fez a discursiva da <em>{e["sigla"]}</em> hoje?'
        sub = 'Guarde o rascunho e anote o que escreveu em cada item. Quando a nota sair, é com isso que se avalia se cabe recurso.'
    else:
        faixa = f'NOTA DA DISCURSIVA · {e["data"]}'
        h1 = f'A nota da discursiva da <em>{e["sigla"]}</em> sai amanhã.'
        sub = 'O prazo de recurso é curto. Separe prova, espelho e padrão de resposta e não perca os pontos que a banca deixou de considerar.'
    return f'''<section class="s {cls}">
<div class="topo"><span class="wm">AUDITOR DISCURSIVAS</span><span class="selo">RECURSO DE DISCURSIVA</span></div>
<div class="card"><span class="sig">{e["sigla"]}</span><span class="org">{e["orgao"]}</span><span class="car">{e["cargos"]}</span><span class="ban">Banca: {e["banca"]}</span><span class="faixa">{faixa}</span></div>
<h1>{h1}</h1>
<p class="sub">{sub}</p>
<div class="grat"><span class="tag">GRATUITA</span><b>Análise de viabilidade</b><span>Você me envia a prova e o espelho; eu digo se há pontos a recuperar. Os valores eu passo no direct.</span></div>
<div class="autor"><img src="foto-samuel.jpg"><div><b>Samuel Wolf</b><div class="cr">Engenheiro pelo ITA · Auditor de Controle Externo do TCE-RJ<br>Nomeado Auditor Fiscal da SEFAZ-RS e da SEFIN Manaus</div></div></div>
<div class="parc">Em parceria com <span class="x">@luvicentecoach</span></div>
<div class="cta">Mande <b>RECURSO</b> no direct de <b>@auditor_discursivas</b></div>
</section>'''

for p in PECAS:
    out = AQUI / 'out-collab' / p['pasta']; out.mkdir(parents=True, exist_ok=True)
    corpo = ''.join(bloco(c, 'feed') for c in p['concursos']) + ''.join(bloco(c, 'story') for c in p['concursos'])
    (out / 'collab.html').write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{corpo}</body></html>', encoding='utf-8')
    for f in ('fonts', 'foto-samuel.jpg'):
        d = out / f
        if not d.exists(): d.symlink_to(AQUI / f)
    subprocess.run(['python3', str(AQUI / 'render.py'), str(out / 'collab.html'), str(out), 'section.feed', 'slide'], check=True)
    subprocess.run(['python3', str(AQUI / 'render.py'), str(out / 'collab.html'), str(out), 'section.story', 'story'], check=True)
