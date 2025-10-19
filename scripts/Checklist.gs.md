*Last updated:* 19/10/2025 – 13:33 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 19/10/2025 – 13:33 (DEV-only)
*Build:* 698f4a9
*
*
*
*
*
*
*Last updated: 19/10/2025 – 12:43 (Europe/Athens)*

// =====================================================================================
// CHECKLIST V7.2.1 — Final Production Build – 17.10.2025 – 12:40
// Auto-day creation restored (Installable Trigger)
// Clean UI Menu (removed manual "Δημιουργία Σημερινής Ημέρας")
// Aligned with V6.3 behavior; full-dynamic template resolve from HoB_Masters/Templates
// =====================================================================================
//
// Function Checklist (Compatibility Contract)
// - onOpen(e)                               ✅ (simple trigger: UI only)
// - onOpen_Installed(e)                     ✅ (installable trigger: full privileges)
// - runTodayInit_()                         ✅ (shared privileged entrypoint)
// - getTemplateTabFromHoBMasters_()         (unchanged; dynamic lookup)
// - hideLocalMasterIfVisible_()             (unchanged)
// - loadMenuDynamically()                   ✅ (UI cleaned)
// - onEdit(e), TIMESTAMP(), testLibExists() (unchanged)
// - runIntegrityCheck_()                    (integrity validator)
//
// =====================================================================================

const ENABLE_PLACEHOLDERS = false;
const HOB_MASTERS_FILE_ID = "1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI";

// SIMPLE onOpen: UI ONLY
function onOpen(e) {
  const ui = SpreadsheetApp.getUi();

  ui.createMenu("🗂️ HoB - Menu")
    .addItem("⏳ Φόρτωση Μενού…", "loadMenuDynamically")
    .addToUi();
}

// INSTALLABLE onOpen: FULL PRIVILEGES
function onOpen_Installed(e) {
  try {
    runTodayInit_();
  } catch (err) {
    try {
      PopupLib.showCustomPopup("⚠️ Σφάλμα στο άνοιγμα:<br><br>" + err.message, "error");
    } catch (_) {
      SpreadsheetApp.getUi().alert("⚠️ Σφάλμα στο άνοιγμα: " + err.message);
    }
  }
}

// AUTO-DAY CREATION LOGIC
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

// TEMPLATE LOOKUP
function getTemplateTabFromHoBMasters_() {
  const fileName = SpreadsheetApp.getActiveSpreadsheet().getName().trim();
  const masters = SpreadsheetApp.openById(HOB_MASTERS_FILE_ID);
  const tplSheet = masters.getSheetByName("Templates");
  if (!tplSheet) return null;

  const last = tplSheet.getLastRow();
  if (last < 2) return null;

  const data = tplSheet.getRange(2, 1, last - 1, 2).getValues();
  for (let i = 0; i < data.length; i++) {
    const [chkName, tplName] = data[i];
    if (String(chkName || "").trim() === fileName && tplName) return String(tplName).trim();
  }
  return null;
}

// MENU LOADER (Cleaned)
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
      menu.addSeparator().addSubMenu(ownerSub);
    }
  }

  menu.addToUi(); // ✅ no manual "create day" anymore
}

// MASTER HIDE HANDLER
function hideLocalMasterIfVisible_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const masterSheet = ss.getSheetByName("MASTER");
  if (!masterSheet) return;
  const others = ss.getSheets().filter(sh => sh.getName() !== "MASTER" && !sh.isSheetHidden());
  if (others.length > 0) masterSheet.hideSheet();
}

// onEdit / TIMESTAMP
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

// END OF FILE — CHECKLIST V7.2.1 — 17/10/2025 – 12:40
// =====================================================================================

// ADMIN TOOLS
// INTEGRITY SELF-CHECK
function runIntegrityCheck() {
  const fn = ["onOpen", "onOpen_Installed", "runTodayInit_", "getTemplateTabFromHoBMasters_", "hideLocalMasterIfVisible_", "loadMenuDynamically"];
  const missing = fn.filter(f => typeof this[f] !== "function");
  if (missing.length > 0) throw new Error("Missing functions: " + missing.join(", "));

  const user = Session.getEffectiveUser().getEmail();
  const owner = SpreadsheetApp.getActiveSpreadsheet().getOwner().getEmail();
  if (user !== owner) console.log("ℹ️ IntegrityCheck: User is not owner (" + user + ")");

  SpreadsheetApp.getUi().alert("✅ Integrity check passed for V7.2.1 – " + new Date());
}

function testLibraryConnection() {
  Logger.log(typeof AdminToolsLib.updateVersionInfo_Remote_);
}

function debugNamespace() {
  Logger.log(Object.keys(AdminToolsLib || {}));
}

function testLibExists() {
  try {
    const has = typeof AdminToolsLib.createNewDay_AUTO;
    SpreadsheetApp.getUi().alert("type of createNewDay_AUTO: " + has);
  } catch (e) {
    SpreadsheetApp.getUi().alert("ERROR: " + e.toString());
  }
}
