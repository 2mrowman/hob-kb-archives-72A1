*Last updated:* 23/10/2025 - 14:46 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 23/10/2025 - 14:46 (DEV-only)
*Build:* 0bf787c

# 🧩 MenuLib — Capability Map (V7.0.0)
**URL:** https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_MenuLib.md
---
---
## Scope
Ανάγνωση & φόρτωση δυναμικού μενού στο Google Sheets. Διαχειρίζεται User vs Owner functions.
## Prerequisites
- **Permissions:** Spreadsheet scope, UI access
- **Imports:** `MenuLib` (V7.0.0) στο project (Apps Script → Libraries)
- **Depends on:** `PopupLib` (for error messages)
## Commands (API Surface)
| Command | Params (type) | Returns | Purpose |
|---|---|---|---|
| `createMenu` | — | void | Δημιουργεί δυναμικό μενού στο UI |
| `getMenuItems` | userType: string | MenuItem[] | Επιστρέφει menu items ανά user type ('user' or 'owner') |
| `addMenuItem` | name: string, functionName: string | void | Προσθέτει custom menu item |
| `refreshMenu` | — | void | Ανανεώνει το μενού (re-creates) |

> Συμπλήρωσε ακριβή signatures σύμφωνα με το `libraries/MenuLib.md`.

## Usage Patterns

**OnOpen (create menu):**
```javascript
function onOpen(e) {
  // 1. Create menu
  MenuLib.createMenu();

  // 2. Auto-create new day (if needed)
  createNewDay_AUTO_Local();
}
```

**User vs Owner menu:**
```javascript
function createMenu() {
  const owner = Session.getActiveUser().getEmail();
  const AUTHORIZED_OWNER = 'hobdeks@gmail.com';

  // Determine user type
  const userType = (owner === AUTHORIZED_OWNER) ? 'owner' : 'user';

  // Get menu items for user type
  const menuItems = MenuLib.getMenuItems(userType);

  // Create menu
  const ui = SpreadsheetApp.getUi();
  const menu = ui.createMenu('HoB Checklist');

  for (let item of menuItems) {
    menu.addItem(item.name, item.functionName);
  }

  menu.addToUi();
}
```

**Custom menu item:**
```javascript
function addCustomMenuItem() {
  MenuLib.addMenuItem('Export Data', 'exportData');
  MenuLib.refreshMenu(); // Re-create menu to show new item
}
```

## Dependencies

**Used by:**
- `Checklist.gs.onOpen()` — Main consumer

**Depends on:**
- `PopupLib` — For error messages

## Recipes (links)
- Checklist.gs.md → "OnOpen Menu Creation": [link to section]
- PopupLib.md → "Error Messages": [link to section]

## Side Effects / Warnings
- **UI dependency:** Only works in trigger contexts with UI access (onOpen, custom menu)
- **1-to-1 mapping:** Each menu item MUST map to exactly ONE function
- **Owner filter:** Menu items are filtered by user type (user vs owner)
- **Refresh required:** After adding custom menu items, call `refreshMenu()`

## Error Handling

**Common errors:**
```javascript
// Error: No UI access (time-driven trigger)
try {
  MenuLib.createMenu();
} catch (error) {
  // Error: "Cannot access UI in this context"
  Logger.log(error.message);
  // Fallback: Log menu items instead
  Logger.log('Menu items: ' + JSON.stringify(MenuLib.getMenuItems('user')));
}

// Error: Invalid function name
try {
  MenuLib.addMenuItem('Invalid', 'nonExistentFunction');
} catch (error) {
  // Error: "Function 'nonExistentFunction' not found"
  Logger.log(error.message);
}
```

## Performance Tips

**1. Cache menu items:**
```javascript
const cache = CacheService.getScriptCache();
const userType = 'user';
let menuItems = cache.get('menuItems_' + userType);

if (!menuItems) {
  menuItems = JSON.stringify(MenuLib.getMenuItems(userType));
  cache.put('menuItems_' + userType, menuItems, 3600); // 1 hour TTL
}

return JSON.parse(menuItems);
```

**2. Lazy menu creation:**
```javascript
// Don't create menu on every onOpen if not needed
function onOpen(e) {
  // Only create menu if user interacts with UI
  if (e && e.authMode === ScriptApp.AuthMode.FULL) {
    MenuLib.createMenu();
  }
}
```

## Changelog
- **V7.0.0** — Current stable version with dynamic menu support
- **V6.5.0** — Added `addMenuItem()` and `refreshMenu()`
- **V6.0.0** — Added user vs owner filtering
- **V5.0.0** — Initial release with `createMenu()`

---

**RAW link (canonical):**  
https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_MenuLib.md

**Manus Audited:** 20/10/2025 – 08:23 (Europe/Athens)

