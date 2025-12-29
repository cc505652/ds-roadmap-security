# CyberOps Concept Mapping

This file captures detection-relevant concepts extracted from the
Cisco CyberOps Associate course.  
It serves as a reference layer feeding SOC alert design and incident reasoning.

---

## Module 1 – The Danger

### Threat Actors
- External attackers targeting exposed services
- Insiders abusing legitimate access
- Organized cybercrime groups
- Advanced Persistent Threats (APTs)

### Motivations
- Financial gain
- Espionage
- Disruption
- Persistence within networks

### Impact Types
- Data exfiltration
- Service disruption
- Lateral movement
- Long-term undetected access

### Detection-Relevant Insight
SOC detection focuses on **observable effects of attacker behavior**, not attacker intent.

---

## Module 2 – Fighters in the War Against Cybercrime

### Modern SOC Purpose
- Continuous monitoring
- Detection of abnormal activity
- Prioritization of actionable alerts
- Coordination of incident response

### Defender Mindset
- Assume compromise is possible
- Prioritize detection over perfect prevention
- Reduce dwell time and impact

### SOC Roles (High Level)
- Tier 1: Alert monitoring and triage
- Tier 2: Investigation and validation
- Tier 3: Advanced analysis and threat hunting

### Detection-Relevant Insight
The SOC exists to **enable response**, not just generate alerts.

---

## Day 1 Summary

- Threat actors vary widely, but detection relies on behavior.
- SOC effectiveness depends on alert quality, not quantity.
- Detection logic must balance visibility with operational reality.

