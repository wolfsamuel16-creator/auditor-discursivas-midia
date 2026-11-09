import sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
sel = sys.argv[3] if len(sys.argv) > 3 else '.slide'
prefix = sys.argv[4] if len(sys.argv) > 4 else 'slide'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 2200})
    pg.goto(src.as_uri()); pg.wait_for_timeout(1200)
    els = pg.query_selector_all(sel)
    for i, e in enumerate(els, 1):
        e.screenshot(path=str(out / f'{prefix}_{i:02d}.png'))
    print(pg.evaluate("""(s)=>[...document.querySelectorAll(s)].map((el,i)=>{
      let over=[];el.querySelectorAll('*').forEach(c=>{const r=c.getBoundingClientRect(),R=el.getBoundingClientRect();
      if(r.bottom>R.bottom-2&&!c.closest('.rodape')||r.right>R.right+1)over.push(c.className||c.tagName)});
      const rod=el.querySelector('.rodape');let clash=0;
      if(rod){const rb=rod.getBoundingClientRect();el.querySelectorAll(':scope > *:not(.rodape)').forEach(c=>{if(c.getBoundingClientRect().bottom>rb.top-8)clash++})}
      return (i+1)+':'+(over.length?'TRANSBORDO '+over.slice(0,3):'ok')+(clash?' COLIDE_RODAPE':'')})""", sel))
    b.close()
