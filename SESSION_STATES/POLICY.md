# Session-state policy
## Work scope
KATEOS_ROOT is kateos/ inside the configured Codex home (default ~/.codex).
Use the explicitly selected project root, or the current repository root when
working in that repository. A generic working directory is not itself a project.
With a project, STATE_DIR is its SESSION_STATES/ directory; read its local
instructions and PROJECT_CONTEXT.md if present. Otherwise STATE_DIR is
KATEOS_ROOT/SESSION_STATES/ and the current request defines the work.
Use only records relevant to that scope; do not import unrelated work from a pointer.
POLICY.md and TEMPLATE.md always come from KATEOS_ROOT/SESSION_STATES/.
For chat sources, resolve these roles from the supplied files and named work scope.
## Resume
Read STATE_DIR/LATEST.md. NONE means no checkpoint has been saved.
An absent directory or pointer means no indexed checkpoint: inspect existing
records if any, and begin from the current request and available project context.
Otherwise the pointer names one record within STATE_DIR. Read it and the current
authoritative sources. A missing named record is an error; report the gap.
Confirm objective, decisions, corrections, valid work, unfinished work,
verification, uncertainty, and next step. Current verified changes govern.
Continue independent work when a required source is unavailable.
## Close
Use the shared TEMPLATE.md. Fill every field with facts or unknown/not-run.
Create STATE_DIR if needed. Use a stable workstream name and the local date.
Choose name_mmdd-aa.md, then ab, ac, through zz: the first unused suffix.
Check prior years too; never overwrite a collision. If all 676 suffixes are
occupied, request a new workstream name. Record the full timestamp and timezone.
Create the record exclusively, reread and verify it, then update STATE_DIR/LATEST.md.
Keep all earlier records; LATEST.md is the only ordinary mutable pointer.
Recheck the pointer before updating; do not replace a newer concurrent checkpoint.
Never reset an active pointer to NONE. Report any conflict.
If saving is unavailable, return the complete record and pointer text with paths;
say saving is pending. A returned message alone is not durable storage.
