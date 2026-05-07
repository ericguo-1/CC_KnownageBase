---
type: business-policy
status: active
policy_area: safe-state
owners: []
tags: [TLF35584, safe-state, business]
---

# TLF35584 Safe-State Policy

## Policy Statement

For the current project family, `SS1` is treated as the primary software-visible safe-state indication, while `SS2` is an optional secondary path used only when a staged or delayed shutdown strategy is required.

## Why This Policy Exists

The PMIC supports `SS1` and `SS2`, but the current project baseline observes `SS1` directly in software and does not independently sample `SS2`. Project clarification also shows that `SS2` is not a universal requirement and is mainly useful for delayed shutdown scenarios.

## Applicability

This page applies to the current handwritten `Gp_TLF35584` driver baseline and project variants that keep the current callout and configuration structure.

## Rules

- Treat `SS1` as the primary software-confirmed safe-state output.
- Treat `SS2` as optional unless the project explicitly requires a staged shutdown strategy.
- Treat safe-state behavior as a configured policy influenced by watchdog thresholds, ERR monitoring, and PMIC supervision settings.
- Do not assume that all ECU variants populate or independently validate `SS2`.
- Keep PMIC safe-state configuration and application-side safety-chain ownership clearly separated in analysis and documentation.

## Exceptions

- A future project variant may actively use `SS2` and would then need a dedicated project page or an update to this policy.
- Some end-to-end safety-chain validation above the PMIC layer is still outside the currently imported software baseline.

## Signals And Inputs

- `SS1`
- `SS2`
- `ERR`
- watchdog error thresholds
- PMIC safe-state related configuration in protected registers

## Expected Outputs Or Actions

- Use `SS1` as the primary observable proof that safe state was asserted.
- Analyze `SS2` only when the project explicitly depends on staged shutdown timing.
- Treat safe-state assertion as part of fault and watchdog escalation analysis rather than as an isolated IO event.

## Related Modules

- [[wiki/concepts/TLF35584_safe_state_control|TLF35584 Safe State Control]]
- [[wiki/projects/TLF35584_board_level_hardware_decisions|TLF35584 Board-Level Hardware Decisions]]
- [[wiki/concepts/TLF35584_driver_callout_and_hardware_binding|TLF35584 Driver Callout And Hardware Binding]]
- [[wiki/business/TLF35584_fault_handling_policy|TLF35584 Fault Handling Policy]]

## Related Decisions

- Current projects simplify software-side safe-state confirmation to `SS1` unless a delayed-shutdown design explicitly justifies `SS2`.

## Sources

- `raw/normalized/manuals/TLF35584/chapters/12_Safe_State_Control_Function/12_Safe_State_Control_Function.md`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Callout.c`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.h`

