# Context Enrichment & Baselining — Making SOC Detection Operational (Cloud-Agnostic)

This document designs the **context enrichment and baselining layer** of the SOC telemetry pipeline.
It is the direct architecture response to Phase 3.5 findings:

> **Detection collapses without context.**  
> Single-feature thresholds fail due to overlap and benign extremes.

The goal of this layer is to reduce false positives and increase alert explainability by attaching:
- identity and asset context
- historical baselines
- peer-group comparisons
- time / environment awareness

This is **not ML**. This is detection engineering and SOC realism.

---

## 1) Why Context Is Required (Phase 3.5 Link)

CICIDS-style telemetry contains flow-level attributes (duration, bytes, packets).
However, Phase 3.5 showed that:

- BENIGN flows can exceed high thresholds (q99)
- Attack and BENIGN distributions overlap heavily
- Volume spikes are often benign (backups, updates, peak usage)
- Correlated features can create redundant, noisy alerting

Therefore, detection must shift from:

> **absolute thresholds** → **relative deviations from baseline + context gating**

---

## 2) Enrichment Layer — What Gets Added

Each telemetry event is enriched with external context before detection logic is applied.

### Enrichment categories
1) **Identity Context**
2) **Asset Context**
3) **Network Context**
4) **Historical Baseline Context**
5) **Peer Group Context**
6) **Temporal (Time) Context**
7) **Known Benign Patterns**

---

## 3) Identity Context

Identity context answers: **who is responsible for the behavior?**

### Fields
- user / service identity (if applicable)
- authentication method / session type
- privilege level (regular vs admin)
- identity reputation / risk tier

### Why it matters
A high-volume flow from:
- a known backup service account → likely benign
- an unknown identity on a workstation → higher risk

---

## 4) Asset Context

Asset context answers: **what system is involved and how important is it?**

### Fields
- asset role (server, workstation, IoT, domain controller)
- criticality tier (low/medium/high)
- ownership (team/system owner)
- environment tag (prod/dev/test)
- expected services and ports

### Why it matters
The same telemetry signal has different meaning on:
- a DB server in production
- a student laptop
- a test VM

---

## 5) Network Context

Network context answers: **where is the traffic happening?**

### Fields
- network zone (internal, DMZ, external)
- subnet classification
- destination category (internal host vs internet)
- geo-location / ASN (if external)
- destination rarity (new vs common)

### Why it matters
A port scan inside the same subnet may be normal inventory activity,
but scanning across sensitive zones is higher risk.

---

## 6) Historical Baselining (Non-ML)

Baselining answers: **what is normal for this entity?**

This is the highest impact false-positive reducer.

### Baseline types
- per asset baseline
- per identity baseline
- per asset+service baseline
- per subnet baseline
- per zone baseline

### Baseline statistics stored
For each entity + time window:
- median
- p90 / p95 / p99
- IQR range
- typical destination count
- typical bytes/sec range

Key principle:
> Use robust statistics (quantiles), not mean-only baselines.

---

## 7) Peer Group Baselining

Peer baselines answer: **is this normal compared to similar assets?**

### Peer grouping examples
- all workstations
- all DB servers
- all student labs
- all internal DNS servers

### Why this matters
Some assets have naturally high throughput.
Peer baselines prevent unfair alerting on “high-activity” systems.

---

## 8) Temporal Context (Time Awareness)

Time context answers: **is this happening at a normal time?**

### Fields
- business hours vs off-hours
- weekend vs weekday
- patch window / backup window flags
- known high-load schedule windows

### Why it matters
Some suspicious-looking spikes are benign because they are scheduled.

---

## 9) Baseline Store & Refresh Strategy

Baselines must be stored and refreshed continuously.

### Baseline store requirements
- queryable by entity + time window
- versioned (baseline changes over time)
- support for drift detection
- retention for comparisons

### Refresh schedule (example)
- compute baselines daily for last 7–30 days
- store rolling baselines for:
  - last 7 days (short-term)
  - last 30 days (stable)
  - last 90 days (seasonality)

### Drift handling
Baselines must adapt without enabling attacker “slow training”.
Use:
- bounded updates
- manual review for high-risk assets
- anomaly exclusion during baseline computation

---

## 10) Context-Aware Detection Logic (No ML)

This layer enables detection logic that is:
- explainable
- baseline-relative
- operationally safe

### Bad detection (naive)
- `Flow Bytes/s > threshold`

### Better detection (context-aware)
- `Flow Bytes/s > asset_baseline_p99 * 1.5`
AND
- `destination_rarity = high`
AND
- `NOT in_known_backup_window`
AND
- `asset_criticality >= medium`

---

## 11) Example: Alert Explanation Template

When an alert fires, context must be visible.

Example explanation:

- Trigger: High bytes/sec deviation
- Asset: FINANCE-DB-01 (critical)
- Baseline: p99 bytes/sec = X, observed = 1.8× p99
- Destination: new external IP (rare)
- Time: off-hours
- Corroboration: increased packet asymmetry

This makes alerts **trustworthy**.

---

## 12) False Positive Controls (SOC Engineering)

### Alert gating techniques
- **time gating** (ignore known benign windows)
- **role gating** (servers behave differently)
- **destination gating** (rare destinations weighted higher)
- **rate limiting** (avoid alert storms)
- **deduplication** (same root cause alert grouping)

### Alert hygiene
- suppress low-impact repeat alerts
- aggregate by entity + time window
- create “incident candidates” instead of raw alerts

---

## 13) Feedback Loop Integration

Analyst outcomes must flow back.

Feedback captured:
- true positive / false positive
- reason tags (benign backup, dev testing, scanner)
- recommended tuning (increase threshold factor, add gating)

Feedback updates:
- rule conditions
- enrichment mappings
- baseline computation exclusions

Key principle:
> Without feedback, detection systems decay.

---

## 14) Summary

This enrichment and baselining design operationalizes the biggest lesson from CICIDS Phase 3.5:

- telemetry without context creates false positives
- thresholds without baselines are unstable
- detection must be relative, explainable, and workflow-aware

This layer enables a SOC pipeline to treat CICIDS-style telemetry as a realistic detection system
rather than a static dataset.
