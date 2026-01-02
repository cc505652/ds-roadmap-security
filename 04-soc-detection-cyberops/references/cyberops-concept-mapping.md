# CyberOps Concept Mapping

This file captures detection-relevant concepts extracted from the
Cisco CyberOps Associate course.
It informs SOC alerting logic and incident reasoning.

---

## Modules 1–2 — Threat Landscape & SOC Mission

Detection focuses on observable behavior.
SOCs exist to enable response, not perfect prevention.

---

## Modules 3–4 — Host Visibility

Host logs provide authentication and process evidence.
They are strongest when correlated with network signals.

---

## Modules 5–10 — Network Behavior

Networks exhibit strong baseline behavior.
Deviations indicate reconnaissance, misuse, or lateral movement.

---

## Modules 11–12 — Network Devices & Security Infrastructure

### Network Devices
- Switches and routers control traffic paths
- Wireless introduces additional attack surfaces

### Security Devices
- Firewalls enforce policy boundaries
- IDS/IPS detect known and anomalous patterns
- Proxies mediate application access

### Detection Insight
Security devices generate alerts based on **policy violations and anomalies**,
not confirmed compromise.

---

## Modules 13–14 — Attackers and Common Attacks

### Attacker Techniques
- Reconnaissance
- Initial access
- Privilege escalation
- Lateral movement
- Persistence

### Common Attacks
- Malware delivery
- Network scanning
- Denial of Service
- Evasion techniques

### Detection Insight
Most attacks reuse common techniques.
Detection targets **patterns**, not individual tools.

---

## Day 4 Summary

- Security infrastructure defines visibility boundaries.
- Attack techniques produce repeatable signals.
- Detection relies on understanding both attacker behavior and defensive controls.
