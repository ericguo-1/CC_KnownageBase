---
type: business-policy
status: active
policy_area: diagnostic-reporting
owners: []
tags: [TLF35584, diagnostics, reporting, business]
---

# TLF35584 Diagnostic Reporting Policy

## Policy Statement

For the current project baseline, PMIC diagnostics are reported as grouped software-visible results prepared by the driver, not as raw register snapshots exposed directly to every consumer.

## Why This Policy Exists

The imported source periodically reads PMIC fault information in `MainFunction`, groups it into software structures, and exposes diagnostic data through dedicated interfaces. This is a reporting policy, not only a register-access detail.

## Applicability

This page applies to the current handwritten `Gp_TLF35584` driver and its current public observation and diagnostic interfaces.

## Rules

- Treat driver diagnostic output as processed software-visible evidence.
- Prefer grouped fault records and explicit diagnostic interfaces over ad hoc raw-register interpretation in upper layers.
- Keep periodic diagnostic collection tied to `MainFunction` execution assumptions.
- Preserve the distinction between internal fault capture, grouped software records, and higher-level DEM or DTC mapping.
- Document open gaps where application-side reporting chains are stubbed or not fully closed.

## Exceptions

- The current baseline still contains incomplete or stubbed higher-level reporting paths in some callout areas.
- Future projects may layer additional DEM or UDS mapping above the current grouped driver outputs.

## Signals And Inputs

- `Gp_TLF35584_GetDevSigDiag()`
- grouped software records such as `ErrRecord_au32[]`
- driver error paths such as `DriverErrPath_u32`
- periodic fault collection through `Gp_TLF35584_GetAllFaultRegister()`

## Expected Outputs Or Actions

- Use driver-exposed diagnostic interfaces as the default project diagnostic entry point.
- Correlate grouped diagnostics with wake, reset, and watchdog context when needed.
- Avoid forcing each consumer to decode PMIC register bytes independently.

## Related Modules

- [[wiki/concepts/TLF35584_driver_fault_diagnostics_and_recovery|TLF35584 Driver Fault Diagnostics And Recovery]]
- [[wiki/business/TLF35584_fault_handling_policy|TLF35584 Fault Handling Policy]]
- [[wiki/projects/TLF35584_manual_to_source_mapping|TLF35584 Manual To Source Mapping]]
- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]

## Related Decisions

- Diagnostic consumers should depend on stable grouped software semantics whenever possible instead of low-level PMIC register interpretation.

## Sources

- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.h`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.c`

