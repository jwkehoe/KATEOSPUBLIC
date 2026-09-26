# KateOS Base: first recovery exercise

This exercise tests whether a documented correction governs adjacent work and a
later resumption. It does not test hidden memory, a provider's internal state,
or broad model quality.

## Materials

- A source file that says Atlas is a prototype and not a production deployment.
- A draft that calls Atlas a production deployment.
- A project context and an empty or existing state directory.

## Run

1. Ask the assistant to inspect the source and draft, identify the conflict,
   and revise the draft.
2. Check that the revision says "prototype" and removes the production claim.
3. Ask for an adjacent artifact: a brief status note or a second paragraph that
   describes Atlas.
4. Check that the same distinction governs that artifact.
5. Save a checkpoint naming the authoritative source, the binding correction,
   the revised work, and the next safe action.
6. Start a fresh session. Supply or open the source, project context, and latest
   checkpoint. Ask for a resumed revision or status note.
7. Check whether the prototype distinction still governs the resumed work.

## Record

Use `EVALUATION/RUN_TEMPLATE.md` when recording this as an evaluation. Preserve:

```text
Date, time, timezone:
Interface and model:
Instruction surface and supplied files:
Prompt or task:
Exact first revision:
Exact adjacent artifact:
Checkpoint used at resumption:
Exact resumed artifact:
Result: held, failed, partial, or not tested
Known limits and unknown conditions:
```

## Interpret the result

- **Held:** the correction governs both adjacent and resumed work, with the
  source and checkpoint available under recorded conditions.
- **Partial:** the correction holds beside the first revision but fails after
  resumption, or the resumed task required a material reminder.
- **Failed:** the assistant repeats the production claim, ignores the source,
  or loses the correction in adjacent work.
- **Not tested:** a needed source, checkpoint, output, or session condition is
  missing.

A held result is one observed recovery check. It is not proof of broad,
long-horizon continuity. Preserve the record and repeat the exercise on work
that matters to you.
