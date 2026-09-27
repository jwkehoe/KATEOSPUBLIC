# KateOS Base

KateOS Base is a portable set of working rules and local files for preserving
objectives, source authority, corrections, task state, and recovery checks
across AI-assisted work.

Start with [QUICKSTART.md](QUICKSTART.md). Read
[PUBLIC_BOUNDARIES.md](PUBLIC_BOUNDARIES.md) before installing it into a
provider surface. Use [FIRST_RECOVERY_EXERCISE.md](FIRST_RECOVERY_EXERCISE.md)
to check whether a documented correction governs adjacent and resumed work.
For a short, plain-language map of the files, read
[README_ELI10.md](README_ELI10.md).

## License and use

KateOS Base is source-available under the
[EP Public Review and Individual-Use License v1.0](LICENSE.md). An individual
may read, inspect, and use it privately for that person's own local work.

Commercial use requires written permission from Exotic Problems LLC. That
includes resale, redistribution, consulting, training, enterprise use, and
hosting or including KateOS in a cloud, SaaS, API, managed-service, or other
third-party offering. Read [COMMERCIAL_LICENSING.md](COMMERCIAL_LICENSING.md)
before proposing that kind of use. Name and logo use is covered by
[TRADEMARKS.md](TRADEMARKS.md).

The Materials are provided as is, without warranty, and are not professional
advice. The complete terms are in [LICENSE.md](LICENSE.md).

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
