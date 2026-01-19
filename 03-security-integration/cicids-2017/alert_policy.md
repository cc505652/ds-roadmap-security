# Phase 5.3 — Alert Policy (Gating + Dedup + Rate Limiting)

This document defines how Phase 5 detection signals are converted into **SOC-usable alerts**.

Phase 5.2 produced an interpretable anomaly score (`anomaly_score`) using robust MAD scoring.
However, raw anomaly scores are not operationally safe to alert on directly.

SOC reality:
- BENIGN traffic contains heavy tails and burst behavior
- naive thresholding creates alert storms
- false positives destroy analyst trust

Goal of Phase 5.3:
✅ control alert volume  
✅ reduce false positives  
✅ create stable, reviewable alert behavior  
✅ make alerts investigation-ready

---

## 1) Inputs (What Phase 5 produces)

### 1.1 Detector Outputs
From `5.2_minimal_anomaly_detector.ipynb`, each flow has:

- `anomaly_score`  
  (max robust deviation across selected SOC features)

- contributing feature deviations:
  - `rz_Flow Duration`
  - `rz_Total Fwd Packets`
  - `rz_Total Backward Packets`
  - `rz_Flow Bytes/s`
  - `rz_Flow Packets/s`

### 1.2 Baseline Artifacts
From `5.1_baseline_modeling.ipynb`:

- BENIGN baseline stats (median/IQR/p95/p99)
- drift awareness across `source_file`
- stability slices

These baseline artifacts inform gating thresholds.

---

## 2) Why alert gating is mandatory (Phase 3.5 alignment)

Phase 3.5 established:

- BENIGN flows can exceed q99 thresholds (burst traffic)
- strong overlap exists between BENIGN and ATTACK behavior
- context dominates detection quality

Therefore:
raw anomaly threshold ≠ detection rule.

Instead:
anomaly threshold produces **signal candidates** → gating turns them into alerts.

---

## 3) Alert Definition

An alert is emitted only if:

1) A detection signal crosses a defined threshold  
2) The alert passes gating policies  
3) The alert is not a duplicate or storm event  
4) The alert contains investigation context fields

---

## 4) Policy Layers (in order)

### Layer A — Threshold Gate (Signal Candidate)
Use quantile thresholds computed from BENIGN baseline.

Recommended SOC gating options:
- `p99` (more sensitive, higher noise)
- `p99.5` (balanced)
- `p99.9` (strict, lower volume)

**Rule A1**
Signal candidate triggers if:

`anomaly_score >= THRESHOLD_Q`

Where THRESHOLD_Q ∈ {p99, p99.5, p99.9}

Output:
- `signal_candidate = True`

---

### Layer B — Entity Grouping (who triggered it?)
SOC alerts must be per entity/service context, not global.

If available:
- entity = `Src IP`
- service = `Dst Port` (or Protocol)
- zone = inferred if possible (internal/external not always available in CICIDS)

**Alert grouping key**
# Phase 5.3 — Alert Policy (Gating + Dedup + Rate Limiting)

This document defines how Phase 5 detection signals are converted into **SOC-usable alerts**.

Phase 5.2 produced an interpretable anomaly score (`anomaly_score`) using robust MAD scoring.
However, raw anomaly scores are not operationally safe to alert on directly.

SOC reality:
- BENIGN traffic contains heavy tails and burst behavior
- naive thresholding creates alert storms
- false positives destroy analyst trust

Goal of Phase 5.3:
✅ control alert volume  
✅ reduce false positives  
✅ create stable, reviewable alert behavior  
✅ make alerts investigation-ready

---

## 1) Inputs (What Phase 5 produces)

### 1.1 Detector Outputs
From `5.2_minimal_anomaly_detector.ipynb`, each flow has:

- `anomaly_score`  
  (max robust deviation across selected SOC features)

- contributing feature deviations:
  - `rz_Flow Duration`
  - `rz_Total Fwd Packets`
  - `rz_Total Backward Packets`
  - `rz_Flow Bytes/s`
  - `rz_Flow Packets/s`

### 1.2 Baseline Artifacts
From `5.1_baseline_modeling.ipynb`:

- BENIGN baseline stats (median/IQR/p95/p99)
- drift awareness across `source_file`
- stability slices

These baseline artifacts inform gating thresholds.

---

## 2) Why alert gating is mandatory (Phase 3.5 alignment)

Phase 3.5 established:

- BENIGN flows can exceed q99 thresholds (burst traffic)
- strong overlap exists between BENIGN and ATTACK behavior
- context dominates detection quality

Therefore:
raw anomaly threshold ≠ detection rule.

Instead:
anomaly threshold produces **signal candidates** → gating turns them into alerts.

---

## 3) Alert Definition

An alert is emitted only if:

1) A detection signal crosses a defined threshold  
2) The alert passes gating policies  
3) The alert is not a duplicate or storm event  
4) The alert contains investigation context fields

---

## 4) Policy Layers (in order)

### Layer A — Threshold Gate (Signal Candidate)
Use quantile thresholds computed from BENIGN baseline.

Recommended SOC gating options:
- `p99` (more sensitive, higher noise)
- `p99.5` (balanced)
- `p99.9` (strict, lower volume)

**Rule A1**
Signal candidate triggers if:

`anomaly_score >= THRESHOLD_Q`

Where THRESHOLD_Q ∈ {p99, p99.5, p99.9}

Output:
- `signal_candidate = True`

---

### Layer B — Entity Grouping (who triggered it?)
SOC alerts must be per entity/service context, not global.

If available:
- entity = `Src IP`
- service = `Dst Port` (or Protocol)
- zone = inferred if possible (internal/external not always available in CICIDS)

**Alert grouping key**
group_key = (Src IP, Dst Port, Protocol)

If columns missing, fallback:
group_key = (Src IP) or (Dst Port) or (source_file)


---

### Layer C — Deduplication (prevent repeated identical alerts)
Dedup prevents “same thing” from creating multiple alerts.

**Rule C1**
Within a suppression window, suppress identical alerts:

- Same `group_key`
- Same dominant contributing feature (top rz feature)
- within `WINDOW_DEDUP_MIN`

Default:
- `WINDOW_DEDUP_MIN = 15 minutes` (conceptual)

---

### Layer D — Rate Limiting (alert storm control)
Rate limiting prevents one entity from dominating analyst queue.

**Rule D1**
Max alerts per entity per time window:

- max = 3 alerts per 10 minutes (conceptual)

If entity exceeds rate:
- suppress additional alerts
- record as `storm_event = True`

---

### Layer E — Severity Scoring (SOC priority)
Raw score alone is not enough. Severity combines:

- anomaly magnitude
- feature risk weight
- contextual multiplier (if available)

Proposed severity levels:
- `Low`
- `Medium`
- `High`
- `Critical`

Example scoring template:

---

### Layer C — Deduplication (prevent repeated identical alerts)
Dedup prevents “same thing” from creating multiple alerts.

**Rule C1**
Within a suppression window, suppress identical alerts:

- Same `group_key`
- Same dominant contributing feature (top rz feature)
- within `WINDOW_DEDUP_MIN`

Default:
- `WINDOW_DEDUP_MIN = 15 minutes` (conceptual)

---

### Layer D — Rate Limiting (alert storm control)
Rate limiting prevents one entity from dominating analyst queue.

**Rule D1**
Max alerts per entity per time window:

- max = 3 alerts per 10 minutes (conceptual)

If entity exceeds rate:
- suppress additional alerts
- record as `storm_event = True`

---

### Layer E — Severity Scoring (SOC priority)
Raw score alone is not enough. Severity combines:

- anomaly magnitude
- feature risk weight
- contextual multiplier (if available)

Proposed severity levels:
- `Low`
- `Medium`
- `High`
- `Critical`

Example scoring template:
severity_score =
w1 * anomaly_score
w2 * feature_risk_weight
w3 * entity_risk_multiplier


Feature risk weights (initial heuristic):
- Flow Bytes/s spike → Medium
- Flow Packets/s spike → Medium
- Large packet count deviation → High
- Multi-feature deviation spikes → High/Critical

---

### Layer F — Investigation Context (Investigation Packet)
Every alert must include the minimum fields needed for Tier-1 triage.

Required fields:
- why fired: threshold + top feature deviations
- `group_key`
- baseline deviation summary
- confidence note + expected false positive modes

---

## 5) Alert Object Schema (Phase 5.4 will implement examples)

Each alert must produce a structured object like:

```json
{
  "alert_id": "uuid",
  "timestamp": "derived_or_index",
  "group_key": {
    "src_ip": "...",
    "dst_port": "...",
    "protocol": "..."
  },
  "severity": "High",
  "signal": {
    "anomaly_score": 12.3,
    "threshold": "p99.5",
    "top_features": [
      {"feature": "Flow Packets/s", "rz": 12.3},
      {"feature": "Total Fwd Packets", "rz": 8.1}
    ]
  },
  "context": {
    "source_file": "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
    "notes": "Heavy-tail benign bursts may cause false positives"
  },
  "actions": [
    "Validate src_ip behavior against baseline",
    "Check for repeated scanning pattern",
    "Escalate if repeated across ports/services"
  ],
  "confidence": "Medium"
}

Feature risk weights (initial heuristic):
- Flow Bytes/s spike → Medium
- Flow Packets/s spike → Medium
- Large packet count deviation → High
- Multi-feature deviation spikes → High/Critical

---

### Layer F — Investigation Context (Investigation Packet)
Every alert must include the minimum fields needed for Tier-1 triage.

Required fields:
- why fired: threshold + top feature deviations
- `group_key`
- baseline deviation summary
- confidence note + expected false positive modes

---

## 5) Alert Object Schema (Phase 5.4 will implement examples)

Each alert must produce a structured object like:

```json
{
  "alert_id": "uuid",
  "timestamp": "derived_or_index",
  "group_key": {
    "src_ip": "...",
    "dst_port": "...",
    "protocol": "..."
  },
  "severity": "High",
  "signal": {
    "anomaly_score": 12.3,
    "threshold": "p99.5",
    "top_features": [
      {"feature": "Flow Packets/s", "rz": 12.3},
      {"feature": "Total Fwd Packets", "rz": 8.1}
    ]
  },
  "context": {
    "source_file": "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
    "notes": "Heavy-tail benign bursts may cause false positives"
  },
  "actions": [
    "Validate src_ip behavior against baseline",
    "Check for repeated scanning pattern",
    "Escalate if repeated across ports/services"
  ],
  "confidence": "Medium"
}
```

6) What this policy achieves

Controls alert volume without pretending anomaly score = truth

Converts raw detector output into SOC-usable alert objects

Demonstrates operational maturity (dedup + rate limiting)

Preserves the project’s core identity:
restraint + credibility + SOC realism
