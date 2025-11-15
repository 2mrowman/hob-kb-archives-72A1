*Last updated:* 15/11/2025 - 17:50 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 15/11/2025 - 17:50 (DEV-only)
*Build:* e1f22e5

# CHANGELOG – Hall of Brands Knowledge Base
**Repository:** hob-kb-archives-72A1  
**Owner:** 2mrowman  
**Timezone:** Europe/Athens (GMT+3)
---
## [V6.0.0] – 20/10/2025
### Added
- **notes_for_gpt.md V6.0.0** — Complete rewrite with 6 new sections (706 lines vs 99 original)
  - PROJECT OVERVIEW — Business context, tech stack, users
  - ARCHITECTURE — Sheets structure, library hierarchy, data flow
  - CODING STANDARDS — GAS conventions, naming, error handling
  - DEPENDENCIES — Library dependency map, version table
  - COMMON PATTERNS — Reusable code patterns, best practices
  - GOTCHAS — Known issues, workarounds, debugging tips
- **CAPABILITY_MAP_HoBMastersLib.md** — API surface documentation for template management library
  - Function signatures, parameters, return values
  - Usage examples, dependencies, error handling

- **CAPABILITY_MAP_MenuLib.md** — API surface documentation for menu creation library
  - Function signatures, parameters, return values
  - Usage examples, dependencies, error handling

- **CAPABILITY_MAP_PopupLib.md** — API surface documentation for UI messages library
  - Function signatures, parameters, return values
  - Usage examples, dependencies, error handling

### Changed
- **RAW_LINKS_INDEX.md** — Added `?ts=1760960086` timestamps to 10 critical files for cache-busting
  - notes_for_gpt.md
  - All CAPABILITY_MAP files (AdminToolsLib, HoBMastersLib, MenuLib, PopupLib)
  - All library .md files (AdminToolsLib, HoBMastersLib, MenuLib, PopupLib, README)

- **notes_for_gpt.md** — Added `?ts=1760960086` timestamps to 28 KB reference links for cache-busting
  - Index files (index.md, INDEX_Checklist_Docs.md, RAW_LINKS_INDEX.md, etc.)
  - Documentation files (Functional_Flow, Flow_Mapping, GAS_Settings, etc.)
  - Library files (all CAPABILITY_MAP and .md files)
  - Script files (Checklist.gs.md, Blink.gs.md, etc.)
  - History files (LATEST.md, MANIFEST.md, RAW_HISTORY_INDEX.md)

### Fixed
- **Cache-busting issue** — ChatGPT now reads updated KB files immediately (no stale cache)
- **Missing context** — ChecklistGPT now has full project context (architecture, standards, patterns)

### Verified
- ✅ ChecklistGPT confirmed reading notes_for_gpt.md V6.0.0 (706 lines)
- ✅ All timestamps consistent (`?ts=1760960086` = 20/10/2025 10:34:46 GMT+3)
- ✅ RAW_LINKS_INDEX.md: 10 timestamps verified
- ✅ notes_for_gpt.md: 28 timestamps verified

---

## [V5.2.1R] – 18/10/2025

### Changed
- **notes_for_gpt.md** — Minor updates to existing structure
- **CAPABILITY_MAP_AdminToolsLib.md** — Initial capability map for AdminToolsLib

### Context
- Original notes_for_gpt.md: 99 lines
- Identified 6 critical gaps in KB coverage
- Planned V6.0.0 complete rewrite

---

## Version History Legend

**Version format:** `MAJOR.MINOR.PATCH[R]`
- **MAJOR** — Breaking changes, complete rewrites
- **MINOR** — New sections, significant additions
- **PATCH** — Bug fixes, small updates
- **R suffix** — Release/production ready

**Change types:**
- **Added** — New files, sections, features
- **Changed** — Updates to existing content
- **Fixed** — Bug fixes, corrections
- **Removed** — Deleted files, deprecated content
- **Verified** — Confirmation checks, validation results

---

**Last updated:** 20/10/2025 – 16:20 (Europe/Athens)

