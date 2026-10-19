// Recorded runs: what the agents produced on the sample data, written by Claude while the
// prototype was being built (2026-10-19). The page plays these when live AI isn't available
// to a viewer, and during the guided tour, so the tour never spends anyone's Claude usage.
// They are labeled "Recorded run" on screen wherever they appear.
window.REPLAY = {
  recorded: "2026-10-19",
  // A7: the page tools it calls, in order, and the summary it writes.
  fileSteps: ["get_financials", "get_loans_and_covenants", "get_deposits_and_payments", "get_documents_and_notes"],
  fileSummary: {
    C101: `## What's in the file
- Metal fabrication in Milwaukee, a client since 2014 with 210 employees; RM is Jordan Ellis. [Loan system]
- Revenue grew from $41.2M in FY2023 to $48.0M in FY2025, up 7.6% last year, with EBITDA of $6.2M (a 12.9% margin). [FS FY2025, p. 4] [A7 calculation]
- A $3M line ($0.4M drawn) and a $1.85M equipment term loan; debt service coverage of 2.4x against a 1.25x minimum. [Compliance certificate Q2 2026]
- Deposits rose from $2.78M in June to $3.16M in September; 24 of 24 payments on time. [Deposit system]`,
    C109: `## What's in the file
- Sawmill and lumber in Ashland, a client since 2015 with 110 employees; RM is Jordan Ellis. [Loan system]
- Only FY2023 and FY2024 are on file: revenue of $32.8M in FY2024, up 7.5%, with EBITDA of $4.1M. [FS FY2024, p. 4]
- A $2.5M line with $1.2M drawn; debt service coverage was 1.9x at its last test, on December 31, 2024. [FY2024 compliance certificate]
- Deposits eased from $1.24M in June to $1.12M in September, down 9.7%; payments on time. [Deposit system]`,
    C111: `## What's in the file
- Industrial distribution in Superior, a client since 2010 with 150 employees; RM is Jordan Ellis. [Loan system]
- Revenue grew from $36.0M in FY2023 to $41.0M in FY2025, up 5.4% last year; EBITDA of $4.2M, a 10.2% margin. [FS FY2025, p. 4] [A7 calculation]
- A $3.5M line with $1.9M drawn and a $5.2M borrowing base; debt to EBITDA of 0.45x against a 3.0x maximum. [Compliance certificate Q2 2026]
- Open request: increase the line to $4.5M. Deposits up 18.6% over 3 months; payments on time. [Request, Oct 14] [Deposit system]`
  },
  // A8: the routine sections of each draft. The borrower risk rating and recommendation are never drafted.
  drafts: {
    "review:C101": `## Borrower and relationship
- Lakeshore Precision Tooling is a metal fabricator in Milwaukee with 210 employees, a client since 2014. [Loan system]
- Jordan Ellis is the relationship manager; total commitments are $4.85M across a line of credit and an equipment term loan. [Loan system]
- The RM's latest note says Q3 orders are ahead of plan, and the owner may want equipment financing for a CNC line in spring 2027; no request has been made. [RM note, Sep 12]

## Financial performance
- Revenue rose from $41.2M in FY2023 to $44.6M in FY2024 and $48.0M in FY2025, up 7.6% last year. [FS FY2025, p. 4] [A7 calculation]
- EBITDA grew to $6.2M in FY2025 from $5.6M, and the margin edged up to 12.9% from 12.6%. [FS FY2025, p. 4] [A7 calculation]
- Net income was $3.0M; total debt fell to $2.25M and cash rose to $2.9M. [FS FY2025, p. 4]

## Covenant compliance
- Debt service coverage was 2.4x at the June 30, 2026 test, against a 1.25x minimum: passes. [Compliance certificate Q2 2026]
- Total debt to EBITDA was 0.36x against a 3.0x maximum: passes. [Compliance certificate Q2 2026]
- The FY2025 statements and the Q2 2026 certificate arrived on time; the Q3 2026 certificate is due November 14. [Documents]

## Collateral and loans
- Line of credit: $3M committed, $0.4M drawn, Prime + 0.25% (floating), matures June 30, 2027. [Loan system]
- Equipment term loan: $1.85M, Fixed 5.85%, matures March 31, 2029. [Loan system]
- Secured by a blanket lien on business assets, and CNC equipment appraised at $2.6M on March 15, 2024. [Equipment appraisal, 2024]

## Changes and items to note
- Possible equipment financing for a CNC line in spring 2027, per the RM; no request made. [RM note, Sep 12]
- Total debt $2.25M at FY2025. [FS FY2025, p. 4]
- Deposits up 13.7% over the last 3 months; every payment on time. [Deposit system] [Loan system]`,
    "review:C109": `## Borrower and relationship
- Chequamegon Timber Works runs a sawmill and lumber business in Ashland with 110 employees, a client since 2015. [Loan system]
- Jordan Ellis is the relationship manager. The RM notes the CFO left in July, and the new controller expects the delayed FY2025 audit in November. [RM note, Oct 2]

## Financial performance
- FY2024 revenue was $32.8M, up 7.5% from $30.5M in FY2023; EBITDA was $4.1M, a 12.5% margin. [FS FY2024, p. 4] [A7 calculation]
- FY2024 net income was $1.3M, with total debt of $1.4M and cash of $0.9M. [FS FY2024, p. 4]
- [NEEDS INPUT: FY2025 financial statements are not in the file]

## Covenant compliance
- Debt service coverage was 1.9x against a 1.25x minimum at its last test, on December 31, 2024. [FY2024 compliance certificate]
- The Q2 2026 compliance certificate is 66 days late. [Documents]
- [NEEDS INPUT: no covenant test in the last 12 months (last: 2024-12-31)]

## Collateral and loans
- Line of credit: $2.5M committed, $1.2M drawn, Prime + 0.50% (floating), matures May 31, 2027. [Loan system]
- Secured by timber inventory and mill equipment. [Security agreement, 2015]

## Changes and items to note
- FY2025 audited statements: 172 days late. [Documents]
- Deposits $1.24M in June, $1.12M in September, down 9.7%. [Deposit system]
- Payments in the last 12 months: all on time. [Loan system]`,
    "memo:C111": `## Borrower and relationship
- The request, as written by Jordan Ellis on October 14: increase the line of credit from $3.5M to $4.5M and extend its maturity to 2028-09-30, at Prime + 0.50% (floating), unchanged. [Request, Oct 14]
- The purpose, as written: carry more inventory for two new mining-equipment supply contracts starting in January. [Request, Oct 14] [RM note, Oct 14]
- Twin Ports Industrial Supply is an industrial distributor in Superior with 150 employees, a client since 2010. [Loan system]

## Financial performance
- Revenue rose from $36.0M in FY2023 to $38.9M in FY2024 and $41.0M in FY2025, up 5.4% last year. [FS FY2025, p. 4] [A7 calculation]
- EBITDA was $4.2M in FY2025, a 10.2% margin, up from $3.9M. [FS FY2025, p. 4] [A7 calculation]
- Net income was $1.7M; total debt fell to $1.9M and cash was $0.9M. [FS FY2025, p. 4]

## Covenant compliance
- Debt service coverage was 2.2x at the June 30, 2026 test, against a 1.25x minimum: passes. [Compliance certificate Q2 2026]
- Total debt to EBITDA was 0.45x against a 3.0x maximum: passes. [Compliance certificate Q2 2026]

## Collateral and loans
- Line of credit today: $3.5M committed, $1.9M drawn, Prime + 0.50% (floating), matures September 30, 2027. [Loan system]
- Secured by eligible receivables and inventory, with a borrowing base of $5.2M on September 30, 2026. [Borrowing base certificate, Sep]

## Changes and items to note
- Requested line $4.5M; borrowing base $5.2M (Sep 30). [Request, Oct 14] [Borrowing base certificate, Sep]
- Deposits up 18.6% over the last 3 months; every payment on time. [Deposit system]`
  },
  // A9: plain-English explanations of the top flags.
  watch: [
    { borrowerId: "C108", headline: "Three warning signs at once at Menomonee",
      explanation: "Debt service coverage was 1.31x against a 1.25x minimum, just 4.8% of headroom. Average deposits fell from $470K in June to $310K in September, down 34%. A payment is 9 days past due today, after one 12 days late in September.",
      toCheck: "Ask Jordan whether the lost catalog order is permanent, and how payroll moving to another bank affects cash." },
    { borrowerId: "C104", headline: "Brewer's Row missed its coverage covenant",
      explanation: "Debt service coverage was 1.18x at the June 30 test, below the 1.25x minimum in the loan agreement. The RM note says food costs squeezed margins and a new general manager started to tighten operations.",
      toCheck: "Ask what the new general manager expects margins to look like by the next test." },
    { borrowerId: "C112", headline: "Rock County is close to its leverage limit",
      explanation: "Total debt to EBITDA was 3.85x against a 4.0x maximum, 3.7% of headroom. The September borrowing base certificate is 4 days late. The RM notes used equipment is selling more slowly.",
      toCheck: "Ask when the September borrowing base certificate will arrive, and how much used inventory is on the lot." },
    { borrowerId: "C107", headline: "Lake Geneva deposits dropped this fall",
      explanation: "Average deposits fell from $560K in June to $350K in September, down 37.5%. The RM note says the boating season ended early and the business builds spring inventory in October, so cash dips every fall.",
      toCheck: "Compare with last fall's deposits to see whether this dip is the usual seasonal one." },
    { borrowerId: "C109", headline: "Chequamegon's statements are months late",
      explanation: "The FY2025 audited statements are 172 days late and the Q2 2026 compliance certificate is 66 days late. The RM note says the CFO left in July and the new controller expects the audit in November.",
      toCheck: "Ask the controller for a firm date for the audit, and for interim figures in the meantime." }
  ],
  // A11 (version 5): the industry background sections, drafted from the approved industry source pack only
  // (src/data/industries.js). No borrower data was given; every sentence ends with its source tag.
  industry: {
    restaurants: `## Industry size and trend
- Upper Midwest full-service restaurant sales were $14.2B in 2025, up 3.1% from 2024. [S1]
- Sales are forecast to grow 2.5% a year through 2028. [S1]

## Main drivers
- Dinner service brings in about 62% of sales. [S1]
- Menu prices have risen: food-away-from-home prices were up 4.0% in the year to October 2025, against 2.4% for grocery prices. [S3]

## Main risks
- Labor is 33% of sales at the median full-service restaurant, up from 30% in 2022. [S2]
- Food costs are 31% of sales at the median full-service restaurant. [S4]
- Closures rose to 6.8% of locations in 2025, from 5.9% in 2024, and operators with several locations closed less often than single-location operators. [S4]

## Outlook
- Sales are forecast to grow 2.5% a year through 2028. [S1]
- 71% of operators surveyed expect staffing to stay hard to find in 2026. [S2]`,
    distribution: `## Industry size and trend
- Upper Midwest industrial distribution sales were $38.5B in 2025, up 1.8% from 2024. [S1]
- Sales are forecast to grow 2.2% a year through 2028. [S1]

## Main drivers
- Distributor sales tend to follow factory output, with a lag of about one quarter. [S4]
- The sample regional manufacturing index averaged 49.6 in the first half of 2026, under the 50 line that marks shrinking activity. [S2]
- New orders in the index rose for three months in a row to September 2026. [S2]

## Main risks
- Distributors surveyed held 74 days of inventory on average in 2025, up from 66 days in 2023. [S3]
- 38% of distributors surveyed said online competitors had taken business from them. [S3]
- Customer concentration is the most common weakness listed for small distributors. [S4]

## Outlook
- Sales are forecast to grow 2.2% a year through 2028, with gross margins averaging 24.5% of sales. [S1] [S3]`,
    metalfab: `## Industry size and trend
- Upper Midwest metal fabrication shipments were $21.7B in 2025, up 2.9% from 2024. [S1]
- Shipments are forecast to grow 2.0% a year through 2028. [S1]

## Main drivers
- Steel is about 35% of the cost of a typical fabricated part. [S2]
- Steel mill product prices were down 6.5% in the year to August 2026. [S2]
- 64% of fabricators surveyed plan to buy automated equipment by 2027. [S3]

## Main risks
- Skilled welders and machinists were the hardest roles to fill for 58% of fabricators surveyed. [S3]
- Fabricators that sell mainly to agriculture and construction see larger swings in orders than those selling to medical and aerospace customers. [S4]

## Outlook
- Shipments are forecast to grow 2.0% a year through 2028. [S1]
- Hiring skilled staff stays the hardest constraint for 58% of fabricators surveyed. [S3]`
  }
};
