// Recorded runs: what the agents produced on the sample data, written by Claude while the
// prototype was being built (2026-10-18). The page plays these when live AI isn't available
// to a viewer, and during the guided tour, so the tour never spends anyone's Claude usage.
// They are labeled "Recorded run" on screen wherever they appear.
window.REPLAY = {
  recorded: "2026-10-18",
  insights: [
    { clientId: "C101", headline: "Idle cash is building at Lakeshore",
      why: "About $2.88M a month sits in accounts that earn no interest (last 3 months), and balances are up 31% since April. The 10-year Treasury yield is up 0.55 points in six months, so cash that sits is worth a conversation.",
      talkingPoints: ["Maria asked in September whether we offer anything better for cash that sits.", "Ask how much cash they want to keep on hand day to day."],
      nextStep: "Bring sweep and money market options to Tuesday's 10:00 check-in, and offer to bring in Priya Natarajan." },
    { clientId: "C105", headline: "Northern Pines pays its bills through another bank",
      why: "About 38 wires and payment batches a month go out from their old bank, while we hold their $4.3M equipment loan. Greg said in June that payroll and fuel payments still run there.",
      talkingPoints: ["Ask what it would take to move payroll and fuel payments.", "Offer a walk-through of our payment tools with the treasury team."],
      nextStep: "Call Greg Baumann this week; the last contact was in June." },
    { clientId: "C102", headline: "Fox River writes 420 checks a month unprotected",
      why: "Fox River issues about 420 checks a month and doesn't use positive pay, the service that stops checks the client didn't issue. Dale mentioned in August that check fraud hit a vendor in their industry.",
      talkingPoints: ["Ask how they catch a forged or altered check today.", "Explain how positive pay works in their daily routine."],
      nextStep: "Raise positive pay at the October 27 annual review prep call." },
    { clientId: "C103", headline: "Driftless staff drive checks to the branch",
      why: "Staff make about 14 branch deposit trips a month, and the co-op doesn't have remote deposit, which lets them scan checks at the office.",
      talkingPoints: ["Ask how much staff time the branch runs take.", "Offer to show remote deposit on a laptop and scanner."],
      nextStep: "Offer Ruth Halvorsen a short remote deposit demo." },
    { clientId: "C104", headline: "Brewer's Row takes cards through another processor",
      why: "The restaurant group takes card payments from diners and has no merchant services with us. Andre said in September that he's unhappy with his current processor's fees.",
      talkingPoints: ["Ask what bothers him most about his current card setup.", "Offer an introduction to the merchant services team."],
      nextStep: "Raise it at Thursday's 15:30 introduction to the new general manager." }
  ],
  briefSteps: [
    { tool: "get_client_record", input: { client_id: "C101" } },
    { tool: "get_open_insights", input: { client_id: "C101" } },
    { tool: "get_recent_activity", input: { client_id: "C101" } },
    { tool: "get_market_context", input: {} }
  ],
  brief: `## At a glance
- Lakeshore Precision Tooling: metal fabrication in Milwaukee, about $48M in revenue and 210 employees, a client since 2014. [Client record]
- Has an operating account, a $3M line of credit ($400K drawn), an equipment term loan and ACH origination. [Client record]
- Balances rose from $2.41M in April to $3.16M in September, and 94% sits in accounts that earn no interest. [Client record]

## Why this meeting matters
Cash is building with nowhere to go, and Maria already asked about it in September. [Activity 2026-09-12] [Insight T1] This is the moment to show we can do more than hold their operating account. [Insight T1]

## Talking points
1. Options for idle cash: a sweep or a money market, and how quickly funds come back when they need them. [Insight T1]
2. Rates context: the 10-year Treasury yield averaged 4.68% in August 2026, up 0.55 points in six months. [Market: Fed H.15]
3. Tom's automation plans for 2027: listen, and bring in Sam Okafor (portfolio manager) for anything that needs credit. [Activity 2026-06-10]

## Questions to ask
- How much cash do you want to keep on hand day to day? [Insight T1]
- What's behind the strong Q3, and will it last? [Activity 2026-09-12]
- Who else at the company should hear about treasury options? [Client record]

## Watch-outs
- Don't quote rates or prices for our products; Priya Natarajan's treasury team handles pricing. [Insight T1]
- Make no credit commitments: equipment financing goes to the portfolio manager. [Activity 2026-06-10]`,
  followup: {
    recap: [
      "Q3 was strong: a new contract with an ag equipment maker means a second shift starting in January.",
      "Cash keeps building in the operating account. Maria is open to a sweep or money market and wants the options and how quickly funds come back.",
      "A vendor of theirs had a check fraud attempt in August; they're interested in positive pay.",
      "Tom may need equipment financing for a new 5-axis CNC line, possibly in spring.",
      "Maria wants our treasury specialist on the next call."
    ],
    email: {
      subject: "Thank you, and next steps from today",
      body: "Hi Maria and Tom,\n\nThank you for your time today, and congratulations on a strong Q3 and the new contract.\n\nHere's what we agreed:\n- I'll send a one-pager on sweep and money market options, including how quickly you can get funds back, by [CHECK: confirm the date for \"end of next week\"].\n- I'll include an overview of positive pay, given the fraud attempt at your vendor.\n- Sam Okafor, our portfolio manager, will reach out about the CNC line when you're ready.\n- Priya Natarajan from our treasury team will join our next conversation.\n\nLet's meet again after your board meeting. [CHECK: the November date]\n\nBest regards,\nJordan Ellis"
    },
    crmNote: "Meeting at the client's office with Maria Chen (CFO) and Tom Lindqvist (owner). Q3 strong; new ag equipment contract; second shift from January. Cash building in the operating account; client open to a sweep or money market and wants options and access terms. Interested in positive pay after a vendor's fraud attempt in August. Possible equipment financing for a CNC line in spring: referred to Sam Okafor (portfolio manager), no commitment made. Treasury specialist to join the next meeting, after their board meeting [CHECK: November date]. AI-drafted, approved by RM.",
    nextSteps: [
      { owner: "Jordan Ellis", item: "Send the one-pager on sweep and money market options, including access to funds", due: "[CHECK: end of next week]" },
      { owner: "Jordan Ellis", item: "Include a positive pay overview", due: "With the one-pager" },
      { owner: "Sam Okafor", item: "Contact Tom about equipment financing for the CNC line", due: "[CHECK: when Tom is ready]" },
      { owner: "Priya Natarajan", item: "Join the next client meeting", due: "Next meeting" },
      { owner: "Jordan Ellis", item: "Schedule the next meeting after the board meeting", due: "[CHECK: November date]" }
    ],
    flags: [
      "Equipment financing is a credit matter: it went to the portfolio manager, and no commitment was made (K8).",
      "No recording: drafted from your own notes, because the client didn't agree to recording (K24)."
    ]
  }
};
