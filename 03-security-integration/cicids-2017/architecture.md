# Architecture — SOC Telemetry Pipeline for CICIDS-Style Detection (Cloud-Agnostic)

This document reframes the CICIDS 2017 dataset into a **real-world, cloud-agnostic SOC telemetry architecture**.

The goal is not deployment. The goal is **system design thinking**:
how CICIDS-style network flow telemetry would be ingested, stored, enriched,
analyzed, and translated into analyst-facing alerts — while maintaining
security controls and operational reliability.

This design explicitly incorporates lessons from:
- Phase 1/2: overlap, variance, and misleading signals
- Phase 3/3.5: false positives, alert fatigue, and context dependency

---

## 1) Objective

Design a SOC telemetry and detection pipeline that:
- Supports scalable ingestion of flow/log data
- Enables detection logic with enrichment and baselining
- Minimizes false positives through context-aware decisions
- Produces explainable alerts for triage and escalation
- Preserves data integrity (tamper-resistance) and access governance

---

## 2) Assumptions & Scope

### Dataset framing
CICIDS represents labeled outcomes from simulated enterprise traffic. In the real world:
- Logs arrive continuously
- Labels do not exist at ingestion time
- Context is external (asset inventory, identity, historical behavior)

### Operational constraints (design drivers)
- Low-latency alerting (minutes, not hours)
- Retention with tiers (hot vs cold)
- High volume, skewed distributions, heavy tails
- Detection is uncertain → alerts must explain why they fired

### Out of scope (by design)
- Production deployment details
- ML-based detection optimization
- Accuracy/F1/ROC claims
- Full SOAR automation

---

## 3) End-to-End Architecture (High Level)

### Pipeline stages
1) **Telemetry Sources**
2) **Collection & Transport**
3) **Ingestion Buffer / Stream**
4) **Parsing + Normalization**
5) **Storage Layer (Hot / Cold)**
6) **Enrichment Layer**
7) **Detection Layer**
8) **Alerting + Case Management**
9) **SOC Investigation + Feedback Loop**

---

## 4) Telemetry Sources

This architecture assumes event streams such as:
- Network flow records (NetFlow/IPFIX-like)
- IDS sensor events
- Firewall allow/deny logs
- DNS logs (optional)
- Endpoint telemetry (optional)

Key point:
> Detection depends on combining weak signals across sources, not single logs.

---

## 5) Collection & Transport

### Collector tier
Collectors are responsible for:
- receiving telemetry from sources
- performing basic validation and schema checks
- tagging events with metadata (sensor ID, location, environment)

### Transport requirements
- authenticated transport
- backpressure support (do not drop events silently)
- retry mechanisms with bounded buffering

---

## 6) Ingestion Buffer / Streaming Layer

A streaming/buffer layer is required to:
- absorb bursts (traffic spikes, attack spikes)
- decouple sources from processing
- ensure replay capability (for reprocessing and audits)

Key properties:
- partitioned by source/time
- replayable stream (at least short window)
- strong delivery guarantees (at-least-once preferred)

---

## 7) Parsing, Normalization & Quality Checks

This stage converts raw telemetry into an analysis-ready schema.

### Steps
- schema normalization (consistent field naming)
- type validation
- infinity / malformed record handling
- duplicate suppression (if applicable)
- timestamp alignment

Quality controls:
- event rate monitoring
- missing-field anomaly detection
- schema drift detection

Key principle:
> Data quality failures must generate operational alerts, not silent corruption.

---

## 8) Storage Layer (Hot / Cold)

### Hot store (low latency)
Purpose:
- fast search for investigations
- dashboards and recent alert context

Characteristics:
- indexed
- optimized for query-by-time, query-by-asset, query-by-signal

### Cold store (long retention)
Purpose:
- long-term audits and historical baselining
- cost-effective retention

Characteristics:
- append-only
- immutable retention controls
- batch query support

Retention strategy example:
- Hot: 7–30 days
- Cold: 90–365 days (policy dependent)

---

## 9) Enrichment Layer (Context Injection)

This is the most important part of the architecture.

Phase 3.5 proved:
> detection collapses without context.

Enrichment attaches external context such as:
- asset inventory (server vs user device vs critical system)
- identity context (service account vs employee vs unknown)
- geo / network zone classification (corp LAN, DMZ, public)
- historical baseline summaries (normal ranges, typical peers)
- known benign schedules (backups, patch windows)

Enrichment output:
A telemetry record becomes:
> event + identity + asset context + baseline reference

---

## 10) Detection Layer (SOC-Aligned)

Detection is framed as **decision support**, not classification.

### Detection types (non-ML)
- rule-like conditions (multi-signal)
- baselining deviations (relative to asset history)
- peer grouping anomalies (asset vs similar assets)
- burst patterns / persistence patterns
- asymmetric communication (rare directionality)

### Signal composition principle
Avoid single-feature detection.

Instead:
- combine multiple weak indicators
- require context checks
- attach reasons for firing

Example (conceptual):
- high flow duration +
- unusual bytes/sec relative to asset baseline +
- destination rarity +
- time-of-day anomaly

---

## 11) Alerting Layer

Alerts must be:
- explainable
- prioritized
- actionable

### Alert contents
- what fired (signals)
- why it fired (context + baseline deviation)
- what asset is affected (criticality)
- suggested next checks (investigation hints)
- confidence/uncertainty indicator

### Alert severity
Severity should depend more on:
- asset criticality
- blast radius
- corroborating evidence
than on raw feature magnitude.

---

## 12) SOC Workflow Integration

### Tier 1 triage
Goal:
- determine if likely benign or needs escalation

Inputs needed:
- alert explanation
- baseline comparison
- recent similar alerts
- quick pivot queries

### Tier 2 investigation
Goal:
- validate and scope the incident

Needs:
- cross-log correlation
- longer historical context
- threat intel references
- response readiness

---

## 13) Feedback Loop (Closing the System)

A SOC pipeline improves only if analyst outcomes are captured.

Feedback should store:
- true positive / false positive decisions
- notes on why it was benign
- detection tuning suggestions

Feedback drives:
- rule tuning
- enrichment improvements
- baseline refinement

Key principle:
> detection systems without feedback loops decay over time.

---

## 14) Security Controls (High-Level)

Telemetry pipelines are security-critical and must be protected.

Controls:
- least privilege access for each stage
- encryption in transit and at rest
- audit logging of all access and config changes
- immutability for cold storage (append-only)
- integrity checks (hashing/signing optional)
- segmentation between ingestion and SOC UI

---

## 15) Architecture Summary

This Phase 4 design shows how CICIDS-style telemetry would function in a realistic SOC pipeline:

- ingestion + buffering prevents event loss
- normalization prevents silent corruption
- enrichment restores missing real-world context
- detection combines weak signals with baselines
- alerts emphasize explainability and triage utility
- feedback loops keep detections maintainable
- security controls protect the pipeline itself

This architecture intentionally remains cloud-agnostic and can later be mapped
to specific implementations once cloud platforms are studied hands-on.
