---
type: project
status: active
tags: [TLF35584, driver, mapping, manual, source]
project_scope: trace manual behavior to concrete source-code locations
aliases: [TLF35584 manual to code mapping, TLF35584 API to register mapping]
---

# TLF35584 Manual To Source Mapping

## Objective

Connect the normalized `TLF35584` manual behavior to the imported driver implementation so later questions can move directly from device concept to the relevant source files, functions, and configuration macros.

## Why This Page Matters

Before this page, the vault had:

- manual-side concept pages
- source-side architecture pages

But it did not yet state clearly which software element implements each manual behavior. This page closes that gap.

## Mapping Principles

- the normalized manual defines the hardware contract
- `Gp_TLF35584_Reg.h` defines the code-visible register namespace
- `Gp_TLF35584_Cfg.h` and `Gp_TLF35584_Cfg.c` define most compile-time register values
- `Gp_TLF35584.c` implements the transaction sequences and runtime behavior
- callout files bind the driver to project-specific MCAL and board behavior

## Behavior To Source Mapping

### 1. Protected Register Access Model

Manual behavior:

- chapter 13 marks `SYSPCFG0`, `SYSPCFG1`, `WDCFG0`, `WDCFG1`, `FWDCFG`, `WWDCFG0`, and `WWDCFG1` as protected
- unlock through `PROTCFG` sequence `AB EF 56 12`
- lock through `PROTCFG` sequence `DF 34 BE CA`
- committed values become visible in `RSYSPCFGx`, `RWDCFGx`, `RFWDCFG`, and `RWWDCFGx`

Source mapping:

- register names: `Gp_TLF35584_Reg.h`
- unlock helper: `Gp_TLF35584_UnlockSeq()` in `Gp_TLF35584.c`
- lock helper: `Gp_TLF35584_LockSeq()` in `Gp_TLF35584.c`
- init write batch: `Gp_TLF35584_InitRegCfg()` in `Gp_TLF35584.c`
- runtime watchdog reconfiguration: `Gp_TLF35584_RtWdgRegCfg()` in `Gp_TLF35584.c`
- protected target values: `Gp_TLF35584_idxRtRegValue_cau8[]` in `Gp_TLF35584_Cfg.c`

Design reading:

The driver already models protected writes as a transaction sequence, which matches the manual well.

### 2. Initial Register Programming

Manual behavior:

- chapter 13 register tables define the writable configuration bytes
- chapter 12 ties safe-state behavior to protected watchdog and ERR-related fields

Source mapping:

- init register address list: `Gp_TLF35584_idxInitRegAddress_cau8[]` in `Gp_TLF35584.c`
- init register values: `Gp_TLF35584_idxRtRegValue_cau8[]` in `Gp_TLF35584_Cfg.c`
- init programming flow: `Gp_TLF35584_InitRegCfg()`
- readback verification: status read within `Gp_TLF35584_InitRegCfg()` against protected-register expected values

Design reading:

Initialization is not handwritten register-by-register logic. It is a table-driven write-and-verify pass.

### 3. State Transition And Regulator Configuration Requests

Manual behavior:

- chapter 13 states `DEVCTRL` must be followed by `DEVCTRLN`
- the second value must be the bitwise inverse of the first
- the request may combine state transition and regulator output configuration

Source mapping:

- register names: `DEVCTRL`, `DEVCTRLN` in `Gp_TLF35584_Reg.h`
- configured base values: `GP_TLF35584_REG_DEVCTRL_VALUE` and `GP_TLF35584_REG_DEVCTRLN_VALUE` in `Gp_TLF35584_Cfg.h`
- normal-mode transition: `Gp_TLF35584_SwitchToNormalMode()`
- standby transition: `Gp_TLF35584_SwitchToStandbyMode()`
- mode-dispatch logic: `Gp_TLF35584_RtSetMode()`
- public trigger path: `Gp_TLF35584_SetDevSigModeOut()` and internal `SetMode_u8` state usage

Design reading:

The manual's paired-write requirement becomes a dedicated software mode-switch command path, not a generic register service.

### 4. Window Watchdog Configuration And Service

Manual behavior:

- `WDCFG0` controls `WWDETHR`, `WWDEN`, service selection, and related watchdog behavior
- `WWDCFG0` and `WWDCFG1` define watchdog timing windows
- service command goes through `WWDSCMD`
- runtime state is reflected in `WWDSTAT`

Source mapping:

- compile-time enable and thresholds: `GP_TLF35584_WWD_EN`, `GP_TLF35584_WWD_ERR_THRE`, `GP_TLF35584_WWD_SEVICE_SELECT`, `GP_TLF35584_WWD_OPEN_WINDOW`, `GP_TLF35584_WWD_CLOSED_WINDOW` in `Gp_TLF35584_Cfg.h`
- register images: `GP_TLF35584_REG_WDCFG0_VALUE`, `GP_TLF35584_REG_WWDCFG0_VALUE`, `GP_TLF35584_REG_WWDCFG1_VALUE`
- SPI service helper: `Gp_TLF35584_WwdSpiService()`
- WDI-pin service helper: `Gp_TLF35584_WwdWdiService()`
- watchdog status readback: `Gp_TLF35584_GetWdgInfo()`
- runtime watchdog reconfiguration: `Gp_TLF35584_RtWdgRegCfg()`

Design reading:

The driver supports both watchdog configuration and runtime servicing, and explicitly keeps the last `WWDSCMD` state in software.

### 5. Functional Watchdog Configuration And Service

Manual behavior:

- `WDCFG0.FWDEN` enables the functional watchdog
- `WDCFG1` defines the functional watchdog error threshold
- `FWDCFG` provides functional-watchdog timing configuration
- `FWDSTAT0` and `FWDSTAT1` expose question, response count, and error counters
- service uses repeated `FWDRSP` writes finished by `FWDRSPSYNC`

Source mapping:

- compile-time enable and thresholds: `GP_TLF35584_FWD_EN`, `GP_TLF35584_FWD_ERR_THRE`, `GP_TLF35584_FWD_WINDOW` in `Gp_TLF35584_Cfg.h`
- register images: `GP_TLF35584_REG_WDCFG0_VALUE`, `GP_TLF35584_REG_WDCFG1_VALUE`, `GP_TLF35584_REG_FWDCFG_VALUE`
- service helper: `Gp_TLF35584_FwdSpiService()`
- watchdog info decode: `Gp_TLF35584_GetWdgInfo()`
- strategy integration: `Gp_TLF35584_WdgService()` and `Gp_TLF35584_SetWdgTriggerCondition()`

Design reading:

This is not a simple feed-the-dog toggle. The source implements a seed-question-driven functional watchdog protocol that lines up with the manual's response model.

### 6. Safe-State And ERR-Related Behavior

Manual behavior:

- chapter 12 defines ERR monitoring and SS1 or SS2 behavior
- safe-state reaction threshold for invalid WWD triggering uses `WDCFG0.WWDETHR`
- the active configured threshold is reflected in `RWDCFG0.WWDETHR`
- functional-watchdog threshold uses `WDCFG1.FWDETHR` and `RWDCFG1.FWDETHR`
- `SYSPCFG1` carries ERR and safe-state related configuration bits such as delay or recovery behavior

Source mapping:

- ERR or safe-state config image: `GP_TLF35584_REG_SYSPCFG1_VALUE` in `Gp_TLF35584_Cfg.h`
- watchdog threshold image: `GP_TLF35584_REG_WDCFG0_VALUE` and `GP_TLF35584_REG_WDCFG1_VALUE`
- runtime disabling path used during fault handling: writes to `WDCFG0` and `SYSPCFG1` around `Gp_TLF35584_DisableWdgFsp()` logic in `Gp_TLF35584.c`
- project binding to actual hardware handling: `Gp_TLF35584_CalloutSafeStateConfirm()` and related callout layer responsibilities

Design reading:

The vault now has enough evidence to say that safe-state behavior is distributed across protected configuration, watchdog thresholds, and board-specific callout assumptions.

### 7. Wake Timer Behavior

Manual behavior:

- `DEVCFG0` contains wake timer enable and cycle selection
- `WKTIMCFG0`, `WKTIMCFG1`, and `WKTIMCFG2` provide wake timer count data

Source mapping:

- register images: `GP_TLF35584_REG_DEVCFG0_VALUE`, `GP_TLF35584_REG_WKTIM0_VALUE`, `GP_TLF35584_REG_WKTIM1_VALUE`, `GP_TLF35584_REG_WKTIM2_VALUE`
- public API: `Gp_TLF35584_SetWkUpTimer()`
- init table inclusion: `Gp_TLF35584_idxInitRegAddress_cau8[]` and `Gp_TLF35584_idxRtRegValue_cau8[]`

Design reading:

Wake timer support is not merely documented; it is exposed as a public driver capability and implemented with protected register writes.

### 8. Fault Collection, Interrupt Flags, And Diagnostic Output

Manual behavior:

- chapter 13 exposes grouped flags such as `IF`, `SPISF`, `SYSSF`, `WKSF`, `MONSF0..3`, `OTFAIL`, `OTWRNSF`
- these are the hardware evidence registers for interrupt and fault cause analysis

Source mapping:

- flag register address list: `Gp_TLF35584_idxFlagRegAddress_cau8[]` in `Gp_TLF35584.c`
- status register address list: `Gp_TLF35584_idxStatusRegAddress_cau8[]`
- bulk update path: `Gp_TLF35584_UpdateFlagReg()`
- bulk fault collection path: `Gp_TLF35584_GetAllFaultRegister()`
- public diagnostic output: `Gp_TLF35584_GetDevSigDiag()`
- fault-record storage: `ErrRecord_au32[]` inside runtime data structures

Design reading:

The source does not treat fault registers as a one-off read. It periodically snapshots, debounces, clears, and projects them into software-visible fault records.

## What Is Now Covered Vs Still Open

Covered by this page:

- manual behavior to source function mapping
- register groups to source tables and helper paths
- configuration macros to functional blocks

Still open:

- which board-level hardware options are actually populated and enabled in the final ECU
- which callout paths are production-complete versus still placeholders or stubs

## Related Pages

- [[wiki/concepts/TLF35584_driver_register_groups|TLF35584 Driver Register Groups]]
- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]
- [[wiki/concepts/TLF35584_driver_watchdog_strategy|TLF35584 Driver Watchdog Strategy]]
- [[wiki/concepts/TLF35584_driver_fault_diagnostics_and_recovery|TLF35584 Driver Fault Diagnostics And Recovery]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]

## Source Anchors

- `raw/normalized/manuals/TLF35584/chapters/12_Safe_State_Control_Function/12_Safe_State_Control_Function.md`
- `raw/normalized/manuals/TLF35584/chapters/13_SPI_Serial_Peripheral_Interface/13_SPI_Serial_Peripheral_Interface.md`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584_Reg.h`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.h`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.c`
