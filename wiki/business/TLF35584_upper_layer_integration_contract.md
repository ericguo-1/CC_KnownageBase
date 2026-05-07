---
type: business-policy
status: active
policy_area: upper-layer-contract
owners: []
tags: [TLF35584, integration, contract, business]
---

# TLF35584 Upper-Layer Integration Contract

## Policy Statement

For the current project baseline, upper layers interact with `Gp_TLF35584` through a small set of staged service interfaces and must respect the driver's periodic execution, mode-request ownership split, and diagnostic reporting model.

## Why This Policy Exists

The driver is not a stateless register proxy. It owns internal state, periodic supervision, watchdog timing, and recovery behavior. Upper layers therefore need a contract that is stricter than “call API and assume the PMIC changed immediately.”

## Applicability

This page applies to the current handwritten `Gp_TLF35584` driver baseline and to application or service layers that invoke its public APIs.

## Rules

- Call `MainFunction` periodically and treat that periodic execution as part of the driver contract.
- Use public interfaces for lifecycle, mode, diagnostics, self-test, and watchdog cooperation rather than bypassing through private assumptions.
- Treat mode request APIs as intent submission, not immediate state guarantees.
- Consume grouped diagnostic outputs through the driver’s reporting interfaces rather than reading raw PMIC meaning independently.
- Keep startup-phase, runtime-phase, and self-test-phase interactions clearly separated in system integration design.

## Exceptions

- Some build variants may not expose every public API in the same way, especially APP-mode dependent interfaces.
- Project-specific service layers may wrap these APIs, but the underlying staged behavior still applies.

## Signals And Inputs

- `Gp_TLF35584_Init()`
- `Gp_TLF35584_MainFunction()`
- `Gp_TLF35584_SetDevSigModeOut()`
- `Gp_TLF35584_GetDevSigDiag()`
- `Gp_TLF35584_GetSystemUnusualReason()`
- `Gp_TLF35584_Bist()`
- `Gp_TLF35584_SetWdgTriggerCondition()`

## Expected Outputs Or Actions

- Keep interface ownership and scheduling expectations explicit in integration documents.
- Separate lifecycle control, diagnostics, and self-test usage in upper-layer design.
- Avoid assumptions that the driver can be used correctly without its periodic execution context.

## Related Modules

- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]
- [[wiki/business/TLF35584_mode_switch_ownership_policy|TLF35584 Mode-Switch Ownership Policy]]
- [[wiki/business/TLF35584_startup_readiness_policy|TLF35584 Startup Readiness Policy]]
- [[wiki/business/TLF35584_diagnostic_reporting_policy|TLF35584 Diagnostic Reporting Policy]]

## Related Decisions

- The driver is integrated as a scheduled supervisory component, not as a one-shot configuration utility.

## Sources

- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.h`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.c`

