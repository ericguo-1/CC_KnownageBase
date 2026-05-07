---
type: business-policy
status: active
policy_area: wake-source-interpretation
owners: []
tags: [TLF35584, wake-source, business]
---

# TLF35584 Wake-Source Interpretation Policy

## Policy Statement

For the current project family, wake-source reporting should be interpreted as a project-specific class mapping, not as a complete hardware-net identification result.

## Why This Policy Exists

The driver decodes wake-source classes such as `WAK` and `ENA`, but board-level evidence shows that the concrete external sources behind those classes vary by project.

## Applicability

This page applies to current project variants that decode wake-source information from PMIC status and report it upward.

## Rules

- Treat `WAK` and `ENA` as stable wake-source classes in software.
- Avoid equating a wake-source class directly with one exact physical net unless project hardware evidence confirms it.
- Document project-specific mappings from PMIC wake-source class to ECU source names when schematic evidence becomes available.
- Use wake-source classification as a useful debugging and startup-context aid, but not as complete board proof by itself.
- Keep wake-source interpretation linked to standby architecture and low-power policy.

## Exceptions

- A single project may map `WAK` or `ENA` differently from another project in the same family.
- Some wake-confirm or routing details may remain outside the current imported callout baseline.

## Signals And Inputs

- `WKSF`
- `WAK`
- `ENA`
- `Gp_TLF35584_GetWakeUpSource()`
- `Gp_TLF35584_GetSystemUnusualReason()`

## Expected Outputs Or Actions

- Preserve wake-source class as reported by the driver.
- Add board-specific mapping pages later when actual ECU routing is confirmed.
- Avoid overclaiming physical source certainty from PMIC class alone.

## Related Modules

- [[wiki/business/TLF35584_wake_policy|TLF35584 Wake Policy]]
- [[wiki/business/TLF35584_system_unusual_reason_policy|TLF35584 System Unusual Reason Policy]]
- [[wiki/projects/TLF35584_board_level_hardware_decisions|TLF35584 Board-Level Hardware Decisions]]
- [[wiki/business/TLF35584_low_power_transition_policy|TLF35584 Low-Power Transition Policy]]

## Related Decisions

- Wake-source reporting is intentionally useful but abstract; detailed physical-source interpretation remains a project-layer task.

## Sources

- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.h`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Callout.c`

