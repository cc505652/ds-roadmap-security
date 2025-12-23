🔍 Phase 1 Breakdown — EDA as a Security Analyst
📘 Notebook 1: Dataset Understanding

Focus: Structure, scope, and caveats

Key aspects:

Multi-day traffic aggregation

Label distribution inspection

Identification of dataset quirks (e.g., column naming issues)

Explicit acknowledgment of dataset limitations

No data modification is performed.

🧹 Notebook 2: Data Cleaning

Focus: Making the data trustworthy without distortion

Steps taken:

Column name normalization

Handling infinite values

Conservative missing value removal

Removal of exact duplicate records

Key principle:

Rare events are preserved wherever possible.

📊 Notebook 3: Basic EDA (Analyst Perspective)

Focus: Behavioral understanding

Analysis includes:

Baseline distributions of normal traffic

Attack vs normal distribution comparisons

Emphasis on variance and overlap

Explicit avoidance of correlation analysis and modeling

Key insight:

No single feature cleanly separates attack and benign traffic.

⚠️ Key Observations

The dataset is highly imbalanced, reflecting real SOC conditions

Attack traffic shows greater variance, not necessarily clear separation

Significant overlap exists between normal and attack behaviors

Detection requires multi-feature reasoning, not single-metric thresholds

🚧 What This Project Does Not Do (By Design)

❌ No machine learning models

❌ No feature ranking or selection

❌ No scaling or normalization

❌ No train/test splits

❌ No accuracy or F1 claims

These are intentionally deferred to later phases.

🔜 Planned Extensions

Future phases (not yet implemented):

Phase 2: Feature behavior & correlation analysis

Phase 3: SOC & detection mapping (alerts, false positives)

Phase 4: Cloud ingestion & security architecture framing

Phase 5: Minimal, restraint-driven anomaly detection

📌 Why This Project Matters

This repository demonstrates:

disciplined analytical thinking

respect for real-world security data complexity

an understanding of SOC realities

the ability to not overclaim results

These qualities are critical for:

SOC analysts

cybersecurity engineers

security data analysts

applied data roles in security domains

🧾 Dataset

Source: CICIDS 2017 (Canadian Institute for Cybersecurity)

Nature: Simulated enterprise traffic with labeled attack scenarios

Disclaimer: Results are interpreted with dataset limitations in mind

✅ Status

Phase 1 complete.
Further phases will build incrementally on this foundation.
