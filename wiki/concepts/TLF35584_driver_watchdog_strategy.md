---
type: concept
status: active
tags: [driver, watchdog, FWD, WWD, TLF35584]
aliases: [TLF35584 driver watchdog]
---

# TLF35584 Driver Watchdog Strategy

## Definition

This page summarizes how the imported driver models watchdog operation in software.

## Configuration Signals

The configuration header shows that watchdog behavior is compile-time configurable through macros such as:

- `GP_TLF35584_WD_MODE`
- `GP_TLF35584_WWD_EN`
- `GP_TLF35584_FWD_EN`
- `GP_TLF35584_WWD_SEVICE_SELECT`
- `GP_TLF35584_FWD_WINDOW`
- `GP_TLF35584_WWD_ERR_THRE`
- `GP_TLF35584_FWD_ERR_THRE`

The currently imported config selects `GP_TLF35584_FWD_WWD_SPI`, which means both FWD and WWD are expected and serviced through SPI in the current build.

## Software Watchdog Modes

The type header defines software-visible combined modes such as:

- `GP_TLF35584_FWD_SPI`
- `GP_TLF35584_FWD_WWD_SPI`
- `GP_TLF35584_WWD_WDI`
- `GP_TLF35584_WWD_SPI`
- `GP_TLF35584_FWD_SPI_WWD_WDI`

The main service dispatcher `Gp_TLF35584_WdgService()` selects the corresponding service pattern according to `WdMode_u8`.

## What The Driver Reads Back

`Gp_TLF35584_GetWdgInfo()` updates these fields from PMIC status registers:

- current PMIC device state
- WWD error count
- FWD last seed or question
- FWD response counter
- FWD error count
- last WWD service command state

This indicates the watchdog strategy is closed-loop rather than fire-and-forget. The driver actively observes watchdog status and uses it in later decisions.

## What The Driver Writes

The code shows direct use of:

- WWD service by SPI through `Gp_TLF35584_WwdSpiService()`
- optional WDI toggling through `Gp_TLF35584_WwdWdiService()` and callout-controlled pin restore
- FWD response handling through `Gp_TLF35584_FwdSpiService()` using the last seed from PMIC status

## Cooperation With Upper Layer

`Gp_TLF35584_SetWdgTriggerCondition()` allows an upper layer to request a bounded period of watchdog servicing by setting `WdgMTrigCnt_u16` and `WdgSwitch_b`.

This implies the driver can cooperate with a higher-level watchdog manager or mode manager rather than deciding watchdog policy entirely by itself.

## Design Consequences

- Watchdog behavior in this driver is a combined hardware-software policy, not just a PMIC register setting.
- Any future analysis of startup, sleep transitions, or reset causes must include watchdog state and service timing.
- The current code should be documented as using PMIC feedback fields like `LastSeed_u8`, `RspCnt_u8`, `FwdErrCnt_u8`, and `WwdErrCnt_u8`.

## Related Pages

- [[wiki/concepts/TLF35584_watchdogs_and_interrupts|TLF35584 Watchdogs And Interrupts]]
- [[wiki/concepts/TLF35584_spi_interface_and_register_access|TLF35584 SPI Interface And Register Access]]
- [[wiki/concepts/TLF35584_driver_init_and_main_loop|TLF35584 Driver Init And Main Loop]]
- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]
