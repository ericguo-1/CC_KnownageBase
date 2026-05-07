---
type: concept
status: active
tags: [TLF35584, state-machine, power-sequencing, wake]
aliases: [TLF35584 state machine]
---

# TLF35584 State Machine And Power Sequencing

## Definition

This page captures the currently ingested understanding of how `TLF35584` organizes its operating modes, wake behavior, and ordered rail bring-up through a state-machine driven sequencing model.

## Why It Matters

For software and detailed design, the important point is that the chip is stateful. The driver is not merely configuring rails; it is coordinating with a power-management state machine whose transitions have prerequisites, side effects, and fault reactions.

## Current States Seen In Sources

The available chapters explicitly mention these operating states:

- `INIT`
- `NORMAL`
- `WAKE`
- `SLEEP`
- `STANDBY`
- `FAILSAFE`

## Wake And Entry Triggers

From the wake chapter:

- `WAK` is level-triggered.
- `ENA` is edge-triggered.
- A valid wake signal can move the device:
  - from `STANDBY` to `INIT`
  - from `SLEEP` to `WAKE`
  - from `FAILSAFE` to `INIT`

The chapter also notes that wake signals detected during transitions can redirect the target state and may generate interrupt or reset behavior.

## Power Sequencing Observations

The state-machine chapter describes ordered power sequencing rather than simultaneous rail startup.

The currently visible sequence indicates:

1. After `POR`, the standby regulator and pre-regulator start.
2. Once threshold conditions are met, the microcontroller supply rail starts.
3. Optional external core supply handling is coordinated before later rails in some configurations.
4. Voltage reference, communication supply, and tracker rails are then enabled in order.
5. Reset delay timing begins only after key thresholds are reached.
6. `ROT` release marks an important milestone for subsequent microcontroller and watchdog interactions.

This means software startup assumptions should not be made solely from a power-good style view. The order and threshold dependencies matter.

## Software Design Consequences

- Driver initialization should model the chip's power-up as a staged sequence.
- State transition requests should be treated as operations with outcomes, not as guaranteed immediate mode changes.
- Wake handling should be explicitly connected to low-power mode exit logic.
- Reset release timing and readiness for SPI activity should likely be treated as stateful conditions in the design.

## Related Pages

- [[wiki/entities/TLF35584|TLF35584]]
- [[wiki/concepts/TLF35584_watchdogs_and_interrupts|TLF35584 Watchdogs And Interrupts]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]

## Source Anchors

- `raw/normalized/manuals/TLF35584/div/05_Wake_Function/05_Wake_Function.md`
- `raw/normalized/manuals/TLF35584/div/11_State_Machine/11_State_Machine.md`
