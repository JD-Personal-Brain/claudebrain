// The guided tour: the first-time guide that plays like a short video (under 2 minutes).
// It plays once on a first visit, can be paused, closed and replayed from "Play the tour",
// and uses only recorded runs, so it never spends anyone's Claude usage. Its actions (watching the
// first flag, the blocked question) count in "How we'd measure it", like anything a viewer does.
// Add #tour to the link to force it to start, or #notour to keep it from starting.
(function () {
  const $ = s => document.querySelector(s);
  const go = s => window.APP.show(s);
  const STEPS = [
    { screen: "today", target: "#todayStats", title: "Meet The PM Assistant", text: "One AI assistant for every portfolio manager (PM): it drafts industry sections, gathers borrower files, drafts reviews and credit memos, and spots weakening borrowers sooner. Sample data throughout.", dur: 6000 },
    { screen: "today", target: ".persona", title: "You're Sam Okafor", text: "A senior PM with 12 business borrowers, paired with relationship manager (RM) Jordan Ellis. The assistant only ever sees Sam's own borrowers.", dur: 4500 },
    { screen: "industry", target: "#indStepsPanel", title: "New: the Industry background drafter (A11)", text: "From approved industry sources only, never borrower data, Claude drafts a memo's industry section, with a source on every sentence. Sam edits and approves it before it goes into the memo.", dur: 8500, before: () => { window.APP.show("industry"); return window.APP.selectInd("restaurants", true); } },
    { screen: "file", target: ".steps-panel", title: "The Borrower file builder (A7)", text: "It checks Sam may see the borrower, then reads four sources itself: the statements, loans and covenants, deposits and payments, and documents and notes.", dur: 8000, before: () => { window.APP.setBorrower("C101"); return window.APP.replayFile(false); } },
    { screen: "file", target: "#fileMissing", title: "Every figure has a source", text: "Every number shows where it came from, and anything missing or late is listed, never filled in with an estimate.", dur: 5500 },
    { screen: "review", target: ".steps-panel", title: "The Review and memo drafter (A8)", text: "From the file, Claude drafts the routine sections of Lakeshore's annual review. Then code checks every number, every gap and every word.", dur: 7500, before: () => window.APP.selectDraft("review:C101", false) },
    { screen: "review", target: ".docmeta-box", title: "The credit officer decides", text: "Every draft is marked AI draft and names the credit officer who makes the decision.", dur: 5000 },
    { screen: "review", target: ".judgment", title: "The judgment stays with the PM", text: "The borrower risk rating and the recommendation are left blank, for Sam to write. Sam writes the judgment and approves the draft as final, then submits it through the bank's normal route. The assistant never submits.", dur: 7000 },
    { screen: "review", target: "#ncBadge", title: "Every number checked", text: "Every number in the draft is matched against the borrower file. Anything it can't trace is highlighted.", dur: 5000 },
    { screen: "review", target: ".dsec.gap", title: "It stops rather than guesses", text: "Chequamegon's latest statements haven't arrived, so the draft marks those sections needs input instead of guessing.", dur: 7500, before: () => window.APP.selectDraft("review:C109", true) },
    { screen: "watch", target: "#watchList .wcard", title: "Coming next: early warning (A9)", text: "Plain rules credit risk owns flag weakening borrowers: late statements, a covenant near its limit, falling deposits, a payment past due. Claude explains each flag with the numbers.", dur: 9000, before: () => window.APP.runWatch("replay") },
    { screen: "watch", target: "#watchList .wcard .wact", title: "Sam decides", text: "Dismiss it with a reason, watch it, or raise it through the bank's own process. The assistant never changes a borrower risk rating.", dur: 7000, before: () => window.APP.watchFirst() },
    { screen: "controls", target: "#breakit", title: "Try to break it", text: "Ask for a borrower risk rating, an approval, a price or another PM's borrower: code checks stop it before any AI sees it, and every action is logged.", dur: 8000, before: () => window.APP.ask("What risk rating should Brewer's Row get?") },
    { screen: "measures", target: "#measureGrid", title: "How we'd know it works", text: "Five measures from day one: usage, quality, business impact, adoption, and risk and controls, with pilot PMs compared against a group without it.", dur: 6500 },
    { screen: "about", target: "#pilotNeeds", title: "What it would take", text: "Approval to use borrower data, the higher-risk review with the credit policy owner, and a small group of PMs. Our assumption, to confirm: data access and review set the pace.", dur: 8000 },
    { screen: "today", title: "Your turn", text: "Start from Today, and run the agents live on Claude from any screen (inside claude.ai, the first run asks your permission). Replay this tour any time.", dur: 4500 }
  ];
  if (Array.isArray(window.TOUR_DURS)) STEPS.forEach((s, n) => { if (window.TOUR_DURS[n]) s.dur = window.TOUR_DURS[n]; });   // the narrated video sets each step to its voiceover's length
  // The voiceover (same voice as the tour video): each step lasts at least as long as its line.
  const V = window.TOUR_VOICE && !Array.isArray(window.TOUR_DURS) ? window.TOUR_VOICE : null;
  if (V) STEPS.forEach((s, n) => { if (V.lens[n]) s.dur = Math.max(s.dur, Math.round(V.lens[n] * 1000) + 400); });
  const audio = V ? new Audio() : null;
  let voiceOn = true; try { voiceOn = localStorage.getItem("pmTourVoice") !== "off"; } catch (e) {}
  function speak(n) {
    if (!audio) return;
    audio.pause();
    if (!voiceOn || !V.clips[n]) return;
    audio.src = V.clips[n]; audio.currentTime = 0;
    blocked = false;
    audio.play().catch(() => { blocked = true; showVoice(); });   // browsers block sound until the viewer clicks (the tour starts by itself on a first visit): the button turns it on
  }
  let blocked = false;
  function showVoice() { const b = $("#tVoice"); if (!b) return; b.hidden = !audio; b.textContent = blocked && voiceOn ? "Turn on the voice" : voiceOn ? "Voice on" : "Voice off"; b.setAttribute("aria-pressed", String(voiceOn && !blocked)); }
  const TOTAL = STEPS.reduce((a, s) => a + s.dur, 0);
  let i = 0, t = 0, last = 0, paused = false, raf = 0, running = false, entering = false, token = 0;
  const fmt = ms => { const s = Math.round(ms / 1000); return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); };
  const reduce = () => window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const startOf = n => STEPS.slice(0, n).reduce((a, s) => a + s.dur, 0);

  function place() {
    const st = STEPS[i], spot = $("#spot"), card = $("#tcard"), tour = $("#tour");
    const el = st.target && document.querySelector(st.target);
    if (!el) { spot.hidden = true; tour.classList.add("dim"); card.classList.remove("at-top"); return; }
    tour.classList.remove("dim"); spot.hidden = false;
    const r = el.getBoundingClientRect(), pad = 6, vh = window.innerHeight;
    const top = Math.max(r.top - pad, 4), h = Math.max(24, Math.min(r.height + pad * 2, vh - top - 8));
    Object.assign(spot.style, { left: Math.max(r.left - pad, 4) + "px", top: top + "px", width: Math.min(r.width + pad * 2, window.innerWidth - 8) + "px", height: h + "px" });
    card.classList.toggle("at-top", top + h / 2 > vh * 0.55);
  }
  async function enter(n) {
    const my = ++token; entering = true;
    i = Math.max(0, Math.min(n, STEPS.length - 1)); t = startOf(i);
    const st = STEPS[i];
    go(st.screen);   // every step names its screen, so Back and Next always land in the right place
    $("#tTitle").textContent = st.title; $("#tText").textContent = st.text;
    $("#tcount").textContent = `Step ${i + 1} of ${STEPS.length}`;
    $("#tNext").textContent = i === STEPS.length - 1 ? "Finish" : "Next";
    $("#tBack").disabled = i === 0;
    if (st.before) { try { await st.before(); } catch (e) {} }
    if (my !== token) return;
    t = startOf(i); speak(i);
    (window.__tourLog = window.__tourLog || []).push({ step: i, at: performance.now() });   // the step's clock starts once its screen is ready
    const el = st.target && document.querySelector(st.target);
    if (el) el.scrollIntoView({ block: "center", behavior: reduce() ? "auto" : "smooth" });
    entering = false;
    setTimeout(place, reduce() ? 0 : 450); place();
  }
  function frame(now) {
    if (!running) return;
    if (!paused && !entering) t += now - last;
    last = now;
    if (!paused && !entering && t >= startOf(i + 1)) { if (i === STEPS.length - 1) { stop(); return; } enter(i + 1); }
    $("#tbar").style.width = Math.min(100, t / TOTAL * 100) + "%";
    $("#tclock").textContent = fmt(t) + " / " + fmt(TOTAL);
    place();
    raf = requestAnimationFrame(frame);
  }
  function start() {
    if (running) return;
    $("#tour").hidden = false; running = true; paused = false; $("#tPause").textContent = "Pause"; showVoice();
    enter(0); last = performance.now(); raf = requestAnimationFrame(frame);
    window.AGENTS.log("Tour", "Started the guided tour", "", "Adoption");
  }
  function stop() {
    running = false; token++; cancelAnimationFrame(raf); $("#tour").hidden = true; if (audio) audio.pause();
    try { localStorage.setItem("pmTourSeen", "1"); } catch (e) {}
    window.AGENTS.log("Tour", "Finished or closed the tour", "", "Adoption");
  }
  $("#tourBtn").addEventListener("click", start);
  $("#tSkip").addEventListener("click", stop);
  $("#tNext").addEventListener("click", () => { if (entering) return; if (i === STEPS.length - 1) stop(); else enter(i + 1); });
  $("#tBack").addEventListener("click", () => { if (!entering) enter(i - 1); });
  $("#tPause").addEventListener("click", () => { paused = !paused; $("#tPause").textContent = paused ? "Play" : "Pause"; if (audio && voiceOn) { if (paused) audio.pause(); else audio.play().catch(() => {}); } });
  if ($("#tVoice")) $("#tVoice").addEventListener("click", () => {
    if (blocked && voiceOn) { speak(i); showVoice(); return; }   // the click itself lets the browser play sound
    voiceOn = !voiceOn; try { localStorage.setItem("pmTourVoice", voiceOn ? "on" : "off"); } catch (e) {}
    showVoice(); if (voiceOn && !paused) speak(i); else if (audio) audio.pause();
  });
  document.addEventListener("keydown", e => { if (running && e.key === "Escape") stop(); });
  window.addEventListener("resize", () => running && place());
  window.addEventListener("scroll", () => running && place(), { passive: true });

  let seen = false; try { seen = localStorage.getItem("pmTourSeen") === "1"; } catch (e) {}
  const hash = location.hash.replace("#", "");
  if (hash === "tour" || (!seen && hash !== "notour")) setTimeout(start, 900);
  window.TOUR = { start, stop, STEPS, TOTAL, audio };
})();
