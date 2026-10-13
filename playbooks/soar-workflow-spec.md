# Automated Incident Response Playbook: Credential Stuffing Containment

## Workflow Architecture

1. **Trigger:** Azure Sentinel Incident Creation (Severity: High / Rule: Distributed Credential Stuffing).

2. **Data Extraction:** Parse incident entities to extract the `SourceIPs` array and target `UserPrincipalName`.

3. **Containment Action:** 
   - Call Azure Network Security Group (NSG) REST API.
   - Append high-priority inbound rule: `Action: Deny`, `Source: [Attacker IP]`, `Destination: Any`.

4. **Notification:** Post incident summary and automated mitigation status to the SOC Teams/Slack webhook.