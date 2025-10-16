// Version: V7.1.1R – 16/10/2025 – Classic Stable Revert (based on V7.1.0)
// Summary:
// – Επιστροφή 1:1 στη σταθερή λογική του V7.1.0 (όπως δούλευε χθες).
// – Απλό, ελαφρύ onOpen + δυναμικό μενού που φορτώνει όταν το πατήσεις.
// – Σταθερό HoB_Masters ID + ανάγνωση Templates με safe catch (ΧΩΡΙΣ permission stacktrace).
// – Διατηρείται το onEdit (Retail Stable Build V7.0.2).
//
// ✅ Function checklist
// ✅ onOpen
// ✅ createNewDay_AUTO_Local
// ✅ getTemplateTabFromHoBMasters_
// ✅ loadMenuDynamically
// ✅ onEdit
// ✅ TIMESTAMP
// ✅ testLibExists / testTemplateTab / testHoBMastersLib / testLibLink / showTestPopup
// ✅ installAllTriggers_   ← helper για εύκολη εγκατάσταση triggers

// ==========================
// HoB – CONFIG
// ==========================
const HOB_MASTERS_FILE_ID = '1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI'; // (from V7.1.0)

// ==========================
// onOpen – (run as INSTALLED trigger)
// ==========================
function onOpen(e) {
  const ui = SpreadsheetApp.getUi();
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  // Προσωρινό μενού για αίσθηση φόρτωσης
  ui.createMenu('🗂️ HoB - Menu')
    .addItem('⏳ Φόρτωση Μενού...', 'loadMenuDynamically')
    .addToUi();

  try {
    const todayName = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'dd/MM');
    const exists = ss.getSheetByName(todayName);

    // Αν δεν υπάρχει σημερινό φύλλο → το δημιουργούμε μέσω τοπικού wrapper
    if (!exists) {
      createNewDay_AUTO_Local(); // (όπως στο V7.1.0)
    }

    // Κρύψε MASTER μόνο αν υπάρχει άλλο ορατό tab
    const master = ss.getSheetByName('MASTER');
    const visibleSheets = ss.getSheets().filter(sh => sh.getName() !== 'MASTER');
    if (master && visibleSheets.length > 0 && !master.isSheetHidden()) {
      master.hideSheet();
    }
  } catch (err) {
    // Σιωπηλή καταγραφή – δεν “βομβαρδίζουμε” τον χρήστη με stacktrace
    Logger.log('❌ onOpen error (V7.1.0R): ' + err);
  }
}

// Ανάγνωση template από HoB_Masters/“Templates” (safe catch όπως στο V7.1.0)
// ✅ Ανάγνωση template από HoB_Masters (διορθωμένη για full column scan A–C)
// ==========================
function getTemplateTabFromHoBMasters() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const fileName = ss.getName().trim();

  try {
    const masters = SpreadsheetApp.openById(HOB_MASTERS_FILE_ID);
    const tplSheet = masters.getSheetByName('Templates');
    if (!tplSheet) {
      Logger.log('⚠️ Δεν βρέθηκε φύλλο "Templates" στο HoB_Masters');
      return null;
    }

    // 🔹 Διαβάζει όλες τις στήλες (A–C ή περισσότερες)
    const lastRow = tplSheet.getLastRow();
    const lastCol = tplSheet.getLastColumn();
    const data = tplSheet.getRange(2, 1, lastRow - 1, lastCol).getValues();

    // 🔹 Ελέγχει γραμμή–γραμμή
    for (let i = 0; i < data.length; i++) {
      const chkName = String(data[i][0]).trim(); // CHECKLIST FILENAME
      const tplName = String(data[i][1]).trim(); // TEMPLATE
      if (chkName && chkName === fileName) {
        Logger.log(`✅ Template found for "${fileName}": ${tplName}`);
        return tplName;
      }
    }

    Logger.log(`⚠️ Δεν βρέθηκε template για "${fileName}" στο HoB_Masters`);
    return null;

  } catch (err) {
    // 🔹 Αν αποτύχει openById (π.χ. απλό trigger χωρίς άδεια)
    Logger.log('⚠️ getTemplateTabFromHoBMasters_: openById failed: ' + err);
    return null;
  }
}

// Δημιουργία νέας ημέρας (τοπικός wrapper όπως στο V7.1.0)
// ==========================
function createNewDay_AUTO_Local() {
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const todayName = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'dd/MM');
    const existingSheet = ss.getSheetByName(todayName);

    // Μικρή καθυστέρηση για να προλάβει να “σταθεί” το UI
    Utilities.sleep(1500);

    if (existingSheet) {
      try { PopupLib.showInfoMessage('ℹ️ Υπάρχει ήδη ημέρα: <b>' + todayName + '</b>'); } catch (_) {}
      return;
    }

    try { PopupLib.showInfoMessage('⏳ Δημιουργία νέας ημέρας σε εξέλιξη…'); } catch (_) {}

    const templateTab = getTemplateTabFromHoBMasters_(); // μπορεί να επιστρέψει null (ασφαλές)
    if (templateTab) {
      AdminToolsLib.createNewDay_AUTO(HOB_MASTERS_FILE_ID, templateTab);
    } else {
      try { PopupLib.showErrorMessage('❌ Δεν βρέθηκε template στο HoB_Masters.'); } catch (_) {}
    }
  } catch (err) {
    Logger.log('⚠️ createNewDay_AUTO_Local error: ' + err);
  }
}

// Trigger Setup (όπως στο V7.1.0 – + reminder κάθε 30’ αν θέλεις)
// ==========================
function installAllTriggers() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const triggers = ScriptApp.getProjectTriggers();
  const log = (msg) => console.log('⚙️ [Triggers] ' + msg);

  // onOpen (From spreadsheet – On open)
  const hasOnOpen = triggers.some(t =>
    t.getHandlerFunction() === 'onOpen' &&
    t.getEventType() === ScriptApp.EventType.ON_OPEN
  );
  if (!hasOnOpen) {
    ScriptApp.newTrigger('onOpen').forSpreadsheet(ss).onOpen().create();
    log('✅ Εγκαταστάθηκε trigger για onOpen');
  } else {
    log('ℹ️ Υπάρχει ήδη trigger για onOpen');
  }

  // remindMissingNames (κάθε 30')
  const hasReminder = triggers.some(t =>
    t.getHandlerFunction() === 'remindMissingNames' &&
    t.getEventType() === ScriptApp.EventType.CLOCK
  );
  if (!hasReminder) {
    ScriptApp.newTrigger('remindMissingNames').timeBased().everyMinutes(30).create();
    log('✅ Εγκαταστάθηκε trigger για remindMissingNames (κάθε 30’)');
  } else {
    log('ℹ️ Υπάρχει ήδη trigger για remindMissingNames');
  }

  try { PopupLib.showSuccessMessage('✅ Οι triggers εγκαταστάθηκαν επιτυχώς!'); } catch (_) {}
}

// ==========================
// Δυναμικό μενού (όπως στο V7.1.0 – μέσω MenuLib μόνο)
// ==========================
function loadMenuDynamically() {
  const userEmail = Session.getEffectiveUser().getEmail();
  const ownerEmail = MenuLib.getOwnerEmail();                // η MenuLib ξέρει τον owner
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const ui = SpreadsheetApp.getUi();
  const menu = ui.createMenu('🗂️ HoB - Menu');

  // User items από φύλλο ρυθμίσεων (MenuLib)
  const userItems = MenuLib.getMenuItemsFromSheet('user');
  userItems.forEach(i => menu.addItem(i.name, 'MenuLib.' + i.func)); // καλεί ΑΠΕΥΘΕΙΑΣ MenuLib

  // Owner-only, ΜΟΝΟ όταν ο ενεργός χρήστης είναι και owner του αρχείου
  if (userEmail === ownerEmail && ss.getOwner().getEmail() === userEmail) {
    const ownerItems = MenuLib.getMenuItemsFromSheet('owner');
    if (ownerItems.length > 0) {
      const ownerSub = ui.createMenu('🛠️ Εργαλεία Ιδιοκτήτη');
      ownerItems.forEach(i => ownerSub.addItem(i.name, 'MenuLib.' + i.func)); // επίσης μέσω MenuLib
      menu.addSeparator().addSubMenu(ownerSub);
    }
  }

  menu.addToUi();
}

// ==========================
// onEdit – Retail Stable Build V7.0.2 (όπως πριν)
// ==========================
function onEdit(e) {
  try {
    const sheet = e.range.getSheet();
    const sheetName = sheet.getName();
    const col = e.range.getColumn();
    const row = e.range.getRow();
    const val = e.range.getValue();
    const timestampFormat = 'HH:mm:ss.000" - "dd/MM';
    if (['START', 'MASTER'].includes(sheetName)) return;

    const colB = 2, colC = 3, colD = 4;

    if (col === colC) {
      const rangeB = sheet.getRange(row, colB);
      const rangeD = sheet.getRange(row, colD);

      if (val === '' || val === null) {
        rangeB.clearContent();
        rangeD.clearContent();
        return;
      }
      if (!rangeB.getValue()) {
        rangeB.setValue('Όνομα Επώνυμο?').setFontColor('#d32f2f').setFontWeight('bold');
      }
      rangeD.setNumberFormat(timestampFormat).setValue(new Date());
      SpreadsheetApp.flush();
    }

    if (col === colB && val && val !== 'Όνομα Επώνυμο?') {
      e.range.setFontColor(null).setFontWeight(null).setBackground(null);
    }
  } catch (error) {
    console.error('❌ Σφάλμα στο onEdit:', error);
  }
}

// ==========================
// Helpers για δοκιμές (ίδια με V7.1.0)
// ==========================
function TIMESTAMP() {
  return Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'HH:mm:ss.000" - "dd/MM');
}
function testLibExists() {
  try {
    const has = typeof AdminToolsLib.createNewDay_AUTO;
    SpreadsheetApp.getUi().alert('type of createNewDay_AUTO: ' + has);
  } catch (e) {
    SpreadsheetApp.getUi().alert('ERROR: ' + e.toString());
  }
}
function testTemplateTab() {
  const ss = SpreadsheetApp.openById(HOB_MASTERS_FILE_ID);
  const sheet = ss.getSheetByName('WRHMaster');
  SpreadsheetApp.getUi().alert(sheet ? '✅ Exists!' : '❌ Not found');
}
function testHoBMastersLib() {
  const result = HoBMastersLib.createNewDay({
    masterId: HOB_MASTERS_FILE_ID,
    templateTab: 'MASTER1',
    showAlerts: true
  });
  Logger.log(result);
}
function testLibLink() { Logger.log(typeof HoBMastersLib.createNewDay); }
function showTestPopup() { PopupLib.showInfoMessage('✅ Test popup λειτουργεί σωστά!'); }
