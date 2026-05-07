---
type: business-policy
status: active
policy_area: wake
owners: []
tags: [TLF35584, wake, business]
---

# TLF35584 Wake Policy

## Policy Statement

For the current project family, `TLF35584` wake handling is treated as a system-level wake classification policy rather than a simple PMIC state transition.

## Why This Policy Exists

The PMIC can report different wake-source classes and may redirect low-power transitions when a valid wake arrives. Software therefore needs a policy for how wake causes are interpreted and exposed upward.

## Applicability

This page applies to project variants that use the handwritten `Gp_TLF35584` driver and decode PMIC wake information through the current source baseline.

## Rules

- Treat `WAK` and `ENA` as meaningful wake-source classes in the software contract.
- Interpret `WAK` and `ENA` according to project wiring, not only by generic PMIC capability.
- Assume low-power entry may be interrupted by a valid wake event and that the observed resulting state can differ from the requested target state.
- Treat wake classification as an observable output that may be needed by upper-layer wake analysis.
- Keep standby-domain assumptions explicit when reasoning about who can still detect and propagate wake while the main domain is asleep.

## Exceptions

- The exact external net bound to `WAK` or `ENA` is project-dependent and still needs schematic confirmation for a concrete ECU.
- The current callout baseline does not fully close all wake-confirm paths, so some project variants may report less than the hardware can theoretically distinguish.

## Signals And Inputs

- `WAK`
- `ENA`
- PMIC wake flag information such as `WKSF`
- low-power states such as `STANDBY`, `SLEEP`, and `FAILSAFE`

## Expected Outputs Or Actions

- Report wake-source class upward when available.
- Distinguish requested low-power transition from observed resulting state.
- Preserve enough wake-cause information for later fault or startup analysis.

## Related Modules

- [[wiki/projects/TLF35584_manual_to_source_mapping|TLF35584 Manual To Source Mapping]]
- [[wiki/projects/TLF35584_board_level_hardware_decisions|TLF35584 Board-Level Hardware Decisions]]
- [[wiki/concepts/TLF35584_wake_and_reset_behavior|TLF35584 Wake And Reset Behavior]]
- [[wiki/concepts/TLF35584_application_integration_notes|TLF35584 Application Integration Notes]]

## Related Decisions

- Wake-source interpretation is project-specific and should not be hard-coded as a universal board truth without schematic evidence.

## Sources

- `raw/normalized/manuals/TLF35584/chapters/05_Wake_Function/05_Wake_Function.md`
- `raw/normalized/manuals/TLF35584/chapters/11_State_Machine/11_State_Machine.md`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Callout.c`

