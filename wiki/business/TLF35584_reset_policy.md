---
type: business-policy
status: active
policy_area: reset
owners: []
tags: [TLF35584, reset, business]
---

# TLF35584 Reset Policy

## Policy Statement

For the current project baseline, PMIC reset behavior is treated as a system-readiness and fault-escalation policy, not only as a hardware side effect.

## Why This Policy Exists

Reset release and reset assertion are tied to sequencing completion, watchdog quality, undervoltage supervision, and fault escalation. Software must therefore reason about reset as part of system state, not as an isolated signal.

## Applicability

This page applies to the current `Gp_TLF35584` driver baseline and project variants that rely on PMIC-side supervision for reset-related behavior.

## Rules

- Treat `ROT` release as a readiness milestone after valid startup sequencing, not merely as a passive electrical event.
- Treat reset causes as part of system fault analysis whenever watchdog escalation, undervoltage, or supervision faults are involved.
- Distinguish between a requested mode transition and the transition actually observed after PMIC supervision and reset logic act.
- Keep reset interpretation tied to wake, watchdog, and fault context when diagnosing startup problems.
- Preserve project-specific distinctions between generic PMIC reset capability and the subset actually used by the product.

## Exceptions

- The current normalized set does not yet provide a fully clean dedicated reset chapter view, so some reset details remain inferred from adjacent chapters and source behavior.
- End-to-end application-side reset policy above the PMIC boundary may still need ECU-level documents.

## Signals And Inputs

- `ROT`
- watchdog escalation
- undervoltage and supervision flags
- PMIC state-machine transitions

## Expected Outputs Or Actions

- Use reset-related observations as part of startup and abnormal-reason analysis.
- Correlate reset with wake source, watchdog state, and grouped fault information where possible.
- Avoid documenting reset as a standalone event without its triggering context.

## Related Modules

- [[wiki/concepts/TLF35584_wake_and_reset_behavior|TLF35584 Wake And Reset Behavior]]
- [[wiki/concepts/TLF35584_monitoring_and_fault_reactions|TLF35584 Monitoring And Fault Reactions]]
- [[wiki/concepts/TLF35584_driver_fault_diagnostics_and_recovery|TLF35584 Driver Fault Diagnostics And Recovery]]
- [[wiki/projects/TLF35584_manual_to_source_mapping|TLF35584 Manual To Source Mapping]]

## Related Decisions

- Reset must be analyzed together with supervision and watchdog context rather than split into a separate isolated troubleshooting path.

## Sources

- `raw/normalized/manuals/TLF35584/chapters/07_Reset_Function/07_Reset_Function.md`
- `raw/normalized/manuals/TLF35584/chapters/11_State_Machine/11_State_Machine.md`
- `raw/normalized/manuals/TLF35584/chapters/15_Window_Watchdog_And_Functional_Watchdog/15_Window_Watchdog_And_Functional_Watchdog.md`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`

