# KateOS Base: clean-start quickstart

This guide creates one small local project. It does not change a provider
setting, upload a file, or claim that any instruction is active outside the
files you can inspect.

## 1. Copy the Base files

Keep the global core in your configured Codex home, normally `~/.codex`:

```text
~/.codex/
|-- AGENTS.md
`-- kateos/
    |-- GLOBAL_CORE.md
    |-- PROJECT_CONTEXT.md
    |-- PROMPTS/
    |   |-- VOICE_RULES.md
    |   |-- ANTI_PATTERNS.md
    |   `-- CLAIM_BOUNDARIES.md
    |-- OPERATIONS/
    |   `-- MODULE_REGISTRY.md
    `-- SESSION_STATES/
        |-- POLICY.md
        `-- TEMPLATE.md
```

Use the provider's documented instruction surface if you want it to receive
the global core. Treat that as a separate provider change: preserve the prior
setting, read back what was saved, and test it before calling it active.

## 2. Create one project

Make a small directory with a source, a project context, and room for state:

```text
prototype-review/
|-- AGENTS.md                 (optional local rules)
|-- PROJECT_CONTEXT.md
|-- source.md
|-- draft.md
`-- SESSION_STATES/
```

Put only the facts for this work in `PROJECT_CONTEXT.md`: objective,
authoritative sources, known decisions, constraints, and next step.

## 3. Use the included example

In `source.md`:

```markdown
# Atlas review

Atlas is a prototype. It has been demonstrated to internal reviewers.
It has not been deployed to production.
```

In `draft.md`:

```markdown
Atlas is a production deployment that now serves internal reviewers.
```

Ask the assistant to inspect both files and revise the draft so it agrees with
the source. The expected correction is narrow: Atlas is a prototype, not a
production deployment.

## 4. Preserve the correction

Save a new checkpoint in `SESSION_STATES/`. Record the source, the correction,
the revised draft, what remains unfinished, and the next safe action. Do not
overwrite an earlier checkpoint.

## 5. Resume and check

In a fresh session, supply or open the project context, the source, and the
latest checkpoint. Ask for an adjacent revision, such as a one-paragraph status
note about Atlas.

The check is whether the prototype distinction governs the new work without
having to be rediscovered from scratch. If it does not, record the failure and
repair the source, state, or workflow that left the correction out.

For a structured version of this check, use `FIRST_RECOVERY_EXERCISE.md`.
