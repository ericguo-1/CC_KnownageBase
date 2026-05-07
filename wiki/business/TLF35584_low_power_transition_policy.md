---
type: business-policy
status: active
policy_area: low-power-transition
owners: []
tags: [TLF35584, low-power, transition, business]
---

# TLF35584 Low-Power Transition Policy

## Policy Statement

For the current project family, low-power entry and exit are treated as observable transition policies with asynchronous interference, not as guaranteed immediate mode changes.

## Why This Policy Exists

The PMIC state machine can redirect or alter low-power transitions when valid wake conditions occur during the transition window. This means the requested target state and the observed resulting state may differ.

## Applicability

This page applies to project variants using the current handwritten driver baseline and relying on PMIC-managed transitions among `NORMAL`, `SLEEP`, `STANDBY`, `WAKE`, `INIT`, and `FAILSAFE`.

## Rules

- Treat low-power transitions as operations with outcomes, not just commands.
- Keep wake handling tied to low-power policy because wake can interrupt or redirect transitions.
- Keep standby-domain availability explicit when reasoning about what remains powered during sleep-related states.
- Avoid documenting a requested low-power state as final truth unless the resulting PMIC state has been observed.
- Include reset and wake side effects when analyzing failed or unexpected low-power transitions.

## Exceptions

- Exact application ownership of all transition requests above the PMIC driver may still depend on ECU-level design documents.
- Different project variants may use only a subset of the PMIC low-power states.

## Signals And Inputs

- requested PMIC state transitions
- wake inputs such as `WAK` and `ENA`
- PMIC observed state
- reset and interrupt side effects during transition windows

## Expected Outputs Or Actions

- Separate "requested mode" from "observed resulting mode" in analysis and documentation.
- Preserve wake and reset context when a low-power transition does not complete as expected.
- Use standby and wake architecture knowledge when diagnosing sleep/standby behavior.

## Related Modules

- [[wiki/concepts/TLF35584_state_machine_and_power_sequencing|TLF35584 State Machine And Power Sequencing]]
- [[wiki/concepts/TLF35584_wake_and_reset_behavior|TLF35584 Wake And Reset Behavior]]
- [[wiki/business/TLF35584_wake_policy|TLF35584 Wake Policy]]
- [[wiki/business/TLF35584_reset_policy|TLF35584 Reset Policy]]

## Related Decisions

- Low-power transition analysis must remain stateful and event-aware rather than assuming that a software request always maps directly to the final PMIC state.

## Sources

- `raw/normalized/manuals/TLF35584/chapters/05_Wake_Function/05_Wake_Function.md`
- `raw/normalized/manuals/TLF35584/chapters/11_State_Machine/11_State_Machine.md`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
