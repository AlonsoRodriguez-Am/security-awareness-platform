# security-awareness-platform
A Gophish-powered framework for enterprise phishing simulations, employee training, and threat metrics visualization. Implements MITRE ATT&amp;CK T1192 with custom templates, automated reporting, and SIEM integration to measure/improve organizational resilience against social engineering attacks.

# Instagram Password Reset Phishing Simulation Template

![GoPhish](https://img.shields.io/badge/GoPhish-Compatible-success)
![License](https://img.shields.io/badge/License-MIT-blue)

A professionally designed email template for simulating Instagram password reset phishing attacks in security awareness training. Compatible with GoPhish.

---

## 📌 Overview
This template mimics an Instagram/Meta password reset confirmation email to:
- Train users in identifying phishing attempts.
- Test organizational resilience against social engineering.
- Track email opens (`{{.Tracker}}`) and link clicks (`{{.URL}}`).

**Disclaimer:** Use only for **authorized** security awareness training.

---

## 🛠️ Features
- **Responsive Design**: Works on desktop/mobile clients.
- **Dynamic Fields**: Personalizes emails using GoPhish variables.
- **Tracking**: Embedded pixel for open-rate metrics.
- **Realistic UI**: Matches Instagram/Meta's official email styling.

---

## ✨ Template Variables
| Variable       | Purpose                          | Example CSV Value  |
|----------------|----------------------------------|--------------------|
| `{{.FirstName}}` | Recipient's first name          | `John`             |
| `{{.Email}}`    | Recipient's email address       | `user@company.com` |
| `{{.URL}}`      | Phishing link (GoPhish-generated) | Auto-filled       |
| `{{.Tracker}}`  | Open-tracking pixel             | Auto-filled       |

---

## 🚀 Deployment

## Technical Details  
**Email Tracking**  
- Opens tracked via hidden pixel image  
- Clicks tracked through link redirection  
- *Note:* Some email clients block tracking pixels by default  

## Ethical Guidelines  
- Obtain proper authorization before testing  
- Provide participant debriefs  
- Securely handle and dispose of test data  

## License  
MIT License  

## Contact  
security-team@yourcompany.com  

### 1. Import into GoPhish
- Navigate to **Email Templates** > **New Template**.
- Paste this HTML or import the file.

### 2. **CSV Requirements**  
   Your targets file should be formatted as:  
   `Email,FirstName`  
   `user1@company.com,Alice`  
   `user2@company.com,Bob`  

### 3. **Tracking Setup**  
   Ensure config.json contains:  
  
   "phish_server": {
     "tracking_enabled": true,
     "open_tracking_enabled": true,
     "click_tracking_enabled": true
   }

## Technical Details  
**Email Tracking**  
- Opens tracked via hidden pixel image  
- Clicks tracked through link redirection  

## Ethical Guidelines  
- Obtain proper authorization before testing  
- Provide participant debriefs  
- Securely handle and dispose of test data  

## License  
MIT License  

## Contact  
alonsorodriguez.am@gmail.com 
