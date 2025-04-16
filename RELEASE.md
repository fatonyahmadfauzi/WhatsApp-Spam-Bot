# Release Notes - WhatsApp-Spam-Bot v2.01

**Release Date**: April 14, 2025  
**Maintainer**: Fatony Ahmad Fauzi

---

## 🚀 **New Features & Improvements**

- **Selenium 4+ Migration**:
  - Replaced deprecated methods with modern `find_element(By.*, ...)` syntax.
  - Enhanced compatibility with latest ChromeDriver (v135+).
- **Multi-Language Support**:
  - Added dynamic detection for **Send** (English) and **Kirim** (Indonesian) buttons.
  - Improved UI compatibility for global WhatsApp Web users.
- **Robust Element Detection**:
  - Updated XPaths for message box and send button to match WhatsApp Web's updated DOM structure.
  - Flexible input box detection via `_ak1r` container for future-proofing.
- **Error Handling**:
  - Added explicit checks for chat availability, message box detection, and send button failures.
- **Bot Prompt Customization**:
  - Retained optional `<Status: X/Y>` prefix with user toggle (Y/N).

---

## 🐛 **Bug Fixes**

- Fixed incorrect message box targeting (previously interfered with search bar).
- Resolved localization issues causing send button failures in non-English interfaces.
- Removed redundant `datetime` import (code cleanup).

---

## ⚙️ **Usage Notes**

1. **Maximize Chrome window** immediately after QR code scan for optimal element detection.
2. Ensure **exact case-sensitive spelling** of user/group names.
3. Use **F12 Developer Tools** to debug DOM changes if elements are not detected.
4. Interval accuracy improved for consistent message pacing.

---

## ⚠️ **Critical Disclaimer**

This tool is **strictly for educational/testing purposes**. Misuse (e.g., spamming) may result in **WhatsApp account suspension**. Use responsibly and adhere to WhatsApp's Terms of Service.

---

## 🔗 **Links**

- [GitHub Repository](https://github.com/Akshayjyoti/WhatsApp-Spam-Bot)
- [ChromeDriver Compatibility Guide](https://chromedriver.chromium.org/)
