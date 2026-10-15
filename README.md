
## Repository Organization Strategy

```text
cloud-native-siem-incident-response/
├── README.md
├── docs/
│   ├── incident-reports/     # Incident writeups & triage logs
│   └── playbooks/            # Standard Operating Procedures (SOPs)
├── forensics/                # Memory dumps, disk artifacts, or PowerShell extraction scripts
├── playbooks/                # Alternative location for IR workflow files / markdown guides
├── splunk/
│   ├── dashboards/           # Dashboard XML configuration files
│   └── saved-searches/       # Exported SPL queries & savedsearches.conf rules
├── sysmon-config/            # sysmonconfig-export.xml
└── detections/               # Raw SPL or KQL detection files

```

---

##  What Belongs in Each Folder

### 1. `docs/incident-reports/`

* **Purpose:** Houses formal post-incident documentation detailing simulated security events.
* **Key Artifacts:**
* Incident Report for **Brute-Force Attack (Event 4625)** detailing time of alert, source IP/user, impact, and remediation.
* Incident Report for **Audit Log Clearance (Event 1102)** detailing anti-forensic activity verification and escalation steps.



### 2. `docs/playbooks/` (or `/playbooks`)

* **Purpose:** Provides step-by-step Standard Operating Procedures (SOPs) for tier-1/tier-2 SOC analysts responding to alerts.
* **Key Artifacts:**
* **Brute-Force Response Playbook:** Steps to identify target accounts, check for successful logon events (`4624`), disable compromised credentials, and block bad IPs.
* **Defense Evasion / Log Clearance Playbook:** Steps to isolate the affected host, check for process creation events (`Sysmon Event 1`), investigate administrative privilege escalation, and preserve system state.



### 3. `forensics/`

* **Purpose:** Stores forensic analysis notes, artifact extractions, or scripts used during investigations.
* **Key Artifacts:**
* PowerShell scripts used to pull event logs or process lists during testing.
* Forensics notes detailing registry or file system changes observed during simulation.



### 4. `splunk/dashboards/`

* **Purpose:** Contains the source code for your visual SOC monitoring dashboards in Splunk.
* **Key Artifacts:**
* **Dashboard XML Files:** Exported XML code for your Splunk security overview panel (e.g., event counts over time, failed logon visualizations, defense evasion tables).



### 5. `splunk/saved-searches/`

* **Purpose:** Stores configuration snippets and rules defining scheduled alerts in Splunk.
* **Key Artifacts:**
* `savedsearches.conf` exports or text files containing your alert definitions, search schedules, threshold conditions (`count > 3`), and SMTP email action settings.



---

##  How to Stage and Commit These Folders

Once you move these folders out of the nested subfolder into your main repository directory, run the following commands in PowerShell to update GitHub:

```powershell
# Stage all updated folders and files
git add docs/ forensics/ playbooks/ splunk/

# Commit the updated portfolio structure
git commit -m "Organize incident reports, playbooks, forensics notes, and Splunk dashboards at repository root"

# Push changes to GitHub
git push origin main

```