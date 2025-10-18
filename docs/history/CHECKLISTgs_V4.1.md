// ✅ CHECKLIST V4.1 - Updated 22.09.2025

/***** HoB Masters – ΡΥΘΜΙΣΕΙΣ ΚΑΤΑΣΤΗΜΑΤΟΣ *****/
const HOB_MASTERS_FILE_ID = "1j4xXEVYhVTzg57nhV-19V16F7AeoUjf6tJimFx4KOPI"; // κοινό για όλους
const TEMPLATE_TAB        = "Master2";

function showCustomPopup(message, type, callback) {
  let color, title, icon;
  if (type === "success")      { color = "#4CAF50"; title = "✅ Επιτυχία!";      icon = "✅"; }
  else if (type === "warning") { color = "#FFC107"; title = "⚠️ Προειδοποίηση!"; icon = "⚠️"; }
  else if (type === "error")   { color = "#F44336"; title = "❌ Προσοχή!";        icon = "❌"; }
  else                         { color = "#2196F3"; title = "ℹ️ Πληροφορία";     icon = "ℹ️"; }

  const html = HtmlService.createHtmlOutput(`
    <div style="font-family: Arial, sans-serif; text-align:center; width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center;">
      <div style="width: 600px; background:#fff; border:2px solid #ccc; box-shadow:5px 5px 15px rgba(0,0,0,25); border-radius:14px; overflow:hidden;">
        <div style="background:${color}; color:#fff; padding:14px 16px; font-size:20px; font-weight:700; text-align:left;">
          ${title}
        </div>
        <div style="padding:28px 30px; background:#fff; color:#000; text-align:center; font-size:17px; line-height:1.5;">
          <div style="margin-bottom:18px; font-weight:700; color:${color}; text-align:center;">
            ${icon} ${title}
          </div>
          <div style="margin: 0 auto 18px auto; max-width:520px;">${message}</div>
          <button style="padding:10px 22px; font-size:16px; background:${color}; color:#fff; border:none; border-radius:6px; cursor:pointer;"
                  onclick="google.script.run.withSuccessHandler(() => google.script.host.close()).onPopupClosed()">OK</button>
        </div>
      </div>
    </div>
  `).setWidth(640).setHeight(360);

  // Save callback to global
  globalThis.__popupCallback__ = callback;
  SpreadsheetApp.getUi().showModalDialog(html, title);
}

/**
 * 📍 Εκτελείται μόλις κλείσει το modal → καλεί το callback
 */
function onPopupClosed() {
  if (typeof globalThis.__popupCallback__ === "function") {
    try {
      globalThis.__popupCallback__();
    } catch (e) {
      console.error("⚠️ Callback execution error:", e);
    } finally {
      globalThis.__popupCallback__ = undefined;
    }
  }
}



function createNewDay_AUTO() {
  const lock = LockService.getScriptLock();

  // 🔒 Αν τρέχει ήδη το script, απλώς σταμάτα (αθόρυβα)
  if (!lock.tryLock(10000)) return;

  const todayName = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "dd/MM");
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const existingSheet = ss.getSheets().find(sheet => sheet.getName() === todayName);

  if (existingSheet) {
  lock.releaseLock();
  showCustomPopup(
    "✅ Υπάρχει ήδη η σημερινή ημέρα (" + todayName + ").<br><br>" +
    "📋 Το αρχείο είναι έτοιμο για συμπλήρωση.",
    "success"
  );
  return;
}


  try {
    // 🔔 Εμφάνισε popup “σε εξέλιξη”
    showCustomPopup("⏳ Η εργασία δημιουργίας νέας ημέρας είναι σε εξέλιξη...", "info");

    // ⚙️ Ξεκίνα δημιουργία
    createNewDayFrom_(TEMPLATE_TAB);
  } catch (error) {
    console.error("❌ Σφάλμα κατά τη δημιουργία νέας ημέρας:", error);
    showCustomPopup("❌ Παρουσιάστηκε σφάλμα κατά τη δημιουργία της νέας ημέρας.", "error");
  } finally {
    lock.releaseLock();
  }
}



function colorAllPlaceholdersB_(sheetName) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName(sheetName);
  if (!sh) return;
  const lastRow = sh.getLastRow();
  if (lastRow < 2) return;
  const rng = sh.getRange(2, 2, lastRow - 1, 1);
  const vals = rng.getValues();
  const colors = rng.getFontColors();
  const weights = rng.getFontWeights();

  for (let i = 0; i < vals.length; i++) {
    if (String(vals[i][0]).trim() === "Όνομα Επώνυμο?") {
      colors[i][0]  = "#d32f2f";
      weights[i][0] = "bold";
    }
  }
  rng.setFontColors(colors).setFontWeights(weights);
}

function createNewDayFrom_(tabName) {
  const res = HoBMastersLib.createNewDay({
    masterId: HOB_MASTERS_FILE_ID,
    templateTab: tabName,
    moveToFront: true,
    showAlerts: false,
    copyProtections: true,
    setLastTabCreated: true
  });

  if (!res.ok) {
    showCustomPopup("❌ " + res.msg, "error");
    return;
  }

  try { hideLocalMasterIfVisible_(); } catch (_){}
  try { colorAllPlaceholdersB_(res.name); } catch (_){ }

  const todayName = res.name || Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "dd/MM");
  showCustomPopup(
    '✅ Το νέο φύλλο "<strong>' + todayName + '</strong>" δημιουργήθηκε επιτυχώς!<br><br>' +
    '📌 <strong>Καλή συνέχεια!</strong><br>' +
    '📝 Μην ξεχνάτε να συμπληρώνετε το ονοματεπώνυμό σας στα κελιά της στήλης <strong>B</strong> με την ολοκλήρωση κάθε εργασίας.',
    "success"
  );
}


/** =======================  AUTO CODE  ======================= */

/** Μενού & μήνυμα ανοίγματος */
function onOpen(e) {
  const ui = SpreadsheetApp.getUi();
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const storeName = ss.getName();
  const now = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'dd/MM/yyyy - HH:mm:ss');
  const userEmail = Session.getEffectiveUser().getEmail();
  const ownerEmail = "hobdeks@gmail.com";

  const menu = ui.createMenu('🗂️ HoB - Menu');
  menu
    .addItem('📦 ΝΕΕΣ ΠΑΡΑΛΑΒΕΣ – ΕΛΛΕΙΨΕΙΣ', 'openNeaParalaviForm')
    .addItem('🛍️ ΣΑΚΟΥΛΕΣ ΑΓΟΡΩΝ – ΠΑΡΑΓΓΕΛΙΑ', 'openSakoulesForm')
    .addItem('💳 CREDIT CARD& TAX FREE-ΕΓΧΕΙΡΙΔΙΟ', 'openForm_CreditTAXFree')
    .addItem('📭 ΕΛΛΕΙΨΕΙΣ', 'openForm_Elleipseis')
    .addItem('💶 ΑΛΛΑΓΕΣ ΤΙΜΩΝ', 'openForm_AllagesTimon')
    .addItem('⚠️ ΕΛΑΤΤΩΜΑΤΙΚΟ ΠΡΟΪΟΝ', 'openForm_ElattomatikosProion')
    .addItem('🔎 CHECK ΚΩΔΙΚΟΥ', 'openForm_CheckKodikou')
    .addItem('📊 ΑΣΤΟΧΙΑΣ ΠΑΡΑΓΓΕΛΙΑΣ', 'openForm_AstoxiasParaggelias')
    .addItem('🚚 ΑΠΟΣΤΟΛΕΣ ΓΕΝ. ΤΑΧΥΔΡΟΜΙΚΗΣ', 'openForm_GenikiTaxydromiki')
    .addItem('📧 ΕΤΑΙΡΙΚΑ EMAIL HoB', 'openForm_EmailsList');

  if (userEmail === ownerEmail) {
    menu.addSeparator()
      .addSubMenu(
        ui.createMenu('🛠️ Εργαλεία Ιδιοκτήτη')
          .addItem('📅 Δημιουργία Νέας Ημέρας', 'createNewDay_AUTO') // ΝΕΟ flow
          .addItem('🧬 Αντίγραφο+Καθάρισμα Αρχείου', 'automatedDuplicateAndCleanup')
          .addItem('👉🏻🗑️ Delete All TABS & Show MASTER', 'showMasterAndDeleteOthers')
          .addItem('🔴 Check Invalid (Όνομα Επώνυμο)', 'remindMissingNames') 
          .addItem('💎 Clear Notes', 'clearAllNotes')
      );
  }

  menu.addToUi();

    // 📌 Κρύψιμο του MASTER κατά το άνοιγμα
var masterSheet = ss.getSheetByName('MASTER');
if (masterSheet && !masterSheet.isSheetHidden()) {
masterSheet.hideSheet();
  }

  // 🔔 Popup αναμονής
  if (userEmail === ownerEmail) {
    showCustomPopup("⏳ Η εργασία δημιουργίας νέας ημέρας είναι σε εξέλιξη...", "info");
  }
}


function clearAllNotes() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet(); // Παίρνει το ενεργό φύλλο
  var range = sheet.getDataRange(); // Παίρνει όλη την περιοχή με δεδομένα
  range.clearNote(); // Διαγράφει όλες τις σημειώσεις στα κελιά
  SpreadsheetApp.getUi().alert("✅ Όλες οι σημειώσεις διαγράφηκαν επιτυχώς!");
}


/** TIMESTAMP helper */
function TIMESTAMP() {
  return Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'HH:mm:ss.000" - "dd/MM');
}

/** Αυτόματη καταγραφή ώρας σε στήλη D & χειρισμός placeholders στη Β */
function onEdit(e) {
  try {
    const sheet = e.range.getSheet();
    const sheetName = sheet.getName();
    const col = e.range.getColumn();
    const row = e.range.getRow();
    const val = e.range.getValue();
    const timestampFormat = 'HH:mm:ss.000" - "dd/MM';

    const excludedSheets = ["START", "MASTER"];
    if (excludedSheets.includes(sheetName)) return;

    const colB = 2, colC = 3, colD = 4;

    // Αν αλλάζει η C και η B είναι κενή → βάλε placeholder (κόκκινο/bold)
    if (col === colC) {
      const cellB = sheet.getRange(row, colB);
      if (!cellB.getValue()) {
        cellB.setValue("Όνομα Επώνυμο?")
             .setFontColor("#d32f2f")
             .setFontWeight("bold");
      }
      // και γράψε ώρα στη D
      const cellD = sheet.getRange(row, colD);
      cellD.setNumberFormat(timestampFormat).setValue(new Date());
    }

    // Αν έγραψε όνομα στη B → αφαίρεσε κόκκινο/bold
    if (col === colB && val && val !== "Όνομα Επώνυμο?") {
  e.range.setFontColor(null).setFontWeight(null).setBackground(null);
}

  } catch (error) {
    console.error("❌ Σφάλμα στο onEdit:", error);
  }
}
