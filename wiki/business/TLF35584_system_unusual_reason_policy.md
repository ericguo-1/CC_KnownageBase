---
type: business-policy
status: active
policy_area: abnormal-reason
owners: []
tags: [TLF35584, abnormal-reason, wake, reset, business]
---

# TLF35584 System Unusual Reason Policy

## Policy Statement

For the current project baseline, system unusual reason reporting is a classification interface that summarizes startup-related abnormal context such as cold-start, reset type, and wake source. It is not a complete root-cause engine by itself.

## Why This Policy Exists

The imported source exposes `Gp_TLF35584_GetSystemUnusualReason()` and related wake/reset decoding paths. That means the project wants an application-facing explanation layer, but the returned fields still need to be interpreted together with diagnostics and supervision context.

## Applicability

This page applies to builds and project variants that expose the current system unusual reason interface.

## Rules

- Treat cold-start, reset type, and wake-source outputs as categorized context for system interpretation.
- Do not treat the unusual-reason interface as a full substitute for diagnostic, watchdog, or fault analysis.
- Correlate unusual-reason outputs with grouped driver diagnostics whenever root-cause certainty matters.
- Keep project-specific wake-source meaning tied to actual hardware wiring and system policy.
- Preserve the distinction between "reported reason class" and "complete underlying cause chain".

## Exceptions

- Exact meaning of some reported classes can still vary with project wiring and ECU-level design.
- Some root causes may require correlation with data not exposed by this single interface.

## Signals And Inputs

- `Gp_TLF35584_GetSystemUnusualReason()`
- cold-start indication
- reset-type decoding
- wake-source decoding
- grouped diagnostic context

## Expected Outputs Or Actions

- Use the interface as a compact startup-context summary.
- Pair it with diagnostic and fault evidence when investigating abnormal startup or wake behavior.
- Document project-specific interpretation rules for returned wake or reset classes when hardware evidence is available.

## Related Modules

- [[wiki/business/TLF35584_wake_policy|TLF35584 Wake Policy]]
- [[wiki/business/TLF35584_reset_policy|TLF35584 Reset Policy]]
- [[wiki/business/TLF35584_diagnostic_reporting_policy|TLF35584 Diagnostic Reporting Policy]]
- [[wiki/projects/TLF35584_board_level_hardware_decisions|TLF35584 Board-Level Hardware Decisions]]

## Related Decisions

- Unusual-reason reporting is intentionally a concise classification layer and should not be mistaken for the whole abnormal-behavior explanation.

## Sources

- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.h`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.c`

