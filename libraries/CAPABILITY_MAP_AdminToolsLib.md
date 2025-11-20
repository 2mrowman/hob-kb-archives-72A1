*Last updated:* 20/11/2025 - 09:26 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 20/11/2025 - 09:26 (DEV-only)
*Build:* ac791c9

# 🧩 AdminToolsLib — Capability Map (V6.8.0)
## Scope
Κεντρικά admin helpers για Google Sheets: προστασίες, ορατότητα, καθαρισμοί, έλεγχοι πρόσβασης.
## Prerequisites
- Permissions: Spreadsheet scope, edit rights.
- Imports: `AdminToolsLib` (V6.8.0) στο project (Apps Script → Libraries).
## Commands (API Surface)
| Command | Params (type) | Returns | Purpose |
|---|---|---|---|
| `protectSheet` | sheetName: string, editors?: string[] | boolean | Προστασία φύλλου από edits εκτός editors. |
| `unprotectAll` |  — | number | Αφαιρεί όλες τις προστασίες στο αρχείο. |
| `hideSheets` | names: string[] | number | Κρύβει λίστα φύλλων. |
| `showSheets` | names: string[] | number | Εμφανίζει λίστα φύλλων. |
| `ensureHeaders` | sheetName: string, headers: string[] | boolean | Δημιουργεί/επιβεβαιώνει headers σειράς 1. |
| `lockRanges` | ranges: string[], editors?: string[] | number | Προστατεύει περιοχές A1. |
| `clearTabsExcept` | keep: string[] | number | Σβήνει tabs εκτός όσων κρατάς. |

> Συμπλήρωσε ακριβή signatures σύμφωνα με το `libraries/AdminToolsLib.md`.

## Usage Patterns
- OnOpen: `ensureHeaders` → `protectSheet` για βασική ασφάλεια UI.  
- Pre-duplication: `unprotectAll` → (ενέργεια) → `protectSheet`.  
- Rollout: `hideSheets` για system tabs, `showSheets` για user tabs.

## Recipes (links)
- Checklist.gs.md → “Init Admin Guards”: <link προς ενότητα>  
- Monthly cleanup: `clearTabsExcept` + `lockRanges`.

## Side Effects / Warnings
- Οι προστασίες είναι stateful· κράτα λίστα editors.  
- Η εκκαθάριση tabs είναι **μη αναστρέψιμη**.

## Changelog
- V6.8.0 — Initial capability map (structure only).

**RAW link (canonical):**  
https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_AdminToolsLib.md
