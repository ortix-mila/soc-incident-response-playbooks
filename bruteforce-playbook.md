# Brute Force Attack Response Playbook

**ID:** SOC-PB-003
**Tactic:** Credential Access
**MITRE ATT&CK Techniques:** [T1110 - Brute Force](https://attack.mitre.org/techniques/T1110/)

## Overview
This playbook details the response process for a brute force attack, where an attacker attempts to gain unauthorized access to an account by systematically guessing passwords. The primary goals are to block the attack, verify account integrity, and strengthen preventative controls.

### Severity Levels
* **Low:** Unsuccessful brute force attempt against a non-critical, single account.
* **Medium:** Unsuccessful brute force attempt against multiple accounts or a privileged account.
* **High:** A brute force attempt has resulted in a successful login to any account.

### Flowchart
```mermaid
graph TD
    subgraph Detection
        A[SIEM Alert: Excessive Failed Logins]
    end

    subgraph Investigation
        A --> B{Identify Source IP & Target Account(s) 👨};
        B --> C{Check IP Reputation & Geolocation ⚡};
        C --> D{Was the login successful? 👨};
    end

    subgraph Containment
        D -- No --> E[Block Source IP at Firewall/WAF ⚡];
        D -- Yes --> F[Disable Compromised Account Immediately ⚡];
        F --> E;
    end

    subgraph Eradication
        E --> G[Scan for Other Activity from Source IP 👨];
    end

    subgraph Recovery
        G --> H[Reset Password for Target Account(s) 👨];
        H --> I[Re-enable Account After Verification 👨];
    end

    subgraph Post-Incident
        I --> J[Document Findings & Attacker IP 👨];
        J --> K[Recommend MFA & Stronger Lockout Policy 👨];
    end
