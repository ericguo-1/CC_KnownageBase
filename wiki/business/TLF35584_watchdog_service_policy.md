---
type: business-policy
status: active
policy_area: watchdog
owners: []
tags: [TLF35584, watchdog, business]
---

# TLF35584 Watchdog Service Policy

## Policy Statement

For the current project baseline, both `WWD` and `FWD` are intentionally enabled and serviced primarily through SPI. Dedicated `WDI`-pin servicing is not part of the normal production strategy.

## Why This Policy Exists

The imported configuration and code show that the project expects both watchdog types to participate, while current project clarification states that `WDI` is intentionally avoided to save MCU pin resources.

## Applicability

This page applies to the current handwritten driver baseline and project variants that keep `GP_TLF35584_WD_MODE = GP_TLF35584_FWD_WWD_SPI`.

## Rules

- Treat combined `FWD + WWD` supervision as the default project watchdog policy.
- Use SPI as the primary watchdog service path.
- Treat `WDI` as intentionally non-participating unless a future variant explicitly reintroduces it.
- Model watchdog servicing as a bounded cooperation mechanism between the PMIC driver and an upper-layer trigger source.
- Include PMIC watchdog feedback fields in watchdog health analysis instead of assuming service is fire-and-forget.

## Exceptions

- The driver still contains `WDI`-related support paths, but current projects do not use them as the normal strategy.
- Future board variants may choose a different watchdog-service mode and would need their own project page or a policy update.

## Signals And Inputs

- `GP_TLF35584_WD_MODE`
- `GP_TLF35584_WWD_EN`
- `GP_TLF35584_FWD_EN`
- PMIC watchdog status fields such as `LastSeed_u8`, `RspCnt_u8`, `FwdErrCnt_u8`, and `WwdErrCnt_u8`
- upper-layer trigger requests through `Gp_TLF35584_SetWdgTriggerCondition()`

## Expected Outputs Or Actions

- Keep watchdog servicing active only when explicitly requested by the intended runtime policy.
- Observe watchdog feedback and counters as part of runtime supervision.
- Treat repeated invalid servicing as a system fault path that can escalate into reset or stronger PMIC reactions.

## Related Modules

- [[wiki/concepts/TLF35584_watchdogs_and_interrupts|TLF35584 Watchdogs And Interrupts]]
- [[wiki/concepts/TLF35584_driver_watchdog_strategy|TLF35584 Driver Watchdog Strategy]]
- [[wiki/projects/TLF35584_board_level_hardware_decisions|TLF35584 Board-Level Hardware Decisions]]
- [[wiki/projects/TLF35584_manual_to_source_mapping|TLF35584 Manual To Source Mapping]]

## Related Decisions

- The current project family prefers SPI-based servicing over consuming a dedicated MCU `WDI` pin.

## Sources

- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.h`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/normalized/manuals/TLF35584/chapters/15_Window_Watchdog_And_Functional_Watchdog/15_Window_Watchdog_And_Functional_Watchdog.md`

