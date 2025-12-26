# Learning & Project Roadmap — Security + Data
This document outlines the structured roadmap followed to build
foundational data science skills and progressively integrate them
into cybersecurity and SOC-oriented problem solving.

The roadmap emphasizes depth, restraint, and real-world applicability
over rapid tool or model accumulation.


## Phase 0 — Foundations
**Focus:**
- Python fundamentals
- Data handling and visualization basics
- Analytical thinking and reproducibility

**Outcome:**
Ability to reason about data before applying advanced techniques.


## Phase 1 — Exploratory Data Analysis as a Security Analyst
**Objective:**
Understand network traffic data from a SOC analyst’s perspective
before attempting any modeling.

**Key Themes:**
- Dataset trust and limitations
- Conservative data cleaning
- Normal vs attack behavioral comparison
- Avoidance of premature modeling

**Primary Artifact:**
CICIDS 2017 — Phase 1 notebooks


## Phase 2 — Data Scientist Thinking (Pre-ML)
**Objective:**
Move from descriptive analysis to critical feature reasoning
without introducing machine learning.

**Key Themes:**
- Feature behavior and stability
- Variance and overlap analysis
- Correlation and assumption testing
- Identification of misleading signals

**Guiding Principle:**
Understanding why modeling would be risky before attempting it.

**Primary Artifact:**
CICIDS 2017 — Feature behavior, correlation, and insights notebooks


## Phase 3 — SOC & Detection Perspective
**Objective:**
Reframe analytical insights into detection and alerting logic
aligned with SOC workflows.

**Key Themes:**
- Alert vs signal distinction
- False positives and alert fatigue
- Analyst triage reasoning
- Operational constraints and missing context

**Primary Artifacts:**
- detection-notes.md
- soc-mapping.md


## Phase 4 — Cloud & Architecture Thinking (Planned)
**Objective:**
Translate detection logic into a cloud-based security architecture.

**Key Themes:**
- Log ingestion pipelines
- SOC visibility and monitoring
- Identity and access considerations
- Control placement and data flow

**Status:**
Planned


## Phase 5 — Minimal, Restraint-Driven ML (Optional)
**Objective:**
Use machine learning as a supporting tool, not the centerpiece.

**Key Themes:**
- Simple anomaly detection
- Emphasis on limitations
- Avoidance of accuracy-centric framing

**Guiding Principle:**
ML supports detection reasoning — it does not replace it.

**Status:**
Optional / Deferred
