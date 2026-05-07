---
type: business-policy
status: active
policy_area: err-monitoring
owners: []
tags: [TLF35584, err, monitoring, business]
---

# TLF35584 ERR Monitoring Policy

## Policy Statement

For the current project baseline, PMIC-side `ERR` monitoring is configured as part of the safety policy, but the end-to-end application-side `SMU/ERR` validation chain is not fully closed in the imported software baseline.

## Why This Policy Exists

The safe-state and board-level pages show that `ERR` participates in PMIC safety behavior, while configuration evidence shows `ERRRECEN` is active but `SMU_CONFIG_ENABLE` and `ERR_BIST_ENABLE` are disabled in the current baseline.

## Applicability

This page applies to the current handwritten driver, current configuration baseline, and projects that inherit the same PMIC-side `ERR` setup.

## Rules

- Treat `ERR` monitoring as a real PMIC safety-policy input.
- Distinguish PMIC-side `ERR` configuration from a fully validated ECU-wide safety chain.
- Do not claim full end-to-end `ERR` supervision coverage unless board and application evidence confirm it.
- Keep `ERR` discussion linked to safe-state consequences and watchdog/fault escalation.
- Document whether a project variant only configures PMIC-side reaction or also closes the application-side alive-monitoring contract.

## Exceptions

- Future projects may enable additional `SMU` or `ERR` validation flows and would then need updated project evidence.
- The current imported software baseline does not prove the whole external safety chain.

## Signals And Inputs

- `ERR`
- `GP_TLF35584_REG_SYSPCFG1_ERRRECEN`
- `GP_TLF35584_REG_SYSPCFG1_ERRREC`
- `GP_TLF35584_SMU_CONFIG_ENABLE`
- `GP_TLF35584_ERR_BIST_ENABLE`

## Expected Outputs Or Actions

- Keep `ERR` as a tracked safety-policy topic in design and debugging.
- Tie `ERR` interpretation to safe-state and reset consequences.
- Mark open validation gaps explicitly rather than assuming complete closure.

## Related Modules

- [[wiki/concepts/TLF35584_safe_state_control|TLF35584 Safe State Control]]
- [[wiki/projects/TLF35584_board_level_hardware_decisions|TLF35584 Board-Level Hardware Decisions]]
- [[wiki/business/TLF35584_safe_state_policy|TLF35584 Safe-State Policy]]
- [[wiki/business/TLF35584_fault_handling_policy|TLF35584 Fault Handling Policy]]

## Related Decisions

- PMIC-side `ERR` behavior is considered part of the active safety policy even when the full application-side validation chain is not yet proven.

## Sources

- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.h`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/normalized/manuals/TLF35584/chapters/12_Safe_State_Control_Function/12_Safe_State_Control_Function.md`

