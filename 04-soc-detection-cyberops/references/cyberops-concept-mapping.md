# CyberOps Concept Mapping

This file captures detection-relevant concepts extracted from the
Cisco CyberOps Associate course and maps them to SOC alert reasoning.

---

## Modules 1–2 — Threat Landscape & SOC Mission

Detection focuses on observable behavior.
SOCs exist to enable response, not perfect prevention.

---

## Modules 3–4 — Host Visibility

Host logs provide authentication and process evidence.
They are most effective when correlated with network signals.

---

## Modules 5–10 — Network Behavior

Networks exhibit predictable baseline behavior.
Deviations often indicate reconnaissance or misuse.

---

## Modules 11–14 — Infrastructure & Attacks

Security devices generate alerts based on policy violations.
Attack techniques produce repeatable behavioral patterns.

---

## Modules 15–16 — Monitoring & Foundational Attacks

### Network Monitoring
- Continuous collection of traffic and events
- Visibility into flows, connections, and anomalies
- Monitoring alone does not imply detection

### Foundational Attacks
- IP spoofing
- ARP poisoning
- TCP session manipulation
- Protocol misuse

### Detection Insight
Monitoring provides **raw signals**.
Detection requires interpretation, thresholds, and context.

---

## Day 5 Summary

- Monitoring generates volume, not answers.
- Foundational attacks exploit protocol trust.
- Poor alert logic converts visibility into noise.
