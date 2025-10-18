*Build: 6a82f18*
*Last updated: 18/10/2025 – 11:34 (Europe/Athens)*
// =====================================================================================
// BLINK V2.0.0 — Final Production Build – 15.10.2025 – 17:53
// =====================================================================================

/***** ΡΥΘΜΙΣΕΙΣ *****/
const NAME_PROMPT = 'Όνομα Επώνυμο?';
const COL_B = 2;
const BLINK_CYCLES = 3; // Αριθμός εναλλαγών (π.χ. Γκρι/Κόκκινο 3 φορές)

/**
 * 📌 Εντοπίζει όλα τα "Όνομα Επώνυμο?" στη στήλη B του ενεργού φύλλου
 * και εμφανίζει custom popup. Όταν ο χρήστης πατήσει OK, κάνει blinking.
 * Δεν τρέχει UI ενέργειες αν το script εκτελείται χωρίς χρήστη (π.χ. από trigger).
 */
function remindMissingNames() {
  // ✅ Αν το script τρέχει από background (π.χ. time trigger), δεν συνεχίζουμε
  try {
    SpreadsheetApp.getUi(); // Αν δεν πετάξει σφάλμα, είμαστε σε UI context
  } catch (e) {
    console.warn("❌ Χωρίς UI context – τερματισμός remindMissingNames");
    return;
  }

  const sh = SpreadsheetApp.getActiveSheet();
  const name = sh.getName();
  if (["START", "MASTER"].includes(name)) return;

  const last = sh.getLastRow();
  if (last < 2) return;

  const rngB = sh.getRange(2, COL_B, last - 1, 1);
  const vals = rngB.getValues();
  const targets = [];

  for (let i = 0; i < vals.length; i++) {
    const val = String(vals[i][0] || "").trim();
    if (val === NAME_PROMPT) {
      targets.push(rngB.getCell(i + 1, 1));
    }
  }

  if (targets.length > 0) {
    const cellRefs = targets.map(c => c.getA1Notation()).join(', ');
    const message = '🚨 Εντοπίστηκαν ' + targets.length + ' κελιά με ασυμπλήρωτο το "<strong>' + NAME_PROMPT + '</strong>" !!!<br><br>' +
      '📍 Κελιά: <strong>' + cellRefs + '</strong><br><br>' +
      '📝 Παρακαλώ συμπληρώστε το ονοματεπώνυμό σας στα κελιά αυτά στη στήλη <strong>B</strong>.';

    PopupLib.showCustomPopup(message, 'error');
    Utilities.sleep(500); // 📌 για σιγουριά πριν το blinking
  //  blinkCellFontColor_(targets, BLINK_CYCLES);
  }
}

/**
 * 🔁 Εναλλάσσει το χρώμα γραμματοσειράς ανάμεσα σε ανοιχτό γκρι και κόκκινο.
 * Τελειώνει πάντα με κόκκινο (προεπιλεγμένο χρώμα προειδοποίησης).
 */
function blinkCellFontColor_(targetRanges, blinkTimes) {
  for (let i = 0; i < blinkTimes; i++) {
    targetRanges.forEach(r => {
      r.setFontColor("#f3f3f3"); // ⚪ Ανοιχτό Γκρι
    });
    SpreadsheetApp.flush();
    Utilities.sleep(100);

    targetRanges.forEach(r => {
      r.setFontColor("#d32f2f"); // 🔴 Κόκκινο
    });
    SpreadsheetApp.flush();
    Utilities.sleep(100);
  }
}
