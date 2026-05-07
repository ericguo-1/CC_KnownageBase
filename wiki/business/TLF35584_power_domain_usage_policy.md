---
type: business-policy
status: active
policy_area: power-domain
owners: []
tags: [TLF35584, power-domain, business]
---

# TLF35584 Power-Domain Usage Policy

## Policy Statement

For the current imported baseline, the project does not use a minimal regulator subset. `STDBY`, `VREF`, `COM`, `QT1`, and `QT2` are treated as participating power domains and should be documented as application-relevant supplies rather than hidden PMIC internals.

## Why This Policy Exists

The current configuration enables the major standby, reference, communication, and tracker-related outputs. The application-oriented material also shows that several of these rails commonly feed external sensors, transceivers, or always-on low-power logic.

## Applicability

This page applies to the current `Gp_TLF35584` configuration baseline and to project analysis that starts from the imported source set.

## Rules

- Treat enabled PMIC outputs as functional project domains, not just register bits.
- Keep the role of `STDBY` explicit in low-power and wake analysis.
- Treat `COM` as communication-relevant supply policy when communication startup or wake behavior is analyzed.
- Treat `VREF`, `QT1`, and `QT2` as application-facing domains when discussing analog behavior, sensor availability, or regulator-related faults.
- Avoid assuming that board rail naming is identical to PMIC register naming; preserve the distinction until board mapping is confirmed.

## Exceptions

- Exact ECU net names and consumer loads of each rail still require board or power-tree documentation.
- Different project variants may map the same PMIC outputs to different external functions.

## Signals And Inputs

- `GP_TLF35584_POWER_LDO_STDBY`
- `GP_TLF35584_POWER_LDO_VREF`
- `GP_TLF35584_POWER_LDO_COM`
- `GP_TLF35584_POWER_LDO_QT1`
- `GP_TLF35584_POWER_LDO_QT2`
- PMIC mode and regulator configuration requests

## Expected Outputs Or Actions

- Include these domains in bring-up, fault, and wake-impact analysis.
- Document rail usage at project level when board evidence becomes available.
- Distinguish PMIC rail enable policy from downstream load behavior when troubleshooting.

## Related Modules

- [[wiki/projects/TLF35584_board_level_hardware_decisions|TLF35584 Board-Level Hardware Decisions]]
- [[wiki/concepts/TLF35584_application_integration_notes|TLF35584 Application Integration Notes]]
- [[wiki/concepts/TLF35584_state_machine_and_power_sequencing|TLF35584 State Machine And Power Sequencing]]
- [[wiki/business/TLF35584_fault_handling_policy|TLF35584 Fault Handling Policy]]

## Related Decisions

- The current software baseline assumes the major regulated outputs participate in normal system behavior and should therefore appear in project reasoning.

## Sources

- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.h`
- `raw/normalized/manuals/TLF35584/chapters/16_Application_Information/16_Application_Information.md`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`

