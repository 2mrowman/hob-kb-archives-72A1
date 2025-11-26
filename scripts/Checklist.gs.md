// CHECKLIST V7.4.6 — Production — 26/11/2025 applied applyValidation to onOpen_Installed


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
  try { AdminToolsLib.onOpenInstalledCore_(e); } catch (err) { console.log('onOpenInstalledCore_ failed:', err); }
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

function applyValidation_B_requires_C() {
  const sh = SpreadsheetApp.getActiveSheet();
  const name = sh.getName();
  if (["START", "MASTER"].includes(name)) return;

  const firstDataRow = 2;              
  const lastRow = Math.max(firstDataRow, sh.getMaxRows());
  const rangeB = sh.getRange(firstDataRow, 2, lastRow - firstDataRow + 1, 1); // B2:B

const rule = SpreadsheetApp.newDataValidation()
  .setAllowInvalid(false)
  .requireFormulaSatisfied('=LEN($C2)>0')
  .setHelpText('Δεν επιτρέπεται η λειτουργία αυτή αν δεν υπάρχει επιλογή στη στήλη C.\nΤο όνομα συμπληρώνεται αυτόματα από το απο πάνω κελί.')
  .build();

rangeB.setDataValidation(rule);

}

// onEdit handler + TIMESTAMP helper V5
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
    const timestampFormat = 'HH:mm:ss.000" - "dd/MM';
    const colB = 2, colC = 3, colD = 4, colE = 5;
    const placeholderB = "Όνομα Επώνυμο?";
    const placeholderE = "Γράψτε το σχόλιο σας εδώ";

    if (col === colC) {
      const numRows = e.range.getNumRows();
      const values = e.range.getValues();

      for (let i = 0; i < numRows; i++) {
        const targetRow = row + i;
        const cellB = sheet.getRange(targetRow, colB);
        const cellD = sheet.getRange(targetRow, colD);
        const cellE = sheet.getRange(targetRow, colE);
        const v = (values[i] && values[i][0] != null) ? String(values[i][0]).trim() : "";

        if (v === "") {
          cellB.clearContent().setFontColor(null).setFontWeight(null);
          cellD.clearContent();
          cellE.clearContent().setFontColor(null).setFontWeight(null);
          continue;
        }

        if (v.toLowerCase().indexOf("σχόλιο") !== -1) {
          if (!cellE.getValue()) {
            cellE.setValue(placeholderE).setFontColor("#d32f2f").setFontWeight("bold");
          }
        } else {
          // Αν αλλάξει από "σχόλιο" σε κάτι άλλο και η Ε έχει το placeholder → καθάρισε
          if (cellE.getValue() === placeholderE) {
            cellE.clearContent().setFontColor(null).setFontWeight(null);
          }
        }

        if (!cellB.getValue()) {
          var sticky = "";
          try {
            var r = targetRow - 1;
            while (r >= 2) {
              var rowVals = sheet.getRange(r, colB, 1, (colE - colB + 1)).getValues()[0]; // B..E
              var isAllEmpty = rowVals.every(function (x) { return String(x || "").trim() === ""; });
              if (isAllEmpty) break;
              var cand = String(rowVals[0] || "").trim();
              if (cand && cand !== placeholderB) { sticky = cand; break; }
              r--;
            }
          } catch (ignore) {}

          if (sticky) {
            cellB.setValue(sticky).setFontColor(null).setFontWeight(null); // δεν αγγίζουμε background
          } else {
            cellB.setValue(placeholderB).setFontColor("#d32f2f").setFontWeight("bold");
          }
        }
        cellD.setNumberFormat(timestampFormat).setValue(new Date());
      }
    }

    if (col === colB) {
      const numRows = e.range.getNumRows();
      const values = e.range.getValues();

      for (let i = 0; i < numRows; i++) {
        const targetRow = row + i;
        const nameCell = sheet.getRange(targetRow, colB);
        const choiceCell = sheet.getRange(targetRow, colC);
        const choiceVal = String(choiceCell.getValue() || "").trim();
        const nameVal = (values[i] && values[i][0] != null) ? String(values[i][0]).trim() : "";

        if (!choiceVal) {
          nameCell.clearContent();
          continue;
        }

        if (nameVal && nameVal !== placeholderB) {
          nameCell.setFontColor(null).setFontWeight(null).setBackground(null);
          try {
            PropertiesService.getDocumentProperties().setProperty('LAST_B_NAME', nameVal);
          } catch (ignore) {}
        }
      }

      try {
        const lastRow = sheet.getLastRow();
        if (lastRow >= 2) {
          const rngAllB = sheet.getRange(2, colB, lastRow - 1, 1);
          const rngAllC = sheet.getRange(2, colC, lastRow - 1, 1);
          const bVals = rngAllB.getValues();
          const cVals = rngAllC.getValues();
          let needWrite = false;
          for (let r = 0; r < bVals.length; r++) {
            const cval = String(cVals[r][0] || "").trim();
            if (!cval && String(bVals[r][0] || "").trim() !== "") {
              bVals[r][0] = ""; // clear content μόνο όπου C είναι κενή
              needWrite = true;
            }
          }
          if (needWrite) rngAllB.setValues(bVals);
        }
      } catch (ignore) {}
    }

    if (col === colE) {
      const numRows = e.range.getNumRows();
      const values = e.range.getValues();

      for (let i = 0; i < numRows; i++) {
        const vE = (values[i] && values[i][0] != null) ? String(values[i][0]).trim() : "";
        if (vE && vE !== placeholderE) {
          e.range.offset(i, 0, 1, 1).setFontColor(null).setFontWeight(null);
        }
      }
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
// _______END OF FILE — CHECKLIST V7.4.6 — Production — 26/11/2025_____
