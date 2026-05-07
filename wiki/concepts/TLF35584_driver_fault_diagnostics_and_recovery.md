---
type: concept
status: active
tags: [driver, diagnostics, faults, recovery, TLF35584]
aliases: [TLF35584 driver diagnostics]
---

# TLF35584 Driver Fault Diagnostics And Recovery

## Definition

This page summarizes how the imported driver collects PMIC faults, debounces them, and maps them into software-visible diagnostic structures.

## Main Fault Path

The key runtime function is `Gp_TLF35584_GetAllFaultRegister()`.

Its behavior indicates the driver does more than cache status registers:

- it refreshes PMIC flag registers
- it checks whether any selected fault registers are non-zero
- it marks `DriverErrPath_u32` with `GP_TLF35584_SYSTEM_ERR`
- it clears PMIC flags and attempts to switch back to normal mode
- it debounces repeated fault observation using retry counters
- after thresholding, it records grouped fault information into `ErrRecord_au32[]`

## Grouped Fault Recording

The type and implementation together show that the driver groups recorded faults by logical output or subsystem, including:

- chip-level fault summary
- tracker 1 and tracker 2 faults
- voltage reference faults
- communication supply faults
- core supply faults
- microcontroller supply faults
- standby faults
- pre-regulator faults
- SPI logical faults

This grouped recording is more analysis-friendly than keeping only raw register bytes.

## Error Path Fields

The driver maintains structured error fields such as:

- `DriverErrPath_u32`
- `BistErrPath_u32`
- `ErrRecord_au32[]`

This means later design or debug questions can often be answered at the software error-path level instead of decoding all PMIC registers every time.

## Recovery Behavior Seen In Code

The code suggests a staged reaction model:

- detect fault register activity
- attempt clearing and mode restoration
- debounce repeated observations
- lock in grouped software-visible fault records after threshold

Interrupts are disabled around critical fault-record updates, which shows the implementation is intentionally protecting consistency of error snapshots.

## Design Consequences

- Diagnostics are a first-class behavior of this driver, not a secondary add-on.
- Any future wiki or design work should distinguish between raw PMIC flags and software-grouped fault semantics.
- The grouped fault arrays are promising anchors for higher-level diagnostic integration and UDS/DTC mapping.

## Related Pages

- [[wiki/concepts/TLF35584_monitoring_and_fault_reactions|TLF35584 Monitoring And Fault Reactions]]
- [[wiki/concepts/TLF35584_driver_callout_and_hardware_binding|TLF35584 Driver Callout And Hardware Binding]]
- [[wiki/concepts/TLF35584_driver_init_and_main_loop|TLF35584 Driver Init And Main Loop]]
- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]
