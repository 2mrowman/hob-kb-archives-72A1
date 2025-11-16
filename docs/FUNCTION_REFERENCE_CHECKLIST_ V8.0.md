*Last updated:* 16/11/2025 - 05:38 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 16/11/2025 - 05:38 (DEV-only)
*Build:* 62ee83c

# 📘 FUNCTION REFERENCE - CHECKLIST V8.0
This section provides a complete reference for all functions in the CHECKLIST automation system. It is designed to be the single source of truth for developers and the AI model, detailing where each function is located, its purpose, and its dependencies.
---
## 📂 Function Index by Location
### Scripts (Main Project)
| Function Name | Description | Calls |
|---|---|---|
| `_safeUi_()` | (Blink.gs) Ensures a safe UI environment before execution. | - |
| `automatedDuplicateAndCleanup()` | (AutoDupl_FileDeleteTabs.gs) Triggers the cleanup process. | - |
| `blinkCellFontColor_()` | (Blink.gs) Blinks the font color of a cell for user feedback. | - |
| `createNewDay()` | (Checklist.gs) Wrapper to create a new day. | `AdminToolsLib.createNewDay_AUTO()` |
| `getTemplateTabFromHoBMasters_()` | (MenuLib.md) Retrieves the template tab name from HoB Masters. | - |
| `loadMenuDynamically()` | (Checklist.gs) Loads the dynamic menu on spreadsheet open. | `MenuLib.loadMenuDynamically()` |
| `onOpen()` | (Checklist.gs) Main trigger when the spreadsheet is opened. | `loadMenuDynamically()`, `createNewDay()` |
| `openForm_AllagesTimon()` | (MenuLib.md) Opens the "Allages Timon" form. | `openUrlInNewTab()` |
| `openForm_AstoxiasParaggelias()`| (MenuLib.md) Opens the "Astoxias Paraggelias" form. | `openUrlInNewTab()` |
| `openForm_CheckKodikou()` | (MenuLib.md) Opens the "Check Kodikou" form. | `openUrlInNewTab()` |
| `openForm_CreditTAXFree()` | (MenuLib.md) Opens the "Credit/TAX Free" form. | `openUrlInNewTab()` |
| `openForm_ElattomatikosProion()` | (Menu_Lib.md) Opens the "Elattomatikos Proion" form. | `openUrlInNewTab()` |
| `openForm_Elleipseis()` | (MenuLib.md) Opens the "Elleipseis" form. | `openUrlInNewTab()` |
| `openForm_EmailsList()` | (MenuLib.md) Opens the "Emails List" form. | `openUrlInNewTab()` |
| `openForm_GenikiTaxydromiki()` | (MenuLib.md) Opens the "Geniki Taxydromiki" form. | `openUrlInNewTab()` |
| `openNeaParalaviForm()` | (MenuLib.md) Opens the "Nea Paralavi" form. | `openUrlInNewTab()` |
| `openSakoulesForm()` | (MenuLib.md) Opens the "Sakoules" form. | `openUrlInNewTab()` |
| `openUrlInNewTab()` | (MenuLib.md) Helper function to open a URL in a new tab. | `HtmlService.createHtmlOutput()` |

### Libraries

| Function Name | Library | Description | Calls |
|---|---|---|---|
| `_safeUi_()` | AdminToolsLib | Ensures a safe UI environment. | - |
| `automatedDuplicateAndCleanup()` | AdminToolsLib | Performs the automated duplication and cleanup. | - |
| `automatedDuplicateAndCleanupFromMenu()` | AdminToolsLib | Menu item to trigger cleanup. | `PopupLib.showErrorMessage()` |
| `automatedDuplicateAndCleanupFromMenu()` | MenuLib | Menu wrapper for cleanup. | `AdminToolsLib.remindMissingNames()` |
| `clearAllNotes()` | AdminToolsLib | Clears all notes from the sheet. | - |
| `clearAllNotesFromMenu()` | MenuLib | Menu wrapper for clearing notes. | `AdminToolsLib.clearAllNotes()` |
| `createNewDay_AUTO()` | AdminToolsLib | Core logic for creating a new day. | `HoBMastersLib.getTemplateTabFromHoBMasters_()` |
| `createNewDayFromMenu()` | MenuLib | Menu wrapper for creating a new day. | `AdminToolsLib.createNewDay_AUTO()` |
| `debugUserContext()` | AdminToolsLib | Logs user context for debugging. | - |
| `debugUserContextFromMenu()` | MenuLib | Menu wrapper for debugging context. | `AdminToolsLib.debugUserContext()` |
| `getMenuItemsFromSheet()` | MenuLib | Reads menu items from the settings sheet. | - |
| `getOwnerEmail()` | MenuLib | Returns the owner's email address. | - |
| `getTemplateTabFromHoBMasters_()` | HoBMastersLib | Retrieves template tab from the master file. | - |
| `hideAllTabsExceptMasters()` | AdminToolsLib | Hides all tabs except the master tabs. | - |
| `loadMenuDynamically()` | MenuLib | Core logic for loading the dynamic menu. | `getMenuItemsFromSheet()` |
| `onOpen_createNewDay_AUTO_Local()` | AdminToolsLib | Local version of the new day creation logic. | `PopupLib.showCustomPopup()` |
| `POPUP_TEST_info_()` | PopupLib | Test function for info popups. | `showCustomPopup()` |
| `POPUP_TEST_success_()` | PopupLib | Test function for success popups. | `showCustomPopup()` |
| `POPUP_TEST_warning_()` | PopupLib | Test function for warning popups. | `showCustomPopup()` |
| `remindMissingNames()` | AdminToolsLib | Reminds users to fill in missing names. | `PopupLib.showCustomPopup()` |
| `remindMissingNamesFromMenu()` | MenuLib | Menu wrapper for reminding missing names. | `AdminTools_Lib.remindMissingNames()` |
| `showCustomPopup()` | PopupLib | Displays a custom popup message to the user. | - |
| `showMasterAndDeleteOthers()` | AdminToolsLib | Shows the master tab and deletes others. | `hideAllTabsExceptMasters()` |
| `showMasterAndDeleteOthersFromMenu()` | MenuLib | Menu wrapper for showing master tab. | `AdminToolsLib.showMasterAndDeleteOthers()` |
| `testAllPopupsFromMenu()` | MenuLib | Menu wrapper to test all popups. | `PopupLib.testAllPopupsFromMenu()` |
| `testLibExists()` | AdminToolsLib | Tests if the library exists. | `PopupLib.showCustomPopup()` |
| `testLibExistsFromMenu()` | MenuLib | Menu wrapper to test library existence. | `AdminToolsLib.testLibExists()` |
| `testTemplateTab()` | AdminToolsLib | Tests the template tab functionality. | `PopupLib.showCustomPopup()` |
| `testTemplateTabFromMenu()` | MenuLib | Menu wrapper to test template tab. | `AdminToolsLib.testTemplateTab()` |
| `updateVersionFromMenu()` | MenuLib | Menu wrapper to update script version. | `AdminToolsLib.updateVersionInfo_Remote_()` |
| `updateVersionInfo_Remote_()` | AdminToolsLib | Updates the version info from a remote source. | - |

---
