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

Monitoring-Based Alert Signals:
- Sudden deviation from baseline traffic patterns
- Abnormal connection rates or session behavior
- Repeated protocol anomalies over time

Vulnerability-Aware Alert Context:
- Alerts should consider asset exposure
- Known vulnerabilities increase alert priority
- Vulnerability presence does not confirm exploitation

Data Integration:
- Asset inventory
- Vulnerability assessment results
- Network and host telemetry

Design Principle:
Vulnerability data enriches alerts but should not trigger them alone.

Design Considerations:
- Alerts must include context, not just counts
- Single events rarely justify escalation
- Correlation improves confidence

### 3. Authentication Anomalies
Access Control Abuse Indicators:
- Successful logins followed by unusual activity
- Privilege usage inconsistent with user role
- Excessive access to sensitive services

Detection Challenges:
- Legitimate credentials reduce alert confidence
- Role context is required for accuracy

