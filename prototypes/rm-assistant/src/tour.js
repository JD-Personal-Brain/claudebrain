// The guided tour: the first-time guide that plays like a short video (under 2 minutes).
// It plays once on a first visit, can be paused, closed and replayed from "Play the tour (under 2 min)",
// and uses only recorded runs, so it never spends anyone's Claude usage. Its actions (using the
// first insight, the blocked question) count in "How we'd measure it", like anything a viewer does.
// Add #tour to the link to force it to start, or #notour to keep it from starting.
(function () {
  const $ = s => document.querySelector(s);
  const go = s => window.APP.show(s);
  const STEPS = [
    { screen: "today", target: "#todayStats", title: "Meet The RM Assistant", text: "One AI assistant for every relationship manager (RM), starting each day on Today: who to call, this week's meetings and what's waiting. The aim is more revenue per RM and more hours with clients.", dur: 6500 },
    { screen: "list", target: ".persona", title: "You're Jordan Ellis", text: "A senior RM with 12 business clients, all made up. The assistant only ever sees Jordan's own clients.", dur: 5500 },
    { screen: "list", target: "#hero", title: "This week at a glance", text: "Each Monday starts here: the clients worth a call this week, and how many signals were found.", dur: 4500 },
    { screen: "list", target: "#listTrace", title: "The Signal finder spots opportunities", text: "Plain rules the business owns, such as idle cash or check fraud exposure, run against each client. It also reads real outside data: the Federal Reserve's 10-year Treasury yield.", dur: 7500, before: () => window.APP.runList("replay") },
    { screen: "list", target: "#listResults .card", title: "Claude explains each one", text: "The Insight writer, running on Claude, turns each client's signals into a plain-English reason, talking points and a next step. Before the RM can use it, every number is checked against the agent's data; anything it can't trace is flagged.", dur: 6500 },
    { screen: "list", target: "#listResults .card .actions", title: "You decide", text: "Use it, change it or reject it. Here Jordan uses the first one: it becomes an opportunity tagged AI-sourced, so the results can be counted.", dur: 7500, before: () => window.APP.acceptFirst() },
    { screen: "brief", target: ".steps-panel", title: "Ready for Tuesday's meeting", text: "Before each meeting, the Prep and follow-up assistant looks up four sources itself (client record, open insights, recent activity, market data), showing every step, then writes a one-page brief with a source on every fact.", dur: 6000, before: () => window.APP.replayBrief(false) },
    { screen: "followup", target: "#consent", title: "After the meeting", text: "The assistant drafts the recap, the follow-up email and the CRM call note. No recording without the client's consent, so here it works from Jordan's notes.", dur: 7500, before: () => window.APP.runFollow("instant") },
    { screen: "followup", target: ".approvebar", title: "Nothing is saved or sent until Jordan approves", text: "Unclear items come back marked CHECK instead of guessed. The note reaches the CRM only after Jordan's click, and Jordan sends the email.", dur: 6500 },
    { screen: "warn", target: "#warnList .wcard", title: "Coming next: early warning", text: "Plain rules flag clients who may be drifting away, like falling balances or payroll moved to another bank, with the numbers behind each flag. A reason to call, never a credit signal.", dur: 7000 },
    { screen: "refer", target: "#refList .rcard", title: "Refer to treasury", text: "It also spots needs the treasury team serves and drafts the hand-off. Jordan sends it, and the referral is tracked from spotted to accepted.", dur: 7000, before: () => window.WAVE2.sendFirstReferral() },
    { screen: "controls", target: "#breakit", title: "Try to break it", text: "Ask for a credit decision, a price or another RM's client: code checks stop common phrasings before any AI sees them, Claude's rules are the second line, and every action is logged.", dur: 8000, before: () => window.APP.ask("Should we approve Lakeshore's line increase?") },
    { screen: "measures", target: "#measureGrid", title: "How we'd know it works", text: "Five measures from day one: usage, quality, business impact, adoption, and risk and controls. In a pilot, RMs with the assistant are compared with RMs without it.", dur: 8000 },
    { screen: "about", target: "#pilotNeeds", title: "What it would take", text: "A pilot needs read access to client and CRM data, a risk partner from day one and a small group of RMs. Our assumption, to confirm: data access sets the pace, not the build.", dur: 8500 },
    { screen: "today", title: "Your turn", text: "Start from Today, and run the agents live on Claude from any screen (inside claude.ai, the first run asks your permission). Replay this tour any time.", dur: 4500 }
  ];
  if (Array.isArray(window.TOUR_DURS)) STEPS.forEach((s, n) => { if (window.TOUR_DURS[n]) s.dur = window.TOUR_DURS[n]; });   // the narrated video sets each step to its voiceover's length
  // The voiceover (same voice as the tour video): each step lasts at least as long as its line.
  const V = window.TOUR_VOICE && !Array.isArray(window.TOUR_DURS) ? window.TOUR_VOICE : null;
  if (V) STEPS.forEach((s, n) => { if (V.lens[n]) s.dur = Math.max(s.dur, Math.round(V.lens[n] * 1000) + 400); });
  const audio = V ? new Audio() : null;
  let voiceOn = true; try { voiceOn = localStorage.getItem("rmTourVoice") !== "off"; } catch (e) {}
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
    try { localStorage.setItem("rmTourSeen", "1"); } catch (e) {}
    window.AGENTS.log("Tour", "Finished or closed the tour", "", "Adoption");
  }
  $("#tourBtn").addEventListener("click", start);
  $("#tSkip").addEventListener("click", stop);
  $("#tNext").addEventListener("click", () => { if (entering) return; if (i === STEPS.length - 1) stop(); else enter(i + 1); });
  $("#tBack").addEventListener("click", () => { if (!entering) enter(i - 1); });
  $("#tPause").addEventListener("click", () => { paused = !paused; $("#tPause").textContent = paused ? "Play" : "Pause"; if (audio && voiceOn) { if (paused) audio.pause(); else audio.play().catch(() => {}); } });
  if ($("#tVoice")) $("#tVoice").addEventListener("click", () => {
    if (blocked && voiceOn) { speak(i); showVoice(); return; }   // the click itself lets the browser play sound
    voiceOn = !voiceOn; try { localStorage.setItem("rmTourVoice", voiceOn ? "on" : "off"); } catch (e) {}
    showVoice(); if (voiceOn && !paused) speak(i); else if (audio) audio.pause();
  });
  document.addEventListener("keydown", e => { if (running && e.key === "Escape") stop(); });
  window.addEventListener("resize", () => running && place());
  window.addEventListener("scroll", () => running && place(), { passive: true });

  let seen = false; try { seen = localStorage.getItem("rmTourSeen") === "1"; } catch (e) {}
  const hash = location.hash.replace("#", "");
  if (hash === "tour" || (!seen && hash !== "notour")) setTimeout(start, 900);
  window.TOUR = { start, stop, STEPS, TOTAL, audio };
})();
