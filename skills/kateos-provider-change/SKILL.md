---
name: kateos-provider-change
description: Safely prepare, verify, and if necessary roll back a KateOS-related provider instruction or configuration change. Use for ChatGPT, Codex, or similar external setting changes; do not use for local file edits alone.
---

# KateOS Provider Change

Read `OPERATIONS/PROVIDER_CHANGE_CONTROL.md`,
`PROMPTS/CLAIM_BOUNDARIES.md`, and
`OPERATIONS/RUNTIME_ENVELOPE_TEMPLATE.md` from the configured KateOS root.

Identify the exact provider surface and intended change. Capture and verify a
private backup before proposing an external write. Record the runtime envelope
and prepare a smoke task that can expose a material regression.

Obtain explicit user confirmation immediately before changing an external
provider setting. After the change, read the same surface back and compare the
saved content with the intended content. Stop on a mismatch. Run the smoke task
only after a successful read-back, preserving its inputs, outputs, conditions,
and review through `EVALUATION/RUN_TEMPLATE.md`.

If read-back fails, the user requests reversal, or the smoke task exposes a
material regression the user wants reversed, restore the exact private backup,
read it back, and preserve the resulting record privately. Do not claim that a
local file proves provider placement, runtime application, recovery, or user
acceptance.
