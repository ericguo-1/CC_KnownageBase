---
type: concept
status: active
tags: [TLF35584, application, integration, hardware]
aliases: [TLF35584 application notes]
---

# TLF35584 Application Integration Notes

## Definition

This page collects integration-level notes from the currently ingested application-oriented material and adjacent regulator chapters.

## Why It Matters

The wiki should not only preserve abstract chip behavior. It should also capture the practical integration cues that later affect schematic review, driver assumptions, and detailed design tradeoffs.

## Current Observations

### Example Application Circuit Exists

The `Application Information` chapter clearly presents the device as part of a larger application circuit rather than as an isolated PMIC. This is useful because later software design should assume interaction with:

- external loads
- optional external post regulator paths
- wake and enable lines
- supervision dependencies between rails

### Recommended Passive Values Are Provided

The current normalized content includes recommended values for:

- step-up inductor and capacitor
- step-down filter inductor and capacitor

These values are not yet software requirements by themselves, but they are strong hardware-integration anchors and may explain timing or stability assumptions seen elsewhere in the manual.

### Optional External Post Regulator

The current post-regulator text indicates an optional external core-supply regulator path controlled with:

- `EVC` enable signal
- `SYN` synchronization signal
- `VCI` monitoring path

This matters to software because some sequencing and monitoring behavior depends on whether this external-core-supply option is active.

## Software-Relevant Integration Implications

- Some state-machine behavior depends on hardware configuration pins such as `SEC` or frequency-related setup.
- Driver assumptions about rail availability may differ between designs using internal-only outputs and designs using the external core-supply path.
- Documentation for software should identify which hardware options are actually enabled in the target project.

## Cross-Project Power-Rail Usage Conventions

The following conventions are not tied to only one imported project. They reflect common `TLF35584` usage patterns across multiple products.

### `QT1` And `QT2`

Typical role:

- often used to supply external sensors

Why it matters to software:

- if sensors are powered from `QT1` or `QT2`, PMIC mode transitions and regulator faults can directly affect sensor availability
- software diagnostics should treat these rails as application-facing supplies, not only as internal PMIC implementation detail

### `COM`

Typical role:

- often used to supply communication transceivers

Why it matters to software:

- communication availability may depend on PMIC regulator state
- bus startup, wake behavior, and communication diagnostics can all be influenced by the `COM` rail state

### `VREF`

Typical role:

- often used as reference supply for analog sampling or ADC-related circuits

Why it matters to software:

- analog measurement stability and plausibility may depend on `VREF`
- abnormal ADC behavior can sometimes be explained by regulator or reference-supply issues rather than only by software faults

### `STDBY`

Typical role:

- often used to keep an always-on or low-power supervision domain alive while the main `QUC` domain is already shut down
- a common pattern is to keep an AURIX internal `SCR` domain powered during standby so it can detect wake sources and wake `TLF35584`, which then wakes the main AURIX domain
- in other products the same role may be served by external low-power devices that must remain powered while the main MCU sleeps

Why it matters to software:

- standby behavior is part of the overall system wake architecture, not only a PMIC low-power mode detail
- wake analysis should always ask which logic remains powered from `STDBY` and which logic is already off with `QUC`

## Suggested Follow-Up

- Add a project-specific page later that maps real board usage of `TLF35584` pins and options.
- Extract hardware/software boundary assumptions for:
  - wake wiring
  - watchdog servicing path
  - interrupt routing
  - optional external post regulator usage

## Related Pages

- [[wiki/entities/TLF35584|TLF35584]]
- [[wiki/concepts/TLF35584_state_machine_and_power_sequencing|TLF35584 State Machine And Power Sequencing]]
- [[wiki/concepts/TLF35584_monitoring_and_fault_reactions|TLF35584 Monitoring And Fault Reactions]]
- [[wiki/projects/TLF35584_board_level_hardware_decisions|TLF35584 Board-Level Hardware Decisions]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]

## Source Anchors

- `raw/normalized/manuals/TLF35584/div/16_Application_Information/16_Application_Information.md`
- currently visible normalized post-regulator and sequencing content in the ingested tree
