# KateOS Base, in plain English

KateOS is a way to keep AI-assisted work from wandering off and making you
repeat yourself. It gives the assistant standing rules, gives each project its
own facts and decisions, and leaves a paper trail when work must continue later.

It is not a new AI model. It is not a promise that an AI remembers everything.
It is not proof that a provider saved your settings. It is a set of files and a
way of using them carefully.

## The basic idea

Think of it as three notebooks:

1. **House rules** — how the assistant should reason, write, use sources, and
   handle mistakes.
2. **Project notebook** — what this job is, which facts control it, and what
   has already been decided.
3. **Bookmark** — where work stopped and what needs to happen next.

The goal is simple: less time spent putting the assistant back on the rails.

## Start here

| File | What it does |
|---|---|
| `README.md` | The front door: what this repository contains. |
| `PUBLIC_BOUNDARIES.md` | Says what KateOS can help with and what it cannot prove. |
| `QUICKSTART.md` | Shows a small first setup and example. |
| `FIRST_RECOVERY_EXERCISE.md` | Tests whether one correction still holds later. |
| `CONTINUITY_FRACTURE_V2_KATEOSPUBLIC.md` | The longer explanation plus exact copies of the public source files. |

## The house rules

| File | What it does |
|---|---|
| `AGENTS.md` | Tells a coding agent which shared KateOS files to read and when. |
| `GLOBAL_CORE.md` | The standing rules: inspect evidence, respect scope, correct mistakes, and say what is known. |
| `PROJECT_CONTEXT.md` | A fill-in-the-blanks page for one project’s goal, sources, decisions, and next step. |
| `PROMPTS/VOICE_RULES.md` | Keeps the writing direct, useful, and human. |
| `PROMPTS/ANTI_PATTERNS.md` | Lists bad habits to catch: filler, fake certainty, and corporate fog. |
| `PROMPTS/CLAIM_BOUNDARIES.md` | Explains the difference between a file existing, being used, being tested, and being accepted. |
| `PROMPTS/HUMANIZER.md` | Helps revise writing without inventing experience or changing its meaning. |
| `PROMPTS/RECOVERY.md` | What to do when the work has drifted and needs to be rebuilt from evidence. |
| `PROMPTS/EVALUATION_CRITERIA.md` | A plain checklist for judging a response or draft. |

## The project bookmark

| File | What it does |
|---|---|
| `SESSION_STATES/POLICY.md` | Says where checkpoints live and how to resume them. |
| `SESSION_STATES/TEMPLATE.md` | The form used to save a checkpoint: goal, sources, decisions, work done, unknowns, and next step. |

Do not overwrite the old bookmark. Make a new one. That lets you see what
changed and go back to a known point if needed.

## Extra tools, used only when needed

| File | What it does |
|---|---|
| `OPERATIONS/MODULE_REGISTRY.md` | Says which extra tools belong to which kind of task. |
| `OPERATIONS/RUNTIME_ENVELOPE_TEMPLATE.md` | Records the model, setting, files, tools, and unknowns when those details matter. |
| `OPERATIONS/RECOVERY_INVENTORY_TEMPLATE.md` | Lists what can and cannot be rebuilt after a break. |
| `OPERATIONS/PROVIDER_CHANGE_CONTROL.md` | The safety checklist for changing ChatGPT, Codex, or another provider’s settings. |
| `skills/kateos-provider-change/SKILL.md` | The reusable instruction for following that provider-change checklist. |

These are not chores for every question. Use them when changing settings,
testing behavior, or recovering important work.

## Checking whether it worked

| File | What it does |
|---|---|
| `EVALUATION/TEST_1.md` through `TEST_5.md` | Five sample tests for reasoning, evidence, collaboration, correction, and opening a new working relationship. |
| `EVALUATION/SUITE_RULES.md` | Explains how to score those tests without treating a score as magic. |
| `EVALUATION/RUN_TEMPLATE.md` | Records what was tested, under which conditions, and what remains unknown. |

## Backup and recovery

| File | What it does |
|---|---|
| `config/COPY_BEFORE_FIRST_INSTALL_KEEP_FOREVER.conf` | Says the first copy of a configuration must be kept and never overwritten. |
| `scripts/kateos_backup_config.sh` | Makes that permanent first copy and a timestamped copy for each later change. |
| `scripts/kateos_recover_config.sh` | Lists or restores a backup. It refuses to overwrite an existing target unless you explicitly say to replace it. |

By default, backups live in `~/KATOSBACKUP/`, not in this public repository.

## The one sentence version

KateOS helps you keep the rules, the current job, and the place you stopped in
separate places—then check whether they still shape the work.
