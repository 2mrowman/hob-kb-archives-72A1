*Build: ${SHORT_SHA}*
*Last updated: 17/10/2025 – 17:49 (Europe/Athens)*
// =====================================================================================
// HoB - Menu Library
// Version: V7.2.0 – 17/10/2025 – Cleaned menu loader + Owner submenu with version updater
// =====================================================================================
//
// ✅ Functions included in this version:
// getOwnerEmail
// getMenuItemsFromSheet
// loadMenuDynamically (cleaned)
// getTemplateTabFromHoBMasters_
// User Tools (openNeaParalaviForm … openForm_EmailsList)
// openUrlInNewTab
// Wrappers (AdminToolsLib, PopupLib, HoBMastersLib)
// createNewDayFromMenu
// updateVersionFromMenu
// =====================================================================================

// --------------------------
// Constants
// --------------------------
const HOB_MASTERS_FILE_ID = '1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI';
const MENU_SHEET_ID       = '1JeDKj1CdWlAgPGnsRxCu2Fi1rkKxIBXeS861WXZDpEQ';
const MENU_SHEET_NAME     = 'Menu';

// --------------------------
// Owner Email
// --------------------------
function getOwnerEmail() {
  return "hobdeks@gmail.com";
}

// =====================================================================================
// MENU LOADER (Cleaned)
// =====================================================================================
function loadMenuDynamically() {
  const userEmail = Session.getEffectiveUser().getEmail();
  const ownerEmail = MenuLib.getOwnerEmail();
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const ui = SpreadsheetApp.getUi();
  const menu = ui.createMenu("🗂️ HoB - Menu");

  const userItems = MenuLib.getMenuItemsFromSheet("user");
  userItems.forEach(i => menu.addItem(i.name, "MenuLib." + i.func));

  if (userEmail === ownerEmail && ss.getOwner().getEmail() === userEmail) {
    const ownerItems = MenuLib.getMenuItemsFromSheet("owner");
    if (ownerItems.length > 0) {
      const ownerSub = ui.createMenu("🛠️ Εργαλεία Ιδιοκτήτη");
      ownerItems.forEach(i => ownerSub.addItem(i.name, "MenuLib." + i.func));
      ownerSub.addItem("🧩 Ενημέρωση Έκδοσης Script", "MenuLib.updateVersionFromMenu"); // ✅ new entry
      menu.addSeparator().addSubMenu(ownerSub);
    }
  }

  menu.addToUi(); // ✅ fully dynamic (no hardcoded items)
}

// --------------------------
// Load menu items from MenuListTable
// --------------------------
function getMenuItemsFromSheet(menuType) {
  var ss    = SpreadsheetApp.openById(MENU_SHEET_ID);
  var sheet = ss.getSheetByName(MENU_SHEET_NAME);
  var data  = sheet.getDataRange().getValues();
  if (!data || data.length < 2) return [];

  var header   = data[0];
  var idxStore = header.indexOf('Store Name');
  var idxMenu  = header.indexOf('Menu Name');
  var idxFunc  = header.indexOf('Function Name');
  var idxType  = header.indexOf('Type');

  if (idxStore === -1 || idxMenu === -1 || idxFunc === -1 || idxType === -1) {
    throw new Error('MenuLib.getMenuItemsFromSheet: Λείπουν απαιτούμενες στήλες.');
  }

  var out = [];
  var typeFilter = (menuType != null) ? String(menuType) : null;

  for (var r = 1; r < data.length; r++) {
    var row = data[r];
    if (!row || row.length === 0) continue;

    var typeVal = (row[idxType] || '').toString().trim();
    if (typeFilter && typeVal !== typeFilter) continue;

    out.push({
      store: (row[idxStore] || '').toString(),
      name:  (row[idxMenu]  || '').toString(),
      func:  (row[idxFunc]  || '').toString(),
      type:  typeVal
    });
  }
  return out;
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
  for (let i = 0; i < data.length; i++) {
    const [chkName, tplName] = data[i];
    if (chkName && String(chkName).trim() === fileName) {
      return tplName;
    }
  }
  return null;
}

// --------------------------
// User Tools (Forms / Links)
// --------------------------
function openNeaParalaviForm() { openUrlInNewTab("https://docs.google.com/document/d/1qR3HybnWVqBfvyw2PVIM_yis9cXoBzm2MHLWk8L8kO0/edit?usp=sharing"); }
function openSakoulesForm() { openUrlInNewTab("https://docs.google.com/spreadsheets/d/17vuZ8bQt2G2Z0yN-7PGBo3U2IA2lnNH1ElMzbCUI18I/edit?usp=sharing"); }
function openForm_CreditTAXFree() { openUrlInNewTab("https://drive.google.com/file/d/1X-nZymdDICcRFP1r2TG7QuyArHw8swlJ/view?usp=sharing"); }
function openForm_Elleipseis() { openUrlInNewTab("https://docs.google.com/document/d/1tEumPOt3GSSLF5mLBk9PcOMISQRjUQ58f4gHd0X1ugc/edit?usp=sharing"); }
function openForm_AllagesTimon() { openUrlInNewTab("https://docs.google.com/document/d/14QROsEOZZx8DT_MFfLZOJPLq89wVo41cPT4JTpPen5w/edit?usp=sharing"); }
function openForm_ElattomatikosProion() { openUrlInNewTab("https://docs.google.com/document/d/1buWOggRgUYjijcOSds4z6t4SkQZqL7leKar9r-dv-vI/edit?usp=sharing"); }
function openForm_CheckKodikou() { openUrlInNewTab("https://docs.google.com/document/d/1nyuKkQCwb6EzK_WKy4m1ZvOm2RJp2xCM5dIKDxp0_sI/edit?usp=sharing"); }
function openForm_AstoxiasParaggelias() { openUrlInNewTab("https://docs.google.com/document/d/1c1tyNvI70_Qd4GnblSau9NVhSGK4h2EyAOMHYx_RW08/edit?usp=sharing"); }
function openForm_GenikiTaxydromiki() { openUrlInNewTab("https://docs.google.com/document/d/1nZEajIgrwQOyMWBcZ61KDPagnvacZfDsMcCI69XVkXI/edit?usp=sharing"); }
function openForm_EmailsList() { openUrlInNewTab("https://docs.google.com/spreadsheets/d/1_RyDNnbcTIUyoU-3sOYvihsFmQ8VZmEJsVmqPGu-lms/edit?usp=sharing"); }

// --------------------------
// Helper: Άνοιγμα URL σε νέο tab
// --------------------------
function openUrlInNewTab(url) {
  var html = HtmlService.createHtmlOutput(
    "<script>window.open('" + url + "', '_blank');google.script.host.close();</script>"
  );
  SpreadsheetApp.getUi().showModelessDialog(html, "Άνοιγμα");
}

// --------------------------
// Wrappers (AdminToolsLib / PopupLib / HoBMastersLib)
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
    PopupLib.showErrorMessage("❌ Σφάλμα στο createNewDayFromMenu:<br>" + err);
  }
}

// --------------------------
// ✅ Owner-only: Trigger Version Updater
// --------------------------
function updateVersionFromMenu() {
  const user = Session.getEffectiveUser().getEmail();
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const owner = ss.getOwner().getEmail();
  const allowed = getOwnerEmail();

  if (user !== owner || user !== allowed) {
    PopupLib.showErrorMessage("⛔ Μόνο ο ιδιοκτήτης (" + allowed + ") μπορεί να ενημερώσει την έκδοση.");
    return;
  }

  try {
    AdminToolsLib.updateVersionInfo_Remote_();
  } catch (err) {
    PopupLib.showErrorMessage("⚠️ Σφάλμα κατά την ενημέρωση:<br><br>" + err.message);
  }
}
