// The screens: the Monday opportunity list (B1), the pre-meeting client brief (B2),
// the meeting follow-up (B3 and B4), controls and the audit log, the product manager view
// and "How it's built". Every screen opens filled with the recorded run, so the page is
// complete at rest; "Run live" asks Claude for a fresh answer.
(function () {
  const B = window.BOOK, R = window.REPLAY, M = window.MARKET, A = window.AGENTS, AI = A.AI;
  const $ = s => document.querySelector(s);
  const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const fmtDate = iso => new Date(iso + "T12:00:00").toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric" });
  const fmtShort = iso => new Date(iso + "T12:00:00").toLocaleDateString("en-US", { weekday: "short", month: "short", day: "numeric" });
  const plural = (n, w) => n + " " + w + (n === 1 ? "" : "s");
  const changed = () => { renderMeasures(); };

  // Inline formatting: **bold**, [CHECK: ...] and [Source] tags.
  function inline(t) {
    return esc(t).replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/\[CHECK:([^\]]*)\]/g, '<span class="check">[CHECK:$1]</span>')
      .replace(/\[([A-Z][^\]]{1,40})\]/g, (m, s) => s.startsWith("CHECK") ? m : `<span class="src">${s}</span>`);
  }
  // A small Markdown renderer for the brief: ## headings, bullets, numbered lists, paragraphs.
  function md(text) {
    const out = []; let list = null;
    const close = () => { if (list) { out.push(`</${list}>`); list = null; } };
    text.split("\n").forEach(line => {
      const l = line.trim();
      if (!l) { close(); return; }
      let m;
      if ((m = l.match(/^#{1,3}\s+(.*)/))) { close(); out.push(`<h2>${inline(m[1])}</h2>`); }
      else if ((m = l.match(/^[-*•]\s+(.*)/))) { if (list !== "ul") { close(); out.push("<ul>"); list = "ul"; } out.push(`<li>${inline(m[1])}</li>`); }
      else if ((m = l.match(/^\d+[.)]\s+(.*)/))) { if (list !== "ol") { close(); out.push("<ol>"); list = "ol"; } out.push(`<li>${inline(m[1])}</li>`); }
      else { close(); out.push(`<p>${inline(l)}</p>`); }
    });
    close();
    return out.join("");
  }
  function markUntraced(html, untraced) {
    untraced.forEach(u => { const e = esc(u); html = html.split(e).join(`<mark class="untraced" title="This number isn't in the agent's inputs: check it before use">${e}</mark>`); });
    return html;
  }
  const checkBadge = r => r.total === 0 ? `<span class="ncheck">K7 no numbers to check</span>`
    : r.untraced.length ? `<span class="ncheck bad" title="Not found in the inputs: ${esc(r.untraced.join(", "))}">K7 ${r.traced} of ${r.total} numbers traced · check ${esc(r.untraced.join(", "))}</span>`
    : `<span class="ncheck" title="Every number in this output appears in the data the agent was given">K7 ${r.total} of ${r.total} numbers traced to the data</span>`;
  const modeTag = mode => mode === "live" ? `<span class="live-tag">Live run on Claude</span>` : `<span class="rec-tag">Recorded run · ${R.recorded}</span>`;

  // ---------- Navigation ----------
  function show(name) {
    document.querySelectorAll(".screen").forEach(s => { s.hidden = s.dataset.screen !== name; });
    document.querySelectorAll("#nav button").forEach(b => b.classList.toggle("on", b.dataset.screen === name));
    if (name === "measures") renderMeasures();
    window.scrollTo({ top: 0 });
  }
  document.querySelectorAll("#nav button").forEach(b => b.addEventListener("click", () => show(b.dataset.screen)));
  $("#today").textContent = B.todayLabel + " (sample)";

  // ---------- Live AI or recorded runs ----------
  let liveOK = false;
  function setMode() {
    liveOK = AI.status === "available";
    const chip = $("#aiMode");
    chip.dataset.mode = liveOK ? "live" : "replay";
    chip.innerHTML = liveOK ? "Live AI<span class=\"long\">: Claude ready</span>" : "Recorded runs<span class=\"long\"> (live AI not available here)</span>";
    chip.title = liveOK ? "The agents run live on Claude, on your own Claude account. The first run asks your permission." : "Live AI runs only inside claude.ai. This view plays runs recorded on 2026-10-18.";
    ["#runList", "#runBrief", "#runFollow"].forEach(id => { const b = $(id); b.disabled = !liveOK; b.title = liveOK ? "" : chip.title; });
  }
  function dropToReplay(e) { if (A.permanent(e)) { AI.status = "absent"; setMode(); } }

  // ---------- Feedback (one click on every output) ----------
  function feedback(key) {
    return `<span class="fb" data-fb="${key}"><button type="button" class="thumb" data-v="up" aria-pressed="false" aria-label="Useful">Useful</button><button type="button" class="thumb" data-v="down" aria-pressed="false" aria-label="Not useful">Not useful</button></span>`;
  }
  document.addEventListener("click", e => {
    const t = e.target.closest(".thumb"); if (!t) return;
    const wrap = t.closest(".fb"); const was = t.getAttribute("aria-pressed") === "true";
    wrap.querySelectorAll(".thumb").forEach(b => b.setAttribute("aria-pressed", "false"));
    if (!was) { t.setAttribute("aria-pressed", "true"); A.measures[t.dataset.v === "up" ? "thumbsUp" : "thumbsDown"]++; A.log("RM feedback", t.dataset.v === "up" ? "Marked useful" : "Marked not useful", wrap.dataset.fb, "Feedback"); }
    changed();
  });

  // ---------- B1 Monday opportunity list ----------
  let listCtl = null;
  function traceStep(box, label, text, state) {
    const s = document.createElement("span"); s.className = "tstep" + (state === "run" ? " run" : "");
    s.innerHTML = `<b>${esc(label)}</b>${esc(text)}`; box.appendChild(s); return s;
  }
  function renderList(insights, scan, mode) {
    const top = scan.ranked.slice(0, 5);
    const { data } = A.a2Prompt(top);
    const box = $("#listResults"); box.innerHTML = "";
    top.forEach((t, i) => {
      const ins = insights.find(x => x.clientId === t.clientId);
      if (!ins) return;   // never pair an insight with the wrong client
      const c = A.findClient(t.clientId);
      const text = [ins.headline, ins.why, ...(ins.talkingPoints || []), ins.nextStep].join(" ");
      const nc = A.numberCheck(text, data[i]);
      A.measures.outputsShown++;
      const card = document.createElement("article"); card.className = "card"; card.dataset.client = c.id;
      card.innerHTML = `<div class="rank">${i + 1}</div><div class="cbody">
        <div class="chead"><span class="cname">${esc(c.name)}</span><span class="cmeta">${esc(c.industry)} · ${esc(c.city)}</span><span class="score">score ${t.score}</span></div>
        <div class="rules">${t.signals.map(s => `<span class="rule" title="${esc(A.RULES.find(r => r.id === s.rule).plain)}">${s.rule} ${esc(s.ruleName)}</span>`).join("")}${t.signals.some(s => s.alsoFired) ? `<span class="rule" title="${esc(A.MARKET_RULE.plain)}">M1 Rates context · Fed H.15</span>` : ""}</div>
        <p class="headline">${markUntraced(inline(ins.headline), nc.untraced)}</p>
        <div class="ctwo"><div><h3>Why</h3><p>${markUntraced(inline(ins.why), nc.untraced)}</p></div>
          <div><h3>Talking points</h3><ul>${(ins.talkingPoints || []).map(p => `<li>${markUntraced(inline(p), nc.untraced)}</li>`).join("")}</ul></div></div>
        <div><h3 class="sr">Next step</h3><p><strong>Next step:</strong> <span class="nextstep">${markUntraced(inline(ins.nextStep), nc.untraced)}</span></p></div>
        <div class="actions">
          <button type="button" class="btn btn-sm btn-primary" data-act="accept">Accept: create opportunity</button>
          <button type="button" class="btn btn-sm" data-act="change">Change next step</button>
          <button type="button" class="btn btn-sm btn-quiet" data-act="dismiss">Dismiss</button>
          <span class="sp"></span>${checkBadge(nc)}${feedback(c.id)}
        </div></div>`;
      box.appendChild(card);
    });
    const rest = scan.ranked.length - top.length;
    const note = document.createElement("p"); note.className = "muted";
    note.innerHTML = `${modeTag(mode)} A1 found ${plural(scan.signals.length, "signal")} across ${plural(scan.ranked.length, "client")}; the top 5 are shown${rest > 0 ? `, ${rest} more on the full list` : ""}. Nothing here changes a client record until you accept.`;
    box.appendChild(note);
    changed();
  }
  $("#listResults").addEventListener("click", e => {
    const b = e.target.closest("button[data-act]"); if (!b) return;
    const card = b.closest(".card"); const c = A.findClient(card.dataset.client); const acts = card.querySelector(".actions");
    if (b.dataset.act === "accept") {
      card.classList.add("accepted"); A.measures.opportunities++; A.measures.used++;
      A.log("RM", "Accepted an insight", `${c.name}: opportunity created, tagged AI-sourced`, "K1, K2");
      acts.innerHTML = `<span class="done-note">Opportunity created in the CRM (sample), tagged "AI-sourced", so results can be counted.</span>`;
    } else if (b.dataset.act === "change") {
      const span = card.querySelector(".nextstep");
      if (span.isContentEditable) { span.contentEditable = "false"; b.textContent = "Change next step"; A.measures.changed++; A.log("RM", "Changed the next step", c.name, "K1"); }
      else { span.contentEditable = "true"; span.focus(); b.textContent = "Done changing"; }
    } else if (b.dataset.act === "dismiss") {
      acts.innerHTML = `<span class="muted">Why dismiss?</span>` + ["Not now", "Not relevant", "Already handled"].map(r => `<button type="button" class="btn btn-sm" data-act="reason" data-r="${r}">${r}</button>`).join("");
    } else if (b.dataset.act === "reason") {
      card.classList.add("dismissed"); A.measures.rejected++;
      A.log("RM", "Dismissed an insight", `${c.name}: ${b.dataset.r}`, "K1");
      acts.innerHTML = `<span class="muted">Dismissed: ${esc(b.dataset.r)}. The reason helps tune A1's rules.</span>`;
    }
    changed();
  });

  async function runList(mode) {
    const trace = $("#listTrace"), state = $("#listState");
    trace.innerHTML = ""; $("#listResults").innerHTML = '<div class="skeleton"></div><div class="skeleton"></div>';
    const scan = A.runA1(); A.measures.runs++;
    traceStep(trace, "A1", `Checked ${scan.scanned} clients against ${A.RULES.length} rules: ${plural(scan.signals.length, "signal")}`);
    await wait(mode === "instant" ? 0 : 350);
    traceStep(trace, "M1", `Rates context: 10-year Treasury ${M.latest.yield}% (${M.latest.month}), up ${M.change6m} points in 6 months · Fed H.15, copy fetched ${M.fetched}`);
    await wait(mode === "instant" ? 0 : 350);
    const top = scan.ranked.slice(0, 5);
    if (mode !== "live") {
      const s = traceStep(trace, "A2", "Writing 5 insights", mode === "instant" ? "" : "run");
      if (mode !== "instant") await wait(900);
      s.classList.remove("run"); s.lastChild.textContent = "Wrote 5 insights (recorded run)";
      A.log("A2 Insight writer", "Wrote insights (recorded run)", "5 clients", "K7");
      renderList(R.insights, scan, "replay"); state.innerHTML = ""; return;
    }
    const s = traceStep(trace, "A2", "Writing 5 insights live on Claude…", "run");
    state.textContent = "Claude is writing. The first live run asks your permission.";
    listCtl = new AbortController(); $("#stopList").hidden = false; $("#runList").disabled = true;
    const t0 = Date.now();
    try {
      const { prompt } = A.a2Prompt(top);
      const out = await AI.sample.json(prompt, { modelTier: "quick", signal: listCtl.signal });
      if (!Array.isArray(out) || !out.length) throw { code: "invalid_json" };
      A.measures.liveRuns++;
      s.classList.remove("run"); s.lastChild.textContent = `Wrote ${out.length} insights live in ${((Date.now() - t0) / 1000).toFixed(1)} s`;
      A.log("A2 Insight writer", "Wrote insights (live)", `${out.length} clients`, "K7, K8");
      renderList(out, scan, "live"); state.textContent = "";
    } catch (e) {
      s.classList.remove("run"); s.lastChild.textContent = "Stopped";
      state.textContent = A.errText(e) + " Showing the recorded run."; dropToReplay(e);
      A.log("A2 Insight writer", "Live run did not finish", e && e.code, "K25");
      renderList(R.insights, scan, "replay");
    } finally { $("#stopList").hidden = true; setMode(); }
  }
  $("#runList").addEventListener("click", () => runList("live"));
  $("#replayList").addEventListener("click", () => runList("replay"));
  $("#stopList").addEventListener("click", () => listCtl && listCtl.abort());

  // ---------- B2 Pre-meeting client brief ----------
  let briefClient = "C101", briefCtl = null;
  function renderMeetings() {
    const box = $("#meetings");
    const ms = A.myClients().filter(c => c.nextMeeting).sort((a, b) => a.nextMeeting.date.localeCompare(b.nextMeeting.date));
    box.innerHTML = ms.map(c => `<button type="button" class="meet" role="radio" aria-checked="${c.id === briefClient}" data-client="${c.id}"><strong>${esc(c.name)}</strong><small>${fmtShort(c.nextMeeting.date)} · ${c.nextMeeting.time} · ${esc(c.nextMeeting.purpose)}</small></button>`).join("");
  }
  $("#meetings").addEventListener("click", e => {
    const b = e.target.closest(".meet"); if (!b) return;
    briefClient = b.dataset.client; renderMeetings();
    if (briefClient === "C101") replayBrief(true);
    else { $("#briefSteps").innerHTML = ""; $("#briefDoc").innerHTML = `<p class="muted">${liveOK ? "Press <strong>Run A3 live</strong> to draft this client's brief." : "The recorded run covers Lakeshore Precision Tooling. Open this page in claude.ai to brief this client live."}</p>`; }
  });
  function addToolStep(list, tool, input) {
    const li = document.createElement("li");
    li.innerHTML = `Called <code>${esc(tool)}</code>(${esc(Object.values(input || {}).join(", "))}) <span class="st">…</span>`;
    list.appendChild(li);
    return {
      done(out) { li.querySelector(".st").outerHTML = `<span class="st-ok">done</span><details><summary>What it returned</summary><pre>${esc(JSON.stringify(out, null, 1))}</pre></details>`; },
      fail(msg) { li.querySelector(".st").outerHTML = `<span class="st-bad">refused: ${esc(msg)}</span>`; }
    };
  }
  function finishBrief(text, c, mode) {
    const inputs = { record: A.clientRecord(c.id), activity: c.activity, market: A.marketFacts(), signals: A.myClients().length && A.RULES.filter(r => r.test(c)).map(r => r.facts(c)) };
    const nc = A.numberCheck(text, inputs);
    A.measures.outputsShown++;
    $("#briefDoc").innerHTML = `<div class="docbar">${modeTag(mode)}${checkBadge(nc)}<span class="sp"></span><button type="button" class="btn btn-sm" id="useBrief">Use this brief</button>${feedback("brief " + c.id)}</div>
      <p class="muted">For ${esc(B.rm.name)} · ${esc(c.name)} · ${fmtDate(c.nextMeeting.date)}, ${c.nextMeeting.time} · ${esc(c.nextMeeting.where)}</p>${markUntraced(md(text), nc.untraced)}`;
    $("#useBrief").addEventListener("click", ev => { A.measures.used++; A.log("RM", "Used the brief", c.name, "K1"); ev.target.outerHTML = `<span class="done-note">Marked as used</span>`; changed(); });
    changed();
  }
  const DRAFTING = `<p class="hint">Still drafting. The number check (K7) runs as soon as the draft is finished, before you can use it.</p>`;
  async function replayBrief(instant) {
    const c = A.findClient("C101"); briefClient = "C101"; renderMeetings();
    const list = $("#briefSteps"); list.innerHTML = ""; $("#briefDoc").innerHTML = `<p class="muted">Drafting…</p>`;
    const tools = A.makeTools(({ tool, input }) => addToolStep(list, tool, input));
    for (const st of R.briefSteps) { await tools.find(t => t.name === st.tool).execute(st.input, {}); if (!instant) await wait(450); }
    if (!instant) {
      const words = R.brief.split(/(\s+)/); let shown = "";
      for (let i = 0; i < words.length; i += 12) { shown += words.slice(i, i + 12).join(""); $("#briefDoc").innerHTML = DRAFTING + md(shown); await wait(40); }
    }
    A.log("A3 Prep and follow-up", "Drafted the brief (recorded run)", c.name, "K7");
    finishBrief(R.brief, c, "replay");
  }
  async function runBrief() {
    const c = A.findClient(briefClient); const list = $("#briefSteps"), doc = $("#briefDoc"), state = $("#briefState");
    list.innerHTML = ""; doc.innerHTML = `<p class="muted">Thinking… (the first live run asks your permission)</p>`;
    briefCtl = new AbortController(); $("#stopBrief").hidden = false; $("#runBrief").disabled = true; A.measures.runs++;
    const t0 = Date.now();
    try {
      let result;
      if (AI.tools) {
        const tools = A.makeTools(({ tool, input }) => addToolStep(list, tool, input));
        result = await AI.sample(A.a3BriefPrompt(c, true), { tools, modelTier: "quick", signal: briefCtl.signal, onText: ({ text }) => { doc.innerHTML = DRAFTING + md(text); } });
      } else {
        const li = document.createElement("li"); li.textContent = "Read the client record, open insights, recent activity and market data (this view can't run page tools, so they're given in the prompt)"; list.appendChild(li);
        result = await AI.sample(A.a3BriefPrompt(c, false), { modelTier: "quick", signal: briefCtl.signal, onText: ({ text }) => { doc.innerHTML = DRAFTING + md(text); } });
      }
      const text = result.text.slice(result.text.indexOf("##") >= 0 ? result.text.indexOf("##") : 0);
      A.measures.liveRuns++;
      A.log("A3 Prep and follow-up", "Drafted the brief (live)", `${c.name}, ${((Date.now() - t0) / 1000).toFixed(1)} s`, "K7, K8");
      finishBrief(text, c, "live"); state.textContent = "";
    } catch (e) {
      state.textContent = A.errText(e); dropToReplay(e);
      A.log("A3 Prep and follow-up", "Live run did not finish", e && e.code, "K25");
      if (c.id === "C101") { state.textContent += " Showing the recorded run."; replayBrief(true); } else doc.innerHTML = `<p class="muted">${esc(e && e.text || "")}</p>`;
    } finally { $("#stopBrief").hidden = true; setMode(); }
  }
  $("#runBrief").addEventListener("click", runBrief);
  $("#replayBrief").addEventListener("click", () => replayBrief(false));
  $("#stopBrief").addEventListener("click", () => briefCtl && briefCtl.abort());

  // ---------- B3 and B4 Meeting follow-up ----------
  let followCtl = null, followOriginalNote = "";
  $("#notes").value = B.meetingNotes.text;
  function renderFollow(d, mode) {
    const c = A.findClient(B.meetingNotes.clientId);
    const { data } = A.a3FollowupPrompt(c, { ...B.meetingNotes, text: $("#notes").value });
    const nc = A.numberCheck([...(d.recap || []), d.email && d.email.body, d.crmNote].join(" "), data);
    A.measures.outputsShown++;
    followOriginalNote = d.crmNote || "";
    const checks = (JSON.stringify(d).match(/\[CHECK/g) || []).length;
    $("#followOut").innerHTML = `<div class="out">
      <div class="docbar">${modeTag(mode)}<span class="status" id="draftStatus">Draft: not saved or sent</span>${checkBadge(nc)}<span class="sp"></span>${feedback("follow-up " + c.id)}</div>
      ${checks ? `<p class="hint">${plural(checks, "item")} marked CHECK: A3 didn't guess where your notes were unclear (K25).</p>` : ""}
      <div><h3>Recap</h3><ul class="plain">${(d.recap || []).map(r => `<li>${inline(r)}</li>`).join("")}</ul></div>
      <div><h3>Follow-up email · you send it yourself</h3>
        <label class="sr" for="emailSubject">Email subject</label><input type="text" id="emailSubject" value="${esc(d.email && d.email.subject)}">
        <label class="sr" for="emailBody">Email body</label><textarea id="emailBody" rows="11">${esc(d.email && d.email.body)}</textarea>
        <div class="runbar"><button type="button" class="btn btn-sm" id="copyEmail">Copy the email</button><span class="runstate" id="copyState"></span></div></div>
      <div><h3>Call note for the CRM (B4)</h3><label class="sr" for="crmNote">Call note</label><textarea id="crmNote" rows="6">${esc(d.crmNote)}</textarea>
        <div class="runbar"><button type="button" class="btn btn-sm btn-primary" id="approveNote">Approve and save the call note</button><span class="runstate" id="approveState"></span></div></div>
      <div><h3>Next steps</h3><div class="tw"><table class="steps-table"><thead><tr><th>Owner</th><th>What</th><th>By when</th></tr></thead><tbody>
        ${(d.nextSteps || []).map(s => `<tr><td>${esc(s.owner)}</td><td>${inline(s.item)}</td><td>${inline(s.due)}</td></tr>`).join("")}</tbody></table></div></div>
      ${(d.flags || []).length ? `<div><h3>Things to know</h3><ul class="flags">${d.flags.map(f => `<li>${inline(f)}</li>`).join("")}</ul></div>` : ""}
    </div>`;
    $("#copyEmail").addEventListener("click", () => {
      const txt = $("#emailSubject").value + "\n\n" + $("#emailBody").value;
      const ok = () => { $("#copyState").textContent = "Copied. Send it yourself from your email: the assistant never sends email (K1)."; A.log("RM", "Copied the email to send", c.name, "K1"); };
      try { navigator.clipboard.writeText(txt).then(ok, () => { $("#emailBody").select(); $("#copyState").textContent = "Select-all done: press Ctrl+C or Cmd+C to copy. You send it yourself (K1)."; }); }
      catch (e) { $("#emailBody").select(); $("#copyState").textContent = "Press Ctrl+C or Cmd+C to copy. You send it yourself (K1)."; }
    });
    $("#approveNote").addEventListener("click", () => {
      const note = $("#crmNote").value; const left = (note.match(/\[CHECK/g) || []).length;
      if (left) { $("#approveState").innerHTML = `<span class="hint">Confirm the ${plural(left, "item")} marked CHECK in the note first: you're the one who knows the answer.</span>`; return; }
      if (note.trim() !== followOriginalNote.trim()) A.measures.changed++;
      A.measures.approvals++; A.measures.used++;
      A.log("RM", "Approved the call note", `${c.name}: saved to the CRM (sample), tagged AI-drafted`, "K2");
      $("#draftStatus").textContent = "Call note saved · email not sent"; $("#draftStatus").classList.add("saved");
      $("#approveState").innerHTML = `<span class="done-note">Saved to the CRM (sample), tagged "AI-drafted". Only now, after your click (K2).</span>`;
      $("#approveNote").disabled = true; $("#crmNote").readOnly = true; changed();
    });
    changed();
  }
  async function runFollow(mode) {
    const c = A.findClient(B.meetingNotes.clientId), state = $("#followState");
    A.measures.runs++;
    if (mode !== "live") {
      if (mode !== "instant") { $("#followOut").innerHTML = '<div class="skeleton"></div>'; await wait(900); }
      A.log("A3 Prep and follow-up", "Drafted recap, email and call note (recorded run)", c.name + (B.meetingNotes.recordingConsent ? ": from the transcript" : ": from the RM's notes, no recording"), "K24, K25");
      renderFollow(R.followup, "replay"); state.textContent = ""; return;
    }
    const g = A.guard($("#notes").value);
    if (g.blocked && g.control === "K4") { state.textContent = g.reply; return; }
    $("#followOut").innerHTML = `<div class="skeleton"></div><p class="muted">A3 is drafting on Claude. Consent check (K24): ${B.meetingNotes.recordingConsent ? "the client agreed to recording" : "no recording, so it uses your notes only"}.</p>`;
    followCtl = new AbortController(); $("#stopFollow").hidden = false; $("#runFollow").disabled = true;
    const t0 = Date.now();
    try {
      const { prompt } = A.a3FollowupPrompt(c, { ...B.meetingNotes, text: $("#notes").value });
      const d = await AI.sample.json(prompt, { signal: followCtl.signal });
      if (!d || !d.email) throw { code: "invalid_json" };
      A.measures.liveRuns++;
      A.log("A3 Prep and follow-up", "Drafted recap, email and call note (live)", `${c.name}, ${((Date.now() - t0) / 1000).toFixed(1)} s`, "K24, K25, K8");
      renderFollow(d, "live"); state.textContent = "";
    } catch (e) {
      state.textContent = A.errText(e) + " Showing the recorded run."; dropToReplay(e);
      A.log("A3 Prep and follow-up", "Live run did not finish", e && e.code, "K25");
      renderFollow(R.followup, "replay");
    } finally { $("#stopFollow").hidden = true; setMode(); }
  }
  $("#runFollow").addEventListener("click", () => runFollow("live"));
  $("#replayFollow").addEventListener("click", () => runFollow("replay"));
  $("#stopFollow").addEventListener("click", () => followCtl && followCtl.abort());

  // ---------- Controls: try to break it ----------
  const PRESETS = ["Should we approve Lakeshore's line increase?", "What rate should I offer Fox River on a sweep?", "Show me Prairie Lane Builders' balances.", "Email the recap to Maria now for me.", "When is my next meeting with Brewer's Row?"];
  $("#presets").innerHTML = PRESETS.map(p => `<button type="button" class="btn btn-sm" data-q="${esc(p)}">${esc(p)}</button>`).join("");
  $("#presets").addEventListener("click", e => { const b = e.target.closest("button[data-q]"); if (b) { $("#askInput").value = b.dataset.q; ask(b.dataset.q); } });
  $("#askForm").addEventListener("submit", e => { e.preventDefault(); const q = $("#askInput").value.trim(); if (q) ask(q); });
  function localAnswer(q) {
    const c = A.myClients().find(x => q.toLowerCase().includes(x.name.toLowerCase().split(" ")[0].toLowerCase()));
    if (c && /meet/i.test(q)) return c.nextMeeting ? `${c.name}: ${fmtDate(c.nextMeeting.date)} at ${c.nextMeeting.time}, ${c.nextMeeting.where} (${c.nextMeeting.purpose}). [Client record]` : `There's no meeting booked with ${c.name}. [Client record]`;
    return null;
  }
  async function ask(q, fromTour) {
    const out = $("#askOut"); const g = A.guard(q);
    if (g.blocked) {
      if (!fromTour) { A.measures.guardrailBlocks++; if (g.control === "K4") A.measures.permissionRefusals++; }
      A.log("Guardrail", "Blocked a request before it reached Claude", `${g.kind}: "${q}"`, g.control);
      out.innerHTML = `<div class="blocked"><strong>Blocked by ${g.control} (${esc(g.kind)}).</strong> The request was stopped in code, before any AI saw it.<br>${esc(g.reply)}</div>`;
      changed(); return;
    }
    if (!liveOK) {
      const a = localAnswer(q);
      out.innerHTML = a ? `<div class="allowed">${inline(a)}<br><span class="muted">Answered from the record by the page (live AI isn't available in this view).</span></div>` : `<div class="allowed">This request passed the guardrails. Live AI isn't available in this view, so there's no answer here; inside claude.ai, Claude answers from your own book only, or says it can't help.</div>`;
      A.log("Guardrail", "Passed the guardrails", q, "K8"); changed(); return;
    }
    out.innerHTML = `<div class="allowed">Passed the guardrails in code. Asking Claude…</div>`;
    try {
      const { text } = await AI.sample(A.guardPrompt(q), { modelTier: "quick", onText: ({ text }) => { out.innerHTML = `<div class="allowed">${inline(text)}</div>`; } });
      const refused = /^I can't help/i.test(text.trim());
      if (refused) { A.measures.guardrailBlocks++; A.log("RM Assistant", "Declined a request (Claude's own check)", q, "K8, K25"); }
      const nc = refused ? null : A.numberCheck(text, A.myClients().map(c => A.clientRecord(c.id)));
      if (!refused) A.log("RM Assistant", "Answered from the RM's book", q, "K4, K7");
      out.innerHTML = `<div class="${refused ? "blocked" : "allowed"}">${nc ? markUntraced(inline(text), nc.untraced) : inline(text)}<br><span class="muted">${refused ? "Declined by Claude, the second line of defence after the guardrails in code." : "Live answer on Claude, from your own clients only."}</span> ${nc ? checkBadge(nc) : ""}</div>`;
    } catch (e) { out.innerHTML = `<div class="allowed">${esc(A.errText(e))}</div>`; dropToReplay(e); }
    changed();
  }

  // ---------- Controls, rules and the audit log ----------
  const CONTROLS = [
    ["K1", "A person decides", "You accept, change or dismiss each insight, and you send every email yourself."],
    ["K2", "Read-only unless approved", "The call note reaches the CRM only after you click approve."],
    ["K3", "AI drafts or flags; a named credit officer decides", "Anything about credit, like equipment financing, goes to the portfolio manager."],
    ["K4", "Users see only what they're allowed to see", "A1 scans only Jordan's 12 clients; A3's tools refuse another RM's clients."],
    ["K7", "Every answer shows its source", "A source on every fact, and every number checked against the agent's data as soon as a draft is finished, before you can use it."],
    ["K8", "Guardrails", "Credit decisions, prices and contacting clients are blocked in code before Claude is asked."],
    ["K12", "An audit log", "Every agent action and every approval is logged below."],
    ["K22", "Simple rules first, and the AI explains", "A1 is plain rules the business owns; AI only explains what fired."],
    ["K24", "Consent before recording", "A3 reads the meeting's consent flag: no consent, no transcript, so here it drafts from your notes."],
    ["K25", "Agents stop rather than guess", "Unclear dates and owners come back marked CHECK for you to confirm."]
  ];
  $("#ctlGrid").innerHTML = CONTROLS.map(([k, n, w]) => `<div class="ctl-card"><span><span class="ctl">${k}</span> <strong>${esc(n)}</strong></span><span class="where">${esc(w)}</span></div>`).join("");
  $("#ruleTable tbody").innerHTML = A.RULES.map(r => `<tr><td><span class="rule">${r.id}</span> ${esc(r.name)}</td><td>${esc(r.plain)}</td><td class="num">${r.score({ checksPerMonth: 0, branchDepositsPerMonth: 0, wiresElsewherePerMonth: 0, balances: [1, 1, 1, 1, 1, 1], nonInterestShare: 0 })}</td></tr>`).join("")
    + `<tr><td><span class="rule">M1</span> ${esc(A.MARKET_RULE.name)}</td><td>${esc(A.MARKET_RULE.plain)}</td><td class="num">+${A.MARKET_RULE.bonus}</td></tr>`;
  function renderAudit() {
    const tb = $("#auditTable tbody");
    tb.innerHTML = A.audit.length ? A.audit.map(a => `<tr><td>${a.time}</td><td>${esc(a.agent)}</td><td>${esc(a.action)}</td><td>${esc(a.detail)}</td><td>${esc(a.control)}</td></tr>`).join("")
      : `<tr><td colspan="5" class="empty">Nothing yet. Run an agent and its actions appear here.</td></tr>`;
  }
  A.onAudit(renderAudit);

  // ---------- Product manager view ----------
  function renderMeasures() {
    const m = A.measures; const pct = m.numbersChecked ? Math.round(m.numbersTraced / m.numbersChecked * 100) + "%" : "–";
    const cards = [
      ["Usage", m.used + " of " + m.outputsShown, "outputs used, of those shown", [`${m.runs} agent runs, ${m.liveRuns} live on Claude`]],
      ["Quality", pct, "of numbers traced to the data (K7)", [`${m.thumbsUp} marked useful, ${m.thumbsDown} not useful`, "Accuracy on the test set: [X] until set"]],
      ["Business impact", String(m.opportunities), "opportunities created, tagged AI-sourced", ["Pipeline and wins: [X] until the pilot", "Against a comparison group of RMs"]],
      ["Adoption", m.liveRuns ? "Active" : "Not yet", "this RM, this session", ["Weekly active RMs: [X] in the pilot", "Repeat use week after week"]],
      ["Risk and controls", String(m.guardrailBlocks), "requests blocked by guardrails", [`${m.permissionRefusals} refused outside the RM's book (K4)`, `${m.changed} drafts changed by the RM (overrides)`, `${m.approvals} approved before saving (K2)`]]
    ];
    $("#measureGrid").innerHTML = cards.map(([k, big, what, list]) => `<div class="mcard"><span class="kind">${k}</span><span class="big">${esc(big)}</span><span class="what">${esc(what)}</span><ul>${list.map(l => `<li>${esc(l)}</li>`).join("")}</ul></div>`).join("");
  }

  // ---------- How it's built ----------
  $("#marketLine").innerHTML = `<strong>Outside data:</strong> ${esc(M.name)}, ${esc(M.publisher)}, monthly from ${M.series[0].month} to ${M.latest.month}, public domain, through the datahub.io copy on GitHub. Saved copy fetched ${M.fetched}; latest value ${M.latest.yield}%.`;

  // ---------- Start ----------
  $("#consent").innerHTML = `<span class="ctl">K24</span><span>Recording: ${B.meetingNotes.recordingConsent ? "<strong>the client agreed</strong>. In the real product A3 would use the Teams transcript; this prototype has notes only." : "<strong>the client didn't agree</strong>, so A3 drafts from your own notes."}</span>`;
  renderMeetings(); renderAudit(); renderMeasures();
  runList("instant"); replayBrief(true); runFollow("instant");
  A.measures.runs = 0; // the filled-in recorded runs at load don't count as runs
  AI.ready.then(setMode);
  setMode();
  window.APP = { show, runList, replayBrief, runFollow, ask };
})();
