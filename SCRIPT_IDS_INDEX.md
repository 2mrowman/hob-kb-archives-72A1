*Last updated:* 24/10/2025 - 08:45 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 24/10/2025 - 08:45 (DEV-only)
*Build:* 4ec5ea0

### SCRIPT_IDS_INDEX.md – Hall of Brands Automation Stack
Centralized reference of all **Google Apps Script** and **Library IDs** used across the HoB ecosystem.  
_Last Updated: 19 Oct 2025_  
_Version: V1.0.0R_  
---
## 🧭 Purpose
This file provides a unified lookup table for all **Script IDs**, **Library IDs**, and **Integration Keys** related to the HoB automation system.  
It enables GPT-based systems and developers to:
- Quickly locate the correct library or script by ID.
- Verify current active versions.
- Detect outdated or deprecated IDs.
---
## 📘 Libraries (`/libraries`)
| Library | Type | Script ID | Description | Notes |
|----------|------|------------|-------------|-------|
| **HoBMastersLib** | Library | `1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI` | Core duplication & day-creation logic (Master Template functions). | Used in all Checklists. |
| **MenuLib** | Library | `18liAb8q4WMrLheskvRq3XQz2y5_EM-J71Df0PsNsQMzlRRRQflCMgAul` | Dynamic menu builder for Checklist UI. | Called on `onOpen()` trigger. |
| **PopupLib** | Library | `12dL6B4_pErrHEDQmFoxAu7jVdKGuzHjt-3NsVgernsqKpgrSXm86C329` | Custom popup modal for user notifications. | Supports modal & alert styles. |
| **AdminToolsLib** | Library | `1ALGlsiH5xHvo_qLscY258CYsOqbYbCZ2HQKz6tl-qj-etV0p2v9r8cZx` | Admin & protection utilities for Sheets. | Handles un/protect & sheet control. |

🟢 *All four libraries are permanently linked in every active CHECKLIST file (V6–V7 series).*

---

## 🧩 Scripts (`/scripts`)
| Script | Type | Script ID | Description | Notes |
|---------|------|------------|-------------|-------|
| **DuplicateDeleteTABS.gs** | Script | `1ryekzwj3owrxXSjt7ty0veKniq9TQq2K` | Duplicates Master tab & deletes all others (monthly cleanup). | Central trigger: 1st of each month. |
| **HoB_Masters_Template** | Script | `1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI` | Main Master Template used in all Checklists. | Basis for V6–V7 builds. |
| **1. CHECKLIST V6 Template (RENTIHOBTEST)** | Script | `1_BWHcIAGz3Jvwj00tB493Q9CKgOdq5ydr4tMmK6cmzA` | Store test version used for RENTIHOB workflow. | Reference for integration testing. |
| **GLYHOBTEST** | Script | `1S02d3Cdh88UMbmDtix6eHEirMpcAkx22X6lpBCWR37c` | Store test version for Glyfada store. | Mirrors RENTIHOBTEST structure. |
| **CHECKLIST V7 Active (Main)** | Script | `1djJdbfzqQHvoQODevC61P-DoKvUW7cz90noZPrUGIYoFR_2qX3m4O4S0` | Production template for 2025 rollout. | **Active** – Updated: 19/10/2025. |

---

## 🌐 External Integrations
| Component | Type | Key / URL | Description | Notes |
|------------|------|------------|-------------|-------|
| **n8n Webhook (AI Agent)** | Endpoint | `https://dekhob.app.n8n.cloud/webhook/aiagent-sheet-comments` | Handles comments from Google Sheets → AI Agent notifications. | Used in RENTIHOBTEST + future 20-checklist integration. |
| **Google Sheets API Project** | API Project Name | `HoB DEKS Google Sheets API` | Main Google Cloud project handling Sheets reads. | Associated API Key below. |
| **Google Sheets API Key** | Key | `AIzaSyDCLDvE0ojqAdDXTn2LHImLlbmwegtEDZU` | Used for direct API read/write in n8n workflows. | Read-only authorized key. |

---

## 🧱 Folder & Asset IDs
| Component | Type | ID | Description |
|------------|------|----|-------------|
| **HoB Duplicate Folder** | Google Drive Folder | `1ryekzwj3owrxXSjt7ty0veKniq9TQq2K` | Storage location for daily duplicated checklist files. |
| **HoB Script Master Template Folder** | Google Drive Folder | `1lEZ5hWvZaBnD_fCjP3dybXY7w9Sx4AVmX4XBYiN6_JX5bM9mgQp7iVnE` | Historical test folder (deprecated; no longer in use). |

---

## 🔐 Version Reference
| Component | Version | Status |
|------------|----------|---------|
| **Checklist.gs** | V7.1.0R | Stable Build |
| **AdminToolsLib** | V6.7.6 | Stable |
| **PopupLib** | V2.0.0R | Stable |
| **MenuLib** | V7.0.0 | Stable |
| **HoBMastersLib** | V1.3 | Stable |

---

## ✅ Usage Notes
1. The GPT Model should read this file before referencing any script or library.  
2. Treat this document as the **single source of truth** for all IDs.  
3. Deprecated IDs (marked as *Historical / Deprecated*) should not be used in future builds.  
4. When a new library version is published, update this index and commit immediately.

---

**Maintained by:** ChecklistGPT V5.0  
**Repository:** https://github.com/2mrowman/hob-kb-archives-72A1  
**Document ID:** SCRIPT_IDS_INDEX.md – V1.0.0R
