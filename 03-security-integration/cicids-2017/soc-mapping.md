# SOC Workflow Mapping — CICIDS 2017
This document maps analytical insights from the CICIDS 2017 dataset into
a conceptual Security Operations Center (SOC) workflow.

The goal is to understand how detection signals are consumed, evaluated,
and acted upon by analysts in real-world environments.

This is a conceptual mapping, not a production design.


## Data Source Context
In a real SOC environment, data similar to CICIDS 2017 would originate from:
- Network flow logs (NetFlow / IPFIX)
- IDS/IPS sensors
- Firewall traffic logs
- Network monitoring tools

These data sources are typically aggregated and normalized before being
used for detection or alerting.


## Alert Generation Stage
An alert may be generated when observed traffic deviates sufficiently
from expected baseline behavior.

Triggers could include:
- Unusual traffic persistence
- Abnormal packet volume patterns
- Asymmetric communication behavior

However, alerts are rarely generated from a single metric and often
require compound conditions.


## Tier 1 Analyst Perspective
When an alert fires, a Tier 1 analyst typically sees:
- Timestamp and basic flow metadata
- Source and destination identifiers
- Triggering conditions or rule references

At this stage, the analyst’s goal is not attribution, but triage:
- Is this alert likely benign?
- Does it warrant escalation?


## Key Triage Questions
A Tier 1 analyst may ask:
- Has this behavior been seen before?
- Is the source asset critical?
- Does the traffic align with known benign activity?
- Is there corroborating evidence from other logs?

Most alerts lack sufficient context to answer these conclusively.


## False Positive Considerations
Many behaviors that resemble attacks in isolation can be benign:
- Scheduled backups
- Software updates
- Legitimate long-lived connections
- High-throughput internal transfers

Without contextual enrichment, these scenarios generate false positives.


## Escalation Logic
If uncertainty remains, alerts may be escalated to Tier 2 analysts.

At this stage, additional context is required:
- Historical behavior of the asset
- Cross-log correlation
- External threat intelligence

CICIDS 2017 does not capture this enrichment layer.


## Dataset Limitations in SOC Context
CICIDS 2017 lacks:
- Asset criticality information
- User identity and intent
- Response actions and outcomes
- Feedback loops from analyst decisions

These limitations restrict direct translation to real SOC workflows.


## Detection Is a Decision-Support Problem
SOC detection systems assist analysts; they do not replace them.

Effective detection:
- Prioritizes analyst time
- Communicates uncertainty
- Supports investigation workflows

Overconfident alerts degrade trust and effectiveness.


## Implications for Detection System Design
Insights from this mapping suggest:
- Alerts should be explainable
- Context enrichment is essential
- Single-signal alerts are insufficient
- Analyst feedback loops matter

Detection quality is measured operationally, not statistically.


## Phase 3 Summary
Phase 3 reframed CICIDS analysis from data exploration to operational
SOC thinking.

The project now reflects:
- Alert and triage awareness
- False positive sensitivity
- Workflow-driven reasoning

This perspective prepares the foundation for future detection-oriented
or architecture-level extensions.
