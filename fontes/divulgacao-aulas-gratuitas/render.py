import sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]); out.mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1200, "height": 2000}, device_scale_factor=1)
    pg.goto(src.as_uri()); pg.wait_for_timeout(800)
    for i, el in enumerate(pg.query_selector_all("section.s"), 1):
        el.screenshot(path=str(out / f"slide_{i:02d}.png"))
    for i, el in enumerate(pg.query_selector_all("section.st"), 1):
        el.screenshot(path=str(out / f"story_{i:02d}.png"))
    # overflow check
    print(pg.evaluate("""[...document.querySelectorAll('section')].map((s,i)=>i+':'+(s.scrollHeight>s.clientHeight?'TRANSBORDO':'ok'))"""))
    b.close()
