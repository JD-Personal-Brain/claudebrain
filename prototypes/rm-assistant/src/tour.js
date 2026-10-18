// The guided tour: the first-time guide that plays like a short video (under 2 minutes).
// It plays once on a first visit, can be paused, skipped and replayed from "Play the tour",
// and uses only recorded runs, so it never spends anyone's Claude usage.
// Add #tour to the link to force it to start, or #notour to keep it from starting.
(function () {
  const $ = s => document.querySelector(s);
  const go = s => window.APP.show(s);
  const STEPS = [
    { title: "Meet The RM Assistant", text: "A concept prototype: one AI assistant for each relationship manager (RM), to help them win business and free up the time to win it. Everything here is sample data. This tour takes under 2 minutes.", dur: 8000 },
    { target: ".persona", title: "You're Jordan Ellis", text: "A senior RM with 12 business clients, all made up. The assistant only ever sees Jordan's own clients.", dur: 7000, before: () => go("list") },
    { target: "#nav", title: "Three capabilities to start", text: "Wave 1 of the plan: the Monday opportunity list, the pre-meeting client brief and the meeting follow-up. More capabilities join the same assistant later.", dur: 9000 },
    { target: "#listTrace", title: "Agent A1 finds the signals", text: "Each night, A1 checks each client against simple rules the business owns, such as idle cash or check fraud exposure, and every Monday the top ones go to the RM. Here it also reads real outside data: the Federal Reserve's 10-year Treasury yield.", dur: 9000, before: () => window.APP.runList("replay") },
    { target: "#listResults .card", title: "Agent A2 explains each one", text: "A2, running on Claude, turns each signal into a plain-English reason, talking points and a next step, using only the numbers behind it.", dur: 8500 },
    { target: "#listResults .card .ncheck", title: "Every number is checked", text: "When a draft is finished, the page checks each number against the data the agent was given, before the RM can use it (control K7). Anything it can't trace is flagged.", dur: 7500 },
    { target: "#listResults .card .actions", title: "You decide", text: "Accept, change or dismiss. Accepting creates an opportunity tagged AI-sourced, so we can count the results. One click of feedback steers what improves next.", dur: 8500 },
    { target: ".steps-panel", title: "A3 prepares you for Tuesday", text: "Before each meeting, A3 calls four tools: the client record, the open insights, recent activity and market data. You see every step it took.", dur: 9500, before: () => { go("brief"); window.APP.replayBrief(false); } },
    { target: "#briefDoc", title: "A one-page brief with sources", text: "Every fact carries its source, and the watch-outs keep the RM away from pricing and credit commitments.", dur: 7500 },
    { target: "#consent", title: "After the meeting", text: "A3 drafts the recap, the follow-up email and the CRM note. No recording without the client's consent (K24), so here it works from Jordan's notes.", dur: 9000, before: () => { go("followup"); window.APP.runFollow("instant"); } },
    { target: "#approveNote", title: "Nothing is saved or sent until you approve", text: "Unclear items come back marked CHECK instead of guessed (K25). The note reaches the CRM only after Jordan's click (K2), and Jordan sends the email (K1).", dur: 9500 },
    { target: "#breakit", title: "Try to break it", text: "Ask for a credit decision, a price or another RM's client: the guardrails stop it in code before any AI sees it (K8, K4). Every action lands in the audit log (K12).", dur: 9000, before: () => { go("controls"); window.APP.ask("Should we approve Lakeshore's line increase?", true); } },
    { target: "#measureGrid", title: "How we'd know it works", text: "The product manager view tracks the five kinds of measures: usage, quality, business impact, adoption, and risk and controls. Adoption is the goal: built into the routines RMs already have.", dur: 9500, before: () => go("measures") },
    { title: "Your turn", text: "Run the agents live on Claude from any screen (inside claude.ai, the first run asks your permission). Replay this tour any time from \"Play the tour\".", dur: 7000, before: () => go("list") }
  ];
  const TOTAL = STEPS.reduce((a, s) => a + s.dur, 0);
  let i = 0, t = 0, last = 0, paused = false, raf = 0, running = false;
  const fmt = ms => { const s = Math.round(ms / 1000); return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); };
  const reduce = () => window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function place() {
    const st = STEPS[i], spot = $("#spot"), card = $("#tcard");
    const el = st.target && document.querySelector(st.target);
    if (!el) { spot.hidden = true; card.classList.remove("at-top"); return; }
    spot.hidden = false;
    const r = el.getBoundingClientRect(), pad = 6, vh = window.innerHeight;
    const top = Math.max(r.top - pad, 4), h = Math.min(r.height + pad * 2, vh - top - 8);
    Object.assign(spot.style, { left: Math.max(r.left - pad, 4) + "px", top: top + "px", width: Math.min(r.width + pad * 2, window.innerWidth - 8) + "px", height: h + "px" });
    card.classList.toggle("at-top", top + h / 2 > vh * 0.55);
  }
  async function enter(n) {
    i = Math.max(0, Math.min(n, STEPS.length - 1)); t = STEPS.slice(0, i).reduce((a, s) => a + s.dur, 0);
    const st = STEPS[i];
    if (st.before) { try { await st.before(); } catch (e) {} }
    const el = st.target && document.querySelector(st.target);
    if (el) el.scrollIntoView({ block: "center", behavior: reduce() ? "auto" : "smooth" });
    $("#tTitle").textContent = st.title; $("#tText").textContent = st.text;
    $("#tcount").textContent = `Step ${i + 1} of ${STEPS.length}`;
    $("#tNext").textContent = i === STEPS.length - 1 ? "Finish" : "Next";
    $("#tBack").disabled = i === 0;
    setTimeout(place, reduce() ? 0 : 450); place();
  }
  function frame(now) {
    if (!running) return;
    if (!paused) { t += now - last; }
    last = now;
    const stepEnd = STEPS.slice(0, i + 1).reduce((a, s) => a + s.dur, 0);
    if (!paused && t >= stepEnd) { if (i === STEPS.length - 1) { stop(); return; } enter(i + 1); }
    $("#tbar").style.width = Math.min(100, t / TOTAL * 100) + "%";
    $("#tclock").textContent = fmt(t) + " / " + fmt(TOTAL);
    place();
    raf = requestAnimationFrame(frame);
  }
  function start() {
    $("#tour").hidden = false; running = true; paused = false; $("#tPause").textContent = "Pause";
    enter(0); last = performance.now(); raf = requestAnimationFrame(frame);
    window.AGENTS.log("Tour", "Started the guided tour", "", "Adoption");
  }
  function stop() {
    running = false; cancelAnimationFrame(raf); $("#tour").hidden = true;
    try { localStorage.setItem("rmTourSeen", "1"); } catch (e) {}
    window.AGENTS.log("Tour", "Finished or skipped the tour", "", "Adoption");
  }
  $("#tourBtn").addEventListener("click", start);
  $("#tSkip").addEventListener("click", stop);
  $("#tNext").addEventListener("click", () => { if (i === STEPS.length - 1) stop(); else enter(i + 1); });
  $("#tBack").addEventListener("click", () => enter(i - 1));
  $("#tPause").addEventListener("click", () => { paused = !paused; $("#tPause").textContent = paused ? "Play" : "Pause"; });
  document.addEventListener("keydown", e => { if (running && e.key === "Escape") stop(); });
  window.addEventListener("resize", () => running && place());
  window.addEventListener("scroll", () => running && place(), { passive: true });

  let seen = false; try { seen = localStorage.getItem("rmTourSeen") === "1"; } catch (e) {}
  const hash = location.hash.replace("#", "");
  if (hash === "tour" || (!seen && hash !== "notour")) setTimeout(start, 900);
  window.TOUR = { start, stop, STEPS, TOTAL };
})();
