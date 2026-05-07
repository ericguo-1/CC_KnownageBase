# Log

## [2026-04-16] init | Vault initialized

- Created core directories for `raw`, `wiki`, `references`, `templates`, and `scripts`.
- Added `README.md`, `AGENTS.md`, `index.md`, and `log.md`.
- Reserved the vault for Codex-assisted ingest, query, and lint workflows.

## [2026-04-16] ingest | TLF35584 first wiki seed

- Used the normalized markdown under `raw/normalized/manuals/TLF35584/div/` as the ingest source.
- Created the first wiki seed pages for:
  - chip entity
  - manual summary
  - state machine and power sequencing
  - watchdogs and interrupts
  - driver design focus
- Registered the new pages in `index.md`.
- Noted current content gaps for SPI and safe-state control chapters.

## [2026-04-16] ingest | TLF35584 second wiki pass

- Expanded the wiki with additional concept pages for:
  - wake and reset behavior
  - monitoring and fault reactions
  - application integration notes
- Linked the new pages back into the entity, summary, project, and index navigation.
- Kept the ingest scoped to normalized markdown only and did not re-read the original PDF.

## Convention

Use this format for future entries:

`## [YYYY-MM-DD] operation | short title`

Examples of operations:

- `ingest`
- `query`
- `lint`
- `refactor`
- `decision`

## [2026-04-17] refactor | TLF35584 normalized manual structure and wiki update

- Copied normalized `TLF35584` manual content into separated `chapters`, `metadata`, and `images` folders while keeping the original `div` tree as a legacy snapshot.
- Added wiki pages for `SPI Interface And Register Access` and `Safe State Control`.
- Updated existing TLF35584 pages to reflect that chapters 12 and 13 are now available.


## [2026-04-17] refactor | TLF35584 stale wording cleanup

- Updated `TLF35584_manual_summary` to remove stale wording about waiting for a next pass on chapters 12 and 13.
- Updated manual source references from legacy `div` wording to the normalized `chapters` path where appropriate.
- Kept only the remaining real knowledge gaps: grouped register extraction, table normalization, and board-specific integration decisions.

## [2026-04-17] ingest | TLF35584 register grouping and manual-to-source mapping

- Confirmed that the normalized SPI chapter already contains the register overview and detailed register-field descriptions needed for driver-facing extraction.
- Added `TLF35584 Driver Register Groups` to reorganize the flat register list into configuration, status, watchdog, wake-timer, fault, and safety domains.
- Added `TLF35584 Manual To Source Mapping` to connect manual behaviors to source functions, configuration macros, and runtime helper flows.
- Updated `TLF35584 Driver Design Focus` so only the remaining real gap is board-specific hardware-decision knowledge.

## [2026-04-17] ingest | TLF35584 board-level hardware decisions

- Added `TLF35584 Board-Level Hardware Decisions` to capture project-side usage of `ERR`, `SS1`, `SS2`, `MPS`, `WDI`, `WAK`, `ENA`, and regulator outputs.
- Separated evidence into confirmed code-backed decisions, strong software implications, and items that still require board or schematic confirmation.
- Recorded that `MPS` and `SS1` are concretely bound in the current callout layer, while `WDI` is stubbed and `SS2` is not independently observed in software.
- Linked the new page into `TLF35584 Driver Design Focus`, `TLF35584 Driver Callout And Hardware Binding`, and `index.md`.

## [2026-04-17] refine | TLF35584 board-level decisions clarified by project input

- Added project-confirmed usage rules for `SS2`, `WDI`, `WAK`, and `ENA`.
- Recorded that `SS2` is optional and mainly used only when delayed shutdown relative to `SS1` is required.
- Recorded that current projects intentionally do not use `WDI`, and prefer SPI watchdog service to avoid consuming an MCU pin.
- Recorded that `WAK` and `ENA` are project-dependent wake-source classes, with `WAK` often tied to a source such as `KL15` and `ENA` often tied to communication-edge wake sources.

## [2026-04-17] refine | TLF35584 generic regulator usage conventions

- Added cross-project usage conventions for `QT1`, `QT2`, `COM`, `VREF`, and `STDBY`.
- Recorded that `QT1` and `QT2` are commonly used for external sensor supply.
- Recorded that `COM` is commonly used for communication transceiver supply.
- Recorded that `VREF` is commonly used as analog or ADC reference supply.
- Recorded that `STDBY` is commonly used to keep an always-on low-power domain alive, such as an AURIX internal `SCR` domain or another wake-capable external device.

## [2026-04-28] refactor | business layer introduced and top-level structure clarified

- Expanded `README.md` into a detailed structure guide covering top-level areas, wiki responsibilities, source handling rules, and knowledge flow.
- Added `wiki/business/README.md` as the dedicated landing page for business-layer knowledge.
- Added reusable templates for `business-page`, `business-policy`, and `business-scenario`.
- Updated `index.md`, `wiki/README.md`, and `AGENTS.md` to recognize the new `business` area and clarify separation between concept, implementation, business, and decision knowledge.

## [2026-04-28] ingest | first TLF35584 business policy pages and encoding cleanup

- Added first business-layer pages for `TLF35584` wake, reset, watchdog-service, and fault-handling policy.
- Linked the new business pages into `index.md`.
- Rewrote `欢迎.md` into a clean Chinese landing page.
- Replaced the garbled `references/patterns/llm-wiki.md` content with a clean, concise pattern note plus a short Chinese summary.

## [2026-04-28] refactor | Chinese README and second wave of TLF35584 business policy pages

- Rewrote the top-level `README.md` in Chinese while preserving the clarified structure, flow, and directory responsibilities.
- Added `TLF35584 Safe-State Policy`, `TLF35584 Power-Domain Usage Policy`, and `TLF35584 Low-Power Transition Policy` under `wiki/business/`.
- Updated `index.md` so the new business pages appear in the main seed navigation.

## [2026-04-28] ingest | third wave of TLF35584 business policy pages

- Added `TLF35584 Startup Readiness Policy` to separate init completion from runtime-normal readiness.
- Added `TLF35584 Mode-Switch Ownership Policy` to clarify the split between upper-layer requests and driver-owned execution and verification.
- Added `TLF35584 Diagnostic Reporting Policy` to capture the rule that grouped driver diagnostics are the default reporting surface.
- Added `TLF35584 System Unusual Reason Policy` to frame cold-start, reset, and wake outputs as a classification layer rather than a complete root-cause engine.
- Updated `index.md` to expose the new business pages in the seed navigation.

## [2026-04-28] ingest | fourth wave of TLF35584 business policy pages

- Added `TLF35584 BIST Usage Policy` to define self-test as a controlled startup or service-phase activity.
- Added `TLF35584 ERR Monitoring Policy` to separate PMIC-side ERR behavior from end-to-end SMU validation closure.
- Added `TLF35584 Upper-Layer Integration Contract` to clarify API, scheduling, and ownership expectations for integrators.
- Added `TLF35584 Wake-Source Interpretation Policy` to keep wake-source classes separate from concrete board-net identification.
- Added `TLF35584 MPS Test-Mode Policy` to document MPS as a constrained board-aware control path.
- Updated `wiki/business/README.md` examples and added the new business pages to `index.md`.
