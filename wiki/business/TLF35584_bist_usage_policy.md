---
type: business-policy
status: active
policy_area: bist
owners: []
tags: [TLF35584, bist, self-test, business]
---

# TLF35584 BIST Usage Policy

## Policy Statement

For the current project baseline, `BIST` is treated as a controlled startup-phase verification activity rather than a routine runtime service.

## Why This Policy Exists

The imported source explicitly recommends calling `Gp_TLF35584_Bist()` only during cold power-on and suggests retry logic when it returns not OK. The implemented BIST flow also touches watchdog, analog safety-path, and optional ERR-related checks.

## Applicability

This page applies to project variants using the current handwritten `Gp_TLF35584` driver and its public `Gp_TLF35584_Bist()` interface.

## Rules

- Treat `BIST` as a startup-phase or dedicated service-phase action, not a periodic runtime API.
- Prefer invoking `BIST` only when system conditions match the driver assumptions, especially around cold power-on.
- Use retry logic when `BIST` fails if the project accepts transient SPI or supply disturbance as a plausible cause.
- Keep `BIST` result interpretation separate from normal runtime diagnostic reporting.
- Document which BIST subfunctions are actually enabled by configuration in the concrete project baseline.

## Exceptions

- Some BIST branches are compile-time controlled and may be disabled in the current project configuration.
- A project-specific service or factory mode may define additional allowed BIST windows, but that is outside the current imported baseline.

## Signals And Inputs

- `Gp_TLF35584_Bist()`
- `GP_TLF35584_ANA_BIST_ENABLE`
- `GP_TLF35584_FWD_BIST_ENABLE`
- `GP_TLF35584_WWD_BIST_ENABLE`
- `GP_TLF35584_ERR_BIST_ENABLE`
- `BistErrPath_u32`

## Expected Outputs Or Actions

- Use `BIST` as a controlled confidence check of safety-related paths.
- Preserve BIST-specific fault interpretation rather than merging it blindly into ordinary runtime faults.
- Keep startup sequencing and reset-context assumptions visible when documenting BIST behavior.

## Related Modules

- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]
- [[wiki/business/TLF35584_startup_readiness_policy|TLF35584 Startup Readiness Policy]]
- [[wiki/business/TLF35584_safe_state_policy|TLF35584 Safe-State Policy]]
- [[wiki/business/TLF35584_fault_handling_policy|TLF35584 Fault Handling Policy]]

## Related Decisions

- The project treats self-test as a controlled phase activity, not as a generic always-available service.

## Sources

- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.h`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.h`

