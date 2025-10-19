*Last updated:* 19/10/2025 – 15:07 (Europe/Athens)

*Last synced with VERSIONS_INDEX.md:* 19/10/2025 – 15:07 (DEV-only)

*Build:* f37c300



*



*



*



*



*



*



*



*



*



*



*



*



*



*

*
*
*
*
*
*
*
*
*Last updated: 19/10/2025 – 12:43 (Europe/Athens)*


// === BLINK V2.0.1 — Hotfix: “server error” exclusion (no throws when no UI) ======
// Aligned with V2.0.0 (15.10.2025) — minimal, safe UI-guard; no behavior change for users.

// 0) Helper — returns Ui or null (prevents exceptions in headless triggers)
function _safeUi_() {
  try { return SpreadsheetApp.getUi(); } catch (e) { return null; }
}

// 1) Patch remindMissingNames: early return if no UI; never throw
function remindMissingNames() {
  const ui = _safeUi_();
  if (!ui) {                     // ✅ Headless context (e.g., time-based trigger)
    console.warn("Blink.remindMissingNames: headless context — skipped without error");
    return;                      //  → No exception → No generic failure email
  }

  const NAME_PROMPT = 'Όνομα Επώνυμο?';
  const COL_B = 2;
  const BLINK_CYCLES = 3;

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
    if (val === NAME_PROMPT) targets.push(rngB.getCell(i + 1, 1));
  }

  if (targets.length === 0) return;

  const cellRefs = targets.map(c => c.getA1Notation()).join(', ');
  const message =
    ' Εντοπίστηκαν ' + targets.length + ' κελιά με ασυμπλήρωτο το "' + NAME_PROMPT + '" !!!\n' +
    ' Κελιά: ' + cellRefs + '\n' +
    ' Παρακαλώ συμπληρώστε το ονοματεπώνυμό σας στα κελιά αυτά στη στήλη B.';

  try {
    PopupLib.showCustomPopup(message, 'error');   // ❗UI-only call, guarded above
    Utilities.sleep(500);
    // blinkCellFontColor_(targets, BLINK_CYCLES); // (αν χρειάζεται, άφησέ το ενεργό)
  } catch (e) {
    console.error("Blink.remindMissingNames popup failed (suppressed):", e);
    // Do not rethrow → avoids Apps Script failure emails
  }
}

// 2) (unchanged) Blink effect — kept as-is; safe to call only in UI context
function blinkCellFontColor_(targetRanges, blinkTimes) {
  for (let i = 0; i < blinkTimes; i++) {
    targetRanges.forEach(r => { r.setFontColor("#f3f3f3"); });
    SpreadsheetApp.flush();
    Utilities.sleep(100);
    targetRanges.forEach(r => { r.setFontColor("#d32f2f"); });
    SpreadsheetApp.flush();
    Utilities.sleep(100);
  }
}
