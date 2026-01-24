# CICIDS 2017 — Detection Engineering Design Review

---

## 1. Problem Statement

Modern Security Operations Centers (SOCs) struggle not with a lack of detection logic, but with **alert overload, false positives, and analyst fatigue**.
Many intrusion detection approaches focus on improving model accuracy, while ignoring whether the resulting alerts are *operationally usable*.

The core problem this project addresses is:

> **How can raw network telemetry be transformed into a small, trustworthy, SOC-actionable alert queue—without relying on heavy machine learning or overconfident metrics?**

This project treats intrusion detection as a **detection engineering problem**, not a classification exercise.
The objective is not to maximize detections, but to design a system that:

* respects SOC constraints,
* produces explainable alerts,
* minimizes analyst workload,
* and remains robust under noisy, imbalanced traffic.

---

## 2. Dataset Constraints & Reality

This project is built on the **CICIDS 2017 dataset**, a labeled collection of simulated enterprise network traffic.

While widely used in academic research, CICIDS has important limitations that must be acknowledged:

* Traffic is **simulated**, not organically generated
* Attacks occur in **bursty, scripted scenarios**
* Data is **highly imbalanced** (BENIGN traffic dominates)
* No real asset identity, user context, or business criticality exists
* Timestamp granularity is insufficient for clean daily baselining

Instead of ignoring these constraints, the project treats them as **design inputs**.

Key design choices influenced by dataset reality:

* Avoidance of train/test split obsession
* Conservative handling of rare events
* Use of `source_file` as a proxy for operational “day”
* Explicit documentation of blind spots and assumptions

The goal is not to claim real-world performance, but to demonstrate **sound detection reasoning under imperfect data conditions**.

---

## 3. Why Naïve Detection Fails

Early analysis of CICIDS quickly reveals why many intrusion detection approaches fail in practice:

### Single-feature thresholds collapse

* BENIGN traffic often exceeds high quantiles (p99, p99.5)
* Attack and normal behaviors overlap heavily
* Variance, not separation, dominates feature distributions

### Correlation is misleading

* Many features correlate due to shared volume effects
* Correlation strength does not imply detection usefulness
* Independent thresholding increases false positives

### Raw anomaly scores are not alerts

* Anomaly ≠ malicious intent
* Detector outputs without policy controls create alert storms
* High recall without gating destroys analyst trust

These observations motivate a core principle of this project:

> **Detection quality is determined more by alert policy and context than by model sophistication.**

---

## 4. Project Evolution (Phase 1 → Phase 5)

This project intentionally evolves in disciplined stages, mirroring how detection systems mature in real SOC environments.

### Phase 1 — EDA as a Security Analyst

* Dataset understanding and conservative cleaning
* No modeling, no correlation, no assumptions
* Focused on understanding “normal” vs “attack” behavior

### Phase 2 — Data Scientist Thinking (Pre-ML)

* Feature behavior analysis and correlation stress-testing
* Explicit identification of misleading signals
* Avoided premature modeling despite temptation

### Phase 3 — SOC & Detection Perspective

* Reframed analysis into detection signals
* Mapped features to alert concepts
* Introduced false positives, triage, and alert fatigue thinking

### Phase 3.5 — Detection Stress Testing

* Broke naïve detection logic under realistic thresholds
* Demonstrated context dependency and alert instability
* Proved why single-metric detection fails operationally

### Phase 4 / 4.5 — Architecture & Cloud Mapping

* Designed a cloud-agnostic SOC telemetry pipeline
* Integrated baselining, enrichment, governance, and threat modeling
* Mapped architecture to Azure and AWS equivalents


## 5. Detection Engineering Layer

The detection layer is intentionally minimal by design.

Rather than relying on multiple models or opaque scoring systems, this project implements a **single, interpretable anomaly detector** supported by strong policy controls.

### Baseline Modeling

* Baselines are built **only from BENIGN traffic**
* Robust statistics are used:

  * median
  * Median Absolute Deviation (MAD)
* This choice avoids sensitivity to heavy tails and outliers

Baselines are treated as **behavioral references**, not truth.

### Anomaly Scoring

* A robust z-score is computed per feature:

  `|x − median| / MAD`
* Feature deviations are aggregated conservatively using:

  `anomaly_score = max(feature deviations)`

This produces:

* an interpretable score
* no probability claims
* no accuracy claims

The detector answers only one question:

> “How unusual is this flow relative to known normal behavior?”


### 6. Alert Economics & SOC Impact

Raw anomaly scores are **never alerts**.

This project explicitly separates:

* detection (scoring)
* alerting (policy)

### Alert Gating Controls

The following SOC-native controls are applied:

* **Quantile-based thresholds**

  * p95 → exploratory
  * p99 → aggressive
  * p99.5 → production-like
* **Deduplication**

  * repeated alerts collapsed by entity
* **Rate limiting**

  * one alert per entity per window
* **Severity scoring**

  * anomaly magnitude + context weighting

### Resulting Alert Economics

After full gating:

* alert volume collapses from tens of thousands to **single digits**
* analyst workload drops to **minutes per day**
* false positives remain, but are bounded and explainable

This demonstrates a critical SOC principle:

> A detection system succeeds when analysts trust the alerts—not when it detects everything.


## 7. Architecture Overview

The detection logic operates inside a **cloud-agnostic SOC telemetry pipeline** designed in Phase 4.

### Pipeline Stages

1. Telemetry sources (network flows, logs)
2. Collection and transport
3. Parsing and normalization
4. Quality checks and schema enforcement
5. Hot / cold storage with retention
6. Enrichment and baselining
7. Detection and alerting
8. Investigation and response

### Key Architectural Insights

* Context must be added **before detection**, not after
* Baselines belong in the enrichment layer
* Detection logic must assume **noisy inputs**
* Governance and integrity controls are as important as detection logic

The architecture treats the SOC itself as a **high-value system under attack**, not a passive observer.


## 8. Threat Model & Controls

The telemetry pipeline is threat-modeled as an attack surface.

### Key Threats Considered

* Telemetry suppression (SOC blinding)
* Baseline poisoning
* Alert flooding (SOC denial of service)
* Rule tampering
* Evidence deletion or manipulation
* Unauthorized log access

### Controls Defined

* RBAC separation between detection authors and operators
* Immutable storage (WORM) for raw logs
* Audit trails for rule changes
* Integrity monitoring on baselines
* Alert rate limiting and suppression windows

This ensures the detection system is **defensible**, not just functional.


## 9. What This System Can and Cannot Do

### What it CAN do

* Produce a small, high-confidence alert queue
* Provide explainable alert context
* Support analyst triage and investigation
* Scale conceptually to real SOC environments
* Integrate with SIEM platforms

### What it CANNOT do

* Guarantee detection of all attacks
* Replace analyst judgment
* Claim real-world accuracy metrics
* Operate without context or governance
* Compete with production IDS systems

These limitations are intentional and explicitly documented.


## 10. Conclusion — Why This Is SOC-Ready

This project does not attempt to build a “perfect detector”.

Instead, it demonstrates:

* disciplined analytical progression
* respect for data limitations
* realistic SOC economics
* detection engineering maturity
* architectural and governance awareness

By prioritizing **alert quality over quantity**, and **credibility over performance claims**, the system reflects how intrusion detection actually works in production environments.
The value of this system lies not in detection novelty, but in its disciplined alignment with how real SOCs operate under uncertainty, scale, and constraint.

This makes the project suitable for:

* SOC analyst roles
* detection engineering roles
* security architecture discussions
* consulting and solution design interviews
