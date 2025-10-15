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

## 🧠 Hall of Brands – GPT Knowledge Base (Centralized Index)

Use this file as the single Knowledge Base entry for all Custom GPTs  
(e.g., ChecklistGPT, GitHub Coach, HoB Analyst).  
It provides structured links to all technical and documentation assets hosted in this repository.

---

### 🔗 Core Repository
**Main URL:**  
https://2mrowman.github.io/hob-kb-archives-72A1/  
**GitHub Source:**  
https://github.com/2mrowman/hob-kb-archives-72A1  

---

### 📘 Documentation
| Area | Link |
|------|------|
| System Overview | https://2mrowman.github.io/hob-kb-archives-72A1/SYSTEM_OVERVIEW.md |
| Functional Flow (Checklist V7) | https://2mrowman.github.io/hob-kb-archives-72A1/docs/Functional_Flow_CHECKLIST_V7.md |
| Flow Mapping (Checklist V7) | https://2mrowman.github.io/hob-kb-archives-72A1/docs/Flow_Mapping_CHECKLIST_V7.md |
| Project Settings (GAS) | https://2mrowman.github.io/hob-kb-archives-72A1/docs/GAS_CHECKLIST_V6.2_Project_Settings.md |

---

### ⚙️ Libraries
| Library | Version | Link |
|----------|----------|------|
| MenuLib | V7.0.0 | https://2mrowman.github.io/hob-kb-archives-72A1/libraries/B_MenuLib_V7.0.0.md |
| PopupLib | V2.0.0R | https://2mrowman.github.io/hob-kb-archives-72A1/libraries/C_PopupLib_Code.gs_V2.0.0R.md |
| AdminToolsLib | V6.7.4 | https://2mrowman.github.io/hob-kb-archives-72A1/libraries/D_AdminToolsLib_V6.7.4.md |
| HoBMastersLib | V7.1.0R | https://2mrowman.github.io/hob-kb-archives-72A1/libraries/E_HoBMastersLib_V7.1.0R.md |

---

### 🧩 Scripts
| Script | Version | Link |
|---------|----------|------|
| Checklist (V6 → V7.1.0R) | https://2mrowman.github.io/hob-kb-archives-72A1/scripts/1_CHECKLIST_V6_V7.1.0R.md |
| Auto Duplicate & Delete Tabs | https://2mrowman.github.io/hob-kb-archives-72A1/scripts/Auto%20Duplicate%20Delete%20Tabs.md |
| Blink Helper | https://2mrowman.github.io/hob-kb-archives-72A1/scripts/Blink%20Helper.md |

---

### 🧰 Additional Docs
| Title | Link |
|--------|------|
| Functional Reference Table | https://2mrowman.github.io/hob-kb-archives-72A1/docs/Functional_Reference_Table.md |
| Troubleshooting Guide | https://2mrowman.github.io/hob-kb-archives-72A1/docs/Troubleshooting.md |

---

### 🧾 For GPT Builder Connection
When setting up a Custom GPT (e.g., *ChecklistGPT V5*):
1. Open **Edit → Knowledge → Add URLs**  
2. Paste this single link:  

📅 **Last Updated:** 15 Oct 2025  
🔖 **Maintainer:** DEK / Hall of Brands Automation System

Knowledge Base Tagging:
[Category: HoB Automation / Checklist System / GAS Integration]


