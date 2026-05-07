---
type: project
status: active
tags: [driver, code, architecture, TLF35584]
project_scope: source-driven driver architecture view
---

# TLF35584 Driver Code Architecture

## Objective

Capture the actual software structure of the imported `Gp_TLF35584` driver so that future design, debugging, and reasoning can use the code architecture directly instead of inferring everything from the datasheet.

## Source Layout

The imported source is split into two main areas:

- implementation and interface:
  - `Gp_TLF35584.c`
  - `Gp_TLF35584.h`
  - `Gp_TLF35584_Reg.h`
  - `Gp_TLF35584_Types.h`
- configuration and hardware adaptation:
  - `Gp_TLF35584_Cfg.h`
  - `Gp_TLF35584_Cfg.c`
  - `Gp_TLF35584_Callout.h`
  - `Gp_TLF35584_Callout.c`

## Architectural Shape

The driver is organized around four layers:

1. public APIs exposed to the application
2. internal helper functions for SPI access, watchdog service, mode switching, and register updates
3. compile-time configuration in `Cfg.h`
4. project-specific callouts for MCAL and hardware interaction

## Public API Groups

### Lifecycle

- `Gp_TLF35584_Init`
- `Gp_TLF35584_MainFunction`

### Control And Mode

- `Gp_TLF35584_SetDevSigModeOut`
- `Gp_TLF35584_SetDevMpsMode`
- `Gp_TLF35584_SetWkUpTimer`

### Observation And Diagnostics

- `Gp_TLF35584_GetDevSigModeIn`
- `Gp_TLF35584_GetDevSigDiag`
- `Gp_TLF35584_GetSystemUnusualReason`

### Self-Test

- `Gp_TLF35584_Bist`

### Watchdog Cooperation

- `Gp_TLF35584_SetWdgTriggerCondition`

## Internal Execution Model

The implementation maintains internal software states:

- `WAIT_STATE`
- `PREPARERUN_STATE`
- `RUN_STATE`
- `ERROR_STATE`

This software state machine overlays the hardware PMIC states such as `INIT`, `NORMAL`, `STANDBY`, and `WAKE`.

## Important Internal Helpers

The code strongly centers around these internal helpers:

- register read/write and protected access:
  - `Gp_TLF35584_WriteCmd`
  - `Gp_TLF35584_ReadCmd`
  - `Gp_TLF35584_UnlockSeq`
  - `Gp_TLF35584_LockSeq`
- watchdog and status:
  - `Gp_TLF35584_WdgService`
  - `Gp_TLF35584_GetWdgInfo`
  - `Gp_TLF35584_WwdSpiService`
  - `Gp_TLF35584_WwdWdiService`
  - `Gp_TLF35584_FwdSpiService`
- mode handling:
  - `Gp_TLF35584_GetState`
  - `Gp_TLF35584_SwitchToNormalMode`
  - `Gp_TLF35584_SwitchToStandbyMode`
  - `Gp_TLF35584_RtSetMode`
- diagnostics and fault handling:
  - `Gp_TLF35584_GetAllFaultRegister`
  - `Gp_TLF35584_UpdateFlagReg`
  - `Gp_TLF35584_UpdateStatusReg`
  - `Gp_TLF35584_ClearFlagReg`

## Driver Design Reading

The code suggests that the practical driver architecture is event and supervision driven. The key center of gravity is not only SPI access but the coordination of:

- startup sequencing
- watchdog behavior
- fault observation and recording
- mode repair and transition requests
- hardware abstraction through callouts

## Related Pages

- [[wiki/summaries/TLF35584_driver_source_summary|TLF35584 Driver Source Summary]]
- [[wiki/concepts/TLF35584_driver_init_and_main_loop|TLF35584 Driver Init And Main Loop]]
- [[wiki/concepts/TLF35584_driver_watchdog_strategy|TLF35584 Driver Watchdog Strategy]]
- [[wiki/concepts/TLF35584_driver_fault_diagnostics_and_recovery|TLF35584 Driver Fault Diagnostics And Recovery]]
- [[wiki/concepts/TLF35584_driver_callout_and_hardware_binding|TLF35584 Driver Callout And Hardware Binding]]
