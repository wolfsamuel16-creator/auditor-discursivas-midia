from playwright.sync_api import sync_playwright
ic = {
 "como-funciona": '<path d="M60 40h80M60 80h80M60 120h50" /><circle cx="35" cy="40" r="8"/><circle cx="35" cy="80" r="8"/><circle cx="35" cy="120" r="8"/>',
 "resultados": '<polyline points="20,140 70,95 105,120 175,45"/><polyline points="135,45 175,45 175,85"/>',
 "aulas-gratis": '<rect x="45" y="20" width="110" height="150" rx="10"/><path d="M70 60h60M70 90h60M70 120h40"/>',
 "quem-sou": '<circle cx="100" cy="65" r="35"/><path d="M35 170c10-40 40-55 65-55s55 15 65 55"/>',
 "duvidas": '<path d="M70 70a30 30 0 1 1 45 26c-10 6-15 12-15 24"/><circle cx="100" cy="155" r="4" fill="#F04E23"/>',
}
html = """<html><body style="margin:0;width:1080px;height:1920px;background:#2A3544;display:flex;align-items:center;justify-content:center">
<div style="width:720px;height:720px;border-radius:50%;background:#2A3544;border:14px solid #F04E23;display:flex;align-items:center;justify-content:center">
<svg width="400" height="400" viewBox="0 0 200 200" fill="none" stroke="#F04E23" stroke-width="12" stroke-linecap="round" stroke-linejoin="round">{}</svg></div></body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    for k,v in ic.items():
        pg.set_content(html.format(v)); pg.screenshot(path=f"capa-{k}.png")
    b.close()
