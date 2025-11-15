*Last updated:* 15/11/2025 - 17:53 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 15/11/2025 - 17:53 (DEV-only)
*Build:* c8f9d2d

// HoB - Admin Tools Library
// Version: V6.13.1 – 15.11.2025 – Dynamic FOLDER ID lookup from Checklist_Master_Tables - Added E1 comment reminder  - LockService remindMissingNames added
// ✅ Functions included in this version:
// createNewDay_AUTO (external master copy controlled by caller)
// automatedDuplicateAndCleanup
// showMasterAndDeleteOthers
// remindMissingNames
// clearAllNotes
// debugUserContext
// testLibExists
// testTemplateTab
// testAllPopupsFromAdmin
// ===== ΡΥΘΜΙΣΕΙΣ =====
const HOB_MASTERS_FILE_ID   = '1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI'; // HoB_Masters
const MASTER_SHEET_NAME     = 'MASTER';
const NAME_PROMPT   = 'Όνομα Επώνυμο?';
const COL_B         = 2;        // Στήλη B
const BLINK_CYCLES  = 3;        // Προαιρετικό blinking

// 📌 Δημιουργία νέας ημέρας (όνομα tab: dd/MM) + κρύψιμο MASTER
function createNewDay_AUTO(masterId, templateTab) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const tz = Session.getScriptTimeZone();
  const todayName = Utilities.formatDate(new Date(), tz, 'dd/MM'); // π.χ. 30/09

  const exists = ss.getSheetByName(todayName);
  if (exists) {
    try { ss.toast('Υπάρχει ήδη ημέρα: ' + todayName, 'ℹ️ Πληροφορία', 3); } catch (_) {}
    const masterSheet = ss.getSheetByName(MASTER_SHEET_NAME);
    if (masterSheet && !masterSheet.isSheetHidden()) masterSheet.hideSheet();
    return;
  }

  const masters = SpreadsheetApp.openById(masterId);
  const tpl = masters.getSheetByName(templateTab);
  if (!tpl) {
    try { PopupLib.showCustomPopup('❌ Δεν βρέθηκε template: <b>' + templateTab + '</b>', 'error'); } catch (_) {}
    return;
  }

  const newSheet = tpl.copyTo(ss).setName(todayName);
  ss.setActiveSheet(newSheet);
  ss.moveActiveSheet(0);

  const master = ss.getSheetByName(MASTER_SHEET_NAME);
  if (master && !master.isSheetHidden()) master.hideSheet();

  try { PropertiesService.getDocumentProperties().setProperty('lastTabCreated', new Date().toISOString()); } catch (_) {}
  try { PopupLib.showCustomPopup('✅ Δημιουργήθηκε η νέα ημέρα: <b>' + todayName + '</b>', 'success'); } catch (_) {}
}

/**
 * Κύρια ρουτίνα:
 * 1) Αντιγράφει το ΤΡΕΧΟΝ Spreadsheet στον φάκελο ως YYMM_OriginalName (προηγούμενος μήνας)
 * 2) Αφαιρεί editors στο ΝΕΟ αντίγραφο (εκτός owner)
 * 3) ΣΤΟ ΤΡΕΧΟΝ αρχείο: εμφανίζει MASTER & διαγράφει τα υπόλοιπα tabs
 *
 * @returns {GoogleAppsScript.Drive.File} Το νέο αντίγραφο αρχείου
 */
function automatedDuplicateAndCleanup() {
  try {
    Logger.log('🚀 Έναρξη Duplicate & Cleanup');

    // 🔹 IDs αντλούνται δυναμικά από HoB_Masters → "Checklist_Master_Tables"
    const activeSpreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    const activeName = activeSpreadsheet.getName();

    const masters = SpreadsheetApp.openById(HOB_MASTERS_FILE_ID);
    const masterSheet = masters.getSheetByName('Checklist_Master_Tables') || masters.getSheetByName('Templates');

    if (!masterSheet) {
      throw new Error('Δεν βρέθηκε το φύλλο "Checklist_Master_Tables" ή "Templates" στο HoB_Masters.');
    }

    const data = masterSheet.getDataRange().getValues();
    const headers = data[0].map(h => String(h).trim().toUpperCase());
    const idxName = headers.indexOf('CHECKLIST FILENAME');
    const idxFileId = headers.indexOf('FILE ID');
    const idxFolder = headers.indexOf('FOLDER ID');

    if (idxName === -1 || idxFileId === -1 || idxFolder === -1) {
      throw new Error('Λείπουν στήλες: CHECKLIST FILENAME / FILE ID / FOLDER ID στο master sheet.');
    }

    let folderId = '';
    let originalFileId = '';

    for (let r = 1; r < data.length; r++) {
      if (String(data[r][idxName]).trim() === activeName) {
        originalFileId = String(data[r][idxFileId]).trim();
        folderId = String(data[r][idxFolder]).trim();
        break;
      }
    }

    if (!folderId || !originalFileId) {
      throw new Error('Δεν βρέθηκαν FILE ID / FOLDER ID για "' + activeName + '" στο master sheet.');
    }

    // (1) Πηγαίο αρχείο (ΤΡΕΧΟΝ)
    const originalFile = DriveApp.getFileById(originalFileId);
    const originalName = originalFile.getName().replace(/Copy of |of /gi, '').trim();

    // (2) Υπολογισμός YYMM (προηγούμενος μήνας)
    const today = new Date();
    let yy = today.getFullYear().toString().slice(-2);
    let mm = today.getMonth(); // 0..11
    if (mm === 0) {
      mm = 12;
      yy = (parseInt(yy, 10) - 1).toString();
    }
    const yymm = yy + ('0' + mm).slice(-2);

    // (3) Αντιγραφή στο φάκελο
    const folder = DriveApp.getFolderById(folderId);
    const newFileName = yymm + '_' + originalName;
    const newFile = originalFile.makeCopy(newFileName, folder);
    Logger.log('✅ Αντίγραφο αρχείου: ' + newFileName);

    // (4) Αφαίρεση editors εκτός owner στο ΝΕΟ αντίγραφο
    removeAllUsersExceptOwner_(newFile);

    // (5) ΚΑΘΑΡΙΣΜΟΣ ΣΤΟ ΤΡΕΧΟΝ Spreadsheet
    showMasterAndDeleteOthers();

    try {
      PopupLib.showSuccessMessage('✅ Δημιουργήθηκε αντίγραφο: <b>' + newFileName + '</b><br>📋 Καθαρίστηκε το ΤΡΕΧΟΝ αρχείο (κρατήθηκε μόνο το <b>' + MASTER_SHEET_NAME + '</b>).');
    } catch (_) {}

    Logger.log('✅ Ολοκλήρωση Duplicate & Cleanup');
    return newFile;

  } catch (error) {
    Logger.log('⚠️ Σφάλμα: ' + error.toString());
    try {
      PopupLib.showErrorMessage('⚠️ Σφάλμα στο automatedDuplicateAndCleanup:<br><br>' + error.toString());
    } catch (_) {}
    throw error; // Re-throw για να το δει ο trigger
  }
}

/** Αφαίρεση όλων των editors εκτός owner (Drive File) */
function removeAllUsersExceptOwner_(file) {
  const editors = file.getEditors();
  const owner = file.getOwner();
  if (editors && editors.length > 0) {
    editors.forEach(function(user) {
      if (user.getEmail() !== owner.getEmail()) file.removeEditor(user);
    });
    Logger.log('✅ Αφαιρέθηκαν οι editors εκτός owner για: ' + file.getName());
  } else {
    Logger.log('ℹ️ Δεν βρέθηκαν επιπλέον editors για: ' + file.getName());
  }
}

// ==========================
// 📌 Show MASTER & Delete Others (ΣΤΟ ΤΡΕΧΟΝ αρχείο)
// ==========================
function showMasterAndDeleteOthers() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const masterSheet = ss.getSheetByName(MASTER_SHEET_NAME);
  if (!masterSheet) {
    try { PopupLib.showCustomPopup('❌ Δεν βρέθηκε φύλλο <b>' + MASTER_SHEET_NAME + '</b>.', 'error'); } catch (_) {}
    return;
  }
  masterSheet.showSheet();

  ss.getSheets().forEach(function (sheet) {
    if (sheet.getName() !== MASTER_SHEET_NAME) ss.deleteSheet(sheet);
  });

  try { PopupLib.showCustomPopup('📋 Εμφανίστηκε το <b>' + MASTER_SHEET_NAME + '</b> και διαγράφηκαν τα υπόλοιπα.', 'info'); } catch (_) {}
}

// ==========================
// 📌 Remind Missing Names (τρέχον φύλλο)
// ==========================
// Helper — returns Ui or null (prevents exceptions in headless triggers)
function _safeUi_() {
  try { return SpreadsheetApp.getUi(); } catch (e) { return null; }
}

/**
 * Checks for missing names ("Όνομα Επώνυμο?") in column B.
 *
 * Behavior:
 * - UI context (menu call): Shows popup dialog
 * - Headless context (time-driven trigger): Updates B1 cell with notification
 *
 * @returns {void}
 */
function remindMissingNames() {
  const ui = _safeUi_();
  const isHeadless = !ui;

  const NOTIFICATION_CELL = 'B1';
  const ORIGINAL_B1_TEXT = 'Η ΕΡΓΑΣΙΑ ΕΓΙΝΕ ΑΠΟ\n(Όσοι συμμετείχαν)';

  // ==== ΝΕΕΣ ΣΤΑΘΕΡΕΣ ΓΙΑ ΤΟ Ε1 (ίδιο μοτίβο με Β1) ====
  const NOTIFICATION_CELL_COMMENTS = 'E1';
  const ORIGINAL_E1_TEXT = 'ΣΧΟΛΙΟ/ΑΙΤΙΑ';
  const COMMENT_PLACEHOLDER = 'Γράψτε το σχόλιο σας εδώ';
  const COL_C = 3; // Κατάσταση Εργασίας
  const COL_E = 5; // Σχόλιο/Αιτία

  // [RELIABILITY] Αποτροπή ταυτόχρονων εκτελέσεων & προσωρινών σφαλμάτων storage
  const lock = LockService.getScriptLock();
  let haveLock = false;
  try {
    try { haveLock = lock.tryLock(30000); } catch (_) {}

    function _safeGetValues_(range) {
      for (let i = 0; i < 3; i++) {
        try { return range.getValues(); }
        catch (err) {
          if (String(err).indexOf('FAILED_PRECONDITION') !== -1) { Utilities.sleep(500 * (i + 1)); continue; }
          throw err;
        }
      }
      return range.getValues();
    }
    function _safeGetBackground_(range) {
      for (let i = 0; i < 3; i++) {
        try { return range.getBackground(); }
        catch (err) {
          if (String(err).indexOf('FAILED_PRECONDITION') !== -1) { Utilities.sleep(500 * (i + 1)); continue; }
          throw err;
        }
      }
      return range.getBackground();
    }

    const sh = SpreadsheetApp.getActiveSheet();
    const name = sh.getName();

    // Skip START and MASTER sheets
    if (["START", "MASTER"].includes(name)) {
      if (isHeadless) {
        console.log("remindMissingNames: Skipped (START/MASTER sheet)");
      }
      return;
    }

    const last = sh.getLastRow();
    if (last < 2) {
      if (isHeadless) {
        console.log("remindMissingNames: Skipped (no data rows)");
      }
      return;
    }

    // Find all cells with NAME_PROMPT in column B
    const rngB = sh.getRange(2, COL_B, last - 1, 1);
    const vals = _safeGetValues_(rngB);
    const targets = [];

    for (let i = 0; i < vals.length; i++) {
      const val = String(vals[i][0] || "").trim();
      if (val === NAME_PROMPT) {
        targets.push(rngB.getCell(i + 1, 1));
      }
    }

    const b1Cell = sh.getRange(NOTIFICATION_CELL);

    // Case 1: Missing names found
    if (targets.length > 0) {
      const cellRefs = targets.map(c => c.getA1Notation()).join(', ');
      const message =
        '🚨 Εντοπίστηκαν ' + targets.length +
        ' κελιά με ασυμπλήρωτο το "' + NAME_PROMPT + '" !!!\n' +
        '📍 Κελιά: ' + cellRefs + '\n' +
        '📝 Παρακαλώ συμπληρώστε το ονοματεπώνυμό σας στα κελιά αυτά στη στήλη B.';

      if (isHeadless) {
        // Headless context: Update B1 cell with notification
        try {
          b1Cell.setValue(targets.length + '- ΟΝΟΜΑΤΑ ΛΕΙΠΟΥΝ!\n(' + cellRefs + ')').setWrap(true);
          b1Cell.setBackground('#ff0000');  // Original gray background (adjust if needed)
          b1Cell.setFontColor('#ffffff');   // Black text
          b1Cell.setFontWeight('bold');
          b1Cell.setHorizontalAlignment('center');
          SpreadsheetApp.flush();
          console.log("remindMissingNames: B1 notification updated (" + targets.length + " missing names)");
        } catch (e) {
          console.error("remindMissingNames: Failed to update B1 notification:", e);
        }
      } else {
        // UI context: Show popup dialog
        try {
          PopupLib.showCustomPopup(message, 'error');
          Utilities.sleep(500);
          console.log("remindMissingNames: Popup shown (" + targets.length + " missing names)");
        } catch (e) {
          console.error("remindMissingNames: Popup failed (suppressed):", e);
        }
      }
    }
    // Case 2: No missing names - restore B1 to original
    else {
      if (isHeadless) {
        try {
          // Check if B1 currently has notification (red background)
          const currentBg = _safeGetBackground_(b1Cell);
          if (currentBg === '#ff0000' || currentBg === '#FF0000') {
            // Restore original B1 text and style
            b1Cell.setValue(ORIGINAL_B1_TEXT);
            b1Cell.setBackground('#d9d9d9');  // Original gray background (adjust if needed)
            b1Cell.setFontColor('#000000');   // Black text
            b1Cell.setFontWeight('bold');
            b1Cell.setHorizontalAlignment('center');
            SpreadsheetApp.flush();
            console.log("remindMissingNames: B1 notification cleared (all names filled)");
          } else {
            console.log("remindMissingNames: No missing names, B1 already normal");
          }
        } catch (e) {
          console.error("remindMissingNames: Failed to restore B1:", e);
        }
      } else {
        // UI context: No popup needed
        console.log("remindMissingNames: No missing names found");
      }
    }

    // ====== ΝΕΟ BLOCK: Έλεγχος & υπόμνηση για ΣΧΟΛΙΑ στο E1 (ίδιο μοτίβο) ======

    // Find rows where column C requires comment (contains "σχόλιο") and column E is empty or has placeholder
    const rngC = sh.getRange(2, COL_C, last - 1, 1);
    const rngE = sh.getRange(2, COL_E, last - 1, 1);
    const valsC = _safeGetValues_(rngC);
    const valsE = _safeGetValues_(rngE);
    const commentTargets = [];

    for (let i = 0; i < valsC.length; i++) {
      const cVal = String(valsC[i][0] || "").toLowerCase();
      if (cVal.indexOf("σχόλιο") !== -1) {
        const eVal = String(valsE[i][0] || "").trim();
        if (eVal === "" || eVal === COMMENT_PLACEHOLDER) {
          commentTargets.push(rngE.getCell(i + 1, 1)); // store E-cell for reporting
        }
      }
    }

    const e1Cell = sh.getRange(NOTIFICATION_CELL_COMMENTS);

    // Case 1 (E1): Missing comments found
    if (commentTargets.length > 0) {
      const eRefs = commentTargets.map(c => c.getA1Notation()).join(', ');
      const messageComments =
        '🚨 Εντοπίστηκαν ' + commentTargets.length +
        ' κελιά χωρίς συμπληρωμένο σχόλιο.\n' +
        '📍 Κελιά: ' + eRefs + '\n' +
        '📝 Παρακαλώ συμπληρώστε τα σχόλιά σας στη στήλη Ε.';

      if (isHeadless) {
        // Headless context: Update E1 cell with notification
        try {
          e1Cell.setValue('ΣΥΜΠΛΗΡΩΣΤΕ ΤΑ ΣΧΟΛΙΑ ΣΑΣ!\n(' + eRefs + ')').setWrap(true);
          e1Cell.setBackground('#ff0000');  // Original gray background (adjust if needed)
          e1Cell.setFontColor('#ffffff');   // Black text
          e1Cell.setFontWeight('bold');
          e1Cell.setHorizontalAlignment('center');
          SpreadsheetApp.flush();
          console.log("remindMissingNames: E1 notification updated (" + commentTargets.length + " missing comments)");
        } catch (e) {
          console.error("remindMissingNames: Failed to update E1 notification:", e);
        }
      } else {
        // UI context: Show popup dialog
        try {
          PopupLib.showCustomPopup(messageComments, 'warning');
          Utilities.sleep(500);
          console.log("remindMissingNames: Popup shown for comments (" + commentTargets.length + ")");
        } catch (e) {
          console.error("remindMissingNames: Popup for comments failed (suppressed):", e);
        }
      }
    }
    // Case 2 (E1): No missing comments - restore E1 to original
    else {
      if (isHeadless) {
        try {
          // Check if E1 currently has notification (red background)
          const currentBgE = _safeGetBackground_(e1Cell);
          if (currentBgE === '#ff0000' || currentBgE === '#FF0000') {
            // Restore original E1 text and style
            e1Cell.setValue(ORIGINAL_E1_TEXT);
            e1Cell.setBackground('#d9d9d9');  // Original gray background (adjust if needed)
            e1Cell.setFontColor('#000000');   // Black text
            e1Cell.setFontWeight('bold');
            e1Cell.setHorizontalAlignment('center');
            SpreadsheetApp.flush();
            console.log("remindMissingNames: E1 notification cleared (all comments OK)");
          } else {
            console.log("remindMissingNames: No missing comments, E1 already normal");
          }
        } catch (e) {
          console.error("remindMissingNames: Failed to restore E1:", e);
        }
      } else {
        // UI context: No popup needed
        console.log("remindMissingNames: No missing comments found");
      }
    }
  } finally {
    if (haveLock) { try { lock.releaseLock(); } catch (_) {} }
  }
}

// ==========================
// 📌 Clear All Notes (όλα τα tabs εκτός START/MASTER)
// ==========================
function clearAllNotes() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  ss.getSheets().forEach(function (sheet) {
    const nm = sheet.getName();
    if (nm === 'START' || nm === MASTER_SHEET_NAME) return;
    sheet.getDataRange().clearNote();
  });
  try { PopupLib.showCustomPopup('🧽 Καθαρίστηκαν όλα τα Notes.', 'success'); } catch (_) {}
}

// ==========================
// 📌 Debug Context
// ==========================
function debugUserContext() {
  const email = Session.getEffectiveUser().getEmail();
  const docTitle = SpreadsheetApp.getActiveSpreadsheet().getName();
  const msg = '👤 Χρήστης: <b>' + email + '</b><br>' +
              '📄 Αρχείο: <b>' + docTitle + '</b><br>' +
              '🕒 Ώρα: <b>' + new Date().toLocaleString() + '</b>';
  try { PopupLib.showCustomPopup(msg, 'info'); } catch (_) {}
}

// ==========================
// ✅ Tests
// ==========================
function testLibExists() { return true; }

function testTemplateTab() {
  const masters = SpreadsheetApp.openById(HOB_MASTERS_FILE_ID);
  const tplSheet = masters.getSheetByName('Templates');
  if (!tplSheet) throw new Error('Δεν βρέθηκε φύλλο Templates στο HoB_Masters');
  return true;
}

function testAllPopupsFromAdmin() {
  try {
    PopupLib.showErrorMessage('🚨 Test Error από AdminToolsLib');   Utilities.sleep(300);
    PopupLib.showInfoMessage('ℹ️ Test Info από AdminToolsLib');     Utilities.sleep(300);
    PopupLib.showSuccessMessage('✅ Test Success από AdminToolsLib'); Utilities.sleep(300);
    PopupLib.showWarningMessage('⚠️ Test Warning από AdminToolsLib');
  } catch (err) {
    Logger.log('Σφάλμα στο testAllPopupsFromAdmin: ' + err);
  }
}

