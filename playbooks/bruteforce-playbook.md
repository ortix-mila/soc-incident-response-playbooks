
graph TD
    subgraph Detection
        A["SIEM Alert: Excessive Failed Logins"]
    end

    subgraph Investigation
        A --> B{"Identify Source IP & Target Account(s) "};
        B --> C{"Check IP Reputation & Geolocation "};
        C --> D{"Was the login successful? "};
    end

    subgraph Containment
        D -- "No" --> E["Block Source IP at Firewall/WAF "];
        D -- "Yes" --> F["Disable Compromised Account Immediately "];
        F --> E;
    end

    subgraph Eradication
        E --> G["Scan for Other Activity from Source IP "];
    end

    subgraph Recovery
        G --> H["Reset Password for Target Account(s) "];
        H --> I["Re-enable Account After Verification "];
    end

    subgraph Post-Incident
        I --> J["Document Findings & Attacker IP "];
        J --> K["Recommend MFA & Stronger Lockout Policy "];
    end
