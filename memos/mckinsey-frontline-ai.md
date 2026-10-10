# McKinsey's frontline AI use cases, and how our RM plan covers them

A core reference for choosing which use cases to build, and the framework the RM plan is now organized on. It summarizes McKinsey's
article "Agentic AI is here. Is your bank's frontline team ready?" and checks the
RM plan against its five use cases. Checked against the article's text, pasted
in by me on 2026-10-10.

> **Source.** Kumar Kanagasabai, Chris Lu and Shital Chheda (McKinsey):
> https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready
> Based on a survey of about 400 US and Canadian bankers, RMs and sales leaders.
> McKinsey's numbers come from its own client work and early pilots, not
> controlled studies, so treat them as directional. ⚠️ The page I pasted showed no
> publication date; the RM plan says December 2025, which I haven't confirmed.

## The headline numbers

| Finding | McKinsey's words |
|---|---|
| Revenue and cost | Banks that rewire one frontline area end to end "enjoy between 3 and 15 percent higher revenues per RM and 20 to 40 percent lower cost to serve" |
| Time with clients | "In many commercial banks, relationship managers spend just 25 to 30 percent of their time in client dialogue" |
| Time freed | "ten to 12 hours a week returned to each banker", improving the coverage ratio (clients per banker) by about 40 percent |
| Top problems | Excessive admin, low-quality leads, and difficult meeting prep. 53 percent cite a shortage of high-quality leads as their biggest barrier |
| Where banks go wrong | "Banks are moving fastest on the least valuable tools" |

## The five use cases

| # | Use case | What the AI does | Reported impact (McKinsey) |
|---|---|---|---|
| 1 | **Prospecting** (market maps and next best opportunities) | Combines data sources into ranked lists of high-potential clients, refreshed as markets change | About 30% pipeline growth and 10% higher revenue; one bank saw twice the conversion rate of traditional leads |
| 2 | **Lead nurturing** (including cross-sell) | An agent replies to inquiries, sends tailored content and books meetings, passing only qualified leads to the RM | Two to three times more qualified leads; 5% higher conversion (early pilots) |
| 3 | **Account planning and meeting prep** (account intelligence) | Pulls data from many sources into an account plan or briefing in minutes, with talking points | About 25% less prep time; 10% more time with clients |
| 4 | **Deal structuring and pricing** (dynamic deal scoring) | Recommends pricing and discounts from past deals and client data, and speeds approvals | 10% margin gains; one bank cut deal turnaround from five days to two |
| 5 | **Coaching** (AI sales coaching) | Reviews call transcripts and gives each banker personal guidance | Customer satisfaction up seven points; new bankers up to speed 20% faster |

McKinsey ties these to the stages of a sale: prospecting and deal close
(use case 1), outreach (2), early and late-stage conversations (3, with
coaching in late stage), and negotiation (4).

## How our RM plan covers them

| McKinsey use case | In our RM plan | Coverage |
|---|---|---|
| 1. Prospecting | Wave 3: prospect lookalikes (B8). Wave 1's weekly opportunity list finds next best opportunities in existing clients | **Partly.** New-client prospecting comes late (wave 3), and McKinsey reports its biggest numbers here |
| 2. Lead nurturing, including cross-sell | Wave 2: referral prompts (B6) for cross-sell between teams. Nothing contacts prospects on its own | **Partly, by design.** Our rule is that nothing reaches a client without the RM, so an agent that writes to prospects by itself is out of scope today |
| 3. Account planning and meeting prep | Wave 1: pre-meeting client brief (B2). Wave 3: RM assistant (B7) | **Covered**, and first in line |
| 4. Deal structuring and pricing | Not in the plan. The plan keeps the AI away from pricing and credit decisions (control K3) | **Not covered, by design.** Pricing touches fair-lending rules, so it would need a much higher bar |
| 5. Coaching | Not in the plan. The onboarding coach (A6) answers "how do I use this?" only | **Not covered** |

**Also in our plan, not in McKinsey's five:** early warning when a client may
leave (B5), and the meeting follow-up (B3) and call notes saved to the CRM (B4),
which tackle McKinsey's number one problem, excessive admin.

**What this means:** wave 1 lines up with McKinsey's most-cited problem (meeting
prep and admin). The gaps are coaching, which is low risk and could fit an early
wave, and prospecting, which McKinsey rates highest for revenue and we have in
wave 3. Lead nurturing and pricing are left out on purpose, for governance
reasons. Each open question is a decision in the Open Items log (D6 to D8).

## What it changed: the RM plan now uses McKinsey's framework (decided 2026-10-10)

The RM plan is now organized around McKinsey's five use cases, with our AI
products underneath each one and a return profile for each (the plan's "Core
use cases" section). Two of our products sit "beyond McKinsey's five": admin
off the RM's plate (McKinsey's top problem, which its five use cases don't
name) and keeping clients. Open questions:
- **Prospecting earlier?** (D7) McKinsey's biggest revenue numbers are in prospecting, and our prospect lookalikes come in wave 3. Outside prospect data may set the pace.
- **Add coaching?** (D6) Low risk, uses call transcripts the meeting features already need, and McKinsey reports faster ramp-up for new bankers.
- **Lead nurturing and pricing stay out for now?** (D8) An agent that writes to prospects on its own, or recommends prices, conflicts with "nothing reaches a client without the RM" and the fair-lending control (K3).

## McKinsey's five principles for capturing the value

1. Define the business model and the value it should create.
2. Rework a frontline area end to end, not piece by piece, with a repeatable playbook for scaling.
3. Build reusable technology: an orchestration layer for agents, a data foundation (an "ontology" of the bank's workflows, decisions and knowledge), and trust and security.
4. Put governance in place: how much each agent may do on its own, monitoring and audit.
5. Upskill the workforce, as RM roles change.

**Where our framework already does this:** 1 is the value model and the
sponsor's outcome (Discover); 2 is the six-step process and the playbook; 3 is
the agent library, the data contract and the Glossary (our working vocabulary,
which plugs into the bank's ontology); 4 is the Controls Catalog and
"assistive first"; 5 is Release and adopt (training on users' own work and
champions). ⚠️ Role redesign (new roles such as "agent orchestrator") isn't
covered yet.

_Last updated: 2026-10-10_
