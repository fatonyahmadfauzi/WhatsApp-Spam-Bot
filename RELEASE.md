# Release Notes - WhatsApp-Spam-Bot v2.1

**Release Date**: April 20, 2025  
**Maintainer**: Fatony Ahmad Fauzi

---

## 🚀 **New Features & Improvements**

### Unlimited Message Configuration:

- Added the ability to configure multiple unique messages during runtime.
- Users can input a sequence of messages that will repeat for the specified number of cycles.

### Bot Prompt Customization:

- Retained the option to include `<Status>` prefixes in messages.

### Selenium 4+ Migration:

- Ensured compatibility with the latest Selenium standards.
- Modernized element selection methods to match updated WhatsApp Web DOM.

### Multi-Language Support:

- Seamlessly handles both "Send" (English) and "Kirim" (Indonesian) buttons.

---

## 🐛 **Bug Fixes**

- Resolved issues with message box detection in certain WhatsApp Web updates.
- Improved error handling for scenarios where elements are not found (e.g., incorrect user/group name).

---

## ⚙️ **Usage Notes**

1. Always maximize the Chrome window after scanning the QR code.
2. Input user or group names exactly as they appear in WhatsApp (case-sensitive).
3. Use **Developer Tools (F12)** to debug any DOM-related issues.
4. Specify intervals accurately to avoid sending messages too quickly.

---

## ⚠️ **Critical Disclaimer**

This tool is **strictly for educational and testing purposes**. Misuse, such as spamming, may result in **WhatsApp account suspension**. Always use responsibly and in compliance with WhatsApp's Terms of Service.
