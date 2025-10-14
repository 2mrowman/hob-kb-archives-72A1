# 🗂️ **INDEX – HoB CHECKLIST Documentation (V7.1.0R)**

## 📘 Overview
This index provides a complete documentation map for the **Hall of Brands CHECKLIST Automation System (V7.1.0R – Popup Restoration Build)**.  
All references below point to the relevant Markdown files, libraries, and images within this repository.

---

## 📁 Documentation (Docs/)
| File | Description |
|------|--------------|
| [README.MD](../README.MD) | Main repository overview and architecture summary |
| [notes_for_gpt.md](../notes_for_gpt.md) | GPT indexing context and knowledge base structure |
| [Docs/GAS ChecklistV6.2_Project Settings.md](GAS%20ChecklistV6.2_Project%20Settings.md) | GAS configuration details, IDs, and permissions |
| [Docs/Flow_Mapping_CHECKLIST_V7.md](Flow_Mapping_CHECKLIST_V7.md) | Technical flow mapping – triggers, libraries, dependencies |
| [Docs/Functional_Flow_CHECKLIST_V7.md](Functional_Flow_CHECKLIST_V7.md) | Functional flow – user perspective and daily logic |

---

## 🧩 Libraries (Overview)
| Library | Description | Version |
|----------|--------------|----------|
| `AdminToolsLib` | Central automation and workflow engine | V6.7.6 |
| `PopupLib` | Custom popup, modal & fallback UI handling | V2.0.0 |
| `MenuLib` | Dynamic HoB menu generator | V7.0.0 |
| `HoBMastersLib` | Template duplication and master tab handler | V1.3 |
| `DuplicateDeleteTABS` | Controlled file duplication and cleanup | V1.1 |

---

## 🧱 Core Scripts
| Script | Purpose |
|---------|----------|
| `Checklist.gs` | Main trigger handler (onOpen, onEdit, onInstall) |
| `Blink.gs` | Visual user feedback (cell blinking, missing name alerts) |
| `AutoDupl_File&DeleteTabs.gs` | Monthly duplication and cleanup routine |

---

## 🖼️ Visual References (Docs/Images/)
| Diagram | File | Description |
|----------|------|-------------|
| **Core Script Structure** | `flow_core_script_structure.png` | Displays the global logic of `Checklist.gs` and library connections |
| **Trigger Flow (onOpen / onEdit / Time)** | `flow_onOpen_onEdit_triggers.png` | Illustrates trigger-based flow of events |
| **Inter-library Dependencies** | `flow_interlibrary_dependencies.png` | Shows dependency and communication between libraries |

---

## 🧠 Knowledge Base Metadata
- **Main Context File:** `notes_for_gpt.md`  
- **Tagging:** `[Category: HoB Automation / Checklist System / GAS Integration]`
- **Knowledge Hierarchy:**
  1. `Functional_Flow_CHECKLIST_V7.md` → operational flow reference  
  2. `Flow_Mapping_CHECKLIST_V7.md` → technical mapping reference  
  3. `GAS_ChecklistV6.2_Project_Settings.md` → configuration reference

---

## 🕹️ Version Information
| Component | Version | Date | Notes |
|------------|----------|------|-------|
| Checklist System | V7.1.0R | 13/10/2025 | Popup Restoration Build |
| AdminToolsLib | V6.7.6 | 25/09/2025 | Stable automation build |
| PopupLib | V2.0.0 | 07/10/2025 | Modal + native fallback |
| MenuLib | V7.0.0 | 25/09/2025 | Dynamic menu builder |
| HoBMastersLib | V1.3 | 25/09/2025 | Template duplication handler |

---

## 🧾 Author & Credits
**Author:** DEK – BD‑PM (Business Development & Project Manager)  
**Organization:** Hall of Brands  
**Email:** dek@beyondlimits.events  
**Location:** Athens, Greece  
**Revision Date:** 13 October 2025

© 2025 Hall of Brands | Internal Developer Documentation Only
