// Records the guided tour as a video file for people who'd rather watch than click.
// Run from prototypes/rm-assistant:  node tests/record-video.js [prototype-v1.html]
// With NARRATION=<lens.json> (written by video/narrate.py), each tour step lasts as long as its
// voiceover line, and the script saves when each step really started (timing.json), so the voice
// can be laid down in sync. Writes to $OUT (default /tmp/rm-assistant-video). video/make-video.py
// then turns the raw recording and the voice clips into the final mp4.
const path = require("path"), fs = require("fs");
const { chromium } = require(process.env.PW || "playwright");
const FILE = path.resolve(process.argv[2] || "prototype-v1.html");
const OUT = process.env.OUT || "/tmp/rm-assistant-video";
fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const lens = process.env.NARRATION ? JSON.parse(fs.readFileSync(process.env.NARRATION, "utf8")).lens : null;
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 }, recordVideo: { dir: OUT, size: { width: 1280, height: 800 } } });
  if (lens) await ctx.addInitScript(d => { window.TOUR_DURS = d; }, lens.map(s => Math.max(3500, Math.round(s * 1000) + 700)));
  const t0 = Date.now();                       // the recording starts with the page
  const p = await ctx.newPage();
  await p.goto("file://" + FILE + "#tour");
  await p.waitForFunction(() => window.TOUR && document.querySelector("#tour") && !document.querySelector("#tour").hidden, null, { timeout: 10000 });
  await p.waitForFunction(() => document.querySelector("#tour").hidden, null, { timeout: 300000, polling: 250 });
  await p.waitForTimeout(1500);
  const steps = await p.evaluate(() => (window.__tourLog || []).map(s => ({ step: s.step, at: performance.timeOrigin + s.at })));
  const t1 = Date.now();
  const v = await p.video().path();
  await ctx.close(); await browser.close();
  fs.renameSync(v, path.join(OUT, "rm-assistant-tour.webm"));
  fs.writeFileSync(path.join(OUT, "timing.json"), JSON.stringify({ realSeconds: (t1 - t0) / 1000, steps: steps.map(s => ({ step: s.step, at: (s.at - t0) / 1000 })) }, null, 1));
  console.log("recorded", ((t1 - t0) / 1000).toFixed(1), "s of real time to", OUT);
})();
