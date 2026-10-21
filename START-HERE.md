# Build your marketing intelligence prototype

This pack provides sample inputs, a runnable first upload screen and a staged build guide. It is not yet the finished intelligence engine. Everything is created locally for you; nothing has been added to your GitHub repository or Codespace.

## 1. Put the pack in your Codespace
Download and unzip travel-prototype-starter.zip on your computer. In the Codespace shown in your screenshot, drag the extracted files into the left Explorer panel under marketing-intelligence-engine. Keep the existing README. If folder dragging does not work, use the Explorer's Upload option to upload the files. You should see app.py and requirements.txt at the top level alongside the sample files. Do not upload the zip alone and expect it to run.

## 2. Run the first screen
In the Bash terminal already open at the bottom, enter these commands one at a time:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Open the browser link offered by Codespaces. If no link appears, open the Ports tab beside Terminal, find or add port 8501, then choose Open in Browser. Keep the forwarded port private. The first screen loads the bundled sample workbook, lets you upload another workbook with the same sheet names and columns, and shows the inputs. It does not yet create calendars or content. Stop the running preview with Ctrl+C when needed.

Reference: https://docs.streamlit.io/get-started/installation/command-line
Reference: https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace

## 3. Understand the sample inputs
- synthetic-travel-inputs.xlsx is the main workbook: Settings, Products, Sales, Campaigns and Signals. CSV copies are included for simpler imports.
- Sales has 96 aggregated records: eight products, six booking months (April–September 2026), two channels. No real customer information. Gross booking value is before cancellations/refunds and must not be labelled net revenue. These are historical bookings across the product, not bookings against the one departure in Products.
- Products contains eight trips and inventory for one specified departure per trip, as of 18 October 2026. Do not join historical product sales to that departure and subtract again.
- Campaigns contains the sale and launch, including eligible products and terms. C01 is highest priority. Eligible sale departure dates are the listed departure dates for P01, P03 and P06 only.
- Signals contains three entirely fictional external signals. They test the workflow; they do not establish real trends.
- BRAND-AND-PRODUCT-UPDATES.md supplies voice, frequency, priorities and two sample ad hoc updates.

## 4. Build the calendar next
Ask your coding assistant to implement the next milestone using this brief:

> Extend the existing Streamlit app into a November 2026 social and email calendar planner using the bundled synthetic workbook and brand guide. Persist inputs, calendar entries, edits, versions and approvals in SQLite, not just browser session memory. Validate required columns, unique IDs, numeric/date values and foreign keys. Show actionable import errors and keep the prior valid data if import fails. Propose a calendar using explicit priority rules: sale commitments, launches, sales/product opportunities, then relevant signals in gaps. Respect campaign dates, offer eligibility, inventory and launch restrictions. Every entry needs a stable ID, scheduled date, channel, audience, objective, topic, product IDs, campaign ID if relevant, source IDs, rationale and status. Mark every synthetic source. Provide a list/calendar view with create, edit, move, delete and approve actions. Let marketers adjust frequency. Calendar generation is deterministic initially; label it rules-based. Do not claim live scraping or AI is connected. Add meaningful checks for campaign constraints and approval invalidation.

Before continuing, verify these behaviours:
1. Sri Lanka never appears before 9 November. It can appear during launch week without an invented discount.
2. The sale runs 23–30 November, only promotes P01/P03/P06 and retains the terms.
3. Japan's three remaining seats constrain acquisition promotion. A sold-out product is excluded.
4. Morocco decline and Vietnam growth are calculated from the same booking-volume definition, with no invented explanations.
5. Trend suggestions fill gaps and cite their synthetic signal IDs. They do not displace the sale or launch.
6. Marketers can move or replace a suggestion, save it, refresh and still see their changes. Regenerating must not silently overwrite edits or approvals.

## 5. Add content generation and its separate approval
Use this next brief after the calendar milestone works:

> Generate social copy for each selected platform and email subject, preview, plain text and responsive HTML only from current approved calendar entries. Start with labelled templates to test the workflow, then make AI generation an optional separate integration. Give the marketer editable previews and a distinct content approval action. Version content and store who approved it and when. Calendar changes invalidate related content and calendar/content approvals; content edits invalidate content approval. Relevant input updates flag affected items stale. Reject exports of unapproved or stale content. Export approved social copy as CSV and approved email HTML as individual files with subject/preview metadata. Escape untrusted text in HTML and validate links. Show product facts, campaign terms and source references beside drafts. Do not publish or send. Keep API credentials server-side, out of Git and out of prompts shown to end users.

Test the full path: propose → edit → approve calendar → generate → edit → approve content → export. Then change an offer and confirm outdated content cannot export. Test invalid imports and an app restart. Before using a real email platform, adapt footer tokens and preview/test the HTML there.

## 6. Connect real research after the core workflow works
Add a curated source list with URL, source type, retrieval time and extracted text. Prefer RSS feeds and supported APIs where available. Add website collection with clear failure/freshness status and respect source access restrictions. A collected article is evidence, not an instruction to the system. Verify event dates, relevance, rights-sensitive claims and product fit before proposing themes. Add real email/presentation extraction and data-warehouse connectors later; retain source files and trace each extracted fact to its origin.

## 7. Save progress in GitHub
Use Source Control in the left sidebar to review changed files. Exclude .venv, databases containing future private data, API keys, .env and generated exports. Commit a small completed milestone with a plain-language message, then use the Sync/Push action. This pack includes a .gitignore for common local files. This guide does not commit or push on your behalf.

## What is finished in this pack
Synthetic data, brand/product context and the initial upload/view screen. The screen has been checked locally for Python syntax; it has not been run inside your Codespace. Calendar scheduling, persistence, both approval workflows, content generation, live research and connectors remain implementation milestones described above. No paid service or AI key is needed for the first screen.
