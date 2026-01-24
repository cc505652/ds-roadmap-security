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

### Phase 5 — Detection Engineering Layer

* Built robust baselines (median + MAD)
* Implemented minimal anomaly detection (interpretable, single method)
* Added alert gating, deduplication, rate limiting, and severity
* Generated investigation packets for analyst consumption
* Evaluated system using SOC metrics (alert volume, workload, stability)

Each phase intentionally avoids overclaiming and builds toward **operational credibility** rather than flashy results.


Then we continue.
