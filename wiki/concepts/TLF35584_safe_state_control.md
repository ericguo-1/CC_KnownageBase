---
type: concept
status: active
tags: [TLF35584, safe-state, ERR, safety]
aliases: [TLF35584 safe state control]
---

# TLF35584 Safe State Control

## Definition

This page captures the safe-state control behavior described in the currently ingested `TLF35584` normalized manual content.

## Why It Matters

The safe-state control function is one of the strongest links between PMIC supervision and system safety behavior. It defines when `SS1` and `SS2` are driven low, which events contribute to safe-state activation, and how watchdog and error-monitoring outcomes influence the external safety path.

## Inputs To Safe State Control

The normalized chapter describes the following contributors:

- ERR pin monitoring from the microcontroller safety management unit
- overvoltage and undervoltage of microcontroller-related regulators
- window watchdog failure threshold comparison
- functional watchdog failure threshold comparison
- thermal shutdown relevant to FAILSAFE
- internal clock
- SPI state transition requests

## Main Outputs

The function controls two safety outputs:

- `SS1`
- `SS2`

`SS2` may be delayed relative to `SS1` by configurable delay `tSS2`.

## Programmable Behavior

The chapter indicates that the following can be configured via SPI:

- watchdog failure thresholds that activate `SS1/SS2`
- immediate versus recovery-delay reaction for `ERR`
- recovery delay time `tREC`
- delay between `SS1` and `SS2`

This matters because system-safety behavior is not fixed purely by hardware defaults; some policy sits in configuration.

## ERR Monitoring Observations

The normalized text describes `ERR` as a toggling alive signal from the microcontroller safety management unit.

Fault indications include:

- ERR staying low
- ERR staying high
- ERR frequency too high
- invalid duty-cycle timing

When detected as faults, the safe-state outputs are pulled low according to the configured reaction model.

## Design Consequences

- Driver and system design must distinguish between PMIC monitoring faults and safe-state output consequences.
- Safe-state related configuration should be treated as protected configuration, not casual runtime writes.
- Software architecture should document who owns `ERR` signaling assumptions and how `SS1/SS2` behavior is validated.

## Related Pages

- [[wiki/entities/TLF35584|TLF35584]]
- [[wiki/concepts/TLF35584_watchdogs_and_interrupts|TLF35584 Watchdogs And Interrupts]]
- [[wiki/concepts/TLF35584_monitoring_and_fault_reactions|TLF35584 Monitoring And Fault Reactions]]
- [[wiki/concepts/TLF35584_spi_interface_and_register_access|TLF35584 SPI Interface And Register Access]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]

## Source Anchors

- `raw/normalized/manuals/TLF35584/chapters/12_Safe_State_Control_Function/12_Safe_State_Control_Function.md`
