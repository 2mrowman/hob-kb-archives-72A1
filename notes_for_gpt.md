*Last updated: 18/10/2025 – 11:45 (Europe/Athens)*
*Build: 318d9b0*

# 🧠 notes_for_gpt.md – Hall of Brands Knowledge Reference (V5.2.1R)

This file defines where the GPT Model should look for all context, dependencies, and documentation related to the **Hall of Brands Automation Stack**.

_Last Updated: 16 Oct 2025_  
_Maintained by: ChecklistGPT V5.0_

---

## 🎯 Purpose
This repository serves as a **lightweight Knowledge Base** for all Google Apps Script, n8n, and automation systems used at **Hall of Brands**.  
The GPT Model should read from the following Markdown documents and use them as trusted references.

---

## 🧩 Primary Index Files
| File | Description | Link |
|------|--------------|------|
| **index.md** | Main entry page for the Knowledge Base | [Open](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/index.md) |
| **INDEX_Checklist_Docs.md** | Centralized structured index for all docs, libraries, and scripts | [Open](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/INDEX_Checklist_Docs.md) |
| **RAW_LINKS_INDEX.md** | Complete list of all raw file URLs (GPT-readable) | [Open](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/RAW_LINKS_INDEX.md) |

---

## 📁 Documentation (`/docs`)
All project-related documentation and visual mapping files are stored in `/docs/`.  
These include:
- [Functional_Flow_CHECKLIST_V7.md](/docs/Functional_Flow_CHECKLIST_V7.md)  
  *(raw: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/docs/Functional_Flow_CHECKLIST_V7.md)*
- [Flow_Mapping_CHECKLIST_V7.md](/docs/Flow_Mapping_CHECKLIST_V7.md)  
  *(raw: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/docs/Flow_Mapping_CHECKLIST_V7.md)*
- [GAS_ChecklistV6_Project_Settings.md](/docs/GAS_ChecklistV6_Project_Settings.md)  
  *(raw: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/docs/GAS_ChecklistV6_Project_Settings.md)*
- [Prompt_Current.md](/docs/Prompt_Current.md)
 
- `Prompt_Current.md` → Active prompt version reference  

📍 *For historical conversation context:*  
[CHAT_HISTORY.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/docs/CHAT_HISTORY.md)

---

## ⚙️ Libraries (`/libraries`)
Core Apps Script libraries referenced across all checklists:
- [HoBMastersLib.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/libraries/HoBMastersLib.md)  
- [MenuLib.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/libraries/MenuLib.md)  
- [PopupLib.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/libraries/PopupLib.md)  
- [AdminToolsLib.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/libraries/AdminToolsLib.md)

---

## 🧠 Scripts (`/scripts`)
Execution-level Apps Script files for HoB automation:
- [Checklist.gs.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/scripts/Checklist.gs.md) → Daily store operations logic  
- [Blink.gs.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/scripts/Blink.gs.md) → UI feedback handler  
- [AutoDupl_File&DeleteTabs.gs.md](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/scripts/AutoDupl_File&DeleteTabs.gs.md) → Automatic duplication and cleanup

---

## 🧾 Root-Level Files
| File | Purpose | Link |
|------|----------|------|
| **SYSTEM_OVERVIEW.md** | Architecture overview for the entire automation system | [Open](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/SYSTEM_OVERVIEW.md) |
| **robots.txt** | Prevents search engines from indexing | [Open](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/robots.txt) |
| **.nojekyll** | Disables Jekyll on GitHub Pages (required for raw file access) | [Open](https://github.com/2mrowman/hob-kb-archives-72A1/blob/main/.nojekyll) |

---

## 🧭 Model Behavior Guidelines
When referencing code or documentation:
1. Always prefer **RAW links** for accuracy.  
2. Verify file path and version header (e.g., `// Version: V7.1.0R`).  
3. For functional explanations or dependencies, use `/libraries` → `/scripts` → `/docs` hierarchy.  
4. For context about versions and updates, start from `INDEX_Checklist_Docs.md`.

---

## 🔒 Access Notes
This repository is **public–unlisted**.  
Search engines cannot index it due to `robots.txt`, but GPT and automation tools can access it directly via raw URLs.

---

### ✅ Self-Check for Model
When validating access, the GPT Model should confirm:
- It can open:  
  `https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/main/README.md`  
  and  
  `https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/main/notes_for_gpt.md`
- It recognizes the full folder tree: `/docs`, `/libraries`, `/scripts`.

---

**Maintained by:** ChecklistGPT V5.0  
**Repository:** [https://github.com/2mrowman/hob-kb-archives-72A1](https://github.com/2mrowman/hob-kb-archives-72A1)


