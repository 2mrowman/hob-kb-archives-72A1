// ==========================

// HoB - Admin Tools Library

// Version: V6.7.6 - 30.09.2025 - Bugfixes (Drive addFile FileRef, wrappers) - no logic changes

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

const HOB_MASTERS_FILE_ID = '1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI'; // HoB_Masters

const DESTINATION_FOLDER_ID = '1ryekzwj3owrxXSjt7ty0veKniq9TQq2K'; // Φάκελος προορισμού για μηνιαία αντίγραφα

const MASTER_SHEET_NAME = 'MASTER';

const NAME_PROMPT = 'Όνομα Επώνυμο?';

const COL_B = 2; // Στήλη B

const BLINK_CYCLES = 3; // Προαιρετικό blinking

// ==========================

// 📌 Δημιουργία νέας ημέρας (όνομα tab: dd/MM) + κρύψιμο MASTER

// ==========================

function createNewDay_AUTO(masterId, templateTab) {

const ss = SpreadsheetApp.getActiveSpreadsheet();

const tz = Session.getScriptTimeZone();

const todayName = Utilities.formatDate(new Date(), tz, 'dd/MM'); // π.χ. 30/09

const exists = ss.getSheetByName(todayName);

if (exists) {

try { PopupLib.showCustomPopup('ℹ️ Υπάρχει ήδη ημέρα: &lt;b&gt;' + todayName + '&lt;/b&gt;', 'info'); } catch (\_) {}

const masterSheet = ss.getSheetByName(MASTER_SHEET_NAME);

if (masterSheet && !masterSheet.isSheetHidden()) masterSheet.hideSheet();

return;

}

const masters = SpreadsheetApp.openById(masterId);

const tpl = masters.getSheetByName(templateTab);

if (!tpl) {

try { PopupLib.showCustomPopup('❌ Δεν βρέθηκε template: &lt;b&gt;' + templateTab + '&lt;/b&gt;', 'error'); } catch (\_) {}

return;

}

const newSheet = tpl.copyTo(ss).setName(todayName);

ss.setActiveSheet(newSheet);

ss.moveActiveSheet(0);

const master = ss.getSheetByName(MASTER_SHEET_NAME);

if (master && !master.isSheetHidden()) master.hideSheet();

try { PropertiesService.getDocumentProperties().setProperty('lastTabCreated', new Date().toISOString()); } catch (\_) {}

try { PopupLib.showCustomPopup('✅ Δημιουργήθηκε η νέα ημέρα: &lt;b&gt;' + todayName + '&lt;/b&gt;', 'success'); } catch (\_) {}

}

// ==========================

// 📌 FILE-LEVEL Duplicate & Cleanup (ΑΝΤΙΓΡΑΦΟ στο φάκελο + ΚΑΘΑΡΙΣΜΟΣ στο ΤΡΕΧΟΝ αρχείο)

// ==========================

/\*\* Wrapper για Owner Menu (μην αλλάξεις όνομα) \*/

function automatedDuplicateAndCleanupFromMenu() {

try {

automatedDuplicateAndCleanup();

} catch (err) {

try {

PopupLib.showErrorMessage('⚠️ Σφάλμα (Duplicate & Cleanup):&lt;br&gt;&lt;br&gt;&lt;code&gt;' + String(err) + '&lt;/code&gt;');

} catch (\_) {

SpreadsheetApp.getUi().alert('Σφάλμα (Duplicate & Cleanup): ' + String(err));

}

throw err;

}

}

/\*\*

\* Κύρια ρουτίνα:

\* 1) Αντιγράφει το ΤΡΕΧΟΝ Spreadsheet στον φάκελο ως YYMM_OriginalName (προηγούμενος μήνας)

\* 2) Αφαιρεί editors στο ΝΕΟ αντίγραφο (εκτός owner)

\* 3) ΣΤΟ ΤΡΕΧΟΝ αρχείο: εμφανίζει MASTER & διαγράφει τα υπόλοιπα tabs

\*/

function automatedDuplicateAndCleanup() {

Logger.log('🚀 Έναρξη Duplicate & Cleanup');

// (1) Πηγαίο αρχείο (ΤΡΕΧΟΝ)

const ss = SpreadsheetApp.getActiveSpreadsheet();

const originalFileId = ss.getId();

const originalFile = DriveApp.getFileById(originalFileId);

let originalName = originalFile.getName().replace(/Copy of |of /gi, '').trim();

// (2) Υπολογισμός YYMM (προηγούμενος μήνας) - ΔΕΝ αλλάζει

const today = new Date();

let yy = today.getFullYear().toString().slice(-2);

let mm = today.getMonth(); // 0..11

if (mm === 0) { mm = 12; yy = (parseInt(yy, 10) - 1).toString(); }

const yymm = yy + ('0' + mm).slice(-2);

// (3) Αντιγραφή στο φάκελο (Drive File API)

const folder = DriveApp.getFolderById(DESTINATION_FOLDER_ID);

const newFileName = yymm + '\_' + originalName;

const newFile = originalFile.makeCopy(newFileName, folder);

Logger.log('✅ Αντίγραφο αρχείου: ' + newFileName);

// (4) Αφαίρεση editors εκτός owner στο ΝΕΟ αντίγραφο

removeAllUsersExceptOwner_(newFile);

// (5) ΚΑΘΑΡΙΣΜΟΣ ΣΤΟ ΤΡΕΧΟΝ Spreadsheet

showMasterAndDeleteOthers();

try {

PopupLib.showSuccessMessage(

'✅ Δημιουργήθηκε αντίγραφο: &lt;b&gt;' + newFileName + '&lt;/b&gt;&lt;br&gt;📋 Καθαρίστηκε το ΤΡΕΧΟΝ αρχείο (κρατήθηκε μόνο το &lt;b&gt;' + MASTER_SHEET_NAME + '&lt;/b&gt;).'

);

} catch (\_) {}

Logger.log('✅ Ολοκλήρωση Duplicate & Cleanup (copy→remove editors στο νέο, cleanup στο τρέχον).');

return newFile;

}

/\*\* Αφαίρεση όλων των editors εκτός owner (Drive File) \*/

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

try { PopupLib.showCustomPopup('❌ Δεν βρέθηκε φύλλο &lt;b&gt;' + MASTER_SHEET_NAME + '&lt;/b&gt;.', 'error'); } catch (\_) {}

return;

}

masterSheet.showSheet();

ss.getSheets().forEach(function (sheet) {

if (sheet.getName() !== MASTER_SHEET_NAME) ss.deleteSheet(sheet);

});

try { PopupLib.showCustomPopup('📋 Εμφανίστηκε το &lt;b&gt;' + MASTER_SHEET_NAME + '&lt;/b&gt; και διαγράφηκαν τα υπόλοιπα.', 'info'); } catch (\_) {}

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

const targets = \[\];

for (let i = 0; i < vals.length; i++) {

const v = String(vals\[i\]\[0\] || '').trim();

if (v === NAME_PROMPT) targets.push(rngB.getCell(i + 1, 1));

}

if (targets.length > 0) {

const cellRefs = targets.map(c => c.getA1Notation()).join(', ');

const message =

'🚨 Εντοπίστηκαν ' + targets.length +

' κελιά με ασυμπλήρωτο το "&lt;strong&gt;' + NAME_PROMPT + '&lt;/strong&gt;" !!!&lt;br&gt;&lt;br&gt;' +

'📍 Κελιά: &lt;strong&gt;' + cellRefs + '&lt;/strong&gt;&lt;br&gt;&lt;br&gt;' +

'📝 Παρακαλώ συμπληρώστε το ονοματεπώνυμό σας στη στήλη &lt;strong&gt;B&lt;/strong&gt;.';

try { PopupLib.showCustomPopup(message, 'error'); } catch (\_) {}

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

try { PopupLib.showCustomPopup('🧽 Καθαρίστηκαν όλα τα Notes.', 'success'); } catch (\_) {}

}

// ==========================

// 📌 Debug Context

// ==========================

function debugUserContext() {

const email = Session.getEffectiveUser().getEmail();

const docTitle = SpreadsheetApp.getActiveSpreadsheet().getName();

const msg = '👤 Χρήστης: &lt;b&gt;' + email + '&lt;/b&gt;&lt;br&gt;' +

'📄 Αρχείο: &lt;b&gt;' + docTitle + '&lt;/b&gt;&lt;br&gt;' +

'🕒 Ώρα: &lt;b&gt;' + new Date().toLocaleString() + '&lt;/b&gt;';

try { PopupLib.showCustomPopup(msg, 'info'); } catch (\_) {}

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

PopupLib.showErrorMessage('🚨 Test Error από AdminToolsLib'); Utilities.sleep(300);

PopupLib.showInfoMessage('ℹ️ Test Info από AdminToolsLib'); Utilities.sleep(300);

PopupLib.showSuccessMessage('✅ Test Success από AdminToolsLib'); Utilities.sleep(300);

PopupLib.showWarningMessage('⚠️ Test Warning από AdminToolsLib');

} catch (err) {

Logger.log('Σφάλμα στο testAllPopupsFromAdmin: ' + err);

}

}