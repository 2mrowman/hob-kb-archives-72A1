# Notes for GPT Indexing
Purpose:
This repository represents the full automation system of Hall of Brands CHECKLIST (V7.1.0R).

Contains:
- All scripts (.gs) and libraries used across stores.
- Documentation describing technical flow, mapping, and dependencies.
- Master references for each connected Google Sheet file.

Primary Entry Points:
1. Checklist.gs → main coordinator.
2. AdminToolsLib → executes all functional actions.
3. PopupLib → handles all UI communication.
4. HoBMastersLib → handles MASTER tab duplication.
5. MenuLib → manages dynamic menu population.

Key File IDs:
HoB_Masters_File_ID = "1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI"
Template_Tab = "Master1"

Libraries Integration Order:
Checklist.gs → AdminToolsLib → PopupLib → HoBMastersLib → MenuLib.

Important:
- Do not summarize functions; reference file names directly.
- Always respect library interconnections.
- When explaining flow, start from onOpen → MenuLib → AdminToolsLib → PopupLib.
- Treat "GAS_ChecklistV6.2_Project_Settings.md" as configuration base.
- Treat "Flow_Mapping_CHECKLIST_V7.md" as the technical map.
- Treat "Functional_Flow_CHECKLIST_V7.md" as operational flow reference.


---
# 🧠 Hall of Brands – GPT Knowledge Base (Central Index)

This repository represents the **full automation system of Hall of Brands CHECKLIST (V7.1.0R)**.  
It contains all scripts, libraries, and documentation used across store checklists.

---

## 🔗 Core Repository
**Main GitHub Repo:**  
https://github.com/2mrowman/hob-kb-archives-72A1  

**Primary Index:**  
[INDEX_Checklist_Docs.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/INDEX_Checklist_Docs.md)

---

## 📘 Documentation
| Area | Link |
|------|------|
| System Overview | [SYSTEM_OVERVIEW.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/SYSTEM_OVERVIEW.md) |
| Functional Flow (Checklist V7) | [Functional_Flow_CHECKLIST_V7.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/docs/Functional_Flow_CHECKLIST_V7.md) |
| Flow Mapping (Checklist V7) | [Flow_Mapping_CHECKLIST_V7.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/docs/Flow_Mapping_CHECKLIST_V7.md) |
| Project Settings (GAS V6.2) | [GAS ChecklistV6.2_Project Settings.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/docs/GAS%20ChecklistV6.2_Project%20Settings.md) |
| Prompt Reference | [Prompt_Current.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/docs/Prompt_Current.md) |

---

## ⚙️ Libraries
| Library | Version | Link |
|----------|----------|------|
| **HoBMastersLib** | V1.3 | [A. HoBMasterLib - Duplicate.gsV1.3.MD](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/libraries/A.%20HoBMasterLib%20-%20Duplicate.gsV1.3.MD) |
| **MenuLib** | V7.0.0 | [B. MenuLib - MenuLib.gs _V7.0.0.MD](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/libraries/B.%20MenuLib%20-%20MenuLib.gs%20_V7.0.0.MD) |
| **PopupLib** | V2.0.0R | [C. PopupLib - Code.gs_V2.0.0R.MD](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/libraries/C.%20PopupLib%20-%20Code.gs_V2.0.0R.MD) |
| **AdminToolsLib** | V6.7.6 | [D. AdminToolsLib - AdminToolsLib.gs_V6.7.6.MD](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/libraries/D.%20AdminToolsLib%20-%20AdminToolsLib.gs_V6.7.6.MD) |

---

## 🧩 Scripts
| Script | Version | Link |
|---------|----------|------|
| **Checklist.gs** | V7.1.0R | [1CHECKLIST V6 - Checklist.gs_V7.1.0R.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/scripts/1CHECKLIST%20V6%20-%20Checklist.gs_V7.1.0R.md) |
| **Blink Helper** | — | [2CHECKLIST V6 - Blink.gs.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/scripts/2CHECKLIST%20V6%20-%20Blink.gs.md) |
| **Auto Duplicate / Delete Tabs** | — | [3CHECKLIST V6 - AutoDupl_File&DeleteTabs.gs.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/scripts/3CHECKLIST%20V6%20-%20AutoDupl_File%26DeleteTabs.gs.md) |

---

## 🧾 GPT Builder Setup
When connecting this repository to a Custom GPT (e.g. *ChecklistGPT V5.0*):
1. In the GPT editor → **Edit → Knowledge → Add URL**
2. Paste this link:  
   👉 https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/INDEX_Checklist_Docs.md
3. Add tag:  
   `[Category: HoB Automation / Checklist System / GAS Integration]`

---

**Maintained by ChecklistGPT V5.0 – Hall of Brands Automation Stack**  
*Last Updated: 15 Oct 2025*

Knowledge Base Tagging:
[Category: HoB Automation / Checklist System / GAS Integration]





