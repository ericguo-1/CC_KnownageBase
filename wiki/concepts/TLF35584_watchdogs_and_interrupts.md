---
type: concept
status: active
tags: [TLF35584, watchdog, interrupt, supervision]
aliases: [TLF35584 watchdogs]
---

# TLF35584 Watchdogs And Interrupts

## Definition

This page summarizes the currently visible watchdog and interrupt model of `TLF35584` from the normalized manual chapters.

## Watchdog Model

The manual states that the device implements two independent watchdog types:

- a `Window Watchdog (WWD)`
- a `Functional Watchdog (FWD)` or question/answer watchdog

The two watchdogs have independent timers and error counters and may operate in parallel.

## Window Watchdog Highlights

From the available chapter:

- Triggering can be based on `WDI` pin activity or via SPI command to `WWDSCMD`.
- The watchdog uses `Long Open Window`, `Open Window`, and `Closed Window` behavior.
- Correct and incorrect servicing influence an internal failure counter.
- During initialization, watchdog behavior is tied to reset release and the transition out of `INIT`.
- Repeated invalid servicing can escalate from soft reset to hard reset and eventually to `FAILSAFE`.

This is important because the driver or upper software layer may need a clear ownership model for watchdog configuration and servicing.

## Interrupt Model

The interrupt chapter describes a dedicated interrupt generation block with multiple requesters, including:

- state-machine related events
- watchdog service problems
- monitoring block reactions
- SPI errors
- overtemperature and current related events
- ABIST completion

The manual also describes a two-level approach:

- first-level interrupt flags
- second-level status flags for detailed causes

## Recommended Service Flow

The manual explicitly recommends an interrupt service routine that:

1. reads the interrupt flag register
2. reads detailed status flags as needed
3. performs the needed action
4. clears detailed status flags
5. clears the interrupt flag register
6. optionally re-reads the interrupt flag register to detect new pending events

This suggests that a good software architecture should not treat the interrupt line as a single flat event source. The register protocol and follow-up readback are part of the behavior.

## Design Consequences

- Watchdog support should likely be represented as a dedicated software concern rather than folded into generic SPI utilities.
- Interrupt servicing should be modeled around grouped causes and detailed status decoding.
- Failure escalation and state-machine interaction should be captured in design notes and tests.

## Current Register Access Hooks

The normalized SPI and watchdog material now gives direct register anchors for watchdog work:

- WDCFG0.FWDEN to enable the functional watchdog
- WWDSCMD for window watchdog service by SPI
- FWDRSP and FWDRSPSYNC for functional watchdog responses
- FWDSTAT0 for question and response progress

## Related Pages

- [[wiki/entities/TLF35584|TLF35584]]
- [[wiki/concepts/TLF35584_state_machine_and_power_sequencing|TLF35584 State Machine And Power Sequencing]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]
- [[wiki/concepts/TLF35584_spi_interface_and_register_access|TLF35584 SPI Interface And Register Access]]
- [[wiki/concepts/TLF35584_safe_state_control|TLF35584 Safe State Control]]

## Source Anchors

- `raw/normalized/manuals/TLF35584/chapters/14_Interrupt_Generation/14_Interrupt_Generation.md`
- `raw/normalized/manuals/TLF35584/chapters/15_Window_Watchdog_And_Functional_Watchdog/15_Window_Watchdog_And_Functional_Watchdog.md`

