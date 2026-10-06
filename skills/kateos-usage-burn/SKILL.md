---
name: kateos-usage-burn
description: Track and review KateOS subscription allowance burn in Codex, Work, or Chat, and project remaining runway or project usage from measured snapshots. Use for allowance, burn-rate, and resource reviews; excludes API billing estimates.
---

# KateOS usage burn

Locate the current KateOS checkout. Read `MODULES/resource-governance/USAGE_BURN.md` before capture or review. If unavailable, report the gap and give only a current read-only usage snapshot; do not invent history. Keep local ledgers in that checkout's Git-ignored `LOCAL/usage-burn/`.

For Codex/Work, obtain fresh `get_usage_limits` data and pass the JSON to `python3 scripts/usage_burn.py capture --pool codex-work --project <workstream> --source codex-usage-tool` via stdin. Resolve the tool response's JSON text first; do not persist raw output. Add known model, effort, speed, concurrency, outcome, and completed units using matching flags. Values are metadata, not verified attribution. Unknown values stay unknown. Use the actual observation timestamp when importing an older readout.

For ordinary Chat, use only accessible observed UI counters or explicitly user-reported counters, with source and timestamp; record in a separate pool using the module's manual shape. If no quota surface is available, say Chat burn is unknown. Do not browse or scrape credentials to obtain it.

Use `python3 scripts/usage_burn.py review --pool codex-work`, optionally `--planned-hours <hours>` and `--reserve-percent <percent>`. Show remaining allowance, observed interval burn, percentage points/hour, reserve runway, project estimate, and what the project produced. A baseline alone cannot produce a rate. Mention stale snapshots, resets, coarse counter resolution, model changes, and concurrent account usage where material. If a planned period crosses a reset, describe it as a scenario rather than a measured schedule forecast.

During substantial work governed by KateOS, capture at start, milestones, and close per the module. Keep routine captures quiet; flag meaningful changes, reserve risk, or a user-requested review. Never purchase credits, consume reset credits, or change plans/model settings as part of a review. Installation makes this skill discoverable; it does not install a host-wide background collector or deploy instructions to ChatGPT.
