# Phishing Incident Response Playbook

**ID:** SOC-PB-001
**Tactic:** Initial Access
**MITRE ATT&CK Techniques:** [T1566 - Phishing](https://attack.mitre.org/techniques/T1566/)

## Overview
This playbook outlines the steps to investigate, contain, and remediate a reported phishing email incident.

### Severity Levels
* **Low:** Single user reported a generic phishing email, no clicks or credential entry.
* **Medium:** User clicked a link or downloaded an attachment.
* **High:** User submitted credentials, or the phishing email was part of a targeted campaign against multiple high-privilege users.

### Flowchart
```mermaid
graph TD
    subgraph Detection
        A[Alert from Email Gateway / User Report]
    end

    subgraph Investigation
        A --> B{Analyze Email Headers & Body 👨};
        B --> C{Check URLs/Attachments in Sandbox ⚡};
        C --> D{Any Clicks or Credential Entry? 👨};
    end

    subgraph Containment
        D -- Yes --> E[Isolate Host & Reset Credentials ⚡];
        D -- No --> F[Search & Quarantine Email from all Mailboxes ⚡];
        E --> F;
    end

    subgraph Eradication
        F --> G[Block Sender, URL, and Hash ⚡];
        G --> H[Scan Environment for Similar IOCs 👨];
    end

    subgraph Recovery
        H --> I[Re-image Host if Compromised 👨];
        I --> J[Re-enable User Account 👨];
    end

    subgraph Post-Incident
        J --> K[Document Findings & Close Ticket 👨];
        K --> L[User Awareness Training Recommended 👨];
    end
