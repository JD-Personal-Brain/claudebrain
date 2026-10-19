// Sample data. Every source, title, publisher and number here is made up for the prototype.
// The approved industry source pack that A11, the Industry background drafter, reads (workflow B16).
// No real research firm, report or figure is used. In production (our assumption, to confirm with the
// bank) the pack would be the bank's licensed industry research, approved by its content owner (sub-step 2.3).
// A11 reads only this pack: never a borrower's data.
(function () {
  window.INDUSTRY_SOURCES = {
    label: "Sample data: a made-up source pack",
    approvedBy: "the content owner (sample), October 1, 2026",
    // A made-up outside fee per industry section, used only for the sample "outside fees replaced" line on
    // How we'd measure it. The real fee is the bank's to confirm.
    sampleFeePerSection: 2500,
    packs: [
      { id: "restaurants", industry: "Full-service restaurants", region: "Upper Midwest (sample)",
        usedFor: { borrowerId: "C104", doc: "memo", due: "2026-10-23" },
        sources: [
          { tag: "S1", title: "Sample industry report, 2026", publisher: "Sample research firm A", date: "2026-06-30", facts: [
            "Upper Midwest full-service restaurant sales were $14.2B in 2025, up 3.1% from 2024.",
            "Sales are forecast to grow 2.5% a year through 2028.",
            "About 62% of sales come from dinner service."] },
          { tag: "S2", title: "Sample trade association survey, 2026", publisher: "Sample restaurant trade group", date: "2026-04-15", facts: [
            "Labor is 33% of sales at the median full-service restaurant, up from 30% in 2022.",
            "71% of operators surveyed expect staffing to stay hard to find in 2026."] },
          { tag: "S3", title: "Sample government statistics summary, 2025", publisher: "Sample statistics office", date: "2025-12-10", facts: [
            "Food-away-from-home prices rose 4.0% in the year to October 2025, faster than grocery prices at 2.4%.",
            "Full-service restaurant employment in the region was 186,000 in 2025."] },
          { tag: "S4", title: "Sample credit research note, 2026", publisher: "Sample research firm B", date: "2026-08-20", facts: [
            "Restaurant closures in the region rose to 6.8% of locations in 2025, from 5.9% in 2024.",
            "Operators with several locations had lower closure rates than single-location operators.",
            "Food costs are 31% of sales at the median full-service restaurant."] }
        ] },
      { id: "distribution", industry: "Industrial distribution", region: "Upper Midwest (sample)",
        usedFor: { borrowerId: "C111", doc: "memo" },
        sources: [
          { tag: "S1", title: "Sample industry report, 2026", publisher: "Sample research firm A", date: "2026-05-31", facts: [
            "Upper Midwest industrial distribution sales were $38.5B in 2025, up 1.8% from 2024.",
            "Sales are forecast to grow 2.2% a year through 2028."] },
          { tag: "S2", title: "Sample manufacturing activity summary, 2026", publisher: "Sample statistics office", date: "2026-09-30", facts: [
            "The sample regional manufacturing index averaged 49.6 in the first half of 2026; a reading under 50 means activity is shrinking.",
            "New orders in the index rose for three months in a row to September 2026."] },
          { tag: "S3", title: "Sample trade association survey, 2026", publisher: "Sample distributors' trade group", date: "2026-03-20", facts: [
            "Distributors surveyed held 74 days of inventory on average in 2025, up from 66 days in 2023.",
            "Gross margins averaged 24.5% of sales.",
            "38% of distributors surveyed said online competitors had taken business from them."] },
          { tag: "S4", title: "Sample credit research note, 2026", publisher: "Sample research firm B", date: "2026-07-15", facts: [
            "Distributor sales tend to follow factory output, with a lag of about one quarter.",
            "Customer concentration is the most common weakness the note lists for small distributors."] }
        ] },
      { id: "metalfab", industry: "Metal fabrication", region: "Upper Midwest (sample)",
        usedFor: { borrowerId: "C101", doc: "review" },
        sources: [
          { tag: "S1", title: "Sample industry report, 2026", publisher: "Sample research firm A", date: "2026-06-30", facts: [
            "Upper Midwest metal fabrication shipments were $21.7B in 2025, up 2.9% from 2024.",
            "Shipments are forecast to grow 2.0% a year through 2028."] },
          { tag: "S2", title: "Sample price index summary, 2026", publisher: "Sample statistics office", date: "2026-09-15", facts: [
            "Steel mill product prices were down 6.5% in the year to August 2026.",
            "Steel is about 35% of the cost of a typical fabricated part."] },
          { tag: "S3", title: "Sample trade association survey, 2026", publisher: "Sample fabricators' trade group", date: "2026-02-28", facts: [
            "64% of fabricators surveyed plan to buy automated equipment by 2027.",
            "Skilled welders and machinists were the hardest roles to fill for 58% of respondents."] },
          { tag: "S4", title: "Sample credit research note, 2026", publisher: "Sample research firm B", date: "2026-08-01", facts: [
            "Fabricators that sell mainly to agriculture and construction see larger swings in orders than those selling to medical and aerospace customers."] }
        ] }
    ]
  };
})();
