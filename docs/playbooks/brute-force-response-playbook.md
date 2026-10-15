# Playbook: Windows Brute-Force Response SOP

## Objective
Standard Operating Procedure for triaging and mitigating repeated failed logon alerts (`EventCode 4625`).

## Step 1: Triage & Initial Verification
1. Open Splunk and execute the validation query:
   ```spl
   index=main EventCode=4625 | stats count by Account_Name, Client_Computer_Name
   Verify if the count exceeds the baseline threshold (count > 3)

   Step 2: Scope Assessment
Check if successful logons (EventCode 4624) occurred immediately after the failures from the same source.

Identify whether the source is an internal workstation or an external IP.

Step 3: Containment & Remediation
Temporarily disable compromised user accounts if unauthorized access is confirmed.

Block source IP addresses or isolate the offending local host from the network.