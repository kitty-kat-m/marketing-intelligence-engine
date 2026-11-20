# Marketing Intelligence Engine — section rules

Current local build · 20 November 2026

Use this reference when changing the product or preparing a hackathon demo. The five sections are user-facing stages. The implementation files listed below define their exact behavior. The separate travel brand guide applies to the demo company.

## 1. Intelligence — collect and assess inputs

**Company setup.** Accept a company name and HTTPS website. A scan creates an editable draft. Save confirmed findings explicitly. Existing saved profiles are preserved until the user saves changes. A company workspace and the fictional travel demo use separate local databases.

**Website access.** Read the homepage and up to four qualifying internal links discovered there. Give About / Who we are / Our story links priority over other eligible links. Respect robots exclusions. Check public IP addresses, TLS, redirects, HTML responses and response size. Record pages read and pages skipped. Content rendered only through JavaScript can be absent.

**Browser-check fallback.** When public pages are visible to a person but the scanner receives a browser challenge, the marketer can paste descriptive paragraphs with their original URL. The same editorial rules apply. Record the source method as manually supplied text. This path does not inspect page styles, structured service areas or product links.

**Company introduction.** Prefer a factual identity or activity sentence from About-page prose. Retain the company, activity and scope supported by the passage. Convert simple first-person activity statements into third person. Ignore navigation and common promotional or transactional phrases. A clearly stated small-group tour category can support a narrow travel introduction. If the English extraction rules cannot support a sentence, leave it open for the marketer. Do not infer market leadership, mission, quality or worldwide operations from promotional language.

**Voice and design.** Suggest writing instructions only for identifiable patterns in substantive prose, such as direct reader address, specific descriptions of materials or the role of local people. Preserve the relevant passage and URL for review. Navigation headings are not voice examples. These rules propose editorial guidance; they do not establish official brand policy. Report CSS font names and page theme colors as observed website settings. A white page theme does not establish a white brand palette.

**Products and markets.** Scanned products and services form a shortlist with source links. Import or enter verified catalog information separately. Accept Excel, CSV, exported JSON or manual catalog entries. Product IDs must be unique. Optional inventory is a nonnegative whole number. For country suggestions, require an explicit Country in an areaServed declaration or human confirmation. Travel destinations alone are insufficient.

**External and competitor sources.** Saving an external URL records a reference, with optional notes and a product association. This workflow is separate from the company-site scan.

**Listening.** Read sources reads each saved HTTPS source through the same public-address, TLS and size checks as the website scan, following up to three redirects. An RSS/Atom feed becomes one observation per item (up to eight); a page becomes one observation from its paragraphs. Observations carry an ID, date, source and link, title, summary, optional audience quote, themes, linked products, method and status (New, Useful, Dismissed). Without AI, the summary is a plain extract and products are matched by name keywords. With AI, a fast model summarises and links products; quotes are kept only if they appear word for word in the fetched text, and unknown product IDs are dropped. Observations can also be imported from JSON/CSV files or an HTTPS JSON endpoint such as an n8n webhook. Re-reading or re-importing keeps the marketer's status. New observations do not mark existing entries stale; they inform new proposals and AI drafts. Dismissed observations are never used as evidence. Failed sources are reported individually and do not stop the batch. Owned channel and advertising links are references, not authenticated connections. Competitor observations carry a date, source and marketer interpretation. Removing a competitor hides it while retaining its observations.

**Campaign context.** Campaign briefs record dates, phases, markets, messages, restrictions and expected supporting activity. Check overlapping or conflicting messages during review. Overlay toggles change what the calendar shows.

Implementation: company_workspace.py, demo_workspace.py, website_profile.py, editorial_profile.py, competitor_report.py, company_channels.py, campaign_layer.py, listening.py, listening_ui.py.

## 2. Direction — decide how to plan

Choose objective, audience, channels, timing and frequency. The company planner uses selected publishing days and rotates eligible products. Products with zero known inventory are excluded. A linked research note and the most recent non-dismissed observation for the product are added to the proposal's sources and rationale. Saved brand voice can seed the writing guidance. Previously saved controls take precedence.

The travel demo applies its own campaign priorities, launch dates, departure inventory and offer terms. Its editable priorities influence flexible suggestions within those constraints. Historical bookings and current inventory are separate measures. Paid and organic channels have separate scheduling rules. Building adds missing slots and preserves existing entries.

Implementation: company_workspace.py, planner.py, demo_workspace.py, priority_editor.py, audience_regions.py.

## 3. Plan — review calendar proposals

Inspect each entry's topic, date, channel, audience, objective, product facts, evidence and linked campaign restrictions. Check proposed wording and audience fit manually. Region and campaign filters control display. Reviewers can edit, approve, reject or leave feedback. Editing a proposal creates a version and clears approval. Changed relevant inputs or briefs require renewed review. Rejection preserves history. A planning CSV can contain drafts and serves calendar review.

The local reviewer name is a record of the decision, not authenticated identity. A proposal approval covers the plan. The final content has a separate approval.

**AI analysis and draft (optional).** Available when an Anthropic API key is configured. The evidence index for a proposal contains only: its products; related campaigns, signals and cited sales rows (demo); linked research notes and non-dismissed observations (company); linked campaign briefs; reviewer feedback on the proposal; and the top five learnings from results. The model returns a rationale with bracketed evidence IDs, headline, preview text, body, call to action, a testable prediction with a metric, and uncertainties. Checks: citations not in the evidence are removed and warned; numbers in customer copy that do not appear in the evidence are warned; missing campaign terms are warned; a response without copy is rejected. The result is saved on the entry as a new version, which clears approval. Bulk drafting handles up to 12 proposals per click and skips approved and rejected proposals. Redrafting includes reviewer feedback. If the AI is unavailable, the rest of the engine is unaffected.

Implementation: month_calendar.py, review_ui.py, proposal_controls.py, proposal_context.py, campaign_layer.py, planner.py, ai_engine.py, ai_ui.py.

## 4. Assets — draft, preview, approve and export

Create drafts only from eligible, current approved proposals. If the proposal has an AI draft, the creative starts from its headline, preview, body and call to action and is labelled for fact-checking; otherwise it starts from the fact-based template. Check linked-campaign alignment and email objective eligibility. Review product facts, copy, call to action, destination and creative. Preview changes separately from saving. Approval requires a reviewer, fact-check confirmation and a real HTTPS destination. Paid social and display assets also require a finished creative link.

Draft edits clear content approval. Assets reference a specific proposal version. Export only currently approved assets tied to eligible current proposals. The ZIP contains approved records, text and email HTML where applicable. Publishing, sending and activating spend are separate from export.

Implementation: campaign_assets.py, asset_previews.py, campaign_layer.py.

## 5. Learn — results, learnings and next questions

Download a results template listing current proposals. Each row needs entry_id, metric (open_rate, click_rate, conversion_rate, conversions, engagement_rate, reach, revenue) and a nonnegative value; baseline, observation window and notes are optional. Rates are percentages from 0 to 100. Invalid files are rejected with every error listed and saved results are unchanged; blank template rows are skipped. Each result is pinned to the proposal version current at import and carries the proposal's AI prediction. Re-importing the same entry, metric and window replaces the earlier row.

Learnings group results by channel, product and planning angle and compare the mean with the mean baseline. Groups with fewer than three results are labelled as small samples. Learnings are described as observed performance, not proof of cause. The demo can load deterministic fictional results, which are labelled throughout. Suggested next questions (rules-based, or AI when available) can be added to listening prompts shown at the top of Listening. Top learnings are included as evidence in later AI drafts.

Implementation: results_loop.py, learn_ui.py.


## Product direction for listening and learning

These design rules guide work across the five screens. Today the engine reads sources into observations, drafts evidence-grounded proposals with predictions, supports proposal and creative review, exports approved work and imports results. Channel delivery and automated performance sync are future capabilities.

1. **Listen in Intelligence.** Capture a dated observation in the audience's own words, where it appeared, its source and the audience or product it concerns. Start with manual entries from reviews, forums, sales enquiries or owned communities. Keyword alerts and social monitoring can later supply the same fields.
2. **Understand in Direction and Plan.** Link a proposed action to the observation and a business fact. Record the marketer's interpretation, uncertainty and a testable prediction. Group recurring pain points and competitor observations. Any future research summary must preserve links to its evidence. A reviewer can decide to keep listening.
3. **Make in Creative.** Agree the audience, message, offer and measure of success before automating production. Choose email, social, video or voice according to the question being tested and the channel the audience uses.
4. **Ship with a human decision.** Record the intended destination and accountable person. Require human approval of the final version before external delivery. For future delivery integrations, record actual publication time and URL or send receipt. Include owned communities and content discoverable through search when relevant. Treat AI search visibility as an outcome to investigate.
5. **Learn back in Intelligence.** Link results to the signal, proposal version, audience and channel. Record a baseline or comparison, metric definition, observation window, result and follow-up decision. Capture inconclusive tests. Distinguish observed performance from evidence that the campaign caused it. Turn the next unanswered question into a listening prompt.

**Operating rules.** Run a complete test manually before automating it. Track completed experiments, what was learned and which decision changed. Review channel reach, frequency and response before increasing volume or testing another channel. Keep source records exportable and accept manual input when a provider fails. Give each integration an owner, a maintenance budget and a review date. Monitor failures and changes in output quality, including prompt drift. Retire integrations whose evidence no longer justifies their upkeep.

**First prototype milestone.** Demonstrate one traceable cycle using a manually recorded customer question, a proposal with a prediction, human-approved creative, a recorded delivery and an observed result that informs the next question. Use clearly labelled fictional results in demos.

## Maintaining this reference

The default landing page is About the platform, separate from the engine at /engine. It explains the platform purpose, four-step workflow, prototype capabilities and current limitations without inventing team credentials or integrations. Show the full introductory graphic on About only. Top navigation and clear entry links connect the informational page to the engine.

Navigation uses five compact buttons with numbered circles (1–5), icons, one label per step and a highlighted current step. Step 4 is labelled Creative and step 5 Learn. Keep the steps in one row with horizontal scrolling on narrow screens. Show the full explanatory hero on the landing view. Navigation changes do not imply completion or approval.

Proposal dialogs present audience, objective, market and schedule as a compact brief, with reasoning separate from customer-facing copy. An approved, current proposal can open its matching design in Creative using Go to design. Do not edit creative inside the proposal dialog. Proposal approval and content approval remain separate. Version history explains previous saves; removal is a separately labelled, confirmed action that retains history.

New creative templates include a separate email headline and structured cards for the proposal's selected products only. Do not add unrelated products or invent claims, prices, inventory or performance evidence. Existing saved creative is not silently rewritten. Copy starts from the proposal's AI draft when one exists, otherwise from templates. AI only sees the evidence for that proposal, not all company data. Label image links and button destinations in plain language.

For a change to a section, update its inputs, decision rule, output, failure behavior and approval effects here. Mark proposed integrations as future work until they operate through the app. Add a regression check when an incorrect claim, lost edit, or stale approval could recur. Use dated build notes for history and this document for current rules.
