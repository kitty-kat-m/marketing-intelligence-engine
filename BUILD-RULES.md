# Marketing Intelligence Engine — section rules

Current local build · 4 November 2026

Use this reference when changing the product or preparing a hackathon demo. The four sections are user-facing stages. The implementation files listed below define their exact behavior. The separate travel brand guide applies to the demo company.

## 1. Intelligence — collect and assess inputs

**Company setup.** Accept a company name and HTTPS website. A scan creates an editable draft. Save confirmed findings explicitly. Existing saved profiles are preserved until the user saves changes. A company workspace and the fictional travel demo use separate local databases.

**Website access.** Read the homepage and up to four qualifying internal links discovered there. Give About / Who we are / Our story links priority over other eligible links. Respect robots exclusions. Check public IP addresses, TLS, redirects, HTML responses and response size. Record pages read and pages skipped. Content rendered only through JavaScript can be absent.

**Browser-check fallback.** When public pages are visible to a person but the scanner receives a browser challenge, the marketer can paste descriptive paragraphs with their original URL. The same editorial rules apply. Record the source method as manually supplied text. This path does not inspect page styles, structured service areas or product links.

**Company introduction.** Prefer a factual identity or activity sentence from About-page prose. Retain the company, activity and scope supported by the passage. Convert simple first-person activity statements into third person. Ignore navigation and common promotional or transactional phrases. A clearly stated small-group tour category can support a narrow travel introduction. If the English extraction rules cannot support a sentence, leave it open for the marketer. Do not infer market leadership, mission, quality or worldwide operations from promotional language.

**Voice and design.** Suggest writing instructions only for identifiable patterns in substantive prose, such as direct reader address, specific descriptions of materials or the role of local people. Preserve the relevant passage and URL for review. Navigation headings are not voice examples. These rules propose editorial guidance; they do not establish official brand policy. Report CSS font names and page theme colors as observed website settings. A white page theme does not establish a white brand palette.

**Products and markets.** Scanned products and services form a shortlist with source links. Import or enter verified catalog information separately. Accept Excel, CSV, exported JSON or manual catalog entries. Product IDs must be unique. Optional inventory is a nonnegative whole number. For country suggestions, require an explicit Country in an areaServed declaration or human confirmation. Travel destinations alone are insufficient.

**External and competitor sources.** Saving an external URL records a reference, with optional notes and a product association. This workflow is separate from the company-site scan. Owned channel and advertising links are references, not authenticated connections. Competitor observations carry a date, source and marketer interpretation. Removing a competitor hides it while retaining its observations.

**Campaign context.** Campaign briefs record dates, phases, markets, messages, restrictions and expected supporting activity. Check overlapping or conflicting messages during review. Overlay toggles change what the calendar shows.

Implementation: company_workspace.py, demo_workspace.py, website_profile.py, editorial_profile.py, competitor_report.py, company_channels.py, campaign_layer.py.

## 2. Direction — decide how to plan

Choose objective, audience, channels, timing and frequency. The company planner uses selected publishing days and rotates eligible products. Products with zero known inventory are excluded. Saved brand voice can seed the writing guidance. Previously saved controls take precedence.

The travel demo applies its own campaign priorities, launch dates, departure inventory and offer terms. Its editable priorities influence flexible suggestions within those constraints. Historical bookings and current inventory are separate measures. Paid and organic channels have separate scheduling rules. Building adds missing slots and preserves existing entries.

Implementation: company_workspace.py, planner.py, demo_workspace.py, priority_editor.py, audience_regions.py.

## 3. Plan — review calendar proposals

Inspect each entry's topic, date, channel, audience, objective, product facts, evidence and linked campaign restrictions. Check proposed wording and audience fit manually. Region and campaign filters control display. Reviewers can edit, approve, reject or leave feedback. Editing a proposal creates a version and clears approval. Changed relevant inputs or briefs require renewed review. Rejection preserves history. A planning CSV can contain drafts and serves calendar review.

The local reviewer name is a record of the decision, not authenticated identity. A proposal approval covers the plan. The final content has a separate approval.

Implementation: month_calendar.py, review_ui.py, proposal_controls.py, proposal_context.py, campaign_layer.py, planner.py.

## 4. Assets — draft, preview, approve and export

Create template drafts only from eligible, current approved proposals. Check linked-campaign alignment and email objective eligibility. Review product facts, copy, call to action, destination and creative. Preview changes separately from saving. Approval requires a reviewer, fact-check confirmation and a real HTTPS destination. Paid social and display assets also require a finished creative link.

Draft edits clear content approval. Assets reference a specific proposal version. Export only currently approved assets tied to eligible current proposals. The ZIP contains approved records, text and email HTML where applicable. Publishing, sending and activating spend are separate from export.

Implementation: campaign_assets.py, asset_previews.py, campaign_layer.py.

## Maintaining this reference

The default landing page is About the platform, separate from the engine at /engine. It explains the platform purpose, four-step workflow, prototype capabilities and current limitations without inventing team credentials or integrations. Show the full introductory graphic on About only. Top navigation and clear entry links connect the informational page to the engine.

Navigation uses four compact buttons with numbered circles (1–4), icons, one label per step and a highlighted current step. Step 4 is labelled Creative. Keep the steps in one row with horizontal scrolling on narrow screens. Show the full explanatory hero on the landing view. Navigation changes do not imply completion or approval.

Proposal dialogs present audience, objective, market and schedule as a compact brief, with reasoning separate from customer-facing copy. An approved, current proposal can open its matching design in Creative using Go to design. Do not edit creative inside the proposal dialog. Proposal approval and content approval remain separate. Version history explains previous saves; removal is a separately labelled, confirmed action that retains history.

New creative templates include a separate email headline and structured cards for the proposal's selected products only. Do not add unrelated products or invent claims, prices, inventory or performance evidence. Existing saved creative is not silently rewritten. Copy and design currently use templates, not AI synthesis of all company data. Label image links and button destinations in plain language.

For a change to a section, update its inputs, decision rule, output, failure behavior and approval effects here. Mark proposed integrations as future work until they operate through the app. Add a regression check when an incorrect claim, lost edit, or stale approval could recur. Use dated build notes for history and this document for current rules.
