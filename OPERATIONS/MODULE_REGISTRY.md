# KateOS module registry

The global core is always in force. Read only the additional module needed for
the task. A module may add task-specific discipline; it cannot override higher
authority, evidence boundaries, source restrictions, or current user direction.

| Class | Module or source | Activate when | Do not use as |
|---|---|---|---|
| Kernel-required | `GLOBAL_CORE.md`, `PROMPTS/VOICE_RULES.md`, `PROMPTS/ANTI_PATTERNS.md`, `PROMPTS/CLAIM_BOUNDARIES.md`, `SESSION_STATES/POLICY.md` | Every KateOS task | Proof of host or provider behavior |
| Task-activated | `PROMPTS/HUMANIZER.md` | The user asks to humanize or naturally revise a draft | Permission to change claims, authorship, or evidence |
| Task-activated | `PROMPTS/RECOVERY.md` | Repeated drift, continuity fracture, or explicit realignment | Proof that hidden state or a prior model instance returned |
| Task-activated | `EVALUATION/` | A response, configuration, or work pattern needs a scored review | A completed behavioral result without preserved inputs and outputs |
| Task-activated | `OPERATIONS/RUNTIME_ENVELOPE_TEMPLATE.md` | Recovery, evaluation, provider or instruction changes, or a status claim about active/tested/recovered behavior | Mandatory paperwork for an ordinary answer |
| Task-activated | `OPERATIONS/RECOVERY_INVENTORY_TEMPLATE.md` | Reconstructing a configuration, a material work state, or a deployment boundary | A substitute for a current task-state checkpoint |
| Task-activated | `OPERATIONS/PROVIDER_CHANGE_CONTROL.md` and `$kateos-provider-change` | Changing a real provider instruction, personalization, project setting, or related external configuration | Authorization to change a provider surface without a private backup, read-back, and fresh confirmation |
| Operator-required | Private sources, visual canon, restricted client material, prior-chat records | The user names the source or the task requires it and access is authorized | Shared fact, public source, or general project context |
| Separate | Provider backups, placement records, raw transcripts, evaluation run bundles | A named deployment or evaluation workflow | Always-loaded model instructions |
| Excluded | Superseded, unavailable, or unauthorized sources | Never, unless current authority restores them | Evidence of continuity or permission |

For every task-activated or operator-required module, record its name in the
task state or run record when it materially affected the result.
