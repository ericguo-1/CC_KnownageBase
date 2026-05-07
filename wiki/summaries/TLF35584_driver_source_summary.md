---
type: source-summary
status: active
source_path: raw/originals/code/Gp_TLF35584 and raw/originals/code/Conf_Gp_TLF35584
source_type: driver-source-code
tags: [summary, source-code, driver, TLF35584]
---

# TLF35584 Driver Source Summary

## Scope

This summary is based on the currently imported driver source under:

- `raw/originals/code/Gp_TLF35584/`
- `raw/originals/code/Conf_Gp_TLF35584/`

The source set includes the main implementation, public header, type and register headers, configuration headers, and callout bindings.

## High-Level Summary

The imported source shows that `Gp_TLF35584` is not a thin SPI register wrapper. It is a stateful PMIC driver with these responsibilities:

- initialization and startup sequencing
- periodic main-loop supervision
- watchdog servicing for both FWD and WWD modes
- mode switching between INIT, NORMAL, STANDBY, WAKE related paths
- fault register collection and software-visible diagnostics
- built-in self-test support
- hardware abstraction through project callouts for SPI, delay, MPS, interrupt masking, and safe-state confirmation

## Public Interface Surface

The public header currently exposes these main APIs:

- `Gp_TLF35584_Init`
- `Gp_TLF35584_MainFunction`
- `Gp_TLF35584_SetWdgTriggerCondition`
- `Gp_TLF35584_GetDevSigModeIn`
- `Gp_TLF35584_SetDevSigModeOut`
- `Gp_TLF35584_GetDevSigDiag`
- `Gp_TLF35584_Bist`
- `Gp_TLF35584_SetDevMpsMode`
- `Gp_TLF35584_SetWkUpTimer`
- `Gp_TLF35584_GetSystemUnusualReason` when built for APP mode

## Strong Design Signals From Code

### Driver Owns A Software State Machine

The implementation uses internal software states such as:

- `WAIT_STATE`
- `PREPARERUN_STATE`
- `RUN_STATE`
- `ERROR_STATE`

This means later software design should not model the driver as purely stateless services.

### Startup Is Multi-Step

`Gp_TLF35584_Init()` does more than write configuration:

- optional pre-initialization and reset/wakeup reason capture
- hardware state check
- special handling if the PMIC is unexpectedly still in NORMAL state
- watchdog information readback and long-open-window exit service
- disable/prepare watchdog and FSP behavior before protected configuration
- register initialization and INIT-state confirmation
- transition into a software wait state until the user requests move toward normal operation

### MainFunction Performs Recovery Work

`Gp_TLF35584_MainFunction()` is not only periodic servicing. It also:

- runs asynchronous mode-set handling
- reads all fault registers every cycle
- performs PREPARERUN transition behavior
- services watchdogs in RUN state
- clears the first watchdog event caused by timing during startup

### Driver Is Project-Bound Through Callouts

The callout files bind the driver to:

- MCAL SPI sequence and channel
- DIO access for MPS and safe-state observation
- OS interrupt control
- board-specific wake-source and safe-state confirmation hooks

This means knowledge about the driver is incomplete unless the code and callout layers are read together.

## Related Pages

- [[wiki/entities/TLF35584|TLF35584]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]
- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]
- [[wiki/concepts/TLF35584_driver_watchdog_strategy|TLF35584 Driver Watchdog Strategy]]
- [[wiki/concepts/TLF35584_driver_fault_diagnostics_and_recovery|TLF35584 Driver Fault Diagnostics And Recovery]]
- [[wiki/concepts/TLF35584_driver_callout_and_hardware_binding|TLF35584 Driver Callout And Hardware Binding]]
