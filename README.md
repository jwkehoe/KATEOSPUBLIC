# KateOS Base

KateOS Base is a portable set of working rules and local files for preserving
objectives, source authority, corrections, task state, and recovery checks
across AI-assisted work.

Start with [QUICKSTART.md](QUICKSTART.md). Read
[PUBLIC_BOUNDARIES.md](PUBLIC_BOUNDARIES.md) before installing it into a
provider surface. Use [FIRST_RECOVERY_EXERCISE.md](FIRST_RECOVERY_EXERCISE.md)
to check whether a documented correction governs adjacent and resumed work.

## What is included

- Global and project-level working rules.
- Voice, evidence, recovery, and claim-boundary prompts.
- Operations and evaluation templates.
- Append-only checkpoint policy and template.
- Backup and recovery utilities for local configuration.

## What is excluded

Personal source banks, live session records, provider-memory exports, client
material, credentials, and restricted sources are not part of this repository.

## Local configuration backup

Before a first installation or configuration change, run
`scripts/kateos_backup_config.sh`. It creates a permanent original copy and a
timestamped archive in `~/KATOSBACKUP/`. Use
`scripts/kateos_recover_config.sh` to inspect or restore a named archive.

These utilities handle local files. A provider-side setting still needs a
private backup, read-back, smoke test, and explicit confirmation before change.
