---
type: business-policy
status: active
policy_area: fault
owners: []
tags: [TLF35584, faults, diagnostics, business]
---

# TLF35584 Fault Handling Policy

## Policy Statement

For the current project baseline, PMIC faults are handled as grouped system-diagnostic evidence with staged clearing, recovery attempt, debounce, and retained software-visible fault records.

## Why This Policy Exists

The imported driver does not treat PMIC flags as one-shot bytes. It refreshes, groups, clears, retries, and only then locks in software-visible error paths. That makes fault handling part of the product supervision policy.

## Applicability

This page applies to the current `Gp_TLF35584` handwritten driver and the current fault-recording baseline visible in source.

## Rules

- Treat raw PMIC fault flags as input evidence, not as the final diagnostic language exposed upward.
- Attempt controlled clearing and mode restoration before declaring a persistent grouped software fault when the implementation supports it.
- Use debounce or threshold logic before locking in repeated faults as persistent records.
- Preserve grouped fault information for later root-cause analysis instead of forcing every consumer to decode raw PMIC registers.
- Protect fault-snapshot consistency during critical updates.

## Exceptions

- End-to-end DEM, DTC, or UDS mapping is not fully closed in the currently imported baseline.
- Some higher-level application reactions may still live outside the handwritten driver and need separate ECU-level documents.

## Signals And Inputs

- PMIC flag registers
- PMIC status registers
- grouped software error paths such as `DriverErrPath_u32`, `BistErrPath_u32`, and `ErrRecord_au32[]`
- mode-restoration attempts after selected faults

## Expected Outputs Or Actions

- Maintain grouped software-visible fault records.
- Correlate faults with reset, watchdog, and wake analysis when troubleshooting abnormal startup or shutdown behavior.
- Distinguish transient faults from thresholded persistent faults.

## Related Modules

- [[wiki/concepts/TLF35584_monitoring_and_fault_reactions|TLF35584 Monitoring And Fault Reactions]]
- [[wiki/concepts/TLF35584_driver_fault_diagnostics_and_recovery|TLF35584 Driver Fault Diagnostics And Recovery]]
- [[wiki/concepts/TLF35584_driver_callout_and_hardware_binding|TLF35584 Driver Callout And Hardware Binding]]
- [[wiki/projects/TLF35584_manual_to_source_mapping|TLF35584 Manual To Source Mapping]]

## Related Decisions

- Grouped software fault semantics are preferred over forcing every consumer to reason directly from raw PMIC status bytes.

## Sources

- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/normalized/manuals/TLF35584/chapters/14_Interrupt_Generation/14_Interrupt_Generation.md`
- `raw/normalized/manuals/TLF35584/chapters/16_Application_Information/16_Application_Information.md`

