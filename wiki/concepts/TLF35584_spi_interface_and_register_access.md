---
type: concept
status: active
tags: [TLF35584, SPI, registers, protected-registers]
aliases: [TLF35584 SPI interface]
---

# TLF35584 SPI Interface And Register Access

## Definition

This page summarizes the SPI access model of `TLF35584` and the register-access patterns that are directly relevant to driver design.

## Why It Matters

A useful driver for `TLF35584` is largely defined by how it performs SPI transactions, protected-register updates, state-transition requests, and watchdog servicing commands.

## Core SPI Behavior

From the normalized SPI chapter:

- The device operates as an SPI slave.
- `CMD = 0` indicates read access.
- `CMD = 1` indicates write access.
- MOSI data is captured on the rising edge of `SCL`.
- Read data is returned in the same SPI frame.
- During write access, written command data is looped back to `SDO`.
- Maximum SPI clock is `10 MHz` in normal operation and `1.5 MHz` in `SLEEP` state.

## SPI Error Handling

The normalized content explicitly calls out SPI error sources such as:

- wrong parity on write
- write to invalid address
- wrong number of clock cycles while `SCS` is low
- read from invalid address
- invalid frame duration

In case of an SPI error, an interrupt is generated.

## Protected Register Model

The SPI chapter states that these request registers are protected:

- `SYSPCFG0`
- `SYSPCFG1`
- `WDCFG0`
- `WDCFG1`
- `FWDCFG`
- `WWDCFG0`
- `WWDCFG1`

Access requires a dedicated `UNLOCK` sequence written via `PROTCFG`:

1. `0xAB`
2. `0xEF`
3. `0x56`
4. `0x12`

After protected writes are complete, configuration is committed with a dedicated `LOCK` sequence:

1. `0xDF`
2. `0x34`
3. `0xBE`
4. `0xCA`

This means the driver should not model protected configuration as isolated one-register writes. It is a transaction sequence with verification and commit behavior.

## Register Groups Already Relevant

The currently ingested chapter shows these especially relevant registers:

- `WDCFG0`, `WDCFG1`
- `FWDCFG`
- `WWDCFG0`, `WWDCFG1`
- `DEVCTRL`, `DEVCTRLN`
- `WWDSCMD`
- `FWDRSP`, `FWDRSPSYNC`
- `FWDSTAT0`, `FWDSTAT1`
- `PROTCFG`, `PROTSTAT`

## Driver Design Consequences

- SPI access should likely be split into plain access, protected configuration access, and command-style access.
- Protected configuration should have a helper sequence: unlock, write, readback, lock, wait for internal apply time.
- State transitions need special handling because `DEVCTRL` and `DEVCTRLN` must be written consecutively with inverted payload.
- Watchdog service operations should be modeled as dedicated commands, not generic register writes.

## Related Pages

- [[wiki/entities/TLF35584|TLF35584]]
- [[wiki/concepts/TLF35584_watchdogs_and_interrupts|TLF35584 Watchdogs And Interrupts]]
- [[wiki/concepts/TLF35584_safe_state_control|TLF35584 Safe State Control]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]

## Source Anchors

- `raw/normalized/manuals/TLF35584/chapters/13_SPI_Serial_Peripheral_Interface/13_SPI_Serial_Peripheral_Interface.md`
