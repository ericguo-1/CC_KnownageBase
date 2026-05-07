---
type: concept
status: active
tags: [driver, callout, integration, MCAL, hardware, TLF35584]
aliases: [TLF35584 driver integration bindings]
---

# TLF35584 Driver Callout And Hardware Binding

## Definition

This page captures the project-specific dependencies exposed through the driver callout layer.

## Why It Matters

For real integration and later problem analysis, the driver cannot be understood from `Gp_TLF35584.c` alone. It relies on project callouts for hardware control, MCAL access, and interrupt handling.

## SPI Binding

The callout layer binds the PMIC driver to:

- a concrete SPI channel
- a concrete SPI sequence
- synchronous transfer behavior through `Spi_SetupEB()` and `Spi_SyncTransmit()`

This means timing and bus behavior are partly properties of the platform configuration, not only the PMIC driver source.

## DIO And Hardware Pins

The callout layer shows explicit DIO bindings for:

- `SS1`
- `MPS`

The code also documents an inversion detail for MPS test support, which is important because software-visible `MPS normal` and the actual hardware line polarity are not trivially identical.

## OS And Interrupt Control

The callout layer uses:

- `SuspendAllInterrupts()`
- `ResumeAllInterrupts()`

This is important because fault snapshot consistency depends on these hooks during diagnostic recording.

## What Is Stubbed Or Deferred

Some callouts are intentionally minimal or placeholder-like in the imported source:

- DEM reporting is stubbed
- WDI service via DIO is effectively not driven in the current callout body
- wake source confirm currently returns `E_NOT_OK`

This is valuable wiki knowledge because it separates implemented integration from expected extension points.

## Design Consequences

- Any reasoning about actual PMIC behavior on target hardware must include the callout layer.
- Some features may appear supported by core driver code but remain inactive or incomplete until callouts are fully implemented.
- Platform-level issues such as SPI timing, MPS mode control, and safe-state confirmation should be documented together with the PMIC driver, not elsewhere only.

## Related Pages

- [[wiki/projects/TLF35584_driver_code_architecture|TLF35584 Driver Code Architecture]]
- [[wiki/concepts/TLF35584_driver_fault_diagnostics_and_recovery|TLF35584 Driver Fault Diagnostics And Recovery]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]
- [[wiki/projects/TLF35584_board_level_hardware_decisions|TLF35584 Board-Level Hardware Decisions]]
