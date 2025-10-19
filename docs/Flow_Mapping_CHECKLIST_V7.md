*Last updated:* 19/10/2025 – 14:13 (Europe/Athens)

*Last synced with VERSIONS_INDEX.md:* 19/10/2025 – 14:13 (DEV-only)

*Build:* 5d57b05



*



*



*



*

*
*
*
*
*
*
*
*Last updated: 19/10/2025 – 12:43 (Europe/Athens)*
# 📘 **Flow Mapping – CHECKLIST V7.1.0R (Popup Restoration Build)**
*

## 🧩 Overview
Το παρόν αρχείο περιγράφει τη ροή λειτουργίας (flow mapping) του CHECKLIST συστήματος (έκδοση V7.1.0R), συμπεριλαμβανομένων όλων των triggers, scripts και βιβλιοθηκών που συνεργάζονται μέσω του Google Apps Script.  
Είναι το τεχνικό reference document για developers και maintainers του project.

---

## ⚙️ System Architecture Summary

| Επίπεδο | Περιγραφή | Αρχεία |
|----------|------------|--------|
| **Main Project** | Scripts που ανήκουν στο CHECKLIST αρχείο και τρέχουν triggers, onOpen, onEdit, duplication | `Checklist.gs`, `Blink.gs`, `AutoDupl_File&DeleteTabs.gs` |
| **Libraries** | Βιβλιοθήκες GAS που παρέχουν λειτουργίες σε όλα τα stores | `AdminToolsLib`, `PopupLib`, `MenuLib`, `HoBMastersLib` |
| **Master File** | Κεντρικό αρχείο με templates (Master Tabs) | `HoB_Masters` (`File ID: 1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI`) |

---

## 🧱 1. Main Scripts

### 🗂️ `Checklist.gs`
Κεντρικό entry point του project. Χειρίζεται τα triggers και καλεί τις βασικές βιβλιοθήκες.

**Καλεί:**
- `MenuLib.loadMenuDynamically()`
- `AdminToolsLib.createNewDay_AUTO()`
- `PopupLib.showCustomPopup()`
- `HoBMastersLib.getTemplateTabFromHoBMasters_()`

### 🗂️ `Blink.gs`
Ειδική ρουτίνα για feedback στο χρήστη (placeholder “Όνομα Επώνυμο?”).  
Καλεί popup μέσω `PopupLib.showCustomPopup()` και προαιρετικά `blinkCellFontColor_()`.

### 🗂️ `AutoDupl_File&DeleteTabs.gs`
Διαχειρίζεται την αυτόματη αντιγραφή και εκκαθάριση φύλλων.  
Καλεί:
- `AdminToolsLib.automatedDuplicateAndCleanup()`
- `AdminToolsLib.showMasterAndDeleteOthers()`

---

## 🧩 2. Libraries Interconnection

| Library | Ρόλος | Καλείται από | Περιγραφή |
|----------|--------|---------------|------------|
| **AdminToolsLib (V6.7.6)** | Κεντρικό εργαλείο ενεργειών (createNewDay, clearAllNotes, cleanup) | `Checklist.gs`, `AutoDupl_File&DeleteTabs.gs` | Εκτελεί τις λειτουργίες του ιδιοκτήτη (owner-level actions). |
| **PopupLib (V2.0.0)** | Εμφάνιση UI Popups (modal / native / toast) | Όλες | Προσαρμόζεται στο περιβάλλον: αν υπάρχει UI → modal, αλλιώς alert ή toast. |
| **MenuLib (V7.0.0)** | Φόρτωση δυναμικού μενού από το “MenuSettings” sheet | `Checklist.gs` | Δημιουργεί user/owner μενού δυναμικά. |
| **HoBMastersLib (V1.3)** | Πρόσβαση στα MASTER tabs από το κεντρικό αρχείο | `AdminToolsLib`, `Checklist.gs` | Χρησιμοποιείται στη δημιουργία νέας ημέρας (`createNewDay_AUTO`). |

---

## 🧭 3. Functional Flow (Scripts → Libraries)

Η συνολική ροή λειτουργίας:

```
onOpen() → loadMenuDynamically() → MenuLib.getMenuItemsFromSheet()
           ↳ createNewDay_AUTO() → AdminToolsLib
               ↳ HoBMastersLib → duplicate Master tab
               ↳ PopupLib → showCustomPopup()
```

Όλες οι UI ενέργειες (όπως reminders, notes clearing, duplication)  
περνούν μέσω `AdminToolsLib` → που με τη σειρά του καλεί `PopupLib` για ενημέρωση χρήστη.

---

## 🔁 4. Trigger Flow Logic

### 📂 onOpen Trigger
- Εκκινεί τη δημιουργία προσωρινού μενού
- Ελέγχει αν υπάρχει νέα ημέρα (`createNewDay_AUTO_Local`)
- Καλεί `MenuLib` για φόρτωση δυναμικού μενού
- Εμφανίζει popup μέσω `PopupLib`

### 📂 onEdit Trigger
- Αν στη στήλη Β υπάρχει “Όνομα Επώνυμο?” → καλεί `AdminToolsLib.remindMissingNames()`
- Αν είναι drop-down → κάνει validation (MASTER rules)
- Αν είναι checkbox → γράφει timestamp
- Αν είναι σχόλιο → εμφανίζει popup

### 📂 Time-based Trigger
- Τρέχει `remindMissingNames()` κάθε 20–30 λεπτά
- Αν δεν υπάρχει UI context → τερματίζει

---

## 📊 5. Visual Mapping

| Διάγραμμα | Αρχείο | Περιγραφή |
|------------|---------|------------|
| **Core Script Structure** | `flow_core_script_structure.png` | Δείχνει τη ροή του `Checklist.gs`, τα triggers και τις connected libraries |
| **Trigger Flow (onOpen / onEdit / Time)** | `flow_onOpen_onEdit_triggers.png` | Δείχνει τη συμπεριφορά των triggers και τις κλήσεις PopupLib / AdminToolsLib |
| **Inter-library Dependencies** | `flow_interlibrary_dependencies.png` | Εμφανίζει τις σχέσεις μεταξύ scripts & βιβλιοθηκών |

**Ενδεικτική Εμφάνιση (GitHub):**
```markdown
![Core Script Structure](Docs/Images/flow_core_script_structure.png)
![Trigger Flow](Docs/Images/flow_onOpen_onEdit_triggers.png)
![Library Interconnection](Docs/Images/flow_interlibrary_dependencies.png)
```

---

## 🧠 6. Example Call Hierarchies

### ✅ Example 1 – New Day Creation
```
onOpen(e)
 → AdminToolsLib.createNewDay_AUTO()
   → HoBMastersLib.getTemplateTabFromHoBMasters_()
   → PopupLib.showCustomPopup("Ημέρα δημιουργήθηκε επιτυχώς")
```

### ✅ Example 2 – Missing Name Reminder
```
onEdit(e)
 → AdminToolsLib.remindMissingNames()
   → PopupLib.showCustomPopup("Προσθήκη ονόματος απαιτείται")
   → Blink.gs → blinkCellFontColor_()
```

### ✅ Example 3 – Auto Cleanup
```
AutoDupl_File&DeleteTabs.gs
 → AdminToolsLib.automatedDuplicateAndCleanup()
   → PopupLib.showCustomPopup("Εκκαθάριση ολοκληρώθηκε")
```

---
![Dependency Map](https://2mrowman.github.io/hob-kb-archives-72A1/docs/Images/DEPENDENCY_MAP.png)

## 🧾 7. Dependencies Map (textual)

| Από | Προς | Σχέση |
|------|------|--------|
| `Checklist.gs` | `MenuLib`, `AdminToolsLib`, `PopupLib`, `HoBMastersLib` | Άμεση εξάρτηση |
| `AdminToolsLib` | `PopupLib`, `HoBMastersLib` | Έμμεση εξάρτηση |
| `PopupLib` | (καμία) | UI layer μόνο |
| `HoBMastersLib` | `PopupLib` | Εμφάνιση feedback |
| `Blink.gs` | `PopupLib` | Feedback μηνύματα χρήστη |
| `AutoDupl_File&DeleteTabs.gs` | `AdminToolsLib` | Διαχείριση φύλλων |

---

## 📘 8. Version Reference

| Module | Version | Date | Notes |
|---------|----------|------|-------|
| **Checklist.gs** | V7.1.0R | 09-Oct-2025 | Popup Restoration Build |
| **PopupLib** | V2.0.0 | 07-Oct-2025 | Modal + native fallback |
| **AdminToolsLib** | V6.7.6 | 25-Sep-2025 | Stable automation build |
| **MenuLib** | V7.0.0 | 25-Sep-2025 | Dynamic menu builder |
| **HoBMastersLib** | V1.3 | 25-Sep-2025 | Template duplication handler |

---

© Hall of Brands – CHECKLIST Automation Documentation  
Author: **DEK – BD-PM Διευθυντής Ανάπτυξης & Έργου**  
Email: `dek@beyondlimits.events`  
Date: 13/10/2025
