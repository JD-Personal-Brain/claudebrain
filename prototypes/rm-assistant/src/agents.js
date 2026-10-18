// The three agents, their controls and the connection to Claude.
// A1 Signal finder: simple, explainable rules in code (control K22). No AI.
// A2 Insight writer: Claude explains each A1 signal in plain English.
// A3 Prep and follow-up assistant: Claude drafts the pre-meeting brief (using page tools)
//    and the meeting follow-up. Everything it drafts waits for the RM's approval (K1, K2).
// In production (the RM plan, Appendix A): A1 runs on Snowflake Cortex, A2 on Salesforce
// Prompt Builder, A3 on Agentforce or M365 Copilot. Here all run in the page.
(function () {
  const B = window.BOOK, M = window.MARKET;
  const fmtM = v => "$" + (v / 1e6).toFixed(2).replace(/\.?0+$/, "") + "M";
  const myClients = () => B.clients.filter(c => c.rm === B.rm.id);
  const findClient = id => B.clients.find(c => c.id === id || c.name.toLowerCase() === String(id).toLowerCase());

  // ---------- The audit log (K12) ----------
  const audit = [];
  const auditListeners = [];
  function log(agent, action, detail, control) {
    const t = new Date();
    audit.unshift({ time: t.toTimeString().slice(0, 8), agent, action, detail: detail || "", control: control || "" });
    auditListeners.forEach(f => f());
  }

  // ---------- The measures, for the product manager view ----------
  const measures = { runs: 0, liveRuns: 0, outputsShown: 0, used: 0, changed: 0, rejected: 0, thumbsUp: 0, thumbsDown: 0,
    numbersChecked: 0, numbersTraced: 0, guardrailBlocks: 0, approvals: 0, opportunities: 0, permissionRefusals: 0 };

  // ---------- A1 Signal finder: the rule set the business owns ----------
  // Wave 1 covers product gaps, deposits and treasury only (the RM plan, A1).
  const RULES = [
    { id: "T1", name: "Idle operating cash", test: c => nonInterestAvg(c) >= 1000000 && !c.sweep,
      plain: "At least $1M a month on average (last 3 months) in accounts that earn no interest, and no sweep or money market.",
      score: c => 30 + Math.min(20, Math.round(nonInterestAvg(c) / 1e6 * 5)),
      facts: c => ({ nonInterestAvg3m: nonInterestAvg(c), nonInterestShare: c.nonInterestShare, sweepOrMoneyMarket: false }) },
    { id: "T2", name: "Check fraud exposure", test: c => c.checksPerMonth >= 150 && !c.positivePay,
      plain: "150 or more checks a month and no positive pay (the service that stops checks the client didn't issue).",
      score: c => 25 + Math.min(15, Math.round(c.checksPerMonth / 50)),
      facts: c => ({ checksPerMonth: c.checksPerMonth, positivePay: false }) },
    { id: "T3", name: "Branch deposit runs", test: c => c.branchDepositsPerMonth >= 8 && !c.remoteDeposit,
      plain: "8 or more branch deposit trips a month and no remote deposit (scanning checks at the office).",
      score: c => 15 + Math.min(10, Math.round(c.branchDepositsPerMonth / 2)),
      facts: c => ({ branchDepositsPerMonth: c.branchDepositsPerMonth, remoteDeposit: false }) },
    { id: "T4", name: "Payments run through another bank", test: c => c.wiresElsewherePerMonth >= 20,
      plain: "20 or more wires or payment batches a month sent from another bank's account.",
      score: c => 25 + Math.min(15, Math.round(c.wiresElsewherePerMonth / 4)),
      facts: c => ({ wiresElsewherePerMonth: c.wiresElsewherePerMonth, loansWithUs: c.loans.map(l => ({ type: l.type, amount: l.balance || l.committed })) }) },
    { id: "T5", name: "Card acceptance gap", test: c => c.consumerFacing && !c.merchant,
      plain: "A business that takes payments from consumers and has no merchant services with us.",
      score: () => 15, facts: c => ({ merchantServicesWithUs: false, consumerFacing: true }) },
    { id: "G1", name: "Growing balances", test: c => growth(c) >= 25 && !c.seasonal,
      plain: "Balances up 25% or more over 6 months, for a business that isn't seasonal. A reason to ask about plans, never a credit signal.",
      score: () => 10, facts: c => ({ balanceApril: c.balances[0], balanceSeptember: c.balances[5], growthPct: growth(c) }) }
  ];
  const MARKET_RULE = { id: "M1", name: "Rates context", plain: "When the 10-year Treasury yield is up 0.25 points or more over 6 months, idle-cash signals (T1) carry the rates context.", bonus: 5 };
  function nonInterestAvg(c) { const b = c.balances.slice(-3); return Math.round(b.reduce((a, v) => a + v, 0) / 3 * c.nonInterestShare / 10000) * 10000; }
  function growth(c) { return Math.round((c.balances[5] / c.balances[0] - 1) * 100); }
  function marketFacts() { return { series: M.name, source: M.publisher, latestMonth: M.latest.month, latestYield: M.latest.yield, sixMonthsBeforeMonth: M.sixMonthsBefore.month, sixMonthsBeforeYield: M.sixMonthsBefore.yield, change6mPoints: M.change6m, fetched: M.fetched }; }

  function runA1() {
    const clients = myClients(); // K4: A1 scans only this RM's book
    const signals = [];
    clients.forEach(c => RULES.forEach(r => { if (r.test(c)) signals.push({ clientId: c.id, client: c.name, rule: r.id, ruleName: r.name, score: r.score(c), facts: r.facts(c) }); }));
    const rates = M.change6m >= 0.25;
    signals.forEach(s => { if (s.rule === "T1" && rates) { s.score += MARKET_RULE.bonus; s.market = marketFacts(); s.alsoFired = "M1"; } });
    const byClient = {};
    signals.forEach(s => { (byClient[s.clientId] = byClient[s.clientId] || []).push(s); });
    const ranked = Object.values(byClient).map(list => {
      list.sort((a, b) => b.score - a.score);
      return { clientId: list[0].clientId, client: list[0].client, score: list.reduce((a, s) => a + s.score, 0), signals: list };
    }).sort((a, b) => b.score - a.score);
    log("A1 Signal finder", "Scanned the book", `${clients.length} clients, ${RULES.length} rules, ${signals.length} signals`, "K22, K4");
    return { scanned: clients.length, rulesChecked: clients.length * RULES.length, signals, ranked };
  }

  // ---------- K8 guardrails: checked in code before Claude is ever asked ----------
  const GUARDS = [
    { control: "K8", kind: "credit decision",
      re: /\b(approv(e|al of)\b.{0,25}\b(loan|line|credit|limit|request|increase)|decline\b.{0,25}\b(loan|line|credit|request)|underwrit\w*|credit ?worth\w*|credit (decision|limit|score|risk)|risk rating|(bigger|larger|higher|new) (line|loan|limit)|(increase|raise)\b.{0,15}\b(line|limit|loan)|line increase|extend (more )?credit|lend\w*|borrow\w*|grant\b.{0,10}\bloan|qualif\w* for)\b/i,
      reply: "I can't help with credit decisions. They belong to the portfolio manager and the credit officer, so bring in Sam Okafor (portfolio manager)." },
    { control: "K8", kind: "pricing",
      re: /(\b(what|which) (interest )?(rate|price|apr|fee)s?\b|\bapr\b|\b(lower|better|special|best|lowest|discounted) (rate|price|pricing|fee)s?\b|\b(rate|price|pricing|fee)s?\b.{0,20}\b(should|to|can) (i |we )?(offer|give|quote|charge)|\b(offer|give|quote|charge)\b.{0,25}\b(rate|price|discount|fee)s?\b|\bdiscount\b|\bfee waiver\b|\bwaive\b.{0,10}\bfees?\b|how much (should|to|can) (we |i )?charge|\bbeat\b.{0,15}\b(rate|price|offer)\b)/i,
      reply: "I don't set or suggest prices or rates. Pricing belongs to the people who own it, such as the treasury or lending team." }
  ];
  // K1: the assistant drafts; it never contacts a client itself.
  const CONTACT_NAMES = () => B.clients.filter(c => c.rm === B.rm.id).flatMap(c => c.contacts.map(p => p.name.split(" ").pop().toLowerCase()).concat(c.contacts.map(p => p.name.replace(/^Dr\. /, "").split(" ")[0].toLowerCase())));
  function contactsClient(text) {
    const t = text.toLowerCase();
    if (/\bauto-?send\b/.test(t)) return true;
    if (/^\s*(please\s+)?(draft|write|prepare|summari[sz]e)\b/.test(t)) return false;   // asking for a draft is the assistant's job
    if (!/\b(send|e-?mail|text|message|reach out to|contact|call)\b/.test(t.replace(/\bcall notes?\b/g, ""))) return false;
    return /\b(client|customer|them|him|her)\b/.test(t) || CONTACT_NAMES().some(n => new RegExp("\\b" + n + "\\b").test(t));
  }
  function guard(text) {
    for (const g of GUARDS) if (g.re.test(text)) return { blocked: true, control: g.control, kind: g.kind, reply: g.reply };
    if (contactsClient(text)) return { blocked: true, control: "K1", kind: "contacting a client", reply: "I don't contact clients. I draft; you review and send it yourself." };
    const other = B.clients.find(c => c.rm !== B.rm.id && text.toLowerCase().includes(c.name.toLowerCase().split(" ")[0].toLowerCase()));
    if (other) return { blocked: true, control: "K4", kind: "a client outside your book", reply: `${other.name} isn't in your book, so I can't show anything about it. Users see only the clients they're allowed to see.` };
    return { blocked: false };
  }

  // ---------- K7: every number in an AI output must trace to its inputs ----------
  // Allowed numbers come from numeric fields only (not ids, dates or free text); a share (0.94) also counts as a percent (94).
  function collectNumbers(obj, key, out) {
    if (obj == null) return out;
    if (typeof obj === "number") { out.push(obj); if (/share/i.test(key || "") && obj > 0 && obj < 1) out.push(Math.round(obj * 1000) / 10); }
    else if (Array.isArray(obj)) obj.forEach(v => collectNumbers(v, key, out));
    else if (typeof obj === "object") Object.entries(obj).forEach(([k, v]) => collectNumbers(v, k, out));
    return out;
  }
  const MONTHS = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec";
  function numberCheck(text, inputs) {
    const allowed = collectNumbers(inputs, "", []);
    const clean = String(text)
      .replace(/\b\d{4}-\d{2}(-\d{2})?\b/g, " ")                                            // ISO dates
      .replace(new RegExp(`\\b(${MONTHS})[a-z]*\\.? \\d{1,2}(st|nd|rd|th)?\\b`, "gi"), " ")  // month and day
      .replace(new RegExp(`\\b((${MONTHS})[a-z]*\\.?|since|in|of|for|by|from|until|before|after|Q[1-4]) (19|20)\\d{2}\\b`, "gi"), " ") // years, only where they read as dates
      .replace(/\b\d{1,2}:\d{2}\b/g, " ")                                                   // times
      .replace(/\b[A-Z]{1,2}\d{1,3}\b/g, " ")                                               // codes: K7, T1, A3, C101, Q3
      .replace(/\b\d+(st|nd|rd|th)\b/g, " ")                                                // ordinals
      .replace(/\b\d+-(year|axis|month|day|week|minute)\b/gi, " ")
      .replace(/H\.15/g, " ");
    const found = [];
    const re = /(\$)?(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)\s?(million|thousand|billion|M\b|K\b|k\b|B\b|%|percent|points?|pts?)?/g;
    let m;
    while ((m = re.exec(clean))) {
      let v = parseFloat(m[2].replace(/,/g, "")); const unit = (m[3] || "").toLowerCase();
      if (!m[1] && !unit && Number.isInteger(v) && v < 10) continue;   // small counts ("3 talking points")
      if (unit === "million" || unit === "m") v *= 1e6; else if (unit === "thousand" || unit === "k") v *= 1e3; else if (unit === "billion" || unit === "b") v *= 1e9;
      const ok = allowed.some(a => Math.abs(v - a) <= Math.max(0.051, Math.abs(a) * 0.02));
      found.push({ text: m[0].trim(), ok });
    }
    // Amounts written in words can't be traced, so they're flagged.
    (clean.match(/\b(one|two|three|four|five|six|seven|eight|nine|ten|a few|several|hundreds of|thousands of) (hundred|thousand|million|billion)\b/gi) || []).forEach(w => found.push({ text: w, ok: false }));
    const result = { total: found.length, traced: found.filter(f => f.ok).length, untraced: found.filter(f => !f.ok).map(f => f.text) };
    measures.numbersChecked += result.total; measures.numbersTraced += result.traced;
    return result;
  }

  // ---------- The connection to Claude (the artifact's "sample" capability) ----------
  const AI = { sample: null, tools: false, status: "checking" };
  AI.ready = (async () => {
    try {
      if (!window.claude || !window.claude.use) { AI.status = "absent"; return; }
      const s = await window.claude.use("sample");
      if (!s) { AI.status = "absent"; return; }
      AI.sample = s; AI.status = "available";
      try { const l = await s.limits(); AI.tools = !!(l && l.tools); } catch (e) { AI.tools = false; }
    } catch (e) { AI.status = "absent"; }
  })();
  const ERR = { not_granted: "You chose not to let this page use Claude, so it's showing recorded runs.", sampling_disabled: "Claude isn't available on this account, so the page shows recorded runs.",
    rate_limited: "Claude is busy for this account right now. Try again in a minute, or watch the recorded run.", session_expired: "Your Claude session expired. Sign in again to run live.",
    refused: "Claude declined this request.", cancelled: "Stopped." };
  const errText = e => ERR[e && e.code] || "The live run didn't finish. You can try again, or watch the recorded run.";
  const permanent = e => e && ["not_granted", "sampling_disabled", "not_declared", "capability_disabled", "capability_removed"].includes(e.code);

  // ---------- Page tools A3 may call (each one logged; K4 enforced inside) ----------
  function ownClient(id) {
    const c = findClient(id);
    if (!c) throw new Error("No client with that id.");
    if (c.rm !== B.rm.id) { measures.permissionRefusals++; log("A3 Prep and follow-up", "Refused a client outside the RM's book", c.name, "K4"); throw new Error("Not in this RM's book (control K4). Do not use this client."); }
    return c;
  }
  function clientRecord(id) {
    const c = ownClient(id);
    return { id: c.id, name: c.name, industry: c.industry, city: c.city, annualRevenue: c.revenueM * 1e6, employees: c.employees, clientSince: c.since, products: c.products,
      monthlyAverageBalances: B.months.map((mo, i) => ({ month: mo, balance: c.balances[i] })), shareInNonInterestAccounts: c.nonInterestShare,
      loans: c.loans, contacts: c.contacts, nextMeeting: c.nextMeeting, lastContact: c.lastContact };
  }
  function makeTools(onStep) {
    const wrap = (name, label, fn) => ({ name, description: label.desc, inputSchema: label.schema, execute: async input => {
      const step = onStep({ tool: name, input, status: "running" });
      try { const out = fn(input || {}); step.done(out); log("A3 Prep and follow-up", "Called " + name, JSON.stringify(input || {}), label.control); return out; }
      catch (e) { step.fail(e.message); throw e; }
    } });
    const idSchema = { type: "object", properties: { client_id: { type: "string", description: "Client id, like C101" } }, required: ["client_id"] };
    return [
      wrap("get_client_record", { desc: "Returns the CRM record for one of the RM's clients: profile, products, monthly balances, loans, contacts and next meeting. Only the RM's own clients are allowed.", schema: idSchema, control: "K4" }, i => clientRecord(String(i.client_id))),
      wrap("get_open_insights", { desc: "Returns the open A1/A2 insights (rule id, rule name, numbers) for one client.", schema: idSchema, control: "K22" }, i => { ownClient(String(i.client_id)); return runA1Silent().signals.filter(s => s.clientId === findClient(String(i.client_id)).id); }),
      wrap("get_recent_activity", { desc: "Returns the last calls, emails and meetings logged for one client, newest first.", schema: idSchema, control: "K4" }, i => ownClient(String(i.client_id)).activity),
      wrap("get_market_context", { desc: "Returns the latest US 10-year Treasury yield (monthly average) from the Federal Reserve's H.15 release, the value 6 months earlier and the change, with the date the copy was fetched.", schema: { type: "object", properties: {} }, control: "K7" }, () => marketFacts())
    ];
  }
  function runA1Silent() { const s = []; myClients().forEach(c => RULES.forEach(r => { if (r.test(c)) s.push({ clientId: c.id, rule: r.id, ruleName: r.name, facts: r.facts(c) }); })); return { signals: s }; }

  // ---------- Prompts ----------
  const RULES_TEXT = `Rules (they come from the bank's controls, so follow them exactly):
- Use only numbers that appear in the data you're given. Don't calculate new numbers or estimate revenue or profit. (control K7)
- Never recommend or hint at a credit decision, a loan approval, a rate, a price or a fee. If a client may need credit, say to bring in the portfolio manager, ${B.rm.partnerPM.split(" (")[0]}. (control K8)
- The RM decides and contacts the client. Never say that you or the assistant will contact anyone. (control K1)
- If something you need isn't in the data, say so; don't guess. (control K25)
- Plain English for a busy banker. No jargon.`;
  function a2Prompt(top) {
    const data = top.map(t => ({ clientId: t.clientId, client: t.client, signals: t.signals.map(s => ({ rule: s.rule, ruleName: s.ruleName, facts: s.facts, market: s.market })), lastActivity: (findClient(t.clientId).activity[0] || null), nextMeeting: findClient(t.clientId).nextMeeting }));
    return { data, prompt: `You are A2, the Insight writer inside "The RM Assistant", a prototype AI assistant for a commercial bank relationship manager (RM) named ${B.rm.name}. Today is ${B.todayLabel}. All data is made-up sample data.
Your job: turn the signals that agent A1 found (simple rules the business owns) into short insights ${B.rm.name.split(" ")[0]} can act on this week.
${RULES_TEXT}
- Each "why" is at most 45 words and names the numbers behind the signal.

<data>
${JSON.stringify(data, null, 1)}
</data>

Reply with only a JSON array, one object per client, in the same order:
[{"clientId": "C101", "headline": "at most 9 words", "why": "...", "talkingPoints": ["...", "..."], "nextStep": "one sentence"}]` };
  }
  function a3BriefPrompt(c, withTools) {
    const head = `You are A3, the Prep and follow-up assistant inside "The RM Assistant", a prototype for commercial bank relationship managers (RMs). All data is made-up sample data.
Draft a one-page pre-meeting brief for ${B.rm.name} (${B.rm.title}) for the meeting with ${c.name} (client id ${c.id}) on ${c.nextMeeting.date} at ${c.nextMeeting.time}: ${c.nextMeeting.purpose}, with ${c.nextMeeting.attendees.join(" and ")}.
${RULES_TEXT}
- End every fact with its source in square brackets: [Client record], [Activity YYYY-MM-DD], [Insight T1] (use the rule id) or [Market: Fed H.15].
- Partner names you may use: portfolio manager ${B.rm.partnerPM}; treasury specialist ${B.rm.treasurySpecialist}.`;
    const fmt = `Write it in exactly this Markdown layout, under 300 words, nothing before or after:
## At a glance
(3 bullets)
## Why this meeting matters
(2 sentences)
## Talking points
(3 numbered points)
## Questions to ask
(3 bullets)
## Watch-outs
(2 bullets)`;
    if (withTools) return `${head}\nUse your tools to gather the facts first: get_client_record, get_open_insights and get_recent_activity for ${c.id}, and get_market_context.\n\n${fmt}`;
    const data = { clientRecord: clientRecord(c.id), openInsights: runA1Silent().signals.filter(s => s.clientId === c.id), recentActivity: c.activity, market: marketFacts() };
    return `${head}\n\n<data>\n${JSON.stringify(data, null, 1)}\n</data>\n\n${fmt}`;
  }
  function a3FollowupPrompt(c, notes) {
    const record = clientRecord(c.id);
    const data = { client: { name: record.name, contacts: record.contacts, products: record.products }, meeting: { date: notes.date, recordingConsent: notes.recordingConsent, source: notes.recordingConsent ? "meeting transcript" : "RM's own notes (no recording: the client didn't agree to one, control K24)" }, rmNotes: notes.text, partners: { portfolioManager: B.rm.partnerPM, treasurySpecialist: B.rm.treasurySpecialist }, rm: B.rm.name };
    return { data, prompt: `You are A3, the Prep and follow-up assistant inside "The RM Assistant", a prototype for commercial bank relationship managers (RMs). All data is made-up sample data.
${B.rm.name} just met ${c.name}. From the RM's notes below, draft: a short recap, a follow-up email from ${B.rm.name} to the client, a call note for the CRM, and the next steps.
${RULES_TEXT}
- Use only facts from the notes. Where a date, number or owner is unclear, write [CHECK: what to confirm] instead of guessing.
- The email is under 180 words, warm and plain, signed by ${B.rm.name}. It makes no promise about rates, prices or credit.
- The CRM note ends with "AI-drafted, approved by RM."

<data>
${JSON.stringify(data, null, 1)}
</data>

Reply with only a JSON object:
{"recap": ["5 short bullets"], "email": {"subject": "...", "body": "..."}, "crmNote": "...", "nextSteps": [{"owner": "...", "item": "...", "due": "..."}], "flags": ["anything the RM should know, such as a control that applied"]}` };
  }
  function guardPrompt(q) {
    const book = myClients().map(c => ({ id: c.id, name: c.name, industry: c.industry, city: c.city, products: c.products, nextMeeting: c.nextMeeting }));
    return `You are the RM Assistant, a prototype AI assistant for relationship manager ${B.rm.name}. All data is made-up sample data. You may answer only about the RM's own clients, from the data below.
${RULES_TEXT}
- If the question asks for a credit decision, a price or rate, contacting a client, another RM's clients, or anything not in the data, reply in one sentence starting "I can't help with that:" and say why and who can help.
- Otherwise answer in at most 3 sentences, ending with the source in square brackets.

<data>
${JSON.stringify(book, null, 1)}
</data>

The RM asks: ${q}`;
  }

  window.AGENTS = { RULES, MARKET_RULE, runA1, guard, numberCheck, AI, errText, permanent, makeTools, clientRecord, marketFacts, a2Prompt, a3BriefPrompt, a3FollowupPrompt, guardPrompt,
    audit, onAudit: f => auditListeners.push(f), log, measures, findClient, myClients, fmtM, nonInterestAvg, growth };
})();
