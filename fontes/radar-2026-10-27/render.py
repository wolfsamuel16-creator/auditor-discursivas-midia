"""Uso: python3 render.py <pasta com radar.html, fonts/ e foto.jpg> <saida>"""
import sys, pathlib, asyncio
from playwright.async_api import async_playwright
from PIL import Image
async def main(src, out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width':1080,'height':1350}, device_scale_factor=2)
        await pg.goto('file://' + str(pathlib.Path(src).resolve() / 'radar.html')); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
        for i, el in enumerate(await pg.query_selector_all('section.s'), 1):
            f = out / f'slide_{i:02d}.png'; await el.screenshot(path=str(f))
            Image.open(f).resize((1080,1350), Image.LANCZOS).save(f)
        over = await pg.evaluate("""[...document.querySelectorAll('section.s')].map((s,i)=>{const r=s.getBoundingClientRect();
          return (i+1)+':'+[...s.querySelectorAll('*')].filter(e=>{const q=e.getBoundingClientRect();return q.height>0&&!e.closest('.rod')&&!e.closest('.top')&&(q.bottom>r.bottom-100||q.right>r.right-40)}).length}).join(' ')""")
        print('transbordo', over); await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2]))
