// ==========================

// HoB - Menu Library (Dynamic Version)

// Version: V7.0.0 - 07/10/2025 - Owner Visibility Fix + Session Flush

// ==========================

// ✅ Functions included in this version:

// getOwnerEmail

// getMenuItemsFromSheet

// loadMenuDynamically

// getTemplateTabFromHoBMasters_

// User Tools (openNeaParalaviForm … openForm_EmailsList)

// openUrlInNewTab

// Wrappers (AdminToolsLib, PopupLib, HoBMastersLib)

// --------------------------

// Constants

// --------------------------

const HOB_MASTERS_FILE_ID = '1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI';

const MENU_SHEET_ID = '1JeDKj1CdWlAgPGnsRxCu2Fi1rkKxIBXeS861WXZDpEQ';

const MENU_SHEET_NAME = 'Menu';

// --------------------------

// Owner Email

// --------------------------

function getOwnerEmail() {

return "<hobdeks@gmail.com>";

}

// --------------------------

// Load menu items from MenuListTable

// --------------------------

function getMenuItemsFromSheet(menuType) {

var ss = SpreadsheetApp.openById(MENU_SHEET_ID);

var sheet = ss.getSheetByName(MENU_SHEET_NAME);

var data = sheet.getDataRange().getValues();

if (!data || data.length < 2) return \[\];

var header = data\[0\];

var idxStore = header.indexOf('Store Name');

var idxMenu = header.indexOf('Menu Name');

var idxFunc = header.indexOf('Function Name');

var idxType = header.indexOf('Type');

if (idxStore === -1 || idxMenu === -1 || idxFunc === -1 || idxType === -1) {

throw new Error('MenuLib.getMenuItemsFromSheet: Λείπουν απαιτούμενες στήλες.');

}

var out = \[\];

var typeFilter = (menuType != null) ? String(menuType) : null;

for (var r = 1; r < data.length; r++) {

var row = data\[r\];

if (!row || row.length === 0) continue;

var typeVal = (row\[idxType\] || '').toString().trim();

if (typeFilter && typeVal !== typeFilter) continue;

out.push({

store: (row\[idxStore\] || '').toString(),

name: (row\[idxMenu\] || '').toString(),

func: (row\[idxFunc\] || '').toString(),

type: typeVal

});

}

return out;

}

// --------------------------

// Dynamic menu loader (Owner-safe + Session Flush)

// --------------------------

function loadMenuDynamically() {

var lock = LockService.getDocumentLock();

if (!lock.tryLock(5000)) return;

try {

var ui = SpreadsheetApp.getUi();

var ss = SpreadsheetApp.getActiveSpreadsheet();

var userEmail = Session.getEffectiveUser().getEmail();

var realOwner = ss.getOwner().getEmail();

var ownerEmail = getOwnerEmail();

SpreadsheetApp.flush(); // ✅ συγχρονισμός session για αποφυγή race condition

var menu = ui.createMenu("🗂️ HoB - Menu");

// --- User Menu ---

var userItems = getMenuItemsFromSheet("user");

userItems.forEach(function (item) {

if (item.name && item.func) menu.addItem(item.name, item.func);

});

// --- Owner Menu (μόνο για πραγματικό Owner) ---

if (userEmail === realOwner && userEmail === ownerEmail) {

menu.addSeparator();

var ownerMenu = ui.createMenu("🛠️ Εργαλεία Ιδιοκτήτη");

var ownerItems = getMenuItemsFromSheet("owner");

ownerItems.forEach(function (item) {

if (item.name && item.func) ownerMenu.addItem(item.name, item.func);

});

menu.addSubMenu(ownerMenu);

}

menu.addToUi();

} finally {

try { lock.releaseLock(); } catch (\_) {}

}

}

// --------------------------

// Lookup template from HoB_Masters/Templates

// --------------------------

function getTemplateTabFromHoBMasters_() {

const ss = SpreadsheetApp.getActiveSpreadsheet();

const fileName = ss.getName().trim();

const masters = SpreadsheetApp.openById(HOB_MASTERS_FILE_ID);

const tplSheet = masters.getSheetByName('Templates');

if (!tplSheet) return null;

const data = tplSheet.getRange(2, 1, tplSheet.getLastRow() - 1, 3).getValues();

// Columns: A=CHECKLIST FILENAME, B=TEMPLATE, C=FILE ID

for (let i = 0; i < data.length; i++) {

const \[chkName, tplName\] = data\[i\];

if (chkName && String(chkName).trim() === fileName) {

return tplName;

}

}

return null;

}

// --------------------------

// User Tools (Links)

// --------------------------

function openNeaParalaviForm() { openUrlInNewTab("<https://docs.google.com/document/d/1qR3HybnWVqBfvyw2PVIM_yis9cXoBzm2MHLWk8L8kO0/edit?usp=sharing>"); }

function openSakoulesForm() { openUrlInNewTab("<https://docs.google.com/spreadsheets/d/17vuZ8bQt2G2Z0yN-7PGBo3U2IA2lnNH1ElMzbCUI18I/edit?usp=sharing>"); }

function openForm_CreditTAXFree() { openUrlInNewTab("<https://drive.google.com/file/d/1X-nZymdDICcRFP1r2TG7QuyArHw8swlJ/view?usp=sharing>"); }

function openForm_Elleipseis() { openUrlInNewTab("<https://docs.google.com/document/d/1tEumPOt3GSSLF5mLBk9PcOMISQRjUQ58f4gHd0X1ugc/edit?usp=sharing>"); }

function openForm_AllagesTimon() { openUrlInNewTab("<https://docs.google.com/document/d/14QROsEOZZx8DT_MFfLZOJPLq89wVo41cPT4JTpPen5w/edit?usp=sharing>"); }

function openForm_ElattomatikosProion() { openUrlInNewTab("<https://docs.google.com/document/d/1buWOggRgUYjijcOSds4z6t4SkQZqL7leKar9r-dv-vI/edit?usp=sharing>"); }

function openForm_CheckKodikou() { openUrlInNewTab("<https://docs.google.com/document/d/1nyuKkQCwb6EzK_WKy4m1ZvOm2RJp2xCM5dIKDxp0_sI/edit?usp=sharing>"); }

function openForm_AstoxiasParaggelias() { openUrlInNewTab("<https://docs.google.com/document/d/1c1tyNvI70_Qd4GnblSau9NVhSGK4h2EyAOMHYx_RW08/edit?usp=sharing>"); }

function openForm_GenikiTaxydromiki() { openUrlInNewTab("<https://docs.google.com/document/d/1nZEajIgrwQOyMWBcZ61KDPagnvacZfDsMcCI69XVkXI/edit?usp=sharing>"); }

function openForm_EmailsList() { openUrlInNewTab("<https://docs.google.com/spreadsheets/d/1_RyDNnbcTIUyoU-3sOYvihsFmQ8VZmEJsVmqPGu-lms/edit?usp=sharing>"); }

// --------------------------

// Helper: Άνοιγμα URL σε νέο tab

// --------------------------

function openUrlInNewTab(url) {

var html = HtmlService.createHtmlOutput(

"&lt;script&gt;window.open('" + url + "', '\_blank');google.script.host.close();&lt;/script&gt;"

);

SpreadsheetApp.getUi().showModelessDialog(html, "Άνοιγμα");

}

// --------------------------

// Wrappers

// --------------------------

function clearAllNotesFromMenu() { AdminToolsLib.clearAllNotes(); }

function debugUserContextFromMenu() { AdminToolsLib.debugUserContext(); }

function testLibExistsFromMenu() { AdminToolsLib.testLibExists(); }

function testTemplateTabFromMenu() { AdminToolsLib.testTemplateTab(); }

function testAllPopupsFromMenu() { PopupLib.testAllPopupsFromMenu(); }

function automatedDuplicateAndCleanupFromMenu() { AdminToolsLib.automatedDuplicateAndCleanup(); }

function showMasterAndDeleteOthersFromMenu() { AdminToolsLib.showMasterAndDeleteOthers(); }

function remindMissingNamesFromMenu() { AdminToolsLib.remindMissingNames(); }

// --------------------------

// ✅ Create New Day μέσω AdminToolsLib (proxy προς HoBMastersLib)

// --------------------------

function createNewDayFromMenu() {

try {

const templateTab = getTemplateTabFromHoBMasters_();

if (!templateTab) {

PopupLib.showErrorMessage(

"❌ Δεν βρέθηκε template στο HoB_Masters/Templates για το αρχείο: " +

SpreadsheetApp.getActiveSpreadsheet().getName()

);

return;

}

AdminToolsLib.createNewDay_AUTO(HOB_MASTERS_FILE_ID, templateTab); // ✅ Proxy call

} catch (err) {

PopupLib.showErrorMessage("❌ Σφάλμα στο createNewDayFromMenu:&lt;br&gt;" + err);

}

}