🔍 Phase 1 Breakdown — EDA as a Security Analyst

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

🟡 Phase 2 Breakdown — Data Scientist Thinking (Pre-ML)

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

⚠️ Key Observations (Across Phases 1 & 2)

The dataset is highly imbalanced, reflecting real SOC conditions

Attack traffic exhibits greater variance, not clean separability

Significant overlap exists between normal and attack behaviors

Correlation and variance alone are insufficient for detection

Detection requires multi-feature, context-aware reasoning

🚧 What This Project Does Not Do (By Design)

❌ No machine learning models
❌ No feature ranking or selection
❌ No scaling or normalization
❌ No train/test splits
❌ No accuracy, F1, or ROC claims

These are intentionally deferred until detection logic and SOC constraints are clearly framed.

🔜 Planned Extensions

Future phases (incremental by design):

Phase 3: SOC & detection mapping

alerts, false positives, triage thinking

Phase 4: Cloud ingestion & security architecture framing

Phase 5: Minimal, restraint-driven anomaly detection

Machine learning, if used, will be supporting—not central.

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

✅ Status

Phase 1 and Phase 2 complete.
Subsequent phases will build incrementally on this foundation.
