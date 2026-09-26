# Provider change control

Use this control before changing a real provider instruction, personalization,
project setting, or other external configuration that can alter KateOS behavior.
It governs account, project, and provider surfaces; it does not apply to a
local source-file edit by itself.

## Boundary

Preparation is allowed within the task. The external write requires explicit
user confirmation immediately before it happens. Do not treat approval to
draft, inspect, back up, or compare settings as approval to change them.

Never place credentials, private memory exports, restricted client material, or
unredacted personal data in a project repository, public artifact, or ordinary
task checkpoint.

## Prepare

1. Name the provider, account or project surface, intended change, and reason.
2. Read `RUNTIME_ENVELOPE_TEMPLATE.md`; record the known and unknown conditions.
3. Capture the complete prior setting and relevant surrounding configuration in
   a private, user-controlled backup location outside a source-controlled
   project. Record the capture method, time, target surface, and completeness.
4. Reopen the backup and confirm it is readable before proposing the change.
5. Prepare the exact replacement content and a short smoke task that could
   reveal a material regression.
6. State the target, backup location, expected consequence, and rollback path.
   Ask for confirmation immediately before the external write.

## Change and read back

1. Change only the confirmed provider surface.
2. Reopen that same surface and record what was saved. Check for truncation,
   formatting changes, placement in the wrong account or project, or a failed
   save.
3. If the saved content differs from the intended content, stop. Preserve the
   evidence and tell the user; do not claim placement or active behavior.
4. Run the named smoke task only after successful read-back. Preserve its input,
   output, runtime conditions, and review in an evaluation run record.

## Roll back

Roll back when the user directs it, read-back fails, or the smoke task shows a
material regression that the user wants reversed.

1. Restore the exact private backup to the same provider surface.
2. Reopen the surface and verify the restored content.
3. Record the affected change, the rollback time, the check performed, and
   remaining uncertainty.
4. Preserve the failed candidate, test output, and backup evidence privately.
   Do not erase evidence merely because the previous setting was restored.

## Claim boundary

A local replacement file is not a provider change. A saved provider setting is
not proof of behavior. A smoke task is not proof of recovery or broad
acceptance. Use the claim-boundary terms and record only what the evidence
supports.
