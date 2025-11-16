*Last updated:* 16/11/2025 - 06:50 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 16/11/2025 - 06:50 (DEV-only)
*Build:* 475d0eb

// ====ADMIN TOOLS=====
// INTEGRITY SELF-CHECK
function runIntegrityCheck() {
  const fn = [
    "onOpen",
    "onOpen_Installed",
    "runTodayInit_",
    "getTemplateTabFromHoBMasters_",
    "hideLocalMasterIfVisible_",
    "loadMenuDynamically",
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

function _sanity_popup() {
  Logger.log('PopupLib = ' + typeof PopupLib);   // expect: 'object' ή 'function'
  Logger.log('AdminToolsLib = ' + typeof AdminToolsLib);
  PopupLib.showToast('Popup OK from main');      // πρέπει να εμφανιστεί toast
}
function _sanity_admin_calls_popup() {
  // Καλεί internal που χρησιμοποιεί PopupLib (π.χ. reminder)
  AdminToolsLib.remindMissingNames(); // να γράψει toast, όχι dialog, αν είναι time-driven
}

function testLibExists() {
  SpreadsheetApp.getActive().toast(
    'AdminToolsLib=' + typeof AdminToolsLib +
    ' | MenuLib=' + typeof MenuLib +
    ' | PopupLib=' + typeof PopupLib +
    ' | HoBMastersLib=' + typeof HoBMastersLib,
    'Libs', 10);
}

