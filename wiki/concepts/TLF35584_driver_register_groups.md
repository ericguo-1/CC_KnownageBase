---
type: concept
status: active
tags: [TLF35584, registers, driver, mapping]
aliases: [TLF35584 register groups, TLF35584 driver register map]
---

# TLF35584 Driver Register Groups

## Objective

Reorganize the `TLF35584` register space into driver-facing groups so later design and debugging can reason in terms of software responsibilities instead of a flat register list.

## Why This Page Exists

The raw materials already contain a complete register overview in two places:

- the driver header `Gp_TLF35584_Reg.h`
- the normalized manual chapter `13_SPI_Serial_Peripheral_Interface`, especially `Table 22 Register Overview`

What was missing before this page was a software-oriented grouping that explains which registers belong together in the implementation.

## Cross-Check Between Manual And Driver Header

The driver header offsets in `Gp_TLF35584_Reg.h` match the normalized manual register overview for the addressed range `00H` to `33H` and `3FH`.

Examples that align directly:

- `GP_TLF35584_REG_WDCFG0 = 0x06` matches `WDCFG0` at `06H`
- `GP_TLF35584_REG_FWDCFG = 0x08` matches `FWDCFG` at `08H`
- `GP_TLF35584_REG_DEVCTRL = 0x15` matches `DEVCTRL` at `15H`
- `GP_TLF35584_REG_FWDSTAT0 = 0x2A` matches `FWDSTAT0` at `2AH`
- `GP_TLF35584_REG_GTM = 0x3F` matches `GTM` at `3FH`

That means the code-facing register namespace is already anchored to the same address model as the datasheet.

## Driver-Facing Register Groups

### 1. Boot And Static Configuration

Registers:

- `DEVCFG0`
- `DEVCFG1`
- `DEVCFG2`

Driver role:

- startup timing
- wake timer enable and cycle selection
- reset release timing
- selected monitor and external-synchronization behavior

Why grouped this way:

These are the early device-shaping values that define base startup and supervision behavior before the rest of runtime interaction matters.

### 2. Protected Runtime Configuration Request Registers

Registers:

- `PROTCFG`
- `SYSPCFG0`
- `SYSPCFG1`
- `WDCFG0`
- `WDCFG1`
- `FWDCFG`
- `WWDCFG0`
- `WWDCFG1`

Driver role:

- enable or disable watchdog functions
- program watchdog thresholds and windows
- program ERR and safe-state behavior
- control protected system options that require unlock-lock sequencing

Why grouped this way:

The manual says these registers are not independent writes. They form one protected configuration transaction governed by `PROTCFG`, then committed by the lock sequence.

Important manual behavior:

- unlock sequence via `PROTCFG`: `0xAB`, `0xEF`, `0x56`, `0x12`
- lock sequence via `PROTCFG`: `0xDF`, `0x34`, `0xBE`, `0xCA`
- configuration is taken over only after a successful lock sequence

### 3. Protected Configuration Status Mirrors

Registers:

- `RSYSPCFG0`
- `RSYSPCFG1`
- `RWDCFG0`
- `RWDCFG1`
- `RFWDCFG`
- `RWWDCFG0`
- `RWWDCFG1`

Driver role:

- read back committed values
- verify protected writes actually took effect
- compare thresholds or enable states against expected configuration

Why grouped this way:

These status mirrors are the hardware-accepted versions of the protected request registers. They matter for post-write verification and later runtime checks.

### 4. Wake Timer Configuration

Registers:

- `WKTIMCFG0`
- `WKTIMCFG1`
- `WKTIMCFG2`

Driver role:

- configure wake timer duration
- enable or disable timed wake support
- bridge low-power timing requests from software into the PMIC

Why grouped this way:

The driver exposes a dedicated API for wake timer programming, so these registers form their own design concern rather than being treated as generic initialization leftovers.

### 5. Mode And Regulator Request Commands

Registers:

- `DEVCTRL`
- `DEVCTRLN`

Driver role:

- request state transitions
- request regulator-output configuration changes together with state changes

Why grouped this way:

The manual defines a special paired-write rule here: `DEVCTRL` must be followed immediately by `DEVCTRLN`, and the second value must be the bitwise inverse of the first. This is a command protocol, not a simple configuration register write.

### 6. Watchdog Service Commands And Watchdog Status

Registers:

- `WWDSCMD`
- `FWDRSP`
- `FWDRSPSYNC`
- `WWDSTAT`
- `FWDSTAT0`
- `FWDSTAT1`

Driver role:

- service the window watchdog
- answer the functional watchdog question-response sequence
- inspect watchdog counters, question seeds, response count, and error count

Why grouped this way:

These registers define the live watchdog servicing path. They are central to the runtime main loop and cannot be modeled as passive status-only data.

Relevant field examples from the normalized manual:

- `WDCFG0` contains `WWDETHR`, `WWDEN`, `FWDEN`, `WWDTSEL`, `WDCYC`
- `FWDCFG` contains the heartbeat timing field used by functional watchdog behavior
- `FWDSTAT0` exposes the question and response-counter related information used during servicing

### 7. Fault, Interrupt, And Monitoring Flags

Registers:

- `SYSFAIL`
- `INITERR`
- `IF`
- `SYSSF`
- `WKSF`
- `SPISF`
- `MONSF0`
- `MONSF1`
- `MONSF2`
- `MONSF3`
- `OTFAIL`
- `OTWRNSF`

Driver role:

- snapshot abnormal conditions
- clear latched flags where required
- decode fault origin into application-facing diagnostics
- distinguish SPI errors, wake causes, monitor failures, over-temperature conditions, and system-fail paths

Why grouped this way:

The code handles these registers as a coherent fault-observation bank, and later maps individual bits into software fault records.

### 8. Device And Protection Status

Registers:

- `VMONSTAT`
- `DEVSTAT`
- `PROTSTAT`

Driver role:

- read device state
- inspect voltage monitor summary
- inspect protection lock status and sequence progress

Why grouped this way:

These are supervisory state registers that tell the driver whether configuration, mode transitions, and lock-protection logic are behaving as expected.

### 9. Safety And EMC Support Registers

Registers:

- `ABIST_CTRL0`
- `ABIST_CTRL1`
- `ABIST_SELECT0`
- `ABIST_SELECT1`
- `ABIST_SELECT2`
- `BCK_FREQ_CHANGE`
- `BCK_FRE_SPREAD`
- `BCK_MAIN_CTRL`
- `GTM`

Driver role:

- support safety-oriented self-test and analog BIST routines
- support EMC-related buck settings where the project enables them
- expose extra control surfaces used by configuration or BIST logic

Why grouped this way:

These registers are less central to steady-state watchdog service, but they still belong to the same driver boundary because they appear in configuration and self-test code paths.

## Software Reading Of The Register Space

The driver source already reflects this grouped view implicitly:

- `Gp_TLF35584_idxInitRegAddress_cau8` groups the initialization write targets
- `Gp_TLF35584_idxFlagRegAddress_cau8` groups fault and interrupt flag registers
- `Gp_TLF35584_idxStatusRegAddress_cau8` groups status and mirror registers

So the missing piece was not raw register knowledge, but an explicit page naming these groups in driver terms.

## Design Consequences

- protected configuration should be treated as a transaction family, not isolated register writes
- watchdog service registers deserve a dedicated service path in design and test thinking
- `DEVCTRL` and `DEVCTRLN` should be documented as a paired command protocol
- fault and monitoring flags should be reasoned about as a bulk diagnostic collection domain
- wake timer registers are a separate low-power feature group, not just more init bytes

## Related Pages

- [[wiki/concepts/TLF35584_spi_interface_and_register_access|TLF35584 SPI Interface And Register Access]]
- [[wiki/concepts/TLF35584_safe_state_control|TLF35584 Safe State Control]]
- [[wiki/projects/TLF35584_manual_to_source_mapping|TLF35584 Manual To Source Mapping]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]

## Source Anchors

- `raw/normalized/manuals/TLF35584/chapters/13_SPI_Serial_Peripheral_Interface/13_SPI_Serial_Peripheral_Interface.md`
- `raw/normalized/manuals/TLF35584/chapters/12_Safe_State_Control_Function/12_Safe_State_Control_Function.md`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584_Reg.h`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
