### 1. Authentication Anomalies

Additional Host-Level Indicators:
- Repeated SSH authentication failures on Linux hosts
- Sudden use of sudo by non-administrative users
- Windows logon attempts outside normal usage patterns

Relevant Data Sources:
- Windows security event logs
- Linux authentication logs

Limitations:
- Administrative automation may resemble attacker behavior
- Shared accounts reduce attribution accuracy

### 2. Network Reconnaissance
Indicators:
- Port scanning activity
- Excessive connection attempts
- Sequential IP or port probing

Relevant Data Sources:
- Network flow logs
- Firewall logs
- IDS/IPS telemetry

Protocol-Level Signals:
- Incomplete TCP handshakes
- Abnormal UDP traffic patterns
- Excessive ARP requests

Limitations:
- Legitimate scanning tools may appear malicious
- High-volume services can create noise

Infrastructure-Based Alerts:
- Firewall policy violations
- IDS/IPS signature matches
- Repeated blocked connection attempts

Attack Pattern Indicators:
- Reconnaissance followed by access attempts
- Multiple attack techniques from same source
- Evasion behavior after initial detection

Severity Considerations:
- Repeated behavior increases confidence
- Correlated alerts are higher value than isolated signals
