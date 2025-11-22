// onEdit handler + TIMESTAMP helper V4
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
    const colB = 2, colC = 3, colD = 4, colE = 5;
    const placeholderB = "Όνομα Επώνυμο?";
    const placeholderE = "Γράψτε το σχόλιο σας εδώ";

    if (col === colC) {
      const cellB = sheet.getRange(row, colB);
      const cellD = sheet.getRange(row, colD);
      const cellE = sheet.getRange(row, colE);
      const v = (e.value == null) ? "" : String(e.value).trim();

      if (v === "") {
        cellB.clearContent().setFontColor(null).setFontWeight(null);
        cellD.clearContent();
        cellE.clearContent().setFontColor(null).setFontWeight(null);
        return;
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
          var r = row - 1;
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

      // Timestamp στη Δ
      cellD.setNumberFormat(timestampFormat).setValue(new Date());
    }

    if (col === colB) {
      const cellC = sheet.getRange(row, colC);
      const vC = String(cellC.getValue() || "").trim();

      // Αν δεν έχει γίνει επιλογή στη C, καθάρισε το όνομα στη B
      // Στόχος: να μην παραμένουν εγγραφές ονόματος χωρίς αντίστοιχη επιλογή στη στήλη C.
      if (!vC) {
        e.range.clearContent();
        return;
      }

      if (val && val !== "Όνομα Επώνυμο?") {
        e.range.setFontColor(null).setFontWeight(null).setBackground(null);
        try {
          PropertiesService.getDocumentProperties().setProperty('LAST_B_NAME', String(val).trim());
        } catch (ignore) {}
      }
    }

    if (col === colE) {
      const vE = (e.value == null) ? "" : String(e.value).trim();
      if (vE && vE !== placeholderE) {
        e.range.setFontColor(null).setFontWeight(null);
      }
    }
  } catch (err) {
    console.error("❌ Σφάλμα στο onEdit:", err);
  }
}
