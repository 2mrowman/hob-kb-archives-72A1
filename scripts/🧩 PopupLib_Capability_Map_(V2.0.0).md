*Last updated:* 24/10/2025 - 08:45 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 24/10/2025 - 08:45 (DEV-only)
*Build:* 4ec5ea0

# 🧩 PopupLib — Capability Map (V2.0.0)
**URL:** https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_PopupLib.md
---
---
## Scope
Custom modal, native alert ή toast ανά trigger context. Εμφάνιση UI μηνυμάτων με context-aware fallback.
## Prerequisites
- **Permissions:** Spreadsheet scope, UI access (for modal/alert)
- **Imports:** `PopupLib` (V2.0.0) στο project (Apps Script → Libraries)
- **Depends on:** (none) — Standalone library
## Commands (API Surface)
| Command | Params (type) | Returns | Purpose |
|---|---|---|---|
| `showDialog` | title: string, message: string | void | Εμφανίζει custom modal dialog (HTML) |
| `showAlert` | message: string | void | Εμφανίζει native alert (simple) |
| `showToast` | message: string, title?: string, duration?: number | void | Εμφανίζει toast notification (bottom-right) |
| `showPrompt` | title: string, message: string | string | Εμφανίζει prompt dialog (user input) |
| `confirm` | message: string | boolean | Εμφανίζει confirmation dialog (Yes/No) |

> Συμπλήρωσε ακριβή signatures σύμφωνα με το `libraries/PopupLib.md`.

## Usage Patterns

**Custom modal dialog:**
```javascript
function showWelcomeMessage() {
  PopupLib.showDialog(
    'Welcome to HoB Checklist',
    'Today is: ' + Utilities.formatDate(new Date(), 'Europe/Athens', 'dd/MM/yyyy')
  );
}
```

**Toast notification (time-driven trigger):**
```javascript
function remindMissingNames() {
  const missingNames = _getMissingNames();

  if (missingNames.length > 0) {
    // Use toast (works in time-driven triggers)
    PopupLib.showToast(
      'Missing names: ' + missingNames.join(', '),
      'Reminder',
      10 // 10 seconds
    );
  }
}
```

**Confirmation dialog:**
```javascript
function deleteOldTabs() {
  const confirmed = PopupLib.confirm(
    'Are you sure you want to delete old tabs? This action cannot be undone.'
  );

  if (confirmed) {
    _performDeletion();
  }
}
```

**Prompt dialog (user input):**
```javascript
function askForUserName() {
  const userName = PopupLib.showPrompt(
    'Enter your name',
    'Please enter your full name:'
  );

  if (userName) {
    Logger.log('User name: ' + userName);
  }
}
```

## Dependencies

**Used by:**
- `MenuLib` — For error messages
- `AdminToolsLib` — For confirmation dialogs, toast notifications
- `Checklist.gs` — For validation feedback

**Depends on:**
- (none) — Standalone library

## Recipes (links)
- AdminToolsLib.md → "User Confirmation": [link to section]
- Checklist.gs.md → "Validation Feedback": [link to section]

## Side Effects / Warnings
- **Context dependency:** `showDialog()`, `showAlert()`, `showPrompt()`, `confirm()` only work in trigger contexts with UI access (onOpen, onEdit, custom menu)
- **Fallback:** `showToast()` works in ALL contexts (including time-driven triggers)
- **Duration:** Toast duration is in seconds (default: 5 seconds)
- **Blocking:** `showDialog()`, `showAlert()`, `showPrompt()`, `confirm()` are blocking (script waits for user response)
- **Non-blocking:** `showToast()` is non-blocking (script continues immediately)

## Error Handling

**Common errors:**
```javascript
// Error: No UI access (time-driven trigger)
try {
  PopupLib.showDialog('Title', 'Message');
} catch (error) {
  // Error: "Cannot access UI in this context"
  Logger.log(error.message);
  // Fallback: Use toast
  PopupLib.showToast('Message', 'Title', 10);
}

// Error: Empty message
try {
  PopupLib.showToast('');
} catch (error) {
  // Error: "Message cannot be empty"
  Logger.log(error.message);
}
```

## Context-Aware Usage

**Recommended pattern:**
```javascript
function showMessage(message, title) {
  try {
    // Try to show dialog (if UI access available)
    PopupLib.showDialog(title, message);
  } catch (error) {
    // Fallback to toast (works in all contexts)
    PopupLib.showToast(message, title, 10);
  }
}
```

**Trigger context table:**

| Trigger Type | showDialog | showAlert | showPrompt | confirm | showToast |
|--------------|------------|-----------|------------|---------|-----------|
| onOpen | ✅ | ✅ | ✅ | ✅ | ✅ |
| onEdit | ✅ | ✅ | ✅ | ✅ | ✅ |
| Custom menu | ✅ | ✅ | ✅ | ✅ | ✅ |
| Time-driven | ❌ | ❌ | ❌ | ❌ | ✅ |
| Installable trigger | ❌ | ❌ | ❌ | ❌ | ✅ |

## Performance Tips

**1. Use toast for non-critical messages:**
```javascript
// SLOW (blocking, waits for user to close dialog)
PopupLib.showDialog('Info', 'Data saved successfully');

// FAST (non-blocking, continues immediately)
PopupLib.showToast('Data saved successfully', 'Info', 3);
```

**2. Batch confirmations:**
```javascript
// SLOW (multiple confirmation dialogs)
for (let tab of tabs) {
  const confirmed = PopupLib.confirm('Delete tab: ' + tab + '?');
  if (confirmed) {
    _deleteTab(tab);
  }
}

// FAST (single confirmation dialog)
const confirmed = PopupLib.confirm('Delete ' + tabs.length + ' tabs?');
if (confirmed) {
  for (let tab of tabs) {
    _deleteTab(tab);
  }
}
```

**3. Cache user preferences:**
```javascript
const cache = CacheService.getScriptCache();
let showWelcome = cache.get('showWelcome');

if (showWelcome === null) {
  // First time: ask user
  const confirmed = PopupLib.confirm('Show welcome message on every open?');
  cache.put('showWelcome', confirmed.toString(), 86400); // 24 hours
  showWelcome = confirmed.toString();
}

if (showWelcome === 'true') {
  PopupLib.showDialog('Welcome', 'Welcome to HoB Checklist');
}
```

## Changelog
- **V2.0.0** — Current stable version with context-aware fallback
- **V1.5.0** — Added `showPrompt()` and `confirm()`
- **V1.0.0** — Initial release with `showDialog()`, `showAlert()`, `showToast()`

---

**RAW link (canonical):**  
https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_PopupLib.md

**Manus Audited:** 20/10/2025 – 08:24 (Europe/Athens)

