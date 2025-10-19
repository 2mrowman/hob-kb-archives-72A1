*Build: 7e4e5af*
*Last updated: 19/10/2025 – 08:24 (Europe/Athens)*
/** HoBMastersLib v1.3 — Resilient Template Access + Retry Build (09/10/2025)
 *  Βελτίωση ασφάλειας στην πρόσβαση template sheet και αποφυγή προσωρινών σφαλμάτων.
 */

// format dd/MM
function fmtDate_(d, tz) {
  return Utilities.formatDate(d, tz || Session.getScriptTimeZone(), 'dd/MM');
}

function createNewDay(args) {
  try {
    if (!args || !args.masterId || !args.templateTab) {
      return { ok: false, msg: 'Λείπουν απαιτούμενα args (masterId, templateTab).' };
    }

    const ss = args.ss || SpreadsheetApp.getActiveSpreadsheet();
    const tz = Session.getScriptTimeZone();
    const newName = (args.newName && String(args.newName).trim()) || fmtDate_(new Date(), tz);

    const moveToFront = args.moveToFront !== false;
    const showAlerts = args.showAlerts !== false;
    const copyProt = args.copyProtections !== false;
    const setStamp = args.setLastTabCreated !== false;

    const ui = SpreadsheetApp.getUi();

    // ✅ Αν υπάρχει ήδη, ενημερώνει τον χρήστη
    const existing = ss.getSheetByName(newName);
    if (existing) {
      if (showAlerts) {
        try {
          if (typeof showCustomPopup === 'function') {
            showCustomPopup('ℹ️ Υπάρχει ήδη το σημερινό TAB: "' + newName + '"', 'info');
          } else {
            ui.alert('ℹ️ Υπάρχει ήδη το σημερινό TAB: "' + newName + '"');
          }
        } catch (_) {}
      }
      return { ok: false, msg: 'Υπάρχει ήδη "' + newName + '"', name: newName };
    }

    // ✅ Ανοίγει master και template με retry μηχανισμό (3x)
    let master, tpl;
    for (let attempt = 1; attempt <= 3; attempt++) {
      try {
        master = SpreadsheetApp.openById(args.masterId);
        if (!master) throw new Error('Master not accessible');
        tpl = master.getSheetByName(args.templateTab);
        if (tpl) break;
      } catch (e) {
        console.log(`Attempt ${attempt}/3 failed to access template:`, e);
        Utilities.sleep(500);
      }
    }

    if (!tpl) {
      if (showAlerts) ui.alert('❌ Δεν βρέθηκε template "' + args.templateTab + '" στο master.');
      return { ok: false, msg: 'Δεν βρέθηκε template "' + args.templateTab + '"' };
    }

    // ✅ Αντιγραφή template σε νέο sheet
    const newSheet = tpl.copyTo(ss).setName(newName);
    ss.setActiveSheet(newSheet);
    if (moveToFront) ss.moveActiveSheet(0); else ss.moveActiveSheet(ss.getNumSheets());

    // ✅ Αντιγραφή protections
    if (copyProt) {
      const rangeProtections = tpl.getProtections(SpreadsheetApp.ProtectionType.RANGE) || [];
      rangeProtections.forEach(p => {
        try {
          const r = p.getRange();
          const p2 = newSheet.getRange(r.getA1Notation()).protect();
          p2.setDescription(p.getDescription());
          p2.setWarningOnly(p.isWarningOnly());
          if (!p.isWarningOnly()) {
            try { p2.removeEditors(p2.getEditors()); } catch (_) {}
            const editors = p.getEditors();
            if (editors.length) p2.addEditors(editors);
          }
        } catch (_) {}
      });

      const sheetProtections = tpl.getProtections(SpreadsheetApp.ProtectionType.SHEET) || [];
      if (sheetProtections.length) {
        try {
          const sp = sheetProtections[0];
          const sp2 = newSheet.protect();
          sp2.setDescription(sp.getDescription());
          sp2.setWarningOnly(sp.isWarningOnly());
          if (!sp.isWarningOnly()) {
            try { sp2.removeEditors(sp2.getEditors()); } catch (_) {}
            const editors2 = sp.getEditors();
            if (editors2.length) sp2.addEditors(editors2);
          }
        } catch (_) {}
      }
    }

    // ✅ Timestamp αποθήκευσης
    if (setStamp) {
      try {
        PropertiesService.getDocumentProperties().setProperty('lastTabCreated', new Date().toISOString());
      } catch (_) {}
    }

    // ✅ Popup ή Toast για επιτυχία
    if (showAlerts) {
      try {
        if (typeof showCustomPopup === 'function') {
          showCustomPopup('✅ Δημιουργήθηκε το "' + newName + '"', 'success');
        } else {
          ui.alert('✅ Δημιουργήθηκε "' + newName + '"');
        }
      } catch (_) {}
    } else {
      ss.toast('✅ Δημιουργήθηκε "' + newName + '"', 'OK', 3);
    }

    return { ok: true, msg: 'OK ' + newName, name: newName };
  } catch (err) {
    try { SpreadsheetApp.getUi().alert('⚠️ Σφάλμα: ' + err); } catch (_) {}
    return { ok: false, msg: 'Σφάλμα: ' + err };
  }
}
