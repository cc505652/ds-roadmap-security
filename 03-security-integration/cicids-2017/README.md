🔍 CICIDS 2017 — Security Analytics → SOC Detection Project

This repository documents a progressive, discipline-first security analytics project built on the CICIDS 2017 dataset.
The project deliberately evolves from analysis → reasoning → SOC detection thinking, avoiding premature modeling or metric-driven claims.

🟢 Phase 1 — EDA as a Security Analyst

📘 Notebook 1: Dataset Understanding

Focus: Structure, scope, and caveats

Key aspects:

Multi-day traffic aggregation across enterprise scenarios

Label distribution inspection and imbalance awareness

Identification of dataset quirks (e.g., column naming inconsistencies)

Explicit acknowledgment of simulation constraints and limitations

Scope control:
No data modification is performed.

🧹 Notebook 2: Data Cleaning

Focus: Making the data trustworthy without distortion

Steps taken:

Column name normalization

Handling infinite values

Conservative missing value removal

Removal of exact duplicate records

Key principle:
Rare events are preserved wherever possible to avoid suppressing attack behavior.

📊 Notebook 3: Basic EDA (Analyst Perspective)

Focus: Behavioral understanding

Analysis includes:

Baseline distributions of normal traffic

Attack vs normal distribution comparisons

Emphasis on variance, spread, and overlap

Explicit avoidance of correlation analysis and modeling

Key insight:
No single feature cleanly separates attack and benign traffic.

🟡 Phase 2 — Data Scientist Thinking (Pre-ML)

📘 Notebook 4: Feature Behavior Analysis

Focus: Evaluating individual feature stability and usefulness

Analysis includes:

Careful selection of interpretable, SOC-relevant features

Feature-wise comparison using summary statistics and robust plots

Identification of noisy, unstable, and potentially misleading features

Key outcome:
Visual separation does not guarantee statistical usefulness.

📘 Notebook 5: Correlation & Assumption Testing

Focus: Challenging intuitive assumptions

Analysis includes:

Global correlation analysis

Class-wise (normal vs attack) correlation comparison

Identification of volume-driven and redundant relationships

Key insight:
Correlation often reflects shared scale effects rather than detection signal.

📘 Notebook 6: Insights Summary & Pre-Detection Reasoning

Focus: Synthesis and restraint

Highlights:

Consolidated Phase 2 insights

Explicit documentation of misleading signals

Clear articulation of what the data does not support

Key takeaway:
Premature modeling would create false confidence without improving detection reliability.

🟠 Phase 3 — SOC & Detection Perspective

Phase 3 reframes the project from data analysis to operational SOC thinking.

📄 detection-notes.md

Reinterprets analytical findings as detection signals

Explains why single-feature and volume-based alerts fail

Emphasizes false positives, alert fatigue, and analyst trust

📄 soc-mapping.md

Maps signals into a SOC workflow

Covers alert generation, Tier-1 triage, escalation, and uncertainty

Explicitly documents dataset limitations in real SOC environments

📘 Notebook 7: Detection View

Visual, communication-focused notebook

Demonstrates why thresholds break due to overlap and variance

Reinforces detection as a decision-support problem, not classification

Outcome:
The project now reflects how intrusion data is actually consumed in SOC operations.

🔵 Phase 3.5 — SOC Detection Stress Testing (Planned / In Progress)

Phase 3.5 stress-tests detection thinking without introducing ML.

08_signal_candidate_mapping.ipynb
09_false_positive_stress_test.ipynb
10_context_dependency_analysis.ipynb


Purpose:

Map features → hypothetical detection signals

Evaluate false-positive behavior under reasonable thresholds

Demonstrate why detection depends on context, not isolated metrics

This phase focuses on breaking naive detection logic, not optimizing it.

⚠️ Key Observations (Across Phases 1–3)

The dataset is highly imbalanced, reflecting real SOC conditions

Attack traffic shows greater variance, not clean separability

Significant overlap exists between normal and attack behaviors

Correlation and variance alone are insufficient for detection

Detection requires multi-feature, context-aware reasoning

🚧 What This Project Does Not Do (By Design)

❌ No machine learning models
❌ No feature ranking or selection
❌ No scaling or normalization
❌ No train/test splits
❌ No accuracy, F1, or ROC claims

These are intentionally deferred until detection logic and SOC constraints are fully understood.

🔜 Future Extensions

Phase 4: Cloud ingestion & security architecture framing

Phase 5: Minimal, restraint-driven anomaly detection

If ML is introduced, it will be supporting, not central.

📌 Why This Project Matters

This repository demonstrates:

disciplined analytical progression

respect for real-world security data complexity

understanding of SOC realities and trade-offs

ability to resist overclaiming results

These qualities are critical for:

SOC analysts

cybersecurity engineers

security data analysts

applied data roles in security domains

🧾 Dataset

Source: CICIDS 2017 (Canadian Institute for Cybersecurity)

Nature: Simulated enterprise traffic with labeled attack scenarios

Disclaimer: All findings are interpreted with dataset limitations in mind

✅ Current Status

Phase 1 — Complete

Phase 2 — Complete

Phase 3 — Complete

Phase 3.5 — Planned / In Progress

The project continues to evolve incrementally with a security-first, SOC-aligned mindset.
