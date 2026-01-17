# Controls & Threat Model — SOC Telemetry Pipeline (Cloud-Agnostic)

This document threat-models the SOC telemetry pipeline designed in Phase 4
and defines security controls required to keep the pipeline trustworthy.

A SOC pipeline is itself a high-value target:
- If attackers can blind logging, detections fail silently
- If attackers can poison telemetry, alerts become untrustworthy
- If attackers can access SOC logs, it becomes a data breach

This document focuses on protecting:
- telemetry integrity
- detection reliability
- investigation evidence
- access governance

---

## 1) Security Objectives

The pipeline must guarantee:

### 1.1 Integrity
Telemetry must not be modified without detection.

### 1.2 Availability
Telemetry ingestion and alerting must not fail under burst or attack.

### 1.3 Confidentiality
Logs often include sensitive information (internal IPs, endpoints, access patterns).

### 1.4 Auditability
Every access, query, and configuration change must be traceable.

---

## 2) System Boundary (What is Protected)

### Pipeline stages in scope
- telemetry sources
- collection & transport
- ingestion buffer/stream
- parsing/normalization
- storage (hot/cold)
- enrichment + baseline store
- detection logic/rules
- alerting + SOC investigation

### Threat actors
- external attacker (on network)
- compromised endpoint
- malicious insider / stolen SOC credentials
- attacker with partial cloud/network access

---

## 3) High-Level Threats (What Can Go Wrong)

### T1 — Telemetry Suppression (Blinding the SOC)
Attackers prevent logs from reaching the pipeline.
- kill/disable agents
- block collector endpoints
- overwhelm ingestion with noise

Impact:
- missing visibility
- undetected persistence

---

### T2 — Telemetry Tampering (Changing Evidence)
Attackers modify telemetry to hide activity.
- log rewriting
- timestamp manipulation
- schema drift abuse

Impact:
- investigations become unreliable
- false negatives rise

---

### T3 — Telemetry Poisoning (Alert Degradation)
Attackers shape traffic so baselines drift toward malicious behavior.
- slow “training” attacks
- benign-looking persistence
- blending into baseline windows

Impact:
- detection thresholds become useless over time

---

### T4 — Alert Flooding (SOC Denial of Service)
Attackers generate large volumes of alerting signals.
- threshold gaming
- distributed noise generation
- repeated low-signal events

Impact:
- alert fatigue
- real attacks buried in noise

---

### T5 — Privilege Abuse in Detection System
Attackers obtain access to detection config and disable controls.
- rule deletion/modification
- suppressions added
- severity lowered

Impact:
- full SOC bypass

---

### T6 — Data Exfiltration via Log Access
SOC logs expose:
- internal topology
- security tooling
- user behavior patterns
- potential credentials (if logged improperly)

Impact:
- high-severity breach

---

## 4) Controls by Pipeline Stage

---

## 4.1 Telemetry Sources

### Threats
- agent tampering
- log disabling
- endpoint compromise

### Controls
- hardening + EDR protection for agents
- secure configuration baselines
- agent health monitoring (heartbeat)
- local buffering with retry

Key metric:
> missing heartbeat is a security alert, not just an ops issue.

---

## 4.2 Collection & Transport

### Threats
- MITM interception
- fake sensor injection
- replay attacks

### Controls
- mutual authentication (mTLS)
- signed telemetry batches (optional)
- strict allowlists for sensor identities
- replay detection (nonce/time-based)

---

## 4.3 Ingestion Buffer / Streaming

### Threats
- ingestion overload
- partition manipulation
- event drops

### Controls
- backpressure + rate limiting
- dead-letter queue for malformed events
- ingestion SLO monitoring (lag, drop rate)
- burst absorption capacity planning

---

## 4.4 Parsing / Normalization

### Threats
- schema poisoning
- parser exploits
- silent data corruption

### Controls
- schema validation with rejection paths
- quarantine store for invalid events
- schema drift detection alerts
- versioned schemas and parsers

Key principle:
> Never auto-accept unknown fields without review.

---

## 4.5 Storage (Hot / Cold)

### Threats
- log deletion
- tampering with evidence
- unauthorized read access

### Controls
- encryption at rest
- immutability for cold store (append-only / WORM)
- retention policies enforced by policy, not humans
- audit logs for every access/query

Hot store controls:
- fine-grained access scopes
- query rate limits for sensitive logs

---

## 4.6 Enrichment & Baseline Store

### Threats
- baseline poisoning (slow drift attacks)
- asset/identity spoofing
- enrichment source corruption

### Controls
- baseline updates bounded + reviewed for critical assets
- anomaly exclusion from baseline computation windows
- signed/verified enrichment feeds
- RBAC separation for enrichment configuration

Key principle:
> Baselines must adapt slowly and safely.

---

## 4.7 Detection Logic / Rule Store

### Threats
- rule tampering
- suppression abuse
- detection bypass via config changes

### Controls
- change approval workflow (2-person rule)
- version-controlled detection rules
- audit trail for every modification
- rollback capability
- protected “break glass” operations

---

## 4.8 Alerting & Case Management

### Threats
- alert flooding
- forced escalation noise
- workflow disruption

### Controls
- deduplication and grouping into incidents
- severity throttling
- suppression of repeated low-confidence alerts
- analyst queue isolation and workload controls

Goal:
> preserve analyst attention for high-value investigations.

---

## 5) Governance & IAM Model

A detection pipeline must enforce least privilege.

### Recommended RBAC separation
- ingestion operator (no query access)
- SOC analyst (query access, no pipeline config)
- detection engineer (rule config, limited data)
- admin (break-glass only)

Controls:
- MFA for privileged roles
- session timeouts
- approval gates for high-impact changes
- periodic access review

---

## 6) Monitoring the Monitoring System

A SOC pipeline requires meta-monitoring.

You must alert on:
- missing telemetry
- ingestion lag spikes
- baseline drift anomalies
- rule changes
- alert storms
- unusual query behavior (data scraping)

Key insight:
> If attackers can disable monitoring without detection, the SOC is blind.

---

## 7) Summary

This threat model shows that SOC detection is only as strong as the telemetry pipeline.

Key outcomes:
- telemetry integrity must be protected like production data
- baselines can be poisoned; updates must be bounded and audited
- rule stores are high-value targets and require strict governance
- availability matters: alert flooding is an adversarial goal
- SOC pipelines must monitor themselves

This completes Phase 4 by elevating CICIDS-style detection into a secure,
governed, architecture-level system design.
