*Last updated:* 19/10/2025 – 13:30 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 19/10/2025 – 13:30 (DEV-only)
*Build:* 1be131b
*
*
*
*
*Last updated: 19/10/2025 – 12:43 (Europe/Athens)*
// =====================================================================================
// AutoDupl_File&DeleteTabs V1.0.0 — Final Production Build – 10.04.2025 – 12:50
// =====================================================================================

function automatedDuplicateAndCleanup() {
  try {
    Logger.log('🚀 Έναρξη διαδικασίας.');

    // 🔹 Ορισμός του φακέλου προορισμού και του αρχικού αρχείου
    var folderId = "1ryekzwj3owrxXSjt7ty0veKniq9TQq2K"; // ➜ Αντικατέστησε με το ID του φακέλου
    var originalFileId = "1ZqOvmW6TZxFD9LkGknSXlT-gO6fBqzGDDZKfU3mQOuI"; // ➜ Αντικατέστησε με το ID του αρχικού αρχείου

    var folder = DriveApp.getFolderById(folderId);
    var originalFile = DriveApp.getFileById(originalFileId);
    
    // 🔹 Ανάκτηση του ονόματος του αρχείου και αφαίρεση "Copy of" και "of"
    var originalFileName = originalFile.getName().replace(/Copy of |of /gi, "").trim();
    
    // 🔹 Υπολογισμός μήνα και έτους για την ονομασία YYMM
    var today = new Date();
    var year = today.getFullYear().toString().slice(-2);
    var month = today.getMonth();
    if (month === 0) {
      month = 12;
      year = (parseInt(year) - 1).toString();
    }
    var yymm = year + ("0" + month).slice(-2);

    // 🔹 Δημιουργία αντιγράφου με το νέο όνομα
    var newFileName = yymm + "_" + originalFileName;
    var newFile = originalFile.makeCopy(newFileName, folder);

    // 🔹 Αφαίρεση όλων των χρηστών εκτός του ιδιοκτήτη
    removeAllUsersExceptOwner(newFile);

    Logger.log('✅ Το αρχείο αντιγράφηκε ως: ' + newFileName);

    // 🔹 Εμφάνιση χειροκίνητης οδηγίας για διαγραφή script στο νέο αρχείο
    Logger.log("⚠️ ΠΡΟΣΟΧΗ: Το Apps Script μέσα στο αντίγραφο δεν μπορεί να διαγραφεί αυτόματα.");
    Logger.log("📌 ΜΠΟΡΕΙΣ ΝΑ ΤΟ ΔΙΑΓΡΑΨΕΙΣ ΧΕΙΡΟΚΙΝΗΤΑ ΑΝΟΙΓΟΝΤΑΣ ΤΟ ΑΝΤΙΓΡΑΦΟ ΚΑΙ ΠΗΓΑΙΝΟΝΤΑΣ ΣΤΟ Extensions > Apps Script > Διαγραφή κώδικα.");

    // 🔹 Εκτέλεση της διαδικασίας διατήρησης μόνο του φύλλου "MASTER"
    showMasterAndDeleteOthers();

    Logger.log("✅ Επιτυχής δημιουργία αντιγράφου και καθαρισμός φύλλων!");
  } catch (error) {
    Logger.log('⚠️ Σφάλμα: ' + error.toString());
  }
}

// 📌 Διαγραφή όλων των χρηστών εκτός από τον ιδιοκτήτη
function removeAllUsersExceptOwner(file) {
  var editors = file.getEditors();
  var owner = file.getOwner();

  if (editors && editors.length > 0) {
    editors.forEach(function(user) {
      if (user.getEmail() !== owner.getEmail()) {
        file.removeEditor(user);
      }
    });

    Logger.log("✅ Όλοι οι χρήστες εκτός του ιδιοκτήτη αφαιρέθηκαν από το αρχείο: " + file.getName());
  } else {
    Logger.log("ℹ️ Δεν βρέθηκαν επιπλέον συντάκτες για το αρχείο: " + file.getName());
  }
}

// 📌 Διαγραφή όλων των φύλλων εκτός από το "MASTER"
function showMasterAndDeleteOthers() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var masterSheet = ss.getSheetByName("MASTER");

  if (!masterSheet) {
    Logger.log("❌ Δεν βρέθηκε το φύλλο 'MASTER'.");
    return;
  }

  // 📌 Εμφάνιση του MASTER
  masterSheet.showSheet();

  // 📌 Διαγραφή όλων των άλλων φύλλων
  var sheets = ss.getSheets();
  sheets.forEach(function(sheet) {
    if (sheet.getName() !== "MASTER") {
      ss.deleteSheet(sheet);
    }
  });

  Logger.log("✅ Το 'MASTER' εμφανίστηκε και όλα τα άλλα φύλλα διαγράφηκαν!");
}
