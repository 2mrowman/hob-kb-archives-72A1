*Last updated:* 23/10/2025 - 14:34 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 23/10/2025 - 14:34 (DEV-only)
*Build:* 65aa232

// CHECKLIST V7.3.1 — Production — 18/10/2025 – 15:46
// Changes: Formatting to single-line section headers (no ==== bars). Added owner action updateVersionInfo_Remote(desc).
// Behavior: Auto-day on open (installable trigger). Clean HoB menu (no “Δημιουργία Νέας Ημέρας”). Full-dynamic template resolve.
// Function Checklist (Compatibility Contract)
// - onOpen(e)                               ✅ simple trigger: UI only
// - onOpen_Installed(e)                     ✅ installable trigger: full privileges
// - runTodayInit_()                         ✅ shared privileged entrypoint
// - getTemplateTabFromHoBMasters_()         unchanged; dynamic lookup
// - hideLocalMasterIfVisible_()             unchanged
// - loadMenuDynamically()                   ✅ owner tools include “Ενημέρωση Έκδοσης Script”
// - updateVersionInfo_Remote(desc)          ✅ NEW wrapper → AdminToolsLib
// - onEdit(e), TIMESTAMP(), testLibExists() unchanged
// - runIntegrityCheck_()                    integrity validator
// Alignment: HoB KB build 72A1
const ENABLE_PLACEHOLDERS = false; // keep false in production
const HOB_MASTERS_FILE_ID = "1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI";
// SIMPLE onOpen: UI ONLY (no privileged calls)
function onOpen(e) {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu("🗂️ HoB - Menu")
    .addItem("⏳ Φόρτωση Μενού…", "loadMenuDynamically")
    .addToUi();
}

// INSTALLABLE onOpen: FULL PRIVILEGES
function onOpen_Installed(e) {
  try {
    runTodayInit_(); // auto create today's sheet
  } catch (err) {
    try {
      PopupLib.showCustomPopup("⚠️ Σφάλμα στο άνοιγμα:<br><br>" + err.message, "error");
    } catch (_) {
      SpreadsheetApp.getUi().alert("⚠️ Σφάλμα στο άνοιγμα: " + err.message);
    }
  }
}

// SHARED ENTRYPOINT (used by trigger)
function runTodayInit_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const templateTab = getTemplateTabFromHoBMasters_();

  if (!templateTab) {
    PopupLib.showCustomPopup(
      "❌ Δεν βρέθηκε template για το αρχείο:<br><br><b>" +
        ss.getName() +
        "</b><br><br>Έλεγξε το HoB_Masters → <b>Templates</b> tab.",
      "error"
    );
    return;
  }

  AdminToolsLib.createNewDay_AUTO(HOB_MASTERS_FILE_ID, templateTab);
  try { hideLocalMasterIfVisible_(); } catch (_) {}
}

// TEMPLATE LOOKUP from HoB_Masters/Templates
function getTemplateTabFromHoBMasters_() {
  const fileName = SpreadsheetApp.getActiveSpreadsheet().getName().trim();
  const masters = SpreadsheetApp.openById(HOB_MASTERS_FILE_ID);
  const tplSheet = masters.getSheetByName("Templates");
  if (!tplSheet) return null;

  const last = tplSheet.getLastRow();
  if (last < 2) return null;

  const data = tplSheet.getRange(2, 1, last - 1, 2).getValues(); // [[ChecklistName, TemplateTab], ...]
  for (let i = 0; i < data.length; i++) {
    const [chkName, tplName] = data[i];
    if (String(chkName || "").trim() === fileName && tplName) return String(tplName).trim();
  }
  return null;
}

// MENU LOADER (clean; owner submenu only)
function loadMenuDynamically() {
  const userEmail = Session.getEffectiveUser().getEmail();
  const ownerEmail = MenuLib.getOwnerEmail();
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const ui = SpreadsheetApp.getUi();
  const menu = ui.createMenu("🗂️ HoB - Menu");

  // User menu items (from sheet “user”)
  const userItems = MenuLib.getMenuItemsFromSheet("user");
  userItems.forEach(i => menu.addItem(i.name, "MenuLib." + i.func));

  // Owner tools (from sheet “owner”) + Version Update
  if (userEmail === ownerEmail && ss.getOwner().getEmail() === userEmail) {
    const ownerSub = ui.createMenu("🛠️ Εργαλεία Ιδιοκτήτη");
    const ownerItems = MenuLib.getMenuItemsFromSheet("owner");
    ownerItems.forEach(i => ownerSub.addItem(i.name, "MenuLib." + i.func));
    ownerSub.addSeparator().addItem("🧩 Ενημέρωση Έκδοσης Script", "updateVersionInfo_Remote");
    menu.addSeparator().addSubMenu(ownerSub);
  }

  menu.addToUi();
}

// MASTER HIDE HANDLER
function hideLocalMasterIfVisible_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const masterSheet = ss.getSheetByName("MASTER");
  if (!masterSheet) return;
  const others = ss.getSheets().filter(sh => sh.getName() !== "MASTER" && !sh.isSheetHidden());
  if (others.length > 0) masterSheet.hideSheet();
}

// onEdit handler + TIMESTAMP helper
function onEdit(e) {
  try {
    const sheet = e.range.getSheet();
    const name = sheet.getName();
    if (["START", "MASTER"].includes(name)) return;

    const col = e.range.getColumn();
    const row = e.range.getRow();
    const val = e.range.getValue();
    const timestampFormat = 'HH:mm:ss.000" - "dd/MM';
    const colB = 2, colC = 3, colD = 4;

    if (col === colC) {
      const cellB = sheet.getRange(row, colB);
      if (!cellB.getValue()) {
        cellB.setValue("Όνομα Επώνυμο?").setFontColor("#d32f2f").setFontWeight("bold");
      }
      const cellD = sheet.getRange(row, colD);
      cellD.setNumberFormat(timestampFormat).setValue(new Date());
    }

    if (col === colB && val && val !== "Όνομα Επώνυμο?") {
      e.range.setFontColor(null).setFontWeight(null).setBackground(null);
    }
  } catch (err) {
    console.error("❌ Σφάλμα στο onEdit:", err);
  }
}

function TIMESTAMP() {
  return Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'HH:mm:ss.000" - "dd/MM');
}

/**
 * Wrapper for AdminToolsLib.remindMissingNames()
 * Used by time-driven trigger
 */
function remindMissingNames() {
  AdminToolsLib.remindMissingNames();
}

// END OF FILE — CHECKLIST V7.3.1 — 18/10/2025 – 15:46
// =====================================================================================

// ADMIN TOOLS

// VERSION UPDATE (Owner action) — wrapper to AdminToolsLib
function updateVersionInfo_Remote(desc) {
  const ui = SpreadsheetApp.getUi();

  let description = (desc || "").toString().trim();
  if (!description) {
    const p = ui.prompt(
      "🧩 Ενημέρωση Έκδοσης",
      "Πληκτρολόγησε σύντομη περιγραφή αλλαγής (μπαίνει στο header & changelog):",
      ui.ButtonSet.OK_CANCEL
    );
    if (p.getSelectedButton() !== ui.Button.OK) return;
    description = p.getResponseText().trim() || "(no description)";
  }

  try {
    if (typeof AdminToolsLib.updateVersionInfo_Remote === "function") {
      AdminToolsLib.updateVersionInfo_Remote(description);
    } else if (typeof AdminToolsLib.updateVersionInfo_Remote_ === "function") {
      AdminToolsLib.updateVersionInfo_Remote_(description);
    } else {
      throw new Error("Δεν βρέθηκε διαθέσιμη function στο AdminToolsLib (updateVersionInfo_Remote[_]).");
    }
  } catch (err) {
    try { PopupLib.showErrorMessage("❌ Αποτυχία ενημέρωσης έκδοσης: " + err.message); }
    catch (_) { ui.alert("❌ Αποτυχία ενημέρωσης έκδοσης: " + err.message); }
    return;
  }

  try { PopupLib.showSuccessMessage("✅ Η έκδοση ενημερώθηκε επιτυχώς!"); }
  catch (_) { ui.alert("✅ Η έκδοση ενημερώθηκε επιτυχώς!"); }
}

// INTEGRITY SELF-CHECK
function runIntegrityCheck_() {
  const fn = [
    "onOpen",
    "onOpen_Installed",
    "runTodayInit_",
    "getTemplateTabFromHoBMasters_",
    "hideLocalMasterIfVisible_",
    "loadMenuDynamically",
    "updateVersionInfo_Remote",
    "onEdit",
    "TIMESTAMP",
    "testLibExists"
  ];
  const missing = fn.filter(f => typeof this[f] !== "function");
  if (missing.length > 0) throw new Error("Missing functions: " + missing.join(", "));

  const user = Session.getEffectiveUser().getEmail();
  const owner = SpreadsheetApp.getActiveSpreadsheet().getOwner().getEmail();
  if (user !== owner) console.log("ℹ️ IntegrityCheck: User is not owner (" + user + ")");

  SpreadsheetApp.getUi().alert("✅ Integrity check passed for V7.3.1 – " + new Date());
}

// DIAGNOSTICS
function testLibExists() {
  try {
    const has = typeof AdminToolsLib.createNewDay_AUTO;
    SpreadsheetApp.getUi().alert("type of createNewDay_AUTO: " + has);
  } catch (e) {
    SpreadsheetApp.getUi().alert("ERROR: " + e.toString());
  }
}

