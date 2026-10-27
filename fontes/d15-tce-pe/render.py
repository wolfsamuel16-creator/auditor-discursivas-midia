import sys, pathlib, base64, re
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]); foto = pathlib.Path(sys.argv[3]); fonts = pathlib.Path(sys.argv[4])
out.mkdir(parents=True, exist_ok=True)
html = src.read_text(encoding='utf-8')
html = re.sub(r'<link href="https://fonts.googleapis.com[^>]*>', '', html)
ff = ''.join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('{(fonts/fn).as_uri()}')}}" for fam,w,fn in [
 ('Poppins',600,'Poppins-SemiBold.ttf'),('Poppins',700,'Poppins-Bold.ttf'),('Poppins',800,'Poppins-ExtraBold.ttf'),
 ('Lato',400,'Lato-Regular.ttf'),('Lato',700,'Lato-Bold.ttf'),('Lato',900,'Lato-Black.ttf')])
html = html.replace('<style>', '<style>'+ff, 1)
b64 = base64.b64encode(foto.read_bytes()).decode()
assert '<div class="foto">SW</div>' in html
html = html.replace('<div class="foto">SW</div>', f'<div class="foto" style="background-image:url(data:image/jpeg;base64,{b64})"></div>')
tmp = src.with_name('_render.html'); tmp.write_text(html, encoding='utf-8')
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1200, "height": 1500}, device_scale_factor=2)
    pg.goto(tmp.as_uri()); pg.wait_for_timeout(1200)
    print('fonts', pg.evaluate("document.fonts.check(\"800 40px Poppins\") && document.fonts.check(\"400 30px Lato\")"))
    for i, el in enumerate(pg.query_selector_all("div.slide"), 1):
        el.screenshot(path=str(out / f"slide_{i:02d}_2x.png"))
    print(pg.evaluate("""[...document.querySelectorAll('.slide')].map((s,i)=>{const c=s.querySelector('.corpo');const r=s.querySelector('.rod').getBoundingClientRect();const cb=c.getBoundingClientRect();return (i+1)+':'+(cb.bottom>r.top?'SOBREPOE '+Math.round(cb.bottom-r.top):'ok')})"""))
    b.close()
from PIL import Image
for f in sorted(out.glob('slide_*_2x.png')):
    Image.open(f).resize((1080,1350), Image.LANCZOS).save(out/f.name.replace('_2x',''), optimize=True); f.unlink()
