*Last updated:* 28/10/2025 - 09:01 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 28/10/2025 - 09:01 (DEV-only)
*Build:* 053c02a

// CHECKLIST V7.4.0 — Production — 03/11/2025 – 11:30 - automatedDuplicateAndCleanu


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
  if (!e || !e.range) {
  console.log("onEdit: No event object (manual run)");
  return;
}
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

// Wrapper για trigger
function automatedDuplicateAndCleanup() {
  AdminToolsLib.automatedDuplicateAndCleanup();
}
// _______END OF FILE — CHECKLIST V7.4.0 — Production — 03/11/2025_____
