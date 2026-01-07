# Incident Lifecycle

This document describes how a Security Operations Center (SOC)
handles security incidents from initial detection to post-incident review.

The focus is on **decision flow**, not tooling.

---

## 1. Detection

An alert or signal is generated indicating potential malicious activity.

Sources of detection:
- Network telemetry
- Host logs
- Security infrastructure alerts

Challenges:
- High alert volume
- False positives
- Limited initial context

Detection does not confirm compromise.
It initiates investigation.

---

## 2. Triage

The analyst determines:
- Is the alert credible?
- What asset is affected?
- What is the potential impact?

Access-Control Considerations During Triage:
- Was access legitimate or abused?
- Were valid credentials used?
- Does activity align with user role?

Misuse of valid credentials often delays incident confirmation.

---

## 3. Investigation

The analyst gathers context:
- Network activity
- Host behavior
- Authentication history
- Service usage patterns
  
Access Control Investigation Focus:
- Review authentication source and timing
- Compare actions against assigned user role
- Identify privilege escalation after login

Supporting Investigation Context:
- Threat intelligence enrichment
- Endpoint telemetry
- Historical activity patterns

These sources improve confidence but do not replace primary detection signals.

Key Challenge:
Legitimate credentials reduce confidence and slow escalation decisions.

Goal:
Confirm or dismiss malicious activity.

Investigation often relies on correlation across data sources.

---

## 4. Containment

If an incident is confirmed:
- Isolate affected systems
- Block malicious network paths
- Disable compromised accounts

Containment prioritizes limiting spread and impact.

---

## 5. Eradication and Recovery

Actions include:
- Removing malicious artifacts
- Patching vulnerabilities
- Restoring systems to known-good state

Recovery should minimize operational disruption.

---

## 6. Post-Incident Review

Questions addressed:
- What detection worked?
- What signals were missed?
- Where did delays occur?

Outcomes:
- Improved alert logic
- Updated response procedures
- Reduced future risk

---
Evidence and Closure:
- Preserve logs and artifacts
- Document timeline and analyst decisions
- Validate containment effectiveness

Outcome:
Post-incident review feeds detection improvement and reduces future response time.

## Key Insight

Detection is only valuable if it enables **timely and effective response**.
Alerts that cannot be acted upon increase operational burden without improving security.
