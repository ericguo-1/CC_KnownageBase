---
type: business-policy
status: active
policy_area: startup-readiness
owners: []
tags: [TLF35584, startup, readiness, business]
---

# TLF35584 Startup Readiness Policy

## Policy Statement

For the current driver baseline, completion of `Gp_TLF35584_Init()` does not mean the system is already in application-ready normal operation.

## Why This Policy Exists

The imported driver performs a staged startup sequence. After initialization and PMIC checks, the driver enters a software `WAIT_STATE` and defers the move toward runtime normal behavior to later trigger paths and periodic handling.

## Applicability

This page applies to project variants using the current handwritten `Gp_TLF35584` driver and its staged startup model.

## Rules

- Treat `Init complete` as configuration and readiness preparation, not as proof that the PMIC has fully entered its final runtime mode.
- Capture reset and wake-related startup context early, because it is part of later readiness interpretation.
- Keep the distinction between PMIC `INIT` readiness and application-ready `NORMAL` operation explicit in design and debugging.
- Require later mode-transition handling and readback confirmation before claiming that runtime normal state is reached.
- Include watchdog startup handling when reasoning about bring-up timing and readiness.

## Exceptions

- A future driver variant could choose to switch to normal directly during initialization, but that is not the behavior of the current imported baseline.
- ECU-level documents may still impose additional application readiness gates above the PMIC driver.

## Signals And Inputs

- `Gp_TLF35584_Init()`
- PMIC device state readback
- reset and wakeup reason capture
- software states such as `WAIT_STATE`, `PREPARERUN_STATE`, and `RUN_STATE`

## Expected Outputs Or Actions

- Document startup as a staged process.
- Avoid telling upper layers that the PMIC is fully ready only because initialization returned.
- Correlate readiness with observed PMIC state and later transition success.

## Related Modules

- [[wiki/concepts/TLF35584_driver_init_and_main_loop|TLF35584 Driver Init And Main Loop]]
- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]
- [[wiki/business/TLF35584_low_power_transition_policy|TLF35584 Low-Power Transition Policy]]
- [[wiki/business/TLF35584_reset_policy|TLF35584 Reset Policy]]

## Related Decisions

- Startup completion and runtime-normal readiness must stay separated in project reasoning.

## Sources

- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.h`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.c`

