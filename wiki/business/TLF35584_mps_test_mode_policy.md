---
type: business-policy
status: active
policy_area: mps-test-mode
owners: []
tags: [TLF35584, mps, test-mode, business]
---

# TLF35584 MPS Test-Mode Policy

## Policy Statement

For the current project baseline, `MPS` is a real board-controlled signal and `MPS test mode` is a special-purpose control path that must be treated as a constrained operating mode, not as a normal runtime state.

## Why This Policy Exists

The imported callout and driver show that `MPS` is actively wired, polarity is inverted through external hardware, and test-mode handling influences watchdog or ERR-related reset behavior.

## Applicability

This page applies to the current handwritten driver and board baseline where `MPS` is connected and controlled through project callouts.

## Rules

- Treat `MPS normal mode` as the default production path.
- Use `MPS test mode` only in contexts that explicitly require it, such as specific startup or verification flows.
- Keep the external inversion detail visible whenever software and hardware `MPS` behavior are discussed.
- Do not assume that MCU output polarity directly equals PMIC `MPS` pin semantics.
- Tie `MPS` reasoning to reset, watchdog, and self-test context when relevant.

## Exceptions

- Different board variants may implement the external control path differently and would require their own project confirmation.
- Some future products may not expose `MPS` to software in the same way.

## Signals And Inputs

- `MPS`
- `Gp_TLF35584_SetDevMpsMode()`
- `Gp_TLF35584_CalloutMpsTestSupport()`
- PMIC mode and reset context

## Expected Outputs Or Actions

- Keep `MPS` handling documented as a board-aware control path.
- Avoid treating test mode as a casual runtime knob.
- Preserve polarity and usage constraints in design and troubleshooting notes.

## Related Modules

- [[wiki/projects/TLF35584_board_level_hardware_decisions|TLF35584 Board-Level Hardware Decisions]]
- [[wiki/concepts/TLF35584_driver_callout_and_hardware_binding|TLF35584 Driver Callout And Hardware Binding]]
- [[wiki/business/TLF35584_startup_readiness_policy|TLF35584 Startup Readiness Policy]]
- [[wiki/business/TLF35584_bist_usage_policy|TLF35584 BIST Usage Policy]]

## Related Decisions

- `MPS test mode` is treated as a constrained project mechanism, not part of ordinary steady-state application behavior.

## Sources

- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Callout.c`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Callout.h`

