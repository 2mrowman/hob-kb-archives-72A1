*Last updated:* 22/10/2025 - 13:40 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 22/10/2025 - 13:40 (DEV-only)
*Build:* 0e80371

//
// Version: V2.0.0R – 07/10/2025 – Native Fallback Edition (PopupLib): custom modal όπου είναι εφικτό + αυτόματο fallback σε native alert/toast όταν δεν υπάρχει ενεργό UI context
/**
 * PopupLib – Version 2.0.0
 * Στόχος: Να παραμείνει 100% συμβατό με τα υπάρχοντα calls (showCustomPopup, showInfoMessage, showWarningMessage, showErrorMessage, showSuccessMessage, testAllPopupsFromMenu)
 * και να προσθέσει ΑΥΤΟΜΑΤΟ fallback:
 * 1) Προσπάθεια για custom modal (HtmlService + showModalDialog)
 * 2) Αν δεν υπάρχει ενεργό UI context → native alert (SpreadsheetApp.getUi().alert)
 * 3) Αν ούτε alert επιτρέπεται → toast (Spreadsheet.toast)
 * 4) Πάντα σεβόμαστε onClose callback (αν δοθεί), ακόμα και στο fallback
 */
// ✅ Functions included in this version (✅ = νέο/αλλαγμένο σε σχέση με V1.9.4):
//  showCustomPopup
//  showInfoMessage
//  showWarningMessage
//  showErrorMessage
//  showSuccessMessage
// ✅ testAllPopupsFromMenu
// ✅ isUiAvailable_
// ✅ stripHtml_
// ✅ getPopupTitle_
// ✅ generateHtml_

/**
 * ΕΝΙΑΙΟ API – ΜΗΝ αλλάζετε signatures για συμβατότητα με παλιό κώδικα.
 * @param {string} message – επιτρέπεται HTML
 * @param {"info"|"warning"|"error"|"success"} type
 * @param {string=} onClose – (προαιρετικό) όνομα global function για κλήση μετά το κλείσιμο
 */
function showCustomPopup(message, type, onClose) {
  // Προσπαθούμε να δείξουμε custom modal αν υπάρχει ενεργό UI
  try {
    if (isUiAvailable_()) {
      var html = HtmlService.createHtmlOutput(generateHtml_(message, type, onClose))
        .setWidth(420)
        .setHeight(240); // ίδιο προφίλ διαλόγου με V1.9.4 (ελαφρά προσαύξηση ύψους για headers)
      SpreadsheetApp.getUi().showModalDialog(html, getPopupTitle_(type));
      return;
    }
  } catch (err1) {
    // Θα δοκιμάσουμε native fallback
    try { Logger.log("PopupLib: custom modal not available: " + err1); } catch (_) {}
  }

  // Fallback #1: Native alert (blocking) – αφαιρούμε HTML tags για καθαρό κείμενο
  var title = getPopupTitle_(type);
  var plain = stripHtml_(message);
  try {
    var ui = SpreadsheetApp.getUi();
    ui.alert(title + "\n\n" + plain);
    // Κλήση onClose (αν υπάρχει) ακόμη και μετά από native alert
    if (onClose && typeof this[onClose] === "function") {
      try { this[onClose](); } catch (cbErr1) { Logger.log("PopupLib: onClose after alert failed: " + cbErr1); }
    }
    return;
  } catch (err2) {
    try { Logger.log("PopupLib: native alert not available: " + err2); } catch (_) {}
  }

  // Fallback #2: Toast – non-blocking, πάντα διαθέσιμο όταν υπάρχει Active Spreadsheet
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    if (ss) {
      ss.toast(plain, title, 5);
      if (onClose && typeof this[onClose] === "function") {
        try { this[onClose](); } catch (cbErr2) { Logger.log("PopupLib: onClose after toast failed: " + cbErr2); }
      }
      return;
    }
  } catch (err3) {
    try { Logger.log("PopupLib: toast not available: " + err3); } catch (_) {}
  }

  // Τελικό καταφύγιο: logging μόνο
  try { Logger.log("PopupLib: no UI channel available. Title=" + title + " | Message=" + plain); } catch (_) {}
  if (onClose && typeof this[onClose] === "function") {
    try { this[onClose](); } catch (cbErr3) {}
  }
}

/** Βολικές συναρτήσεις (συμβατές με V1.9.4) */
function showInfoMessage(message, onClose)    { showCustomPopup(message, "info", onClose); }
function showWarningMessage(message, onClose) { showCustomPopup(message, "warning", onClose); }
function showErrorMessage(message, onClose)   { showCustomPopup(message, "error", onClose); }
function showSuccessMessage(message, onClose) { showCustomPopup(message, "success", onClose); }

/**
 * Demo/QA – τρέχει διαδοχικά όλα τα popups με onClose callbacks για επαλήθευση ροής
 * (Συμβατό με το spirit του V1.9.4 – ίδιες λεζάντες/σειρά, απλώς πιο ανθεκτικό σε fallback)
 */
function testAllPopupsFromMenu() {
  showErrorMessage("❌ Δοκιμή Error popup<br><small>(V2.0.0 – Native Fallback Edition)</small>", "POPUP_TEST_info_");
}
function POPUP_TEST_info_() {
  showInfoMessage("ℹ️ Δοκιμή Info popup<br><small>Έλεγχος διαδοχικής ροής</small>", "POPUP_TEST_success_");
}
function POPUP_TEST_success_() {
  showSuccessMessage("✅ Δοκιμή Success popup<br><small>Με native fallback όπου απαιτείται</small>", "POPUP_TEST_warning_");
}
function POPUP_TEST_warning_() {
  showWarningMessage("⚠️ Δοκιμή Warning popup<br><small>Τέλος ακολουθίας</small>");
}

/* =========================
 * Internal utilities
 * ========================= */

/**
 * Επιστρέφει true όταν μπορούμε να δείξουμε custom modal:
 * - Υπάρχει ενεργό Spreadsheet
 * - Δεν ρίχνει σφάλμα σε απλές κλήσεις (permission/sandbox)
 */
function isUiAvailable_() {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    if (!ss) return false;
    // Μικρό permission probe
    ss.getName();
    // Απόπειρα πρόσβασης σε UI (αν σπάσει εδώ, θα πιαστεί)
    SpreadsheetApp.getUi();
    return true;
  } catch (_) {
    return false;
  }
}

/** Καθαρίζει HTML για χρήση σε native alert/toast */
function stripHtml_(html) {
  if (!html) return "";
  return String(html).replace(/<[^>]*>/g, "").replace(/&nbsp;/g, " ").trim();
}

/** Τίτλοι ανά τύπο (ίδιο naming με 1.9.4 – μην αλλάξετε για συνέπεια) */
function getPopupTitle_(type) {
  switch (type) {
    case "success": return "Επιτυχία!";
    case "error":   return "Σφάλμα!";
    case "warning": return "Προσοχή!";
    case "info":    return "Πληροφορία";
    default:        return "Ειδοποίηση";
  }
}

/** Δημιουργεί HTML για custom modal (ίδιο αισθητικό προφίλ με V1.9.4) */
function generateHtml_(message, type, onClose) {
  var colors = {
    success: "#4CAF50",
    error:   "#d32f2f",
    warning: "#F9A825",
    info:    "#1976D2",
    default: "#424242"
  };
  var color = colors[type] || colors.default;
  var emoji = (type === "success" ? "✅" :
               type === "error"   ? "❌" :
               type === "warning" ? "⚠️" :
               type === "info"    ? "ℹ️" : "🔔");

  var safeMessage = String(message || "");
  var closeJs = onClose ? ("google.script.run.withFailureHandler(function(e){console && console.log(e);})." +
                           onClose + "();") : "";

  var html =
'<!DOCTYPE html><html><head><base target="_top"><meta charset="UTF-8">' +
'<style>' +
'body{font-family:Arial,system-ui,Segoe UI,Roboto; margin:0; padding:0;}' +
'.wrap{border:1px solid #eee; border-radius:12px; overflow:hidden; box-shadow:0 6px 18px rgba(0,0,0,0.12);}' +
'.hdr{background:'+color+'; color:#fff; padding:10px 14px; font-weight:600; display:flex; align-items:center; justify-content:space-between;}' +
'.hdr .ttl{display:flex; gap:8px; align-items:center;}' +
'.hdr .x{cursor:pointer; font-weight:700;}' +
'.cnt{padding:16px 18px; font-size:14px; line-height:1.5;}' +
'</style></head><body>' +
'<div class="wrap">' +
'  <div class="hdr">' +
'    <div class="ttl"><span>'+emoji+'</span><span>'+getPopupTitle_(type)+'</span></div>' +
'    <div class="x" id="xbtn">✖</div>' +
'  </div>' +
'  <div class="cnt">'+ safeMessage +'</div>' +
'</div>' +
'<script>' +
'  function closeDlg(){ ' + closeJs + ' google.script.host.close(); }' +
'  document.getElementById("xbtn").addEventListener("click", closeDlg);' +
'  // close on ESC' +
'  document.addEventListener("keydown", function(e){ if(e.key==="Escape"){ closeDlg(); }});' +
'</script>' +
'</body></html>';

  return html;
}
