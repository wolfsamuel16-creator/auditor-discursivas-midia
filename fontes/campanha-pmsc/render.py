"""Uso: python3 render.py <html> <pasta_saida> [foto.jpg]  — renderiza .slide (1080x1350) e .story (1080x1920)."""
import sys, re, base64, pathlib, asyncio
from playwright.async_api import async_playwright
FONTS = pathlib.Path('/home/claude/carrossel/fonts')
FF = ''.join(f"@font-face{{font-family:'{a}';font-weight:{w};src:url('file://{FONTS}/{f}')}}" for a, w, f in [
    ('Poppins',600,'Poppins-SemiBold.ttf'),('Poppins',700,'Poppins-Bold.ttf'),('Poppins',800,'Poppins-ExtraBold.ttf'),
    ('Lato',400,'Lato-Regular.ttf'),('Lato',700,'Lato-Bold.ttf'),('Lato',900,'Lato-Black.ttf')])
async def main(src, outdir, foto=None):
    out = pathlib.Path(outdir).resolve(); out.mkdir(parents=True, exist_ok=True)
    html = pathlib.Path(src).read_text(encoding='utf-8')
    html = re.sub(r'<link[^>]+fonts\.googleapis[^>]*>', '', html).replace('<style>', '<style>' + FF, 1)
    if foto:
        b64 = base64.b64encode(pathlib.Path(foto).read_bytes()).decode()
        html = html.replace('<div class="foto">SW</div>', f'<div class="foto" style="background-image:url(data:image/jpeg;base64,{b64})"></div>')
    tmp = out / '_render.html'; tmp.write_text(html, encoding='utf-8')
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 2100})
        await pg.goto('file://' + str(tmp)); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
        for el in await pg.query_selector_all('.slide, .story'):
            n = await el.get_attribute('data-n')
            name = (f'story_{n[2:]}.png' if n.startswith('st') else f'slide_{n}.png')
            await el.screenshot(path=str(out / name))
        bad = await pg.evaluate("""[...document.querySelectorAll('.slide, .story')].map(s=>{const r=s.getBoundingClientRect();
          const lim = s.classList.contains('story') ? 340 : (s.classList.contains('dark')?60:84);
          const over=[...s.querySelectorAll('.corpo *, .st-in *, .pad > div *')].filter(e=>{const q=e.getBoundingClientRect();
            return q.height>0 && (q.bottom>r.bottom-lim || q.right>r.right-50)});
          return s.dataset.n+':'+over.length}).join(' ')""")
        print('transbordo (tudo :0) ->', bad)
        await b.close()
    tmp.unlink()
asyncio.run(main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None))
