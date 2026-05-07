---
type: business-policy
status: active
policy_area: mode-switch
owners: []
tags: [TLF35584, mode-switch, business]
---

# TLF35584 Mode-Switch Ownership Policy

## Policy Statement

For the current project baseline, upper layers own the request for PMIC mode change, while the driver owns the execution, sequencing, retry, and observed-state confirmation of that request.

## Why This Policy Exists

The imported source shows that mode requests enter through public APIs, but the actual switching logic is performed asynchronously through internal runtime handling and validated by PMIC readback.

## Applicability

This page applies to the current handwritten `Gp_TLF35584` driver and the public mode-related interfaces it exposes.

## Rules

- Treat upper-layer mode requests as intents, not guaranteed final results.
- Let the driver own paired register writes, protected access sequences, retry behavior, and actual PMIC state verification.
- Keep requested mode and observed resulting mode separate in analysis, logs, and documentation.
- Preserve the driver software state machine as part of the mode-switch contract.
- Do not bypass driver-controlled mode paths with ad hoc register writes in project reasoning or future extensions.

## Exceptions

- Some direct low-level helper paths exist inside the driver, but they are internal implementation detail rather than application-owned behavior.
- Future platform variants may add more explicit mode orchestration at ECU level, but the current baseline still relies on driver-controlled execution.

## Signals And Inputs

- `Gp_TLF35584_SetDevSigModeOut()`
- internal `SetMode_u8`
- `Gp_TLF35584_RtSetMode()`
- PMIC state readback
- software states such as `PREPARERUN_STATE` and `RUN_STATE`

## Expected Outputs Or Actions

- Keep ownership boundaries explicit between requester and executor.
- Confirm mode-switch success from observed PMIC state, not from API request alone.
- Include retry and error-state behavior in mode-switch documentation.

## Related Modules

- [[wiki/concepts/TLF35584_driver_init_and_main_loop|TLF35584 Driver Init And Main Loop]]
- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]
- [[wiki/projects/TLF35584_manual_to_source_mapping|TLF35584 Manual To Source Mapping]]
- [[wiki/business/TLF35584_startup_readiness_policy|TLF35584 Startup Readiness Policy]]

## Related Decisions

- Mode-change ownership is intentionally split: upper layer decides "what", driver owns "how" and "whether it really happened".

## Sources

- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.h`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.c`

