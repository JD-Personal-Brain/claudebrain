// Records the guided tour as a video file for people who'd rather watch than click.
// Run from prototypes/rm-assistant:  node tests/record-video.js [prototype-v1.html]
// Writes rm-assistant-tour.webm in the scratch folder ($OUT, default /tmp/rm-assistant-video);
// Recording runs the page about 12% slow, so convert it back to real time (the tour's own clock):
//   ffmpeg -ss 0.8 -to 136 -i rm-assistant-tour.webm -vf "setpts=0.884*PTS" -r 25 -c:v libx264 -pix_fmt yuv420p -crf 26 -movflags +faststart rm-assistant-tour.mp4
// Check a frame against the clock on the tour card (at 60 s it should read 1:00) and adjust 0.884 if needed.
const path = require("path"), fs = require("fs");
const { chromium } = require(process.env.PW || "playwright");
const FILE = path.resolve(process.argv[2] || "prototype-v1.html");
const OUT = process.env.OUT || "/tmp/rm-assistant-video";
fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 }, recordVideo: { dir: OUT, size: { width: 1280, height: 800 } } });
  const p = await ctx.newPage();
  await p.goto("file://" + FILE + "#tour");
  const total = await p.evaluate(() => window.TOUR.TOTAL);
  await p.waitForTimeout(total + 2500);
  const v = await p.video().path();
  await ctx.close(); await browser.close();
  fs.renameSync(v, path.join(OUT, "rm-assistant-tour.webm"));
  console.log("recorded", (total / 1000).toFixed(1), "s tour to", path.join(OUT, "rm-assistant-tour.webm"));
})();
