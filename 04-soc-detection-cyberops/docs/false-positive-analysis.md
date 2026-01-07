# False Positive Analysis

This document examines why security monitoring frequently produces
alerts that do not represent real security incidents.

---

## What Creates False Positives?

### 1. Monitoring Without Context
- Raw traffic lacks intent
- Legitimate activity may appear abnormal

---

### 2. Static Thresholds
- Fixed limits do not adapt to environment changes
- Rare but valid behavior triggers alerts

---

### 3. Foundational Protocol Behavior
- ARP broadcasts resemble spoofing
- TCP retransmissions resemble scanning
- Network congestion resembles attack traffic

---

### 4. Legitimate Administrative Activity
- Network scans by IT teams
- Backup and maintenance traffic
- Security testing tools

---

## Operational Impact

- Analyst fatigue
- Reduced trust in alerts
- Missed real incidents

Alert Evaluation Perspective:
- Alerts should be reviewed in context, not isolation
- Historical behavior reduces false escalation
- Analyst judgment is essential for final decisions

---

## Key Insight

False positives are often a **design failure**, not a tuning failure.
Good detection balances visibility, context, and operational reality.
