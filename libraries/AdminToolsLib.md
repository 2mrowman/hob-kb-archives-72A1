*Build: 95c45a5*
*Last updated: 18/10/2025 – 11:41 (Europe/Athens)*
// ==========================
// HoB - Admin Tools Library
// Version: V6.8.0 – 17.10.2025 – Added Universal Version Updater (updateVersionInfo_Universal)
// Version: V6.7.6 – 30.09.2025 – Bugfixes (Drive addFile FileRef, wrappers) – no logic changes
// ==========================
//
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
//
// Notes:
// • Διατηρείται ο αρχικός υπολογισμός YYMM = προηγούμενος μήνας.
// • Δεν αλλάζει η ροή, μόνο διόρθωση τύπων προς Drive (File vs Spreadsheet)
// • Τα ονόματα/wrappers μένουν ως έχουν για συμβατότητα με MenuLib.

/// ===== ΡΥΘΜΙΣΕΙΣ =====
const HOB_MASTERS_FILE_ID   = '1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI'; // HoB_Masters
const DESTINATION_FOLDER_ID = '1ryekzwj3owrxXSjt7ty0veKniq9TQq2K';             // Φάκελος προορισμού για μηνιαία αντίγραφα
const MASTER_SHEET_NAME     = 'MASTER';

const NAME_PROMPT   = 'Όνομα Επώνυμο?';
const COL_B         = 2;        // Στήλη B
const BLINK_CYCLES  = 3;        // Προαιρετικό blinking

// ==========================
// 📌 Δημιουργία νέας ημέρας (όνομα tab: dd/MM) + κρύψιμο MASTER
// ==========================
function createNewDay_AUTO(masterId, templateTab) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const tz = Session.getScriptTimeZone();
  const todayName = Utilities.formatDate(new Date(), tz, 'dd/MM'); // π.χ. 30/09

  const exists = ss.getSheetByName(todayName);
  if (exists) {
    try { PopupLib.showCustomPopup('ℹ️ Υπάρχει ήδη ημέρα: <b>' + todayName + '</b>', 'info'); } catch (_) {}
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

// ==========================
// 📌 FILE-LEVEL Duplicate & Cleanup (ΑΝΤΙΓΡΑΦΟ στο φάκελο + ΚΑΘΑΡΙΣΜΟΣ στο ΤΡΕΧΟΝ αρχείο)
// ==========================

/** Wrapper για Owner Menu (μην αλλάξεις όνομα) */
function automatedDuplicateAndCleanupFromMenu() {
  try {
    automatedDuplicateAndCleanup();
  } catch (err) {
    try {
      PopupLib.showErrorMessage('⚠️ Σφάλμα (Duplicate & Cleanup):<br><br><code>' + String(err) + '</code>');
    } catch (_) {
      SpreadsheetApp.getUi().alert('Σφάλμα (Duplicate & Cleanup): ' + String(err));
    }
    throw err;
  }
}

/**
 * Κύρια ρουτίνα:
 * 1) Αντιγράφει το ΤΡΕΧΟΝ Spreadsheet στον φάκελο ως YYMM_OriginalName (προηγούμενος μήνας)
 * 2) Αφαιρεί editors στο ΝΕΟ αντίγραφο (εκτός owner)
 * 3) ΣΤΟ ΤΡΕΧΟΝ αρχείο: εμφανίζει MASTER & διαγράφει τα υπόλοιπα tabs
 */
function automatedDuplicateAndCleanup() {
  Logger.log('🚀 Έναρξη Duplicate & Cleanup');

  // (1) Πηγαίο αρχείο (ΤΡΕΧΟΝ)
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const originalFileId = ss.getId();
  const originalFile   = DriveApp.getFileById(originalFileId);
  let originalName     = originalFile.getName().replace(/Copy of |of /gi, '').trim();

  // (2) Υπολογισμός YYMM (προηγούμενος μήνας) — ΔΕΝ αλλάζει
  const today = new Date();
  let yy = today.getFullYear().toString().slice(-2);
  let mm = today.getMonth(); // 0..11
  if (mm === 0) { mm = 12; yy = (parseInt(yy, 10) - 1).toString(); }
  const yymm = yy + ('0' + mm).slice(-2);

  // (3) Αντιγραφή στο φάκελο (Drive File API)
  const folder = DriveApp.getFolderById(DESTINATION_FOLDER_ID);
  const newFileName = yymm + '_' + originalName;
  const newFile = originalFile.makeCopy(newFileName, folder);
  Logger.log('✅ Αντίγραφο αρχείου: ' + newFileName);

  // (4) Αφαίρεση editors εκτός owner στο ΝΕΟ αντίγραφο
  removeAllUsersExceptOwner_(newFile);

  // (5) ΚΑΘΑΡΙΣΜΟΣ ΣΤΟ ΤΡΕΧΟΝ Spreadsheet
  showMasterAndDeleteOthers();

  try {
    PopupLib.showSuccessMessage(
      '✅ Δημιουργήθηκε αντίγραφο: <b>' + newFileName + '</b><br>📋 Καθαρίστηκε το ΤΡΕΧΟΝ αρχείο (κρατήθηκε μόνο το <b>' + MASTER_SHEET_NAME + '</b>).'
    );
  } catch (_) {}

  Logger.log('✅ Ολοκλήρωση Duplicate & Cleanup (copy→remove editors στο νέο, cleanup στο τρέχον).');
  return newFile;
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
function remindMissingNames() {
  try { SpreadsheetApp.getUi(); } catch (e) { return; }

  const sh = SpreadsheetApp.getActiveSheet();
  const name = sh.getName();
  if (name === 'START' || name === MASTER_SHEET_NAME) return;

  const last = sh.getLastRow();
  if (last < 2) return;

  const rngB = sh.getRange(2, COL_B, last - 1, 1);
  const vals = rngB.getValues();
  const targets = [];

  for (let i = 0; i < vals.length; i++) {
    const v = String(vals[i][0] || '').trim();
    if (v === NAME_PROMPT) targets.push(rngB.getCell(i + 1, 1));
  }

  if (targets.length > 0) {
    const cellRefs = targets.map(c => c.getA1Notation()).join(', ');
    const message =
      '🚨 Εντοπίστηκαν ' + targets.length +
      ' κελιά με ασυμπλήρωτο το "<strong>' + NAME_PROMPT + '</strong>" !!!<br><br>' +
      '📍 Κελιά: <strong>' + cellRefs + '</strong><br><br>' +
      '📝 Παρακαλώ συμπληρώστε το ονοματεπώνυμό σας στη στήλη <strong>B</strong>.';
    try { PopupLib.showCustomPopup(message, 'error'); } catch (_) {}
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

// =====================================================================================
// ADMINTOOLSLIB V6.8.0 — Universal Version Updater – 17.10.2025 – 13:55
// =====================================================================================
// 🔧 Function: updateVersionInfo_Universal()
// Description:
//  • Updates version header for ANY HoB script (Checklist, Blink, AutoDuplicate, etc.)
//  • Automatically detects prefix (e.g. CHECKLIST / BLINK / AUTODUPLICATE).
//  • Increments patch version (+0.0.1).
//  • Updates build date & time.
//  • Appends line to changelog block at the bottom.
// =====================================================================================
// Usage:
//   1️⃣ Run → AdminToolsLib.updateVersionInfo_Universal()
//   2️⃣ Type the script filename (e.g. Checklist.gs)
//   3️⃣ Type a short description of the change
//   4️⃣ The header and changelog update automatically
// =====================================================================================

function updateVersionInfo_Universal() {
  const ui = SpreadsheetApp.getUi();
  const promptFile = ui.prompt(
    "🔧 Universal Version Updater",
    "Πληκτρολόγησε το ακριβές όνομα του αρχείου (π.χ. Checklist.gs, Blink.gs):",
    ui.ButtonSet.OK_CANCEL
  );

  if (promptFile.getSelectedButton() !== ui.Button.OK) return;
  const filename = promptFile.getResponseText().trim();
  if (!filename) return ui.alert("❌ Δεν δόθηκε όνομα αρχείου.");

  const files = DriveApp.getFilesByName(filename);
  if (!files.hasNext()) {
    ui.alert(`❌ Δεν βρέθηκε αρχείο με όνομα "${filename}" στο Drive.`);
    return;
  }

  const file = files.next();
  const content = file.getBlob().getDataAsString();

  // Detect prefix (CHECKLIST / BLINK / AUTODUPLICATE / HOBMASTERS / etc.)
  const prefixMatch = content.match(/\/\/\s*([A-Z_]+)\s+V(\d+)\.(\d+)\.(\d+)/);
  if (!prefixMatch) {
    ui.alert("⚠️ Δεν βρέθηκε συμβατή γραμμή header (π.χ. // CHECKLIST Vx.x.x).");
    return;
  }

  const prefix = prefixMatch[1];
  const major = parseInt(prefixMatch[2], 10);
  const minor = parseInt(prefixMatch[3], 10);
  const patch = parseInt(prefixMatch[4], 10);

  const newPatch = patch + 1;
  const newVersion = `V${major}.${minor}.${newPatch}`;
  const dateStr = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "dd/MM/yyyy – HH:mm");

  const descPrompt = ui.prompt(
    `Αρχείο: ${filename}\nPrefix: ${prefix}\nΤρέχουσα έκδοση: V${major}.${minor}.${patch}\nΝέα έκδοση: ${newVersion}\n\nΠληκτρολόγησε σύντομη περιγραφή αλλαγής:`,
    ui.ButtonSet.OK_CANCEL
  );
  if (descPrompt.getSelectedButton() !== ui.Button.OK) return;
  const desc = descPrompt.getResponseText().trim() || "(no description)";

  // Build new header
  const newHeader = `// ${prefix} ${newVersion} — ${dateStr}\n// ${desc}`;
  const updated = content.replace(/\/\/\s*[A-Z_]+\s+V.*\n\/\/.*/, newHeader);

  // Append changelog entry
  const logLine = `// ${prefix} ${newVersion} — ${dateStr} — ${desc}\n`;
  const newContent = updated + "\n" + logLine;

  // Save new version
  file.setContent(newContent);

  ui.alert(`✅ ${prefix} ενημερώθηκε επιτυχώς!\n\nΈκδοση: ${newVersion}\nΠεριγραφή: ${desc}`);
}

// =====================================================================================
// REMOTE CLIENT VERSION UPDATER (for use from Checklist menu)
// =====================================================================================
function updateVersionInfo_Remote_() {
  const user = Session.getEffectiveUser().getEmail();
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const owner = ss.getOwner().getEmail();
  const allowed = "hobdeks@gmail.com";
  if (user !== owner || user !== allowed) {
    throw new Error("⛔ Μόνο ο ιδιοκτήτης μπορεί να ενημερώσει την έκδοση.");
  }

  const file = DriveApp.getFileById(ss.getId());
  const content = file.getBlob().getDataAsString();
  const versionRegex = /(\/\/\s*[A-Z_]+\s+V)(\d+)\.(\d+)\.(\d+)/;
  const match = content.match(versionRegex);
  if (!match) throw new Error("Δεν βρέθηκε γραμμή έκδοσης στο αρχείο.");

  const prefix = match[1].replace(/\/|\s|V/g, "").trim();
  const major = parseInt(match[2], 10);
  const minor = parseInt(match[3], 10);
  const patch = parseInt(match[4], 10) + 1;
  const newVersion = `V${major}.${minor}.${patch}`;
  const dateStr = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "dd/MM/yyyy – HH:mm");

  const ui = SpreadsheetApp.getUi();
  const prompt = ui.prompt(
    "🧩 Ενημέρωση Έκδοσης",
    "Γράψε σύντομη περιγραφή αλλαγής:",
    ui.ButtonSet.OK_CANCEL
  );
  if (prompt.getSelectedButton() !== ui.Button.OK) return;
  const desc = prompt.getResponseText().trim() || "(no description)";

  const newHeader = `// ${prefix} ${newVersion} — ${dateStr}\n// ${desc}`;
  const updated = content.replace(/\/\/\s*[A-Z_]+\s+V.*\n\/\/.*/, newHeader);
  const logLine = `// ${prefix} ${newVersion} — ${dateStr} — ${desc}\n`;
  const finalContent = updated + "\n" + logLine;

  file.setContent(finalContent);
  PopupLib.showSuccessMessage("✅ Ενημερώθηκε η έκδοση σε " + newVersion);
}

