# CyberOps Concept Mapping

This file captures detection-relevant concepts extracted from the
Cisco CyberOps Associate course and maps them to SOC reasoning.

---

## Modules 1–2 — Threat Landscape & SOC Mission

Detection focuses on observable behavior.
SOCs exist to enable response, not perfect prevention.

---

## Modules 3–4 — Host Visibility

Host logs provide authentication and process evidence.
They confirm activity but rarely indicate intent alone.

---

## Modules 5–10 — Network Behavior

Networks exhibit strong baseline behavior.
Deviations indicate reconnaissance, misuse, or lateral movement.

---

## Modules 11–14 — Infrastructure & Attacks

Security infrastructure enforces policy boundaries.
Attack techniques produce repeatable behavioral patterns.

---

## Modules 15–16 — Monitoring & Foundations

Monitoring produces raw signals.
Detection requires logic, thresholds, and context.

---

## Modules 17–19 — Enterprise Services, Defense, and Access Control

### Enterprise Services Abuse
- Authentication services are primary attack targets
- Email, file sharing, and application services are abused post-access

### Defense-in-Depth
- Multiple overlapping controls
- Assumes individual controls can fail
- Detection is a core defensive layer

### Access Control Concepts
- Authentication verifies identity
- Authorization defines permissions
- Accounting records activity

### Detection Insight
Most successful attacks abuse **legitimate access paths**.
Detection must focus on abnormal usage, not just blocked attempts.

---

## Modules 20–22 — Threat Intelligence, Cryptography, and Endpoints

### Threat Intelligence
- External context about known threats
- Indicators of compromise (IOCs)
- Tactics, techniques, and procedures (TTPs)

Use:
- Enrichment of alerts
- Prioritization of investigations

Limitation:
- Often reactive and time-lagged

### Cryptography
- Encryption protects confidentiality
- Limits payload inspection
- Shifts detection to metadata and behavior

### Endpoint Protection
- Visibility into host behavior
- Malware and process-level indicators
- Strong investigative value

### Detection Implication
Threat intelligence and endpoint data **support detection**
but rarely replace network-based alerting.

- Access control failures are central to modern incidents.

## Modules 23–25 — Vulnerabilities, Technologies, and Security Data

### Endpoint Vulnerability Assessment
- Asset profiling and exposure identification
- Vulnerabilities represent potential, not incidents
- CVSS expresses severity, not likelihood of exploitation

### Security Technologies
- Firewalls, IDS/IPS, EDR, and monitoring tools
- Each technology produces different data types
- No single tool provides complete visibility

### Network Security Data
- Network flow records
- Firewall and IDS logs
- Endpoint and host logs

### Detection Implication
Security data represents **observations**, not conclusions.
Effective detection correlates multiple data sources over time.

## Modules 26–28 — Alert Evaluation, Security Data Handling, and Incident Response

### Evaluating Alerts
- Alert confidence increases through correlation
- Asset context influences prioritization
- Analyst review determines escalation

### Working with Security Data
- Data is reviewed iteratively
- Historical context matters
- Investigation is hypothesis-driven

### Digital Forensics and Incident Response
- Evidence handling must preserve integrity
- Incident response follows defined phases
- Lessons learned improve future detection

### Detection Insight
Effective SOC operations close the loop:
alert → investigation → response → improvement.

