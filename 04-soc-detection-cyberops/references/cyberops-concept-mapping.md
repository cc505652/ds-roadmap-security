# CyberOps Concept Mapping

This file captures detection-relevant concepts extracted from the
Cisco CyberOps Associate course.
It feeds SOC alert modeling and incident reasoning.

---

## Module 1 – The Danger

Threat actors generate observable effects rather than directly visible intent.
Detection focuses on those effects.

---

## Module 2 – Fighters in the War Against Cybercrime

SOCs exist to:
- monitor continuously
- detect anomalies
- triage alerts
- enable response

---

## Modules 3–4 – Host Operating Systems

Host logs provide:
- authentication evidence
- privilege usage
- process activity

They are most effective when correlated with network behavior.

---

## Modules 5–10 – Network Behavior & Services

### Normal Network Behavior
- Predictable protocol usage
- Stable client–server communication patterns
- Consistent service access paths

### Protocol-Level Visibility
- IP addressing and routing patterns
- TCP session establishment and teardown
- UDP usage for specific services

### Address Resolution (ARP)
- IP-to-MAC mapping within a subnet
- ARP requests are broadcast and predictable

### Network Services
- DNS: name resolution
- DHCP: dynamic address assignment
- NAT: address translation boundaries
- Email, HTTP, file services: application-layer patterns

---

## Detection-Relevant Insights

- Network anomalies often appear **before** host compromise is confirmed.
- Abnormal connection patterns indicate reconnaissance or lateral movement.
- ARP and protocol misuse can signal spoofing or scanning activity.
- Service misuse is often easier to detect than payload content.

---

## Day 3 Summary

- Networks exhibit strong baseline behavior.
- Deviations from baseline are primary detection signals.
- Network telemetry is foundational for SOC alerting.
