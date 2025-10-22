*Last updated:* 22/10/2025 - 13:40 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 22/10/2025 - 13:40 (DEV-only)
*Build:* 0e80371

# 🧩 HoBMastersLib — Capability Map (V1.3)
**URL:** https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_HoBMastersLib.md
---
---
## Scope
Διαχείριση Templates από το κεντρικό αρχείο `HoB_Masters`. Παρέχει πρόσβαση σε template tabs για δημιουργία νέων ημερών.
## Prerequisites
- **Permissions:** Spreadsheet scope, read access to `HoB_Masters` file
- **Imports:** `HoBMastersLib` (V1.3) στο project (Apps Script → Libraries)
- **Master File ID:** `1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI`
## Commands (API Surface)
| Command | Params (type) | Returns | Purpose |
|---|---|---|---|
| `getTemplateTab` | templateName: string | Sheet | Επιστρέφει template tab από HoB_Masters file |
| `getMasterFileId` | — | string | Επιστρέφει το ID του HoB_Masters file |
| `listTemplates` | — | string[] | Επιστρέφει λίστα διαθέσιμων templates |
| `validateTemplate` | templateName: string | boolean | Ελέγχει αν το template υπάρχει |

> Συμπλήρωσε ακριβή signatures σύμφωνα με το `libraries/HoBMastersLib.md`.

## Usage Patterns

**OnOpen (auto-create new day):**
```javascript
function createNewDay_AUTO() {
  // 1. Get template from HoB_Masters
  const template = HoBMastersLib.getTemplateTab('Master1');

  // 2. Duplicate template to current spreadsheet
  const newSheet = template.copyTo(SpreadsheetApp.getActiveSpreadsheet());

  // 3. Rename to today's date
  const today = Utilities.formatDate(new Date(), 'Europe/Athens', 'yyyyMMdd_EEEE');
  newSheet.setName(today);

  return newSheet;
}
```

**Pre-validation:**
```javascript
function checkTemplateExists() {
  const templateName = 'Master1';

  if (!HoBMastersLib.validateTemplate(templateName)) {
    throw new Error('Template not found: ' + templateName);
  }

  return true;
}
```

**List available templates:**
```javascript
function showAvailableTemplates() {
  const templates = HoBMastersLib.listTemplates();
  Logger.log('Available templates: ' + templates.join(', '));
  return templates;
}
```

## Dependencies

**Used by:**
- `AdminToolsLib.createNewDay_AUTO()` — Main consumer
- `Checklist.gs.createNewDay_AUTO_Local()` — Wrapper function

**Depends on:**
- (none) — Standalone library

## Recipes (links)
- Checklist.gs.md → "Auto-create New Day": [link to section]
- AdminToolsLib.md → "Template Management": [link to section]

## Side Effects / Warnings
- **Read-only access:** HoBMastersLib does NOT modify the HoB_Masters file
- **Network dependency:** Requires access to Google Drive (HoB_Masters file)
- **Permission required:** User must have read access to HoB_Masters file
- **Cache:** Template data is NOT cached (fetched on every call)

## Error Handling

**Common errors:**
```javascript
// Error: Template not found
try {
  const template = HoBMastersLib.getTemplateTab('NonExistent');
} catch (error) {
  // Error: "Template 'NonExistent' not found in HoB_Masters"
  Logger.log(error.message);
}

// Error: No access to HoB_Masters
try {
  const template = HoBMastersLib.getTemplateTab('Master1');
} catch (error) {
  // Error: "You do not have permission to access HoB_Masters file"
  Logger.log(error.message);
}
```

## Performance Tips

**1. Validate before fetching:**
```javascript
// SLOW (fetches template even if it doesn't exist)
try {
  const template = HoBMastersLib.getTemplateTab('Master1');
} catch (error) {
  // Handle error
}

// FAST (validates first, then fetches)
if (HoBMastersLib.validateTemplate('Master1')) {
  const template = HoBMastersLib.getTemplateTab('Master1');
}
```

**2. Cache template list:**
```javascript
const cache = CacheService.getScriptCache();
let templates = cache.get('templates');

if (!templates) {
  templates = JSON.stringify(HoBMastersLib.listTemplates());
  cache.put('templates', templates, 3600); // 1 hour TTL
}

return JSON.parse(templates);
```

## Changelog
- **V1.3** — Current stable version
- **V1.2** — Added `validateTemplate()` function
- **V1.1** — Added `listTemplates()` function
- **V1.0** — Initial release with `getTemplateTab()`

---

**RAW link (canonical):**  
https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_HoBMastersLib.md

**Manus Audited:** 20/10/2025 – 08:22 (Europe/Athens)

