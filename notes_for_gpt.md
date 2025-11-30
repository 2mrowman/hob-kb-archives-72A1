*Last updated:* 30/11/2025 - 07:43 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 30/11/2025 - 07:43 (DEV-only)
*Build:* 248c8ba

### notes_for_gpt.md – Hall of Brands Knowledge Reference (V6.2.0)]
**URL:** https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/notes_for_gpt.md?ts=1764478263
---
Οδηγός για το GPT Model: από πού να διαβάζει **structure, versions, flow, history** του HoB automation stack.
---
## 🎯 Purpose
Το repo λειτουργεί ως **lightweight Knowledge Base** για Google Apps Script, n8n και σχετικά συστήματα.  
Το μοντέλο πρέπει να χρησιμοποιεί τα παρακάτω ως **canonical** πηγές.
---
## 🚨 ΚΑΝΟΝΑΣ #0: MANDATORY FILE READING (TOP PRIORITY)
**ΑΥΤΟΣ Ο ΚΑΝΟΝΑΣ ΥΠΕΡΙΣΧΥΕΙ ΟΛΩΝ ΤΩΝ ΑΛΛΩΝ**
### Για ΚΑΘΕ ερώτηση που αφορά κώδικα, bugs, features, ή debugging:
#### **ΒΗΜΑ 1: ΠΑΥΣΗ**
- ❌ ΜΗΝ απαντήσεις αμέσως
- ❌ ΜΗΝ υποθέσεις τι υπάρχει στον κώδικα
- ❌ ΜΗΝ δίνεις γενικές θεωρητικές απαντήσεις

#### **ΒΗΜΑ 2: ΔΙΑΒΑΣΕ (ΥΠΟΧΡΕΩΤΙΚΟ)**
1. Άνοιξε **INDEX_Checklist_Docs.md** (RAW URL με ?ts=)
2. Βρες τα σχετικά files (scripts, libraries)
3. Διάβασε τα **RAW URLs** των files
4. Βρες τα συγκεκριμένα functions που αναφέρονται
5. Κατάλαβε τι κάνει ο υπάρχων κώδικας

#### **ΒΗΜΑ 3: ΕΠΙΒΕΒΑΙΩΣΕ**
Πριν απαντήσεις, ρώτησε τον εαυτό σου:
- ✅ Μπορώ να αναφέρω συγκεκριμένες γραμμές κώδικα;
- ✅ Κατάλαβα τι κάνει ο υπάρχων κώδικας;
- ✅ Έχω πραγματική διάγνωση, όχι υπόθεση;
- ✅ Διάβασα ΟΛΑ τα σχετικά files (scripts + libraries);

Αν ΟΠΟΙΑΔΗΠΟΤΕ απάντηση είναι "ΟΧΙ", **ΣΤΑΜΑΤΑ** και διάβασε τα αρχεία.

#### **ΒΗΜΑ 4: ΑΠΑΝΤΗΣΕ**
Μόνο ΤΟΤΕ δώσε απάντηση:
- Με αναφορές σε πραγματικό κώδικα
- Με συγκεκριμένες γραμμές (π.χ. "στη γραμμή 245 του AdminToolsLib.md")
- Με πραγματική διάγνωση βασισμένη σε ευρήματα

---

### ❌ ΑΠΟΛΥΤΩΣ ΑΠΑΓΟΡΕΥΕΤΑΙ:

1. **Να λες "Δεν έχω πρόσβαση στον κώδικα"**
   - ❌ ΛΑΘΟΣ: "Δεν έχω άμεση πρόσβαση στο σώμα των κώδικων"
   - ✅ ΣΩΣΤΟ: Όλα τα files είναι διαθέσιμα μέσω RAW URLs στο INDEX_Checklist_Docs.md

2. **Να δίνεις λύση χωρίς να διαβάσεις τα αρχεία**
   - ❌ ΛΑΘΟΣ: "Το πρόβλημα είναι ότι..." (χωρίς να έχεις διαβάσει τον κώδικα)
   - ✅ ΣΩΣΤΟ: "Περίμενε να διαβάσω τα αρχεία... [διαβάζει]... Διάβασα το AdminToolsLib.md και βρήκα..."

3. **Να υποθέτεις τι υπάρχει στον κώδικα**
   - ❌ ΛΑΘΟΣ: "Πιθανώς το function καλεί..."
   - ✅ ΣΩΣΤΟ: "Διάβασα τον κώδικα και στη γραμμή 64 το function καλεί..."

4. **Να δίνεις γενικές θεωρητικές απαντήσεις**
   - ❌ ΛΑΘΟΣ: "Γενικά, τα time-driven triggers δεν έχουν UI context..."
   - ✅ ΣΩΣΤΟ: "Διάβασα το AdminToolsLib.md, γραμμή 245: Το remindMissingNames() καλεί PopupLib.showDialog() που δεν δουλεύει σε time-driven triggers (notes_for_gpt.md, γραμμή 514)"

---

### ✅ ΥΠΟΧΡΕΩΤΙΚΟ:

1. **Να διαβάζεις τα αρχεία πρώτα**
   - Πάντα ξεκίνα με INDEX_Checklist_Docs.md
   - Διάβασε τα RAW URLs των σχετικών files
   - Μην απαντήσεις πριν διαβάσεις

2. **Να επιβεβαιώνεις με πραγματικό κώδικα**
   - Αναφέρε συγκεκριμένες γραμμές
   - Παράθεσε κομμάτια κώδικα
   - Εξήγησε τι κάνει ο υπάρχων κώδικας

3. **Να αναφέρεις συγκεκριμένες γραμμές**
   - "Στο AdminToolsLib.md, γραμμή 245..."
   - "Στο Checklist.gs.md, γραμμή 64..."
   - "Στο notes_for_gpt.md, γραμμή 514..."

4. **Να δηλώνεις τι διάβασες**
   - "Διάβασα το AdminToolsLib.md και βρήκα..."
   - "Διάβασα το Checklist.gs.md και είδα ότι..."
   - "Ελέγχοντας το notes_for_gpt.md, επιβεβαίωσα ότι..."

---

### 📚 ΠΑΡΑΔΕΙΓΜΑΤΑ: Σωστή vs Λάθος Προσέγγιση

#### **Παράδειγμα 1: Debugging Request**

**Χρήστης:** "Το remindMissingNames δεν εμφανίζει popup"

**❌ ΛΑΘΟΣ Απάντηση:**
```
"Το πρόβλημα είναι ότι τα time-driven triggers δεν έχουν UI context. 
Πρέπει να χρησιμοποιήσεις DocumentProperties και να εμφανίσεις το popup 
από onOpen/onEdit..."
```
**Γιατί είναι λάθος:**
- Δεν διάβασε τα αρχεία
- Υπέθεσε το πρόβλημα
- Δεν επιβεβαίωσε με πραγματικό κώδικα

---

**✅ ΣΩΣΤΗ Απάντηση:**
```
"Περίμενε να διαβάσω τα σχετικά αρχεία...

[Διαβάζει INDEX_Checklist_Docs.md]
[Διαβάζει AdminToolsLib.md]
[Διαβάζει Checklist.gs.md]

Διάβασα τον κώδικα και βρήκα:

1. **AdminToolsLib.md, γραμμή 245:** 
   Το `remindMissingNames()` καλεί `PopupLib.showDialog()`

2. **Checklist.gs.md, γραμμή 105:** 
   Το trigger που τρέχει το `remindMissingNames()` είναι time-driven (κάθε 20 λεπτά)

3. **notes_for_gpt.md, γραμμή 514 (GOTCHAS section):**
   'PopupLib.showDialog() only works in certain trigger contexts'
   'Why: Apps Script limitations (no UI in time-driven triggers)'

**ΔΙΑΓΝΩΣΗ:**
Το πρόβλημα είναι ότι το `remindMissingNames()` τρέχει από time-driven trigger 
και προσπαθεί να ανοίξει UI dialog με `PopupLib.showDialog()`, που δεν δουλεύει 
σε αυτό το context.

**ΛΥΣΗ:**
Αλλαγή στο AdminToolsLib.md, γραμμή 245:
- Αντί για PopupLib.showDialog()
- Χρησιμοποίησε PopupLib.showToast() (δουλεύει σε time-driven)
- Ή γράψε flag σε DocumentProperties και εμφάνισε το dialog από onOpen/onEdit
"
```
**Γιατί είναι σωστή:**
- Διάβασε τα αρχεία πρώτα
- Αναφέρει συγκεκριμένες γραμμές
- Επιβεβαιώνει με πραγματικό κώδικα
- Δίνει πραγματική διάγνωση

---

#### **Παράδειγμα 2: Feature Request**

**Χρήστης:** "Πώς μπορώ να προσθέσω νέο function στο MenuLib;"

**❌ ΛΑΘΟΣ Απάντηση:**
```
"Πρόσθεσε το function στο MenuLib με camelCase naming και μην ξεχάσεις 
να το προσθέσεις στο function checklist..."
```
**Γιατί είναι λάθος:**
- Δεν διάβασε το MenuLib.md
- Δεν είδε τη δομή του υπάρχοντος κώδικα
- Δίνει γενικές οδηγίες χωρίς context

---

**✅ ΣΩΣΤΗ Απάντηση:**
```
"Περίμενε να διαβάσω τη δομή του MenuLib...

[Διαβάζει INDEX_Checklist_Docs.md]
[Διαβάζει MenuLib.md]
[Διαβάζει CAPABILITY_MAP_MenuLib.md]

Διάβασα το MenuLib (v7.0.0) και βρήκα:

1. **MenuLib.md, γραμμή 12:** Function checklist
   - createMenu()
   - getMenuItemsFromSheet(type)
   - getOwnerEmail()
   [DO NOT remove/rename without approval]

2. **MenuLib.md, γραμμή 45:** Naming convention
   - Public functions: camelCase
   - Private functions: _camelCase

3. **MenuLib.md, γραμμή 78:** Dependencies
   - Depends on: PopupLib
   - Used by: Checklist.gs

4. **CAPABILITY_MAP_MenuLib.md:** Current capabilities
   - Dynamic menu creation
   - Owner/user role separation
   - Integration with PopupLib for error messages

**ΓΙΑ ΝΑ ΠΡΟΣΘΕΣΕΙΣ ΝΕΟ FUNCTION:**

1. **Ενημέρωσε το function checklist (γραμμή 12):**
   ```javascript
   /**
    * FUNCTION CHECKLIST
    * - createMenu()
    * - getMenuItemsFromSheet(type)
    * - getOwnerEmail()
    * - yourNewFunction()  // NEW
    */
   ```

2. **Πρόσθεσε το function με JSDoc:**
   ```javascript
   /**
    * [Brief description]
    * @param {type} paramName - Description
    * @return {type} Description
    */
   function yourNewFunction(paramName) {
     // Implementation
   }
   ```

3. **Update VERSIONS_INDEX.md:**
   - MenuLib: v7.0.0 → v7.1.0 (MINOR version bump)

4. **Test στο sandbox spreadsheet**

5. **Commit με μήνυμα:**
   `[ADD] MenuLib: yourNewFunction() (v7.1.0)`
"
```
**Γιατί είναι σωστή:**
- Διάβασε τα σχετικά αρχεία
- Αναφέρει συγκεκριμένες γραμμές
- Δείχνει τη δομή του υπάρχοντος κώδικα
- Δίνει step-by-step οδηγίες βασισμένες στον πραγματικό κώδικα

---

#### **Παράδειγμα 3: "Που βρίσκεται το X;"**

**Χρήστης:** "Που βρίσκεται το function createNewDay_AUTO();"

**❌ ΛΑΘΟΣ Απάντηση:**
```
"Το function createNewDay_AUTO() βρίσκεται στο AdminToolsLib."
```
**Γιατί είναι λάθος:**
- Δεν διάβασε το INDEX_Checklist_Docs.md
- Δεν έδωσε RAW URL
- Δεν αναφέρει συγκεκριμένη γραμμή

---

**✅ ΣΩΣΤΗ Απάντηση:**
```
"Περίμενε να ελέγξω το INDEX_Checklist_Docs.md...

[Διαβάζει INDEX_Checklist_Docs.md]
[Διαβάζει AdminToolsLib.md]

Το function `createNewDay_AUTO()` βρίσκεται:

**File:** AdminToolsLib.md
**Path:** `/libraries/AdminToolsLib.md`
**RAW URL:** https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/AdminToolsLib.md?ts=1764478263
**Line:** Γραμμή 156 (περίπου, ανάλογα με την έκδοση)

**Function signature:**
```javascript
function createNewDay_AUTO(masterFileId, templateName) {
  // Implementation...
}
```

**Called by:**
- Checklist.gs.md, γραμμή 64: `AdminToolsLib.createNewDay_AUTO(HOB_MASTERS_FILE_ID, templateTab)`

**Dependencies:**
- HoBMastersLib.getTemplateTab()
- PopupLib.showDialog()
"
```
**Γιατί είναι σωστή:**
- Διάβασε το INDEX_Checklist_Docs.md
- Έδωσε RAW URL
- Αναφέρει συγκεκριμένη γραμμή
- Δείχνει dependencies

---

## 🐛 DEBUGGING WORKFLOW (MANDATORY)

### Όταν ο χρήστης αναφέρει bug ή πρόβλημα:

**Checklist (ΟΛΑ πρέπει να είναι ✅ πριν απαντήσεις):**

- [ ] **Διάβασα το INDEX_Checklist_Docs.md**
  - Βρήκα τα σχετικά files (scripts, libraries)

- [ ] **Διάβασα το σχετικό script file**
  - Βρήκα το συγκεκριμένο function που αναφέρεται
  - Κατάλαβα τι κάνει

- [ ] **Διάβασα τις σχετικές libraries**
  - Ελέγξα τις dependencies
  - Κατάλαβα τη ροή δεδομένων

- [ ] **Διάβασα τα capability maps (αν χρειάζεται)**
  - Κατάλαβα τις advanced features

- [ ] **Ελέγξα το notes_for_gpt.md για known issues**
  - Έψαξα στο "GOTCHAS & PITFALLS" section
  - Έψαξα στο "Common Errors" section

- [ ] **Διάγνωσα το πραγματικό πρόβλημα**
  - Όχι υπόθεση, αλλά πραγματική διάγνωση
  - Βασισμένη σε ευρήματα από τον κώδικα

- [ ] **Μπορώ να αναφέρω συγκεκριμένες γραμμές κώδικα**
  - "Στο [file], γραμμή [X]..."
  - Παράθεση κώδικα

- [ ] **Η λύση μου βασίζεται σε πραγματικά ευρήματα**
  - Όχι γενικές θεωρητικές λύσεις
  - Συγκεκριμένες αλλαγές στον υπάρχοντα κώδικα

---

**Αν ΟΛΑ τα παραπάνω είναι ✅, ΤΟΤΕ:**

1. **Γράψε την απάντηση με αυτή τη δομή:**

```
"Διάβασα τα σχετικά αρχεία και βρήκα:

**ΕΥΡΗΜΑΤΑ:**
1. [File], γραμμή [X]: [Τι βρήκες]
2. [File], γραμμή [Y]: [Τι βρήκες]
3. [File], γραμμή [Z]: [Τι βρήκες]

**ΔΙΑΓΝΩΣΗ:**
[Πραγματική διάγνωση βασισμένη στα ευρήματα]

**ΛΥΣΗ:**
[Συγκεκριμένες αλλαγές στον κώδικα]
"
```

2. **Αναφέρε πάντα:**
   - Ποια files διάβασες
   - Ποιες γραμμές κώδικα ελέγξες
   - Τι βρήκες σε κάθε file
   - Πώς συνδέονται τα ευρήματα

3. **Μην ξεχάσεις:**
   - Dependencies (ποια libraries χρησιμοποιούνται)
   - Known issues (από notes_for_gpt.md)
   - Version information (από VERSIONS_INDEX.md)

---

## ✅ SELF-VALIDATION (Πριν στείλεις απάντηση)

**Ρώτησε τον εαυτό σου:**

### 1. "Διάβασα τα αρχεία που χρειάζονται;"
- [ ] INDEX_Checklist_Docs.md
- [ ] Σχετικά scripts
- [ ] Σχετικές libraries
- [ ] notes_for_gpt.md (για known issues)

Αν **ΟΧΙ** → ΣΤΑΜΑΤΑ και διάβασε τα αρχεία

---

### 2. "Μπορώ να αναφέρω συγκεκριμένες γραμμές κώδικα;"
- [ ] "Στο [file], γραμμή [X]..."
- [ ] Μπορώ να παραθέσω κώδικα
- [ ] Μπορώ να εξηγήσω τι κάνει ο κώδικας

Αν **ΟΧΙ** → ΣΤΑΜΑΤΑ και διάβασε τα αρχεία πιο προσεκτικά

---

### 3. "Η λύση μου βασίζεται σε πραγματικά δεδομένα;"
- [ ] Όχι υπόθεση, αλλά πραγματική διάγνωση
- [ ] Βασισμένη σε ευρήματα από τον κώδικα
- [ ] Συγκεκριμένες αλλαγές, όχι γενικές οδηγίες

Αν **ΟΧΙ** → Η απάντησή σου είναι πολύ γενική, διάβασε ξανά

---

### 4. "Αν ο χρήστης με ρωτήσει 'είδες τα αρχεία;', τι θα απαντήσω;"
- [ ] "Ναι, διάβασα [file1], [file2], [file3]"
- [ ] "Βρήκα [X] στη γραμμή [Y] του [file]"
- [ ] "Ελέγξα τις dependencies και βρήκα..."

Αν **ΟΧΙ** → Δεν διάβασες τα αρχεία, επέστρεψε στο ΒΗΜΑ 2

---

### 5. "Είμαι σίγουρος ότι η διάγνωσή μου είναι σωστή;"
- [ ] Επιβεβαίωσα με πραγματικό κώδικα
- [ ] Ελέγξα τις dependencies
- [ ] Ελέγξα για known issues
- [ ] Η λύση μου είναι συγκεκριμένη και εφαρμόσιμη

Αν **ΟΧΙ** → Η διάγνωσή σου είναι υπόθεση, όχι πραγματική

---

**Αν ΟΛΑ τα παραπάνω είναι ΝΑΙ ✅, τότε η απάντησή σου είναι έτοιμη.**

**Αν ΟΠΟΙΟΔΗΠΟΤΕ είναι ΟΧΙ ❌, ΣΤΑΜΑΤΑ και διόρθωσε πριν απαντήσεις.**

---

## 🏢 PROJECT OVERVIEW
### What is Hall of Brands (HoB)?
**Hall of Brands (HoB)** is a retail operations management system for **Hall of Brands & Saint Soles** stores.
**Core systems:**
- **Checklist System (V7.1.0R)** — Daily task management for retail stores
- **KPI Monitoring** — Performance tracking and reporting
- **Training System** — Employee onboarding and skill tracking
- **Automation Stack** — Google Sheets + Apps Script + n8n workflows

**Primary users:**
- **Store managers** — Daily checklist completion
- **Regional managers** — KPI monitoring
- **Admin team (DEK)** — System configuration, maintenance

**Technology stack:**
- **Frontend:** Google Sheets (UI)
- **Backend:** Google Apps Script (automation)
- **Orchestration:** n8n (workflows, future integration)
- **Storage:** Google Drive (files), Google Sheets (data)
- **Workspace:** `beyondlimits.events`
- **Owner:** `hobdeks@gmail.com`

**Business context:**
- **Retail operations:** Daily checklists for opening, closing, inventory, cleaning
- **Multi-store:** Each store has its own checklist spreadsheet
- **Template-driven:** New days created from `Master1` template tab
- **Automation-first:** Minimal manual intervention, auto-create new days on open

---

## 🏗️ ARCHITECTURE

### Google Sheets Structure

**Main spreadsheet:** HoB Checklist (per store)

**Sheets (tabs):**
- **Daily tabs** (e.g., `20251020_Κυριακή`) — Daily checklist (auto-created from template)
- **Master1** — Template tab (hidden, protected)
- **Config** — System settings (store ID, owner email, etc.)
- **Logs** — Automation logs (optional, for debugging)
- **Archive** — Historical data (optional, for reporting)

**Master file:** `HoB_Masters` [Contact admin for Script ID access]
- Contains templates for all stores
- Used by `HoBMastersLib` to create new tabs

### Library Hierarchy

```
Checklist.gs (main script)
├── MenuLib (menu creation)
│   └── PopupLib (UI dialogs)
├── AdminToolsLib (admin functions)
│   ├── HoBMastersLib (template access)
│   └── PopupLib (UI dialogs)
└── Blink.gs (helper script for blinking feedback)
```

**Dependency table:**

| Library | Depends On | Used By |
|---------|------------|---------|
| **HoBMastersLib** | (none) | AdminToolsLib, Checklist.gs |
| **MenuLib** | AdminToolsLib, PopupLib | Checklist.gs |
| **PopupLib** | (none) | MenuLib, AdminToolsLib, Checklist.gs |
| **AdminToolsLib** | HoBMastersLib, PopupLib | MenuLib, Checklist.gs |

### Data Flow

```
User opens spreadsheet
  ↓
onOpen() trigger (Checklist.gs)
  ↓
MenuLib.createMenu() — Loads dynamic menu
  ↓
createNewDay_AUTO_Local() — Checks if today's tab exists
  ↓
If NOT exists → AdminToolsLib.createNewDay_AUTO()
  ↓
HoBMastersLib.getTemplateTab() — Fetches Master1 from HoB_Masters
  ↓
AdminToolsLib duplicates tab, renames to YYYYMMDD_Day
  ↓
PopupLib.showDialog() — Confirms creation
  ↓
User interacts with checklist (checkboxes, dropdowns, comments)
  ↓
onEdit() trigger (Checklist.gs) — Validates input, logs changes
  ↓
Time-driven trigger (every 20 min) — AdminToolsLib.remindMissingNames()
  ↓
PopupLib.showToast() — Reminds user to fill in names
```

### External Integrations

- **n8n workflows:** (Future) Triggered via webhooks for KPI reporting
- **Google Drive:** File storage for templates, logs
- **Email notifications:** Via `GmailApp` (for reminders, alerts)

---

## 📐 CODING STANDARDS

### Naming Conventions

**Functions:**
- **Public functions:** `camelCase` (e.g., `getUserData()`)
- **Private functions:** `_camelCase` with underscore prefix (e.g., `_validateInput()`)
- **Menu entry points:** `on[Action]` (e.g., `onOpenMenu()`)
- **Trigger handlers:** `onOpen(e)`, `onEdit(e)`

**Variables:**
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES = 3`)
- **Local variables:** `camelCase` (e.g., `userName`)
- **Global variables:** `g_camelCase` with `g_` prefix (e.g., `g_config`)

**Files:**
- **Scripts:** `[Name].gs.md` (e.g., `Checklist.gs.md`)
- **Libraries:** `[Name]Lib.md` (e.g., `AdminToolsLib.md`)
- **Documentation:** `[Name]_[Type]_V[X].md` (e.g., `Functional_Flow_CHECKLIST_V7.md`)

### Function Patterns

**Standard function structure:**
```javascript
/**
 * [Brief description]
 * @param {type} paramName - Description
 * @return {type} Description
 */
function functionName(paramName) {
  // 1. Validate input
  if (!paramName) {
    throw new Error('paramName is required');
  }

  // 2. Execute logic
  const result = _processData(paramName);

  // 3. Return result
  return result;
}
```

**Error handling:**
```javascript
try {
  // Risky operation
  const result = riskyFunction();
  return result;
} catch (error) {
  Logger.log('Error in functionName: ' + error.message);
  // Graceful fallback or re-throw
  throw new Error('Failed to execute: ' + error.message);
}
```

### Code Organization

**File structure:**
```javascript
// 1. Header comment (version, last updated, build)
// Version: V7.1.0R
// Last updated: 20/10/2025 – 08:00 (Europe/Athens)
// Build: f1d244f

// 2. Function checklist (compatibility contract)
/**
 * FUNCTION CHECKLIST
 * - onOpen(e)
 * - onEdit(e)
 * - createNewDay_AUTO_Local()
 * [DO NOT remove/rename without approval]
 */

// 3. Constants
const MAX_RETRIES = 3;
const OWNER_EMAIL = 'hobdeks@gmail.com';

// 4. Public functions (alphabetical)
function createNewDay_AUTO_Local() { ... }
function onEdit(e) { ... }
function onOpen(e) { ... }

// 5. Private functions (alphabetical)
function _checkIfTodayExists() { ... }
function _validateInput(input) { ... }

// 6. Helper functions
function _logDebug(message) {
  Logger.log('[DEBUG] ' + message);
}
```

**Function checklist (at top of file):**
```javascript
/**
 * FUNCTION CHECKLIST (compatibility contract)
 * - onOpen(e)
 * - onEdit(e)
 * - createNewDay_AUTO_Local()
 * - getUserData(userId)
 * - updateUserData(userId, data)
 * [DO NOT remove/rename without approval]
 */
```

### Versioning Rules

**Version format:** `MAJOR.MINOR.PATCH` (e.g., `7.1.0`)

**Increment rules:**
- **MAJOR** (e.g., 7.0.0 → 8.0.0) — Breaking change (function signature change, removed function)
- **MINOR** (e.g., 7.0.0 → 7.1.0) — New function, new feature (backward compatible)
- **PATCH** (e.g., 7.0.0 → 7.0.1) — Bug fix, performance improvement (no API change)

**Suffix:**
- **R** (e.g., `7.1.0R`) — Release build (stable, production-ready)
- **RC** (e.g., `7.1.0RC`) — Release candidate (testing)
- **BETA** (e.g., `7.1.0BETA`) — Beta version (experimental)

---

## 🔗 DEPENDENCIES

### Library Dependencies

| Library | Version | Depends On | Used By | Script ID |
|---------|---------|------------|---------|-----------|
| **HoBMastersLib** | v1.3 | (none) | AdminToolsLib, Checklist.gs | Not tracked in repo |
| **MenuLib** | v7.2.3 | AdminToolsLib, PopupLib | Checklist.gs | Not tracked in repo |
| **PopupLib** | v2.0.0 | (none) | MenuLib, AdminToolsLib, Checklist.gs | Not tracked in repo |
| **AdminToolsLib** | v6.14.0 | HoBMastersLib, PopupLib | MenuLib, Checklist.gs | Not tracked in repo |

### Function Dependencies (Critical)

**AdminToolsLib → HoBMastersLib:**
- `AdminToolsLib.createNewDay_AUTO()` → calls `HoBMastersLib.getTemplateTab()`
- `AdminToolsLib.duplicateTab()` → uses template from `HoBMastersLib`

**AdminToolsLib → PopupLib:**
- `AdminToolsLib.createNewDay_AUTO()` → calls `PopupLib.showDialog()` (confirmation)
- `AdminToolsLib.remindMissingNames()` → calls `PopupLib.showToast()` (reminder)

**MenuLib → AdminToolsLib:**
- `MenuLib.createNewDayFromMenu()` → calls `AdminToolsLib.createNewDay_AUTO()`
- `MenuLib.clearAllNotesFromMenu()` → calls `AdminToolsLib.clearAllNotes()`
- `MenuLib.showMasterAndDeleteOthersFromMenu()` → calls `AdminToolsLib.showMasterAndDeleteOthers()`
- `MenuLib.remindMissingNamesFromMenu()` → calls `AdminToolsLib.remindMissingNames()`
- `MenuLib.automatedDuplicateAndCleanupFromMenu()` → calls `AdminToolsLib.automatedDuplicateAndCleanup()`

**MenuLib → PopupLib:**
- `MenuLib.createMenu()` → calls `PopupLib.showDialog()` (error messages)

**Checklist.gs → All:**
- `onOpen()` → calls `MenuLib.createMenu()`, `AdminToolsLib.createNewDay_AUTO()`
- `onEdit()` → calls `PopupLib.showToast()` (validation feedback)

### Breaking Change Rules

**If you modify:**
- `HoBMastersLib.getTemplateTab()` → **MUST** update `AdminToolsLib.createNewDay_AUTO()`
- `PopupLib.showDialog()` → **MUST** update `MenuLib.createMenu()` and `AdminToolsLib.createNewDay_AUTO()`
- `MenuLib.createMenu()` → **MUST** update `Checklist.gs.onOpen()`

**Version increment:**
- Breaking change → MAJOR version bump (e.g., 7.0.0 → 8.0.0)
- New function → MINOR version bump (e.g., 7.0.0 → 7.1.0)
- Bug fix → PATCH version bump (e.g., 7.0.0 → 7.0.1)

**Dependency sync:**
- After updating library → **MUST** update `VERSIONS_INDEX.md`
- After updating library → **MUST** test all dependent scripts

---

## 🔧 LIBRARY SETUP (MANDATORY)

### When Creating or Migrating Libraries

Each library **MUST** have its dependencies loaded **inside the library project** (not just in Checklist.gs).

**Why?** When a library calls another library (e.g., MenuLib calls AdminToolsLib), the dependency must be loaded **in the calling library's project**.

### Setup Order (Bottom-Up)

**1. PopupLib** (No dependencies)
- Dependencies: (none)
- No setup needed
- Deploy first

**2. HoBMastersLib**
- Dependencies: PopupLib (if needed)
- Setup:
  1. Open HoBMastersLib project
  2. Libraries → Add PopupLib (if used)
  3. Deploy

**3. AdminToolsLib**
- Dependencies: HoBMastersLib, PopupLib
- Setup:
  1. Open AdminToolsLib project
  2. Libraries → Add HoBMastersLib
  3. Libraries → Add PopupLib
  4. Deploy

**4. MenuLib**
- Dependencies: AdminToolsLib, PopupLib
- Setup:
  1. Open MenuLib project
  2. Libraries → Add AdminToolsLib
  3. Libraries → Add PopupLib
  4. Deploy

**5. Checklist.gs**
- Dependencies: MenuLib, AdminToolsLib, HoBMastersLib, PopupLib
- Setup:
  1. Open Checklist.gs project
  2. Libraries → Add all 4 libraries
  3. Save

### Version Selection

**For Development (CHECKLIST V7, testing):**
- Use **HEAD** for all libraries
- Instant updates, no redeploy needed
- Easy debugging

**For Production (Store files: RENTIHOB, GLYHOB, etc.):**
- Use **Version 1** (or latest stable version)
- Stable, predictable behavior
- No unexpected changes

### Deployment Workflow

**When redeploying all libraries:**

1. **PopupLib** → Deploy (no dependencies)
2. **HoBMastersLib** → Deploy (depends on PopupLib)
3. **AdminToolsLib** → Deploy (depends on HoBMastersLib, PopupLib)
4. **MenuLib** → Deploy (depends on AdminToolsLib, PopupLib)
5. **Checklist.gs** → Refresh all library versions

**Important:** Always deploy in this order (bottom-up) to avoid dependency errors.

### Re-deployment Same Version

**When you change code or dependencies:**

1. Manage deployments → Select active deployment
2. Edit (pencil icon)
3. Deploy (without changing version number)
4. This updates the existing version with new code

**You do NOT need to create a new version every time.**

### Complete Dependency Map

```
PopupLib (no dependencies)
  ↑
  ├─ HoBMastersLib
  ├─ AdminToolsLib ← HoBMastersLib
  └─ MenuLib ← AdminToolsLib, PopupLib
       ↑
       └─ Checklist.gs ← MenuLib, AdminToolsLib, HoBMastersLib, PopupLib
```

### Troubleshooting: "AdminToolsLib is not defined"

**Error:**
```
ReferenceError: AdminToolsLib is not defined
at clearAllNotesFromMenu(Code:146:36)
```

**Cause:** MenuLib does NOT have AdminToolsLib loaded as a dependency.

**Fix:**
1. Open MenuLib project
2. Libraries → Add AdminToolsLib
   - Script ID: `1o-7UYDTvO3sR4aBGqfp1k-YZYfOxo1ytN2nGg-OJA9__qgZB1Qtd7lI2`
   - Identifier: `AdminToolsLib`
   - Version: HEAD (for dev) or 1 (for prod)
3. Save
4. Redeploy MenuLib
5. Update Checklist.gs → MenuLib version
6. Refresh sheet

**Prevention:** Always check that libraries have their dependencies loaded **inside their own projects**.

---

## 🔄 COMMON PATTERNS

### Adding a New Feature

**Steps:**
1. **Update function checklist** in target file
2. **Add function** following naming conventions
3. **Add JSDoc comment** with params and return type
4. **Add error handling** (try/catch)
5. **Update VERSIONS_INDEX.md** with version bump (MINOR)
6. **Update INDEX_Checklist_Docs.md** if documentation added
7. **Test** in sandbox spreadsheet
8. **Commit** with message: `[ADD] Feature description (vX.Y.Z)`

**Example:**
```javascript
// In Checklist.gs.md

// 1. Add to function checklist
/**
 * FUNCTION CHECKLIST
 * - onOpen(e)
 * - onEdit(e)
 * - createNewDay_AUTO_Local()
 * - exportData() // NEW
 */

// 2. Add function
/**
 * Export checklist data to CSV
 * @return {Blob} CSV file
 */
function exportData() {
  try {
    const data = _getAllData();
    const csv = _convertToCSV(data);
    return Utilities.newBlob(csv, 'text/csv', 'checklist_export.csv');
  } catch (error) {
    Logger.log('Error in exportData: ' + error.message);
    throw new Error('Failed to export data: ' + error.message);
  }
}

// 3. Update VERSIONS_INDEX.md
// Checklist.gs: v7.1.0 → v7.2.0

// 4. Commit
// [ADD] Checklist.gs: exportData() for CSV export (v7.2.0)
```

### Fixing a Bug

**Steps:**
1. **Identify the bug** (file, function, line number)
2. **Read the code** (understand what it does)
3. **Diagnose the root cause** (not just symptoms)
4. **Fix the code** (minimal change)
5. **Test the fix** (verify it works)
6. **Update VERSIONS_INDEX.md** with version bump (PATCH)
7. **Commit** with message: `[FIX] Bug description (vX.Y.Z)`

**Example:**
```javascript
// Before (bug)
function _getMissingNames() {
  const data = sheet.getRange('A2:B').getValues();
  return data.filter(row => row[1] === ''); // BUG: includes empty rows
}

// After (fixed)
function _getMissingNames() {
  const data = sheet.getRange('A2:B').getValues();
  return data.filter(row => row[0] && row[1] === ''); // FIX: check if row[0] exists
}

// Update VERSIONS_INDEX.md
// AdminToolsLib: v6.8.0 → v6.8.1

// Commit
// [FIX] AdminToolsLib: _getMissingNames() now ignores empty rows (v6.8.1)
```

### Updating a Library

**Steps:**
1. **Make changes** to library file
2. **Update function checklist** if functions added/removed
3. **Update VERSIONS_INDEX.md** with new version
4. **Test all dependent scripts** (check DEPENDENCIES section)
5. **Update capability maps** if new features added
6. **Commit** with message: `[UPDATE] Library description (vX.Y.Z)`

**Example:**
```javascript
// In PopupLib.md

// 1. Add new function
/**
 * Show custom HTML popup with icon
 * @param {string} html - HTML content
 * @param {string} type - Type (success, error, warning, info)
 * @param {string} icon - Icon emoji
 */
function showCustomPopupWithIcon(html, type, icon) {
  const template = HtmlService.createTemplate(
    '<div class="popup-' + type + '">' + icon + ' ' + html + '</div>'
  );
  SpreadsheetApp.getUi().showModalDialog(
    template.evaluate().setWidth(400).setHeight(200),
    'Notification'
  );
}

// 2. Update function checklist
/**
 * FUNCTION CHECKLIST
 * - showDialog(title, message)
 * - showToast(message)
 * - showCustomPopup(html, type)
 * - showCustomPopupWithIcon(html, type, icon) // NEW
 */

// 3. Update VERSIONS_INDEX.md
// PopupLib: v2.0.0 → v2.1.0 (MINOR - new function)

// 4. Test in Checklist.gs, MenuLib, AdminToolsLib

// 5. Commit
// [UPDATE] PopupLib: Add showCustomPopupWithIcon() (v2.1.0)
```

---

## ⚠️ GOTCHAS & PITFALLS

### Common Issues and How to Avoid Them

**1. HoBMastersLib Template Name Mismatch**
- **Issue:** `getTemplateTab()` returns `null` because template name doesn't match
- **Why:** Template names in `HoB_Masters/Templates` sheet must exactly match spreadsheet names
- **Fix:** Check `Templates` sheet, verify spelling/capitalization
- **Example:**
  ```javascript
  // In HoB_Masters → Templates sheet:
  // Column A: "HoB Checklist - Store 1"
  // Column B: "Master1_Store1"

  // In Checklist.gs:
  const fileName = SpreadsheetApp.getActiveSpreadsheet().getName(); // "HoB Checklist - Store 1"
  const templateTab = getTemplateTabFromHoBMasters_(); // Returns "Master1_Store1"
  ```

**2. MenuLib Owner Email Check**
- **Issue:** Owner menu items don't appear even though user is owner
- **Why:** `MenuLib.getOwnerEmail()` reads from `Config` sheet, which may be outdated
- **Fix:** Update `Config` sheet with correct owner email, or check `Session.getEffectiveUser().getEmail()`
- **Example:**
  ```javascript
  // In MenuLib.md:
  function getOwnerEmail() {
    const config = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Config');
    return config.getRange('B2').getValue(); // Must match actual owner
  }
  ```

**3. AdminToolsLib Duplicate Tab Race Condition**
- **Issue:** Multiple users opening spreadsheet simultaneously creates duplicate tabs
- **Why:** `createNewDay_AUTO()` checks if tab exists, but another user may create it at the same time
- **Fix:** Add lock mechanism with `LockService`
- **Example:**
  ```javascript
  function createNewDay_AUTO(masterFileId, templateName) {
    const lock = LockService.getScriptLock();
    try {
      lock.waitLock(10000); // Wait up to 10 seconds

      // Check if tab already exists (another user may have created it)
      if (_checkIfTodayExists()) {
        return 'TAB_ALREADY_EXISTS';
      }

      // Create tab
      // ...
    } finally {
      lock.releaseLock();
    }
  }
  ```

**4. Checklist.gs Integrity Validation**
- **Issue:** Spreadsheet corrupted (missing sheets, wrong structure)
- **Why:** Manual edits, accidental deletions
- **Fix:** Add `runIntegrityCheck_()` to `onOpen()`
- **Example:**
  ```javascript
  function runIntegrityCheck_() {
    const ss = SpreadsheetApp.getActiveSpreadsheet();

    // Check 1: Config sheet exists
    if (!ss.getSheetByName('Config')) {
      throw new Error('Config sheet missing');
    }

    // Check 2: Master1 tab exists (hidden)
    const master = ss.getSheetByName('Master1');
    if (!master || !master.isSheetHidden()) {
      throw new Error('Master1 tab missing or visible');
    }

    // Check 3: Owner filter present
    if (!_hasOwnerFilter()) {
      throw new Error('Owner filter missing');
    }

    return 'INTEGRITY_OK';
  }
  ```

**5. PopupLib Context Dependency**
- **Issue:** `PopupLib.showDialog()` only works in certain trigger contexts
- **Why:** Apps Script limitations (no UI in time-driven triggers)
- **Workaround:** Use `PopupLib.showToast()` or `Logger.log()` in time-driven triggers
- **Example:**
  ```javascript
  function remindMissingNames() {
    // This is a time-driven trigger
    const missingNames = _getMissingNames();

    if (missingNames.length > 0) {
      // CORRECT: Use toast (works in time-driven)
      PopupLib.showToast('Missing names: ' + missingNames.join(', '));

      // INCORRECT: Use dialog (fails in time-driven)
      // PopupLib.showDialog('Missing names', missingNames.join(', '));
    }
  }
  ```

### Common Errors

**Error:** `ReferenceError: AdminToolsLib is not defined`
- **Cause:** Library not added to project
- **Fix:** `Resources → Libraries → Add AdminToolsLib` using the Script ID stored in the Apps Script project settings (IDs are not tracked in this repo)

**Error:** `Exception: Service invoked too many times for one day`
- **Cause:** Exceeded daily quota (e.g., email sends: 100/day for free accounts)
- **Fix:** Add rate limiting, use batch operations, upgrade to paid account

**Error:** `TypeError: Cannot read property 'getRange' of null`
- **Cause:** Sheet doesn't exist or wrong name
- **Fix:** Check sheet name spelling, verify sheet exists with `SpreadsheetApp.getActiveSpreadsheet().getSheets()`

**Error:** `Exception: You do not have permission to call SpreadsheetApp.getActiveSpreadsheet`
- **Cause:** Script not authorized
- **Fix:** Run script manually once to authorize, or use `ScriptApp.getOAuthToken()` to pre-authorize

### Performance Tips

**1. Batch operations:**
```javascript
// SLOW (N API calls)
for (let i = 0; i < data.length; i++) {
  sheet.getRange(i + 1, 1).setValue(data[i]);
}

// FAST (1 API call)
sheet.getRange(1, 1, data.length, 1).setValues(data.map(d => [d]));
```

**2. Cache frequently accessed data:**
```javascript
const cache = CacheService.getScriptCache();
let config = cache.get('config');

if (!config) {
  config = JSON.stringify(_loadConfig());
  cache.put('config', config, 3600); // 1 hour TTL
}

return JSON.parse(config);
```

**3. Use PropertiesService for persistent data:**
```javascript
const props = PropertiesService.getScriptProperties();
props.setProperty('lastRun', new Date().toISOString());

// Later
const lastRun = props.getProperty('lastRun');
Logger.log('Last run: ' + lastRun);
```

**4. Minimize getRange() calls:**
```javascript
// SLOW (3 API calls)
const a1 = sheet.getRange('A1').getValue();
const b1 = sheet.getRange('B1').getValue();
const c1 = sheet.getRange('C1').getValue();

// FAST (1 API call)
const values = sheet.getRange('A1:C1').getValues()[0];
const [a1, b1, c1] = values;
```

---

## 🧩 Primary Index Files (RAW)
- index.md — Main entry: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/index.md?ts=1764478263  
- INDEX_Checklist_Docs.md — Structured index: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/INDEX_Checklist_Docs.md?ts=1764478263  
- RAW_LINKS_INDEX.md — All raw URLs: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/RAW_LINKS_INDEX.md?ts=1764478263

---

## 🔧 Core Canonical Files (RAW)
- SYSTEM_OVERVIEW.md — Overview: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/SYSTEM_OVERVIEW.md?ts=1764478263
- VERSIONS_INDEX.md — Versions: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/VERSIONS_INDEX.md?ts=1764478263
- Script IDs — stored in the Apps Script project configuration (no `SCRIPT_IDS_INDEX.md` tracked in this repo)

---

## 📁 Documentation (`/docs`)
Κύρια έγγραφα ροών & ρυθμίσεων:
- Functional_Flow_CHECKLIST_V7.md — raw: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/docs/Functional_Flow_CHECKLIST_V7.md?ts=1764478263  
- Flow_Mapping_CHECKLIST_V8.md — raw: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/docs/Flow_Mapping_CHECKLIST_V8.md?ts=1764478263
- GAS_ChecklistV6_Project_Settings.md — raw: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/docs/GAS_ChecklistV6_Project_Settings.md?ts=1764478263  
- Prompt_Current.md — raw: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/docs/Prompt_Current.md?ts=1764478263  
- Ιστορικό συνομιλιών — RAW history index: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/docs/history/RAW_HISTORY_INDEX.md?ts=1764478263

---

## ⚙️ Libraries (`/libraries`)
Core Apps Script libraries (RAW):

| File | RAW URL |
|------|---------|
| AdminToolsLib.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/AdminToolsLib.md?ts=1764478263 |
| CAPABILITY_MAP_AdminToolsLib.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_AdminToolsLib.md?ts=1764478263 |
| CAPABILITY_MAP_HoBMastersLib.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_HoBMastersLib.md?ts=1764478263 |
| CAPABILITY_MAP_MenuLib.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_MenuLib.md?ts=1764478263 |
| CAPABILITY_MAP_PopupLib.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/CAPABILITY_MAP_PopupLib.md?ts=1764478263 |
| HoBMastersLib.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/HoBMastersLib.md?ts=1764478263 |
| MenuLib.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/MenuLib.md?ts=1764478263 |
| PopupLib.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/PopupLib.md?ts=1764478263 |
| README.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/libraries/README.md?ts=1764478263 |
---

## 🧠 Scripts (`/scripts`)
Execution-level Apps Script files (RAW):

| File | RAW URL |
|------|---------|
| Checklist.gs.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/scripts/Checklist.gs.md?ts=1764478263 |
| Blink.gs.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/scripts/Blink.gs.md?ts=1764478263 |
| AutoDupl_File&DeleteTabs.gs.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/scripts/AutoDupl_File&DeleteTabs.gs.md?ts=1764478263 |
| README.md | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/scripts/README.md?ts=1764478263 |

---

## 🧾 Root-Level Files (RAW)
| File | Purpose | Link |
|------|---------|------|
| SYSTEM_OVERVIEW.md | Technical overview of the automation system | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/SYSTEM_OVERVIEW.md?ts=1764478263 |
| robots.txt | Prevents search engine indexing | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/robots.txt?ts=1764478263 |
| .nojekyll | Disables Jekyll on GitHub Pages (raw access) | https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/.nojekyll?ts=1764478263 |

---

## 🧭 KB READ ORDER (MANDATORY - ENHANCED)

### Για ΚΑΘΕ ερώτηση που αφορά κώδικα:

**ΒΗΜΑ 1: Βρες τα αρχεία**
- Άνοιξε INDEX_Checklist_Docs.md
- Βρες τα σχετικά files (scripts, libraries)

**ΒΗΜΑ 2: Διάβασε τα scripts**
- Διάβασε τα σχετικά scripts από /scripts/
- Βρες τα συγκεκριμένα functions που αναφέρονται

**ΒΗΜΑ 3: Διάβασε τις libraries**
- Διάβασε τις σχετικές libraries από /libraries/
- Κατάλαβε τις dependencies

**ΒΗΜΑ 4: Διάβασε τα capability maps (αν χρειάζεται)**
- Για advanced features

**ΒΗΜΑ 5: ΜΟΝΟ ΤΟΤΕ δώσε απάντηση**
- Με αναφορές σε συγκεκριμένες γραμμές κώδικα
- Με πραγματική διάγνωση, όχι υποθέσεις

### Additional Guidelines:
1. Πάντα άνοιγε **RAW** συνδέσμους **με `?ts=`** (cache-buster).  
2. Έλεγξε header έκδοσης (π.χ. `// Version: …`).  
3. Για dependencies: πρώτα **/libraries**, μετά **/scripts**, κατόπιν **/docs**.  
4. Για εκδόσεις/συμφωνία: διάβασε `VERSIONS_INDEX.md` και σύγκρινε με τον πίνακα του `INDEX_Checklist_Docs.md`.
5. **Follow coding standards** (naming, error handling, versioning).
6. **Check dependencies** before making changes (see Dependency Map).
7. **Test in sandbox** before committing.
8. **Update VERSIONS_INDEX.md** after every change.

---

## 🔒 Access Notes
Το repo είναι **public–unlisted**. Το `robots.txt` και `.nojekyll` μειώνουν indexing· η πρόσβαση γίνεται μέσω **RAW** URLs.

---

## ✅ Session Self-Check (FAST)
1) Φόρτωσε **RAW_LINKS_INDEX.md** → απάντησε **RAW_INDEX_OK**.  
2) **NOTES_OK + FirstHeader** για το παρόν αρχείο.  
3) **VERSIONS_TABLE** από `VERSIONS_INDEX.md` + **SYNC: OK/DIFF** με `INDEX_Checklist_Docs.md`.

---

## 📋 VERSION HISTORY

**CHANGELOG.md** — Version history and release notes
- RAW: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/CHANGELOG.md?ts=1764478263
---

## 🧪 VALIDATION & TESTING

**tests/** — Validation scripts for KB quality assurance
- README: https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main/tests/README.md?ts=1764478263
- validate_links.py — Check URL accessibility
- validate_timestamps.py — Verify ?ts= parameters
- validate_structure.py — Verify KB file structure
---

**Maintained by:** ChecklistGPT V5.5.1 (Enhanced by Manus AI)
**Repository:** https://github.com/2mrowman/hob-kb-archives-72A1  
**Last Enhanced:** 22/10/2025 – 09:30 (Europe/Athens)
**Enhancement:** Added MANDATORY FILE READING rules, DEBUGGING WORKFLOW, EXAMPLES, and SELF-VALIDATION

---

© Hall of Brands Automation Initiative | All rights reserved.

---

## 🔐 Script IDs & API Keys

**For security reasons, Script IDs, Library IDs, and API keys are not included in this public repository.**

**To access Script IDs:**
- Internal team members: Contact admin
- Reference document: Available in private storage (Google Drive)

**Last security update:** 25 Oct 2025
