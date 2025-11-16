*Last updated:* 16/11/2025 - 05:38 (Europe/Athens)
*Last synced with VERSIONS_INDEX.md:* 16/11/2025 - 05:38 (DEV-only)
*Build:* 62ee83c

# 📘 **Flow Mapping – CHECKLIST V8.0**
## 🧩 Overview
This document describes the flow mapping of the CHECKLIST system (Version V8.0), including all triggers, scripts, and libraries. It serves as the primary technical reference.
---
## ⚙️ System Architecture
The system is composed of three main layers:
| Layer | Description | Files / Components |
|---|---|---|
| **Triggers** | Events that initiate workflows | `onOpen()`, `onEdit()`, Time-based |
| **Main Scripts** | Core project files that respond to triggers | `Checklist.gs`, `Blink.gs`, `AutoDupl_File&DeleteTabs.gs` |
| **Libraries** | Shared code for common functionalities | `AdminToolsLib`, `PopupLib`, `MenuLib`, `HoBMastersLib` |
### Visual Architecture Diagram
The following diagram illustrates the high-level interaction between these components:
![Improved Flow Diagram V8.0](https://private-us-east-1.manuscdn.com/sessionFile/9GHksmrmwI6dru4ysZR8b8/sandbox/Eo5w99kAgoamLF9hLNFXwY-images_1761218916391_na1fn_L2hvbWUvdWJ1bnR1L2dhc19hbmFseXNpcy9pbXByb3ZlZF9mbG93X3Y4.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvOUdIa3Ntcm13STZkcnU0eXNaUjhiOC9zYW5kYm94L0VvNXc5OWtBZ29hbUxGOWhMTkZYd1ktaW1hZ2VzXzE3NjEyMTg5MTYzOTFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZGhjMTloYm1Gc2VYTnBjeTlwYlhCeWIzWmxaRjltYkc5M1gzWTQucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=MgD1RXv4i5oTrtMlzwVeplO1HL7wNdXZ4ZuPMiB-8~ug5UtR0VX7nDKbtBIhWeNUSgENsmnOVYkLWEVh8pQ0Wng21s3mcEx3nCheDNPFhdClcCS4naLcljXyoQgb4NLPelWYAWcXio9Zg0ef~HJAPll9yAY8Ysr4dHIt5QFfmsjiqlnl0JyVzbdGI8da84WdcC34uaD-bfMBHbbSms3V3GtXfM9IC~BhNTq4HUAgTew4GJBBGljrvriElug7jA5Ggf-Mm7Yl-lhJNS8FRWAn8cFGJ7pliD9~HvFk-D3o61H7zpj2u5Mrl515Zzu2-vdSRzghCv83URaAdUtNSv9vlQ__)
---
## 🧱 Component Breakdown

### 1. Triggers

- **`onOpen()`**: Fires when a user opens the spreadsheet. It is responsible for initializing the menu and checking if a new day needs to be created.
- **`onEdit()`**: Fires every time a cell is edited. It is used for data validation, timestamping, and triggering contextual popups.
- **Time-based**: Runs at scheduled intervals (e.g., every 30 minutes) to perform background tasks like `remindMissingNames()`.

### 2. Main Scripts

- **`Checklist.gs`**: The main entry point. It handles the `onOpen` and `onEdit` triggers and orchestrates calls to the various libraries.
- **`AutoDupl_File&DeleteTabs.gs`**: Manages the automated duplication of master templates and the cleanup of old tabs.
- **`Blink.gs`**: Provides visual feedback to the user, such as blinking a cell's font color to draw attention.

### 3. Libraries

- **`AdminToolsLib`**: The core library for administrative actions like creating new days, clearing notes, and managing tabs. It is called by both `Checklist.gs` and `AutoDupl_File&DeleteTabs.gs`.
- **`MenuLib`**: Responsible for dynamically building the user and owner menus based on the configuration in the `MenuSettings` sheet.
- **`PopupLib`**: A centralized utility for displaying all user interface feedback, including modals, alerts, and toasts. It provides a consistent user experience.
- **`HoBMastersLib`**: Handles all interactions with the central `HoB_Masters` file, primarily for fetching template tabs.

---

## 🧭 Functional Flow Examples

### Example 1: New Day Creation

1.  `onOpen()` trigger fires in `Checklist.gs`.
2.  `Checklist.gs` calls `AdminToolsLib.createNewDay_AUTO()`.
3.  `AdminToolsLib` calls `HoBMastersLib.getTemplateTabFromHoBMasters_()` to get the correct template.
4.  `AdminToolsLib` duplicates the template and prepares the new sheet.
5.  `AdminToolsLib` calls `PopupLib.showCustomPopup()` to inform the user the day was created.

### Example 2: Missing Name Reminder

1.  `onEdit()` trigger fires in `Checklist.gs` when a user edits a specific cell.
2.  `Checklist.gs` calls `AdminToolsLib.remindMissingNames()`.
3.  `AdminToolsLib` calls `PopupLib.showCustomPopup()` to display a warning.
4.  `Blink.gs` might be called to make the relevant cell blink.

---

This improved structure provides a clearer separation of concerns and a more robust, maintainable codebase.
