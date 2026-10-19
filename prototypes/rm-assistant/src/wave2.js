// Version 4: the Today home screen, and two wave 2 capabilities shown as a preview:
// Early warning (workflow B5: clients who may be drifting away) and Refer to treasury
// (workflow B6: referral prompts). Both use plain rules in code, like the Signal finder (A1),
// and explain each flag from the numbers behind it. The RM decides every action (K1), each
// action is logged (K12), and nothing reaches a client or another team from here: it's sample data.
(function () {
  const B = window.BOOK, A = window.AGENTS;
  const $ = s => document.querySelector(s);
  const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const day = iso => new Date(iso + "T12:00:00");
  const fmtShort = iso => day(iso).toLocaleDateString("en-US", { month: "short", day: "numeric" });
  const fmtDay = iso => day(iso).toLocaleDateString("en-US", { weekday: "long", month: "short", day: "numeric" });
  const monthName = ym => new Date(ym + "-15T12:00:00").toLocaleDateString("en-US", { month: "long" });
  const fmtTime = hm => { const [h, m] = hm.split(":").map(Number); return `${h % 12 || 12}:${String(m).padStart(2, "0")} ${h < 12 ? "a.m." : "p.m."}`; };
  const daysSince = iso => Math.round((day(B.today) - day(iso)) / 864e5);
  const peak = c => Math.max(...c.balances);
  const money = v => v >= 1e6 ? A.fmtM(v) : "$" + Math.round(v / 1000) + "K";
  const m = A.measures; m.warningsActed = m.warningsActed || 0; m.referrals = m.referrals || 0;

  // ---------- Early warning rules (B5): owned by the business, explainable, never a credit signal ----------
  const WARN = [
    { id: "E1", name: "Falling balances", plain: "Balances down 25% or more from their 6-month high, for a business that isn't seasonal.",
      test: c => !c.seasonal && c.balances[5] <= peak(c) * 0.75,
      why: c => `Balances fell from ${money(peak(c))} in ${monthName(B.months[c.balances.indexOf(peak(c))])} to ${money(c.balances[5])} in September, down ${Math.round((1 - c.balances[5] / peak(c)) * 100)}%.` },
    { id: "E2", name: "Payroll moved out", plain: "Payroll now runs through another bank.",
      test: c => !!c.payrollElsewhereSince,
      why: c => `Payroll has run through another bank since ${monthName(c.payrollElsewhereSince)}.` },
    { id: "E3", name: "Gone quiet", plain: "No contact with the client in 90 days or more.",
      test: c => daysSince(c.lastContact) >= 90,
      why: c => `No contact in ${daysSince(c.lastContact)} days; the last was on ${fmtShort(c.lastContact)}.` }
  ];
  // ---------- Referral rules (B6): a need the treasury team serves, from the Signal finder's own rules ----------
  const REFER = [
    { rule: "T4", need: "Payments and payroll", say: c => `about ${c.wiresElsewherePerMonth} wires and payment batches a month go out from another bank's account` },
    { rule: "T2", need: "Fraud protection", say: c => `about ${c.checksPerMonth} checks a month, with no positive pay` },
    { rule: "T5", need: "Card acceptance", say: () => `they take payments from consumers and have no merchant services with us` }
  ];
  const warnings = () => A.myClients().map(c => ({ c, hits: WARN.filter(r => r.test(c)) })).filter(x => x.hits.length).sort((a, b) => b.hits.length - a.hits.length);
  const referrals = () => A.myClients().map(c => ({ c, r: REFER.find(r => A.RULES.find(x => x.id === r.rule).test(c)) })).filter(x => x.r);
  const firstName = c => (c.contacts[0] || { name: "the client" }).name.split(" ")[0];
  const spec = B.rm.treasurySpecialist.split(" (")[0];

  // ---------- Early warning screen ----------
  const warnDone = {};
  function renderWarnings() {
    const list = warnings();
    $("#warnSummary").innerHTML = `<span class="big">${list.length}</span><span>${list.length === 1 ? "client" : "clients"} may be drifting away · ${WARN.length} rules checked across ${A.myClients().length} clients · not a credit signal</span>`;
    $("#warnList").innerHTML = list.map(({ c, hits }) => {
      const d = warnDone[c.id]; const lvl = hits.length >= 2 ? "high" : "watch";
      return `<article class="wcard ${lvl}${d ? " done" : ""}" data-client="${c.id}">
        <div class="whead"><h3>${esc(c.name)}</h3><span class="wlvl">${lvl === "high" ? "Check in this week" : "Keep an eye on"}</span></div>
        <p class="wmeta">${esc(c.industry)} · ${esc(c.city)} · with us since ${c.since}</p>
        ${spark(c)}
        <ul class="wwhy">${hits.map(h => `<li><span class="rule" title="${esc(h.plain)}">${esc(h.name)}</span> ${esc(h.why(c))} <span class="src">Client record</span></li>`).join("")}</ul>
        <div class="wact">${d ? `<span class="done-note">${esc(d)}</span>` : `<button type="button" class="btn btn-primary" data-w="call">Plan a call with ${esc(firstName(c))}</button><button type="button" class="btn btn-quiet" data-w="dismiss">Not a concern</button>`}</div>
      </article>`;
    }).join("") || `<p class="muted">No client is showing a warning sign this week.</p>`;
  }
  function spark(c) {
    const w = 220, h = 46, hi = peak(c), lo = Math.min(...c.balances) * 0.9;
    const pts = c.balances.map((v, i) => `${(i / 5 * (w - 8) + 4).toFixed(1)},${(h - 6 - (v - lo) / (hi - lo || 1) * (h - 14)).toFixed(1)}`).join(" ");
    const last = pts.split(" ").pop().split(",");
    return `<figure class="spark"><svg viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" role="img" aria-label="Balances from April to September: ${c.balances.map(money).join(", ")}"><polyline points="${pts}" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/><circle cx="${last[0]}" cy="${last[1]}" r="4" fill="currentColor"/></svg><figcaption>Balances, April to September</figcaption></figure>`;
  }
  $("#warnList").addEventListener("click", e => {
    const b = e.target.closest("button[data-w]"); if (!b) return;
    const c = A.findClient(b.closest(".wcard").dataset.client);
    if (b.dataset.w === "call") { warnDone[c.id] = `Call with ${firstName(c)} added to your plan for this week. You decide what to say.`; m.warningsActed++; A.log("RM", "Planned a check-in call after an early warning", c.name, "K1"); }
    else { warnDone[c.id] = "Marked as not a concern. The reason goes to the product manager."; m.rejected++; A.log("RM", "Dismissed an early warning", c.name, "K1"); }
    renderWarnings(); renderToday(); if (window.APP && window.APP.refreshMeasures) window.APP.refreshMeasures();
  });

  // ---------- Refer to treasury screen ----------
  const refState = {};   // clientId -> "sent" | "accepted" | "dismissed"
  const draft = (c, r) => `Hi ${spec.split(" ")[0]},\n\nI'd like to bring you in on ${c.name} (${c.industry}, ${c.city}). Today ${r.say(c)}. Could we look at ${r.need.toLowerCase()} together? ${firstName(c)} is the contact.\n\nJordan`;
  function renderReferrals() {
    const list = referrals();
    $("#refSummary").innerHTML = `<span class="big">${list.length}</span><span>clients with a need ${esc(spec)}'s treasury team serves · the RM decides and sends each referral</span>`;
    $("#refList").innerHTML = list.map(({ c, r }) => {
      const st = refState[c.id];
      const stage = ["Spotted", "Referred", "Accepted"]; const at = st === "accepted" ? 2 : st === "sent" ? 1 : 0;
      return `<article class="rcard${st === "dismissed" ? " dismissed" : ""}" data-client="${c.id}" data-rule="${r.rule}">
        <div class="whead"><h3>${esc(c.name)}</h3><span class="rneed">${esc(r.need)}</span></div>
        <p class="wmeta">Why: ${esc(r.say(c))}. <span class="src">Insight: ${esc(A.RULES.find(x => x.id === r.rule).name.toLowerCase())}</span></p>
        <ol class="stages" aria-label="Referral progress">${stage.map((s, i) => `<li class="${i <= at && st !== "dismissed" ? "on" : ""}">${s}</li>`).join("")}</ol>
        ${st === "dismissed" ? `<p class="muted">Dismissed. The reason goes to the product manager.</p>` : st ? `<p class="done-note">${st === "accepted" ? `${esc(spec)} accepted it (sample). The referral is tracked to close in the CRM.` : `Referral created in the CRM (sample) and ${esc(spec)} notified.`}</p>`
        : `<label class="sr" for="ref-${c.id}">Referral note to ${esc(spec)}</label><textarea id="ref-${c.id}" class="refnote" rows="6">${esc(draft(c, r))}</textarea>
        <div class="wact"><button type="button" class="btn btn-primary" data-r="send">Send the referral to ${esc(spec.split(" ")[0])}</button><button type="button" class="btn btn-quiet" data-r="dismiss">Not now</button></div>`}
      </article>`;
    }).join("");
  }
  $("#refList").addEventListener("click", e => {
    const b = e.target.closest("button[data-r]"); if (!b) return;
    const card = b.closest(".rcard"); const c = A.findClient(card.dataset.client);
    if (b.dataset.r === "send") {
      refState[c.id] = "sent"; m.referrals++; m.used.add(`ref:${c.id}`);
      A.log("RM", `Sent a referral to ${spec} (sample: nothing leaves the page)`, c.name, "K1");
      setTimeout(() => { if (refState[c.id] === "sent") { refState[c.id] = "accepted"; A.log("Treasury team (sample)", "Accepted the referral", c.name, ""); renderReferrals(); renderToday(); } }, 1600);
    } else { refState[c.id] = "dismissed"; m.rejected++; A.log("RM", "Dismissed a referral prompt", c.name, "K1"); }
    renderReferrals(); renderToday(); if (window.APP && window.APP.refreshMeasures) window.APP.refreshMeasures();
  });

  // ---------- Today: the RM's day on one screen ----------
  function renderToday() {
    const hour = 8;   // the sample day starts at 8 a.m.
    $("#todayHello").textContent = (hour < 12 ? "Good morning" : "Good afternoon") + ", " + B.rm.name.split(" ")[0];
    const meets = A.myClients().filter(c => c.nextMeeting && (day(c.nextMeeting.date) - day(B.today)) / 864e5 <= 6).map(c => ({ c, mt: c.nextMeeting })).sort((a, b) => (a.mt.date + a.mt.time).localeCompare(b.mt.date + b.mt.time));
    const listLeft = document.querySelectorAll("#listResults .card:not(.accepted):not(.dismissed)").length;
    const followWaiting = /not saved/i.test(($("#draftStatus") || {}).textContent || "");
    const warn = warnings().filter(x => !warnDone[x.c.id]).length;
    const refs = referrals().filter(x => !refState[x.c.id]).length;
    $("#todayStats").innerHTML = [
      [listLeft, "clients worth a call", "list"], [meets.length, meets.length === 1 ? "meeting this week" : "meetings this week", "brief"],
      [warn, warn === 1 ? "client may be drifting" : "clients may be drifting", "warn", true], [refs, refs === 1 ? "referral to make" : "referrals to make", "refer", true]
    ].map(([n, t, s, w2]) => `<button type="button" class="tstat" data-go="${s}"><span class="big">${n}</span><span>${t}</span>${w2 ? `<span class="w2tag">Wave 2 preview</span>` : ""}</button>`).join("");   // wave 2 items carry a tag, as in the PM prototype
    $("#todayAgenda").innerHTML = meets.map(({ c, mt }) => `<li><span class="when">${esc(fmtDay(mt.date))}<br><b>${fmtTime(mt.time)}</b></span><span class="what"><b>${esc(c.name)}</b><br><small>${esc(mt.purpose)} · ${esc(mt.where)}</small></span>${c.id === "C101" ? `<button type="button" class="btn btn-sm btn-primary" data-go="brief">Brief ready</button>` : `<button type="button" class="btn btn-sm" data-go="brief">Prepare</button>`}</li>`).join("");
    const todo = [];
    if (followWaiting) todo.push(["Approve the follow-up for Lakeshore Precision Tooling", "followup", "Waiting for you"]);
    if (listLeft) todo.push([`Decide on ${listLeft} ${listLeft === 1 ? "suggestion" : "suggestions"} on the Monday list`, "list", "This week"]);
    warnings().filter(x => !warnDone[x.c.id]).forEach(x => todo.push([`Check in with ${x.c.name}`, "warn", x.hits.length >= 2 ? "This week" : "Keep an eye on", true]));
    referrals().filter(x => !refState[x.c.id]).slice(0, 2).forEach(x => todo.push([`Refer ${x.c.name} to treasury`, "refer", "When you're ready", true]));
    $("#todayTodo").innerHTML = todo.map(([t, s, w, w2]) => `<li><button type="button" data-go="${s}"><span>${esc(t)}${w2 ? ` <span class="w2tag">Wave 2 preview</span>` : ""}</span><small>${esc(w)}</small></button></li>`).join("") || `<li class="muted">All clear. Time for clients.</li>`;
  }
  $("#s-today").addEventListener("click", e => { const b = e.target.closest("[data-go]"); if (b && window.APP) window.APP.show(b.dataset.go); });

  renderWarnings(); renderReferrals(); renderToday();
  window.WAVE2 = { renderToday, renderWarnings, renderReferrals, WARN, REFER, warnings, referrals, sendFirstReferral: () => { const b = document.querySelector('#refList [data-r="send"]'); if (b) b.click(); } };
})();
