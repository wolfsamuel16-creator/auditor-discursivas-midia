const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve('aula_pmsc.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const head = `<div style="width:100%;font-family:Poppins;font-size:6.5pt;padding:0 18mm;display:flex;justify-content:space-between;margin-top:6mm"><span style="color:#F04E23;font-weight:700;letter-spacing:.28em">AUDITOR DISCURSIVAS</span><span style="color:#2A3544;letter-spacing:.12em">Redação PM-SC 2026</span></div>`;
  const foot = `<div style="width:100%;font-family:Poppins;font-size:6.5pt;padding:0 18mm;text-align:right;color:#2A3544;margin-bottom:6mm">@auditor_discursivas · Página <span class="pageNumber"></span></div>`;
  await p.pdf({ path: 'aula_pmsc.pdf', format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: head, footerTemplate: foot, preferCSSPageSize: true });
  await b.close();
})();
