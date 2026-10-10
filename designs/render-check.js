// Renders EVERY designed page the way a reader sees it and fails on anything incomplete (from L7, L7c, L7d, L19).
// Run from the repo root:  PW=$(npm root -g)/playwright node designs/render-check.js
// Checks each single page (designs/*.html) at 1280 and 400 px wide, and each design-canvas part:
//   - no empty table, no table with only a header
//   - no sideways scrolling at 400 px (phone width)
//   - no stray Markdown marks showing (**, __, | --- |, leftover [text](link))
//   - the page has real text (not a blank render)
//   - canvas parts: content fits the frame in canvas.json (nothing cut off at the bottom)
// Canvas parts need the canvas runtime saved as support.js beside them. It is kept in the repo
// (idea 35); if it goes missing, restore it with the Artifact tool: read the design page with path
// "artifact-type/dc-runtime.js".
// Saves a full-page screenshot of every page to the folder in SHOTS (default /tmp/render-check) to look at.
const fs = require('fs'), path = require('path'), http = require('http');
const { chromium } = require(process.env.PW || 'playwright');
const ROOT = process.cwd(), D = path.join(ROOT, 'designs'), SHOTS = process.env.SHOTS || '/tmp/render-check';
fs.mkdirSync(SHOTS, { recursive: true });
const singles = fs.readdirSync(D).filter(f => f.endsWith('.html')).sort();
const canvases = fs.readdirSync(D).filter(f => fs.existsSync(path.join(D, f, 'canvas.json')));
const server = http.createServer((q, r) => {
  const f = path.join(D, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'Content-Type': f.endsWith('.js') ? 'text/javascript' : 'text/html; charset=utf-8' }); r.end(d); } });
}).listen(0, async () => {
  const port = server.address().port, b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  let bad = 0; const fail = (msg) => { bad++; console.log('FAIL ', msg); };
  const inspect = () => {
    const tables = [...document.querySelectorAll('table')];
    const emptyT = tables.filter(t => t.querySelectorAll('tbody tr, tr').length < 2 || !t.innerText.trim()).length;
    const txt = document.body.innerText;
    const marks = (txt.match(/\*\*[^*\n]{1,60}\*\*|(^|\s)__\w|\|\s*-{3,}\s*\||\]\((https?:|\.\/|\/)[^)]*\)/g) || []).slice(0, 3);
    return { tables: tables.length, emptyT, chars: txt.trim().length, marks,
             sw: document.documentElement.scrollWidth, h: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight) };
  };
  for (const f of singles) {
    for (const w of [1280, 400]) {
      const p = await b.newPage({ viewport: { width: w, height: 900 } });
      await p.goto(`http://localhost:${port}/${f}`); await p.waitForTimeout(400);
      const r = await p.evaluate(inspect);
      if (r.emptyT) fail(`${f} @${w}px: ${r.emptyT} empty table(s)`);
      if (r.chars < 200) fail(`${f} @${w}px: almost no text rendered (${r.chars} characters)`);
      if (w === 400 && r.sw > 400) fail(`${f}: scrolls sideways at phone width (${r.sw}px wide)`);
      if (r.marks.length) fail(`${f}: stray Markdown showing: ${JSON.stringify(r.marks)}`);
      if (w === 1280) await p.screenshot({ path: path.join(SHOTS, f.replace('.html', '.png')), fullPage: true });
      await p.close();
    }
    console.log('ok   ', f);
  }
  for (const c of canvases) {
    if (!fs.existsSync(path.join(D, c, 'support.js'))) { fail(`${c}: support.js (the canvas runtime) is missing, so its parts could not be checked`); continue; }
    const boards = JSON.parse(fs.readFileSync(path.join(D, c, 'canvas.json'))).boards;
    for (const [name, fr] of Object.entries(boards)) {
      const p = await b.newPage({ viewport: { width: fr.w, height: Math.min(fr.h, 1200) } });
      await p.goto(`http://localhost:${port}/${c}/${name}`); await p.waitForTimeout(2500);
      const r = await p.evaluate(inspect);
      if (r.h > fr.h) fail(`${c}/${name}: CUT OFF, content is ${r.h}px but the frame is ${fr.h}px (set "h" to at least ${r.h + 40} in canvas.json)`);
      if (r.emptyT) fail(`${c}/${name}: ${r.emptyT} empty table(s)`);
      if (r.chars < 200) fail(`${c}/${name}: almost no text rendered (${r.chars} characters)`);
      if (r.marks.length) fail(`${c}/${name}: stray Markdown showing: ${JSON.stringify(r.marks)}`);
      await p.screenshot({ path: path.join(SHOTS, `${c}--${name.replace('.dc.html', '')}.png`), fullPage: true });
      await p.close(); if (r.h <= fr.h) console.log('ok   ', `${c}/${name} (content ${r.h}px, frame ${fr.h}px)`);
    }
  }
  await b.close(); server.close();
  console.log(`checked ${singles.length} pages and ${canvases.length} canvas; screenshots in ${SHOTS}`); console.log('problems:', bad);
  process.exit(bad ? 1 : 0);
});
