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

## Day 6 Summary

- Enterprise services are high-value attack surfaces.
- Defense-in-depth relies on layered visibility.
- Access control failures are central to modern incidents.
