---
type: project
status: active
tags: [TLF35584, hardware, board, integration, decisions]
project_scope: board-level hardware usage decisions inferred and confirmed from source and configuration
aliases: [TLF35584 board integration decisions, TLF35584 hardware strategy]
---

# TLF35584 Board-Level Hardware Decisions

## Objective

Capture the project-side hardware usage strategy around `TLF35584`, especially for `ERR`, `SS1`, `SS2`, `MPS`, `WDI`, `WAK`, `ENA`, `LDO`, and tracker-related behavior.

## Scope Boundary

This page mixes two kinds of knowledge on purpose, but they must be read carefully:

- project-specific facts confirmed by imported source or schematic evidence
- cross-project conventions confirmed by domain clarification

When those two disagree, always prefer the project-specific fact for the concrete product under analysis.

## Reading Rule

This page intentionally separates three evidence levels:

- `Confirmed in code/config`: directly visible in imported callout, config, or driver source
- `Confirmed by project clarification`: explicitly confirmed from project-owner or domain clarification, even if the current imported files do not fully encode it
- `Strongly implied`: not stated as a board note, but the software behavior clearly assumes it
- `Still requires board or schematic confirmation`: software mentions the signal or feature, but the final ECU wiring or usage policy is not fully proven from code alone

## Confirmed In Code And Configuration

### MPS is actively wired and software-controlled

Evidence:

- `Gp_TLF35584_Callout.c` binds `MPS` to `DioConf_DioChannel_DO_P10_10_35584_MPS`
- `Gp_TLF35584_CalloutMpsTestSupport()` drives that line
- the callout comment explains an inverted control path through external hardware, likely a MOS stage

Decision captured:

- the project uses `MPS` as a real board control signal
- software explicitly switches between `MPS_NORMALMODE` and `MPS_TESTMODE`
- the hardware path is inverted between MCU output level and the actual `TLF35584` `MPS` pin level

Practical consequence:

- boot, test, and watchdog-related analysis must not assume that MCU output polarity equals PMIC `MPS` polarity

### SS1 is observable on the board

Evidence:

- `Gp_TLF35584_Callout.c` binds `SS1` to `DioConf_DioChannel_DI_P10_08_35584_SS1`
- `Gp_TLF35584_CalloutSafeStateConfirm()` reads that input and treats `STD_LOW` as safe-state assertion

Decision captured:

- the project has at least one board-observable safe-state signal path, and that path is `SS1`
- software knows how to sample it through DIO

Practical consequence:

- later fault or BIST analysis can use `SS1` as the primary software-visible proof that safe state has been asserted

### WAK and ENA are recognized as real wake-source categories

Evidence:

- `Gp_TLF35584.c` defines `WAK_MASK` and `ENA_MASK`
- `Gp_TLF35584_GetWakeUpSource()` explicitly decodes `WAK` and `ENA` from `WKSF`
- `Gp_TLF35584_GetSystemUnusualReason()` exposes wake-source values back to the application

Decision captured:

- the project software treats `WAK` and `ENA` as meaningful wake inputs
- wake-cause analysis is part of the driver contract, not just raw PMIC status

Practical consequence:

- wake problems can be analyzed by checking whether `WAK` or `ENA` was the recorded source, even before hardware documents are loaded

### Standby and post-regulator outputs are configured as enabled

Evidence:

- `Gp_TLF35584_Cfg.h` sets:
  - `GP_TLF35584_POWER_LDO_STDBY = ENABLE`
  - `GP_TLF35584_POWER_LDO_VREF = ENABLE`
  - `GP_TLF35584_POWER_LDO_COM = ENABLE`
  - `GP_TLF35584_POWER_LDO_QT1 = ENABLE`
  - `GP_TLF35584_POWER_LDO_QT2 = ENABLE`
- `GP_TLF35584_REG_SYSPCFG0_VALUE` uses the standby LDO setting
- `GP_TLF35584_REG_DEVCTRL_VALUE` includes `QT2`, `QT1`, `COM`, and `VREF`

Decision captured:

- this project config is not using a minimal regulator subset
- standby supply, `VREF`, `COM`, `QT1`, and `QT2` are all configured as active outputs in the imported software baseline

Practical consequence:

- when analyzing board bring-up or fault behavior, assume that the software expects all major regulated outputs to participate

### Both WWD and FWD are intentionally enabled

Evidence:

- `GP_TLF35584_WWD_EN = ENABLE`
- `GP_TLF35584_FWD_EN = ENABLE`
- `GP_TLF35584_WD_MODE = GP_TLF35584_FWD_WWD_SPI`

Decision captured:

- the project strategy is to run both watchdogs
- watchdog service is intended primarily through SPI in the current baseline

Practical consequence:

- any board-level timing or reset analysis must assume both watchdog paths matter

## Confirmed By Project Clarification

### SS2 is optional and only used in delayed-shutdown scenarios

Project clarification:

- some projects do not use `SS2` at all and only use `SS1`
- `SS2` is mainly valuable because it can be configured with a delay relative to `SS1`
- that delayed behavior is useful only in projects that need staged or delayed shutdown behavior

Decision captured:

- `SS1` is the primary safe-state path
- `SS2` should be treated as an optional secondary path, not a universally required board function

Practical consequence:

- later analysis should not assume `SS2` must be present just because the PMIC provides the pin
- for this project family, `SS2` becomes a feature that depends on shutdown strategy rather than a default requirement

### WDI is intentionally not used in current projects

Project clarification:

- current projects do not use `WDI`
- watchdog servicing is done by SPI
- one reason is to avoid consuming an MCU pin for a dedicated watchdog pulse path

Decision captured:

- `WDI` is not merely unimplemented in software; it is intentionally excluded from the current project strategy

Practical consequence:

- `WDI` can be treated as non-participating for current project analysis unless a future variant explicitly reintroduces it
- SPI watchdog service is the real production path, not just a temporary software shortcut

### WAK and ENA are project-dependent external wake inputs

Project clarification:

- external wake-source wiring varies by project
- `WAK` is commonly connected to a wake source such as `KL15`
- `ENA` is commonly connected to communication-related edge-wake signals

Decision captured:

- `WAK` and `ENA` are both valid wake categories, but their exact external source is not fixed across all projects
- the meaning of each source should be interpreted per project wiring, not only by PMIC capability

Practical consequence:

- for cross-project reasoning, treat `WAK` and `ENA` as wake-source classes
- for single-project root-cause analysis, still confirm the actual external source net names in the schematic

## Strongly Implied By Software Behavior

### SS2 exists functionally, but software does not sample it directly

Evidence:

- config names include `SS1_SS2_SIGNAL_CONFIRM`
- safe-state comments and BIST logic refer to `SS1/SS2`
- the callout confirmation function reads only `SS1`

Implied decision:

- the system concept still includes `SS2`, but current software confirmation is effectively `SS1`-only

Practical consequence:

- from the software point of view, safe-state verification is simplified to one observable line
- if `SS2` has a separate external function, it is not independently verified by the current driver integration

### ERR monitoring is logically enabled, but application-side active confirmation is not fully closed

Evidence:

- `GP_TLF35584_REG_SYSPCFG1_ERRRECEN = 0x01`
- `SYSPCFG1` is used for ERR-related behavior
- `ERR_BIST_ENABLE = DISABLE`
- `SMU_CONFIG_ENABLE = DISABLE`

Implied decision:

- the PMIC-side ERR or safe-state policy is configured
- but the higher-level application-side SMU and ERR validation flow is not fully enabled in this imported baseline

Practical consequence:

- ERR-related faults may still affect PMIC behavior, but the end-to-end project safety chain is not fully observable from this software alone

## Still Requires Board Or Schematic Confirmation

### Exact external use of SS2

What is missing:

- no dedicated DIO binding for `SS2`
- no direct software readback of `SS2`
- for a given project, whether `SS2` is populated and used still depends on the actual shutdown strategy

### Exact WDI routing

What is missing:

- the callout body is stubbed
- no concrete `DioConf_*_WDI` symbol appears in the imported callout

What we can say safely:

- current projects intentionally do not use `WDI`
- only a future or different project variant would require a separate `WDI` wiring confirmation

### Actual board-level distinction between LDO and tracker naming

What is missing:

- software names `QT1` and `QT2`, but does not itself explain the board rail names they feed
- there is no project page yet mapping PMIC outputs to ECU nets

What we can say safely:

- `QT1` and `QT2` are enabled in software
- the driver expects them to participate in state and regulator control

### Physical wake input routing policy for WAK versus ENA

What is missing:

- code can decode both sources
- but the imported files do not say which concrete external nets drive `WAK` and `ENA` in this exact project variant

What we can say safely:

- both categories are meaningful enough to be decoded and reported
- by project convention, `WAK` often corresponds to a wake source such as `KL15`, while `ENA` often corresponds to communication-edge wake sources
- the exact ECU net names still need project hardware material

## Working Board-Level Strategy Summary

If we stay strictly within the evidence imported into the vault, the current project strategy looks like this:

- use `MPS` actively and intentionally, including test-mode handling
- observe `SS1` as the software-visible safe-state indicator
- treat `SS2` as an optional delayed-shutdown path rather than a universally required signal
- decode `WAK` and `ENA` as meaningful wake causes
- keep standby, `VREF`, `COM`, `QT1`, and `QT2` enabled in the PMIC configuration baseline
- use SPI-based watchdog service as the main production path
- treat `WDI` as intentionally unused in current project variants
- leave some higher-level ERR or SMU integration paths either stubbed or deferred

## Best Next Inputs To Strengthen This Page

- board schematic or pin-mux table for `WAK`, `ENA`, `WDI`, `SS1`, and `SS2`
- power-tree document mapping `QT1`, `QT2`, `COM`, `VREF`, and standby rails to ECU loads
- safety architecture note clarifying whether ERR and safe-state outputs are part of an end-to-end safety chain in this project

## Related Pages

- [[wiki/concepts/TLF35584_driver_callout_and_hardware_binding|TLF35584 Driver Callout And Hardware Binding]]
- [[wiki/projects/TLF35584_manual_to_source_mapping|TLF35584 Manual To Source Mapping]]
- [[wiki/projects/TLF35584_driver_design_focus|TLF35584 Driver Design Focus]]

## Source Anchors

- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Callout.c`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Callout.h`
- `raw/originals/code/Conf_Gp_TLF35584/Gp_TLF35584_Cfg.h`
- `raw/originals/code/Gp_TLF35584/Gp_TLF35584.c`
