# Incident Report: Brute-Force Attack Detected (EventCode 4625)

## Incident Overview
* **Incident ID:** INC-2026-001
* **Date/Time:** October 15, 2026
* **Severity:** High
* **Detection Mechanism:** Splunk SIEM Automated Alert
* **Affected Asset:** Local Windows Workstation
* **Trigger Event ID:** Windows Security Event ID 4625 (An account failed to log on)

## Detection & Analysis
A spike in failed logon attempts was detected, exceeding the threshold of 3 failed attempts within the monitoring window.

**Splunk SPL Detection Query:**
```spl
index=main EventCode=4625 
| stats count by Account_Name, Client_Computer_Name, host 
| where count > 3


Response & Remediation
Validation: Confirmed the event via Splunk search and email notification dispatch.

Investigation: Inspected Client_Computer_Name and targeted Account_Name to differentiate between misconfigured service accounts and brute-force activity.

Mitigation: Enforced account lockout policies and reviewed local credential hygiene.