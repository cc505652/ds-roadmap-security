CICIDS 2017 — Security Analytics → SOC Detection Project

This repository documents a progressive, discipline-first security analytics project built on the CICIDS 2017 dataset. The project deliberately evolves from **analysis → reasoning → SOC detection thinking**, avoiding premature modeling or metric-driven claims.

---

## 🟢 Phase 1 — EDA as a Security Analyst

### 📘 Notebook 1: Dataset Understanding  
**Focus:** Structure, scope, and caveats

**Key aspects:**
- Multi-day traffic aggregation across enterprise scenarios  
- Label distribution inspection and imbalance awareness  
- Identification of dataset quirks (e.g., column naming inconsistencies)  
- Explicit acknowledgment of simulation constraints and limitations  

**Scope control:** No data modification is performed.

---

### 🧹 Notebook 2: Data Cleaning  
**Focus:** Making the data trustworthy without distortion

**Steps taken:**
- Column name normalization  
- Handling infinite values  
- Conservative missing value removal  
- Removal of exact duplicate records  

**Key principle:** Rare events are preserved wherever possible to avoid suppressing attack behavior.

---

### 📊 Notebook 3: Basic EDA (Analyst Perspective)  
**Focus:** Behavioral understanding

**Analysis includes:**
- Baseline distributions of normal traffic  
- Attack vs normal distribution comparisons  
- Emphasis on variance, spread, and overlap  
- Explicit avoidance of correlation analysis and modeling  

**Key insight:** No single feature cleanly separates attack and benign traffic.

---

## 🟡 Phase 2 — Data Scientist Thinking (Pre-ML)

### 📘 Notebook 4: Feature Behavior Analysis  
**Focus:** Evaluating individual feature stability and usefulness

**Analysis includes:**
- Careful selection of interpretable, SOC-relevant features  
- Feature-wise comparison using summary statistics and robust plots  
- Identification of noisy, unstable, and potentially misleading features  

**Key outcome:** Visual separation does not guarantee statistical usefulness.

---

### 📘 Notebook 5: Correlation & Assumption Testing  
**Focus:** Challenging intuitive assumptions

**Analysis includes:**
- Global correlation analysis  
- Class-wise (normal vs attack) correlation comparison  
- Identification of volume-driven and redundant relationships  

**Key insight:** Correlation often reflects shared scale effects rather than detection signal.

---

### 📘 Notebook 6: Insights Summary & Pre-Detection Reasoning  
**Focus:** Synthesis and restraint

**Highlights:**
- Consolidated Phase 2 insights  
- Explicit documentation of misleading signals  
- Clear articulation of what the data does not support  

**Key takeaway:** Premature modeling would create false confidence without improving detection reliability.

---

## 🟠 Phase 3 — SOC & Detection Perspective

Phase 3 reframes the project from data analysis to **operational SOC thinking**.

### 📄 detection-notes.md
- Reinterprets analytical findings as detection signals  
- Explains why single-feature and volume-based alerts fail  
- Emphasizes false positives, alert fatigue, and analyst trust  

### 📄 soc-mapping.md
- Maps signals into a SOC workflow  
- Covers alert generation, Tier-1 triage, escalation, and uncertainty  
- Explicitly documents dataset limitations in real SOC environments  

### 📘 Notebook 7: Detection View
- Visual, communication-focused notebook  
- Demonstrates why thresholds break due to overlap and variance  
- Reinforces detection as a decision-support problem, not classification  

**Outcome:** The project now reflects how intrusion data is actually consumed in SOC operations.

---

## 🔵 Phase 3.5 — SOC Detection Stress Testing *(Complete)*

Phase 3.5 stress-tests detection thinking **without introducing ML**.

### 📘 Notebooks
- **Notebook 8:** Signal Candidate Mapping  
  `08_signal_candidate_mapping.ipynb`
- **Notebook 9:** False Positive Stress Test  
  `09_false_positive_stress_test.ipynb`
- **Notebook 10:** Context Dependency Analysis  
  `10_context_dependency_analysis.ipynb`

### 🎯 Purpose
- Map features → detection signal candidates (conceptual alerts)  
- Stress-test detection logic under false-positive constraints  
- Demonstrate why detection collapses without context (identity / asset baselines / history)  

**Key takeaway:** Detection quality is dominated by context and operational constraints, not model scores.

---

## 🔷 Phase 4 — Cloud-Agnostic SOC Telemetry Architecture *(Complete)*

Phase 4 evolves CICIDS from “dataset analysis” into **system design for real SOC pipelines**.

> Personal note: This phase is intentionally cloud-agnostic — the goal is to get the system design right first, then map it to platforms later.

### 📄 architecture.md
- Designed an end-to-end SOC telemetry pipeline:
  - telemetry sources → collection/transport → ingestion stream
  - parsing + normalization + quality checks
  - hot/cold storage + retention strategy
  - enrichment + baselining layer
  - detection layer + alerting + investigation
- Integrated Phase 3.5 lessons directly into architecture:
  - false positives dominate naive detection
  - context dependency must be solved structurally

### 📄 context-enrichment.md
- Defined enrichment and baselining as a first-class SOC layer:
  - identity context + asset criticality + network zone
  - historical baselines (quantiles/IQR), peer-group baselines
  - time awareness (business hours, backup windows)
  - alert gating + deduplication + rate-limiting

### 📄 controls-and-threat-model.md
- Threat-modeled the SOC telemetry pipeline as a high-value target:
  - SOC blinding (telemetry suppression)
  - evidence tampering
  - baseline poisoning
  - alert flooding (SOC DoS)
  - rule store privilege abuse
  - log exfiltration risks
- Defined governance controls:
  - RBAC separation, audit trails, immutability (WORM), integrity monitoring
  - “monitoring the monitoring system” design

### 🖼️ Architecture Diagram
- `diagrams/soc_telemetry_pipeline.png`

**Outcome:** The project now demonstrates realistic SOC pipeline design + governance + adversarial resilience.

---

## 🌶️ Phase 4.5 — Cloud Mapping Appendix *(Complete)*

Maps the cloud-agnostic architecture into practical service equivalents.

### 📄 cloud-mapping.md
- Pipeline stage → Azure mapping (SIEM-oriented approach)
- Pipeline stage → AWS mapping (data lake / detection pipeline approach)
- Control placement:
  - immutability, RBAC/IAM, auditability
- Operational failure modes:
  - ingestion lag, schema drift, alert storms, abnormal log access

**Outcome:** Vendor-neutral architecture with clear cloud translation readiness.

---

## ⚠️ Key Observations (Across Phases 1–4.5)
- The dataset is highly imbalanced, reflecting real SOC conditions  
- Attack traffic shows greater variance, but not clean separability  
- Significant overlap exists between normal and attack behaviors  
- Correlation and variance alone are insufficient for detection  
- False positives dominate naive threshold-based detection  
- Detection requires multi-feature, context-aware reasoning and baselining  
- SOC detection reliability depends on pipeline integrity, governance, and feedback loops  

---

## 🚧 What This Project Does Not Do (By Design)
❌ No machine learning models  
❌ No feature ranking or selection  
❌ No scaling or normalization  
❌ No train/test splits  
❌ No accuracy, F1, or ROC claims  

These are intentionally deferred until detection logic and SOC constraints are fully understood.

---

## 🔜 Future Extensions
- **Phase 5:** Minimal, restraint-driven anomaly detection  
- **Phase 6 (Optional):** Hands-on cloud implementation of pipeline subset  

If ML is introduced, it will be supporting—not central.

---

## 📌 Why This Project Matters

This repository demonstrates:
- disciplined analytical progression  
- respect for real-world security data complexity  
- SOC detection realism (false positives + context dependency)  
- architecture and governance thinking  
- ability to resist overclaiming results  

These qualities are critical for:
- SOC analysts  
- cybersecurity engineers  
- security data analysts  
- detection engineering / SIEM roles  
- cloud security architect trajectory roles  

---

## 🧾 Dataset
**Source:** CICIDS 2017 (Canadian Institute for Cybersecurity)  
**Nature:** Simulated enterprise traffic with labeled attack scenarios  
**Disclaimer:** All findings are interpreted with dataset limitations in mind.

---

## ✅ Current Status
- Phase 1 — Complete ✅  
- Phase 2 — Complete ✅  
- Phase 3 — Complete ✅  
- Phase 3.5 — Complete ✅  
- Phase 4 — Complete ✅  
- Phase 4.5 — Complete ✅  

The project continues to evolve incrementally with a security-first, SOC-aligned mindset.
