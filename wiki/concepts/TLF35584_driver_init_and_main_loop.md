---
type: concept
status: active
tags: [driver, init, main-loop, state-machine, TLF35584]
aliases: [TLF35584 driver init]
---

# TLF35584 Driver Init And Main Loop

## Definition

This page describes how the imported driver actually performs initialization and periodic runtime work.

## Init Flow Observed In Code

`Gp_TLF35584_Init()` performs a staged startup sequence rather than a single register write burst.

### Main Steps

1. If BIST has not already prepared the device, the driver performs pre-initialization and collects reset/wakeup reason.
2. It reads the PMIC device state.
3. If the PMIC is unexpectedly still in `NORMAL`, the driver temporarily enters MPS test support flow and resets PORST-related mode handling.
4. It reads watchdog information.
5. It services the WWD once to leave the long-open-window condition.
6. It disables watchdog and FSP related behavior before protected configuration.
7. It writes initialization register configuration.
8. It re-reads the device state and checks whether the PMIC is now in `INIT`.
9. It sets the internal software state to `WAIT_STATE` and waits for later transition toward normal run behavior.

## MainFunction Flow Observed In Code

`Gp_TLF35584_MainFunction()` performs work in every cycle:

- asynchronous runtime mode-set handling through `Gp_TLF35584_RtSetMode()`
- fault register collection through `Gp_TLF35584_GetAllFaultRegister()`
- software-state-dependent logic

### PREPARERUN_STATE

In `PREPARERUN_STATE`, the driver:

- reconfigures watchdog timing and mode-related watchdog registers
- refreshes watchdog status
- services watchdogs once
- switches the PMIC toward `NORMAL`
- delays and reads back actual state
- retries if transition fails, up to a configured limit

### RUN_STATE

In `RUN_STATE`, the driver:

- periodically services watchdogs according to a software tick counter
- optionally cooperates with external watchdog manager logic via `WdgSwitch_b`
- clears the first watchdog event after startup because the transition timing can exceed watchdog timing windows
- updates watchdog information when a service edge is not due yet

### WAIT_STATE And ERROR_STATE

- `WAIT_STATE` is a holding state after init, waiting for an external trigger path.
- `ERROR_STATE` is a terminal software state for unsuccessful recovery or transition attempts.

## Design Consequences

- The driver should be treated as a scheduled component with explicit periodic execution requirements.
- Init success does not mean the PMIC is already in application-ready normal operation.
- The software state machine is part of the behavior contract and should be documented in any detailed design.

## Related Pages

- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]
- [[wiki/concepts/TLF35584_driver_watchdog_strategy|TLF35584 Driver Watchdog Strategy]]
- [[wiki/concepts/TLF35584_driver_fault_diagnostics_and_recovery|TLF35584 Driver Fault Diagnostics And Recovery]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]
