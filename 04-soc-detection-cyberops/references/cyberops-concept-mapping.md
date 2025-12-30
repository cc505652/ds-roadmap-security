# CyberOps Concept Mapping

This file captures detection-relevant concepts extracted from the
Cisco CyberOps Associate course.
It feeds SOC alert modeling and incident reasoning.

---

## Module 1 – The Danger

### Threat Actors
- External attackers
- Insiders with legitimate access
- Organized cybercrime groups
- Advanced Persistent Threats (APTs)

### Impact Types
- Data exfiltration
- Service disruption
- Lateral movement
- Long-term persistence

### Detection Insight
Detection focuses on **observable behavior**, not attacker intent.

---

## Module 2 – Fighters in the War Against Cybercrime

### SOC Mission
- Continuous monitoring
- Detection of anomalies
- Alert triage
- Incident response coordination

### Defender Mindset
- Assume compromise is possible
- Prioritize detection and response
- Reduce dwell time and blast radius

### Detection Insight
A SOC exists to **enable response**, not just generate alerts.

---

## Modules 3–4 – Host Operating Systems

### Windows Visibility
- Successful and failed authentication events
- Process creation and termination
- Service installation and modification
- Limited file access auditing

### Linux Visibility
- SSH login attempts
- sudo privilege escalation
- Process execution
- File permission changes

### Detection Insight
Host logs provide **confirmation and context** but rarely indicate intent alone.
They are most effective when correlated with network activity.

---

## Day 2 Summary
- Operating systems generate useful evidence but with limited context.
- Host data strengthens investigations, not standalone detection.
- Correlation with network signals is essential.
