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

Knowledge Base Tagging:
[Category: HoB Automation / Checklist System / GAS Integration]
