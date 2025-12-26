# Detection Thinking Notes — CICIDS 2017

This document reframes insights from exploratory data analysis and
feature behavior analysis into a detection and alerting perspective.

The focus is on understanding how analytical signals translate into
SOC alerts, and why many seemingly strong signals fail operationally.

This document intentionally avoids machine learning, accuracy metrics,
and model-centric thinking.

## What Detection Means in a SOC Context

In a SOC, detection does not mean classification accuracy.

Detection means:
- Raising alerts that warrant analyst attention
- Minimizing false positives that cause alert fatigue
- Providing enough context for triage and investigation

A detection system is successful only if analysts trust and act on its alerts.

## The Gap Between Data Signals and Alerts

Not every statistical signal should become an alert.

A signal becomes an alert only if:
- It is rare under normal conditions
- It is explainable to an analyst
- It provides actionable context

Many features that show variance or correlation fail at least one of
these requirements.

## Why Single-Feature Alerts Are Dangerous

Several features in CICIDS 2017 show differences between normal and
attack traffic.

However, using a single feature as an alert trigger is risky because:
- Normal traffic can produce extreme values
- Volume-driven metrics fluctuate naturally
- Attack behavior overlaps heavily with benign behavior

Single-feature thresholds often generate high false positive rates.

## Example: Flow Duration

Flow Duration appears promising because some attacks involve longer or
more persistent connections.

However:
- Legitimate long-lived connections exist (e.g., file transfers, streaming)
- Flow duration alone lacks intent and context
- Threshold-based alerts would trigger frequently in benign scenarios

Flow Duration may contribute to detection, but cannot operate alone.

## Volume-Based Signals and Alert Fatigue

Features such as packet counts and bytes per second often show large
variance during attacks.

However:
- High traffic volume is common during backups, updates, or peak usage
- Volume spikes do not inherently indicate malicious intent

Alerts based purely on volume risk overwhelming analysts with noise.
This leads to alert fatigue and reduced trust in the system.

## Behavioral Overlap Between Normal and Attack Traffic

Analysis consistently shows significant overlap between normal and
attack traffic across most features.

This overlap means:
- Clean separation is unrealistic
- Detection must tolerate ambiguity
- Analysts operate under uncertainty

Detection systems should assist decision-making, not claim certainty.

## Why Correlation Does Not Solve Detection

Correlation analysis revealed strong relationships among volume-based
features.

However:
- Correlation reflects shared scale, not malicious behavior
- Highly correlated features often encode redundant information
- Correlation does not imply usefulness for alerting

Using correlated features blindly can inflate confidence without
improving detection outcomes.

## False Positives vs False Negatives in SOC Operations

In early detection stages:
- False positives consume analyst time
- Excessive noise leads to alert suppression
- Analysts may ignore real threats buried in alerts

SOC systems often prioritize reducing false positives before improving
detection coverage.

## What the Dataset Does Not Capture

CICIDS 2017 lacks several real-world elements, including:
- User identity and intent
- Asset criticality
- Historical behavior context
- Response actions and outcomes

Detection decisions in practice rely heavily on this missing context.

## Detection Design Takeaways

Based on analysis so far:
- No single feature is sufficient for detection
- Alerts must combine multiple weak signals
- Context matters more than raw scores
- Detection is a decision-support problem, not a prediction problem

These insights motivate a shift from feature-centric thinking toward
SOC workflow and triage reasoning.

## Phase 3 Direction

The next step is to map these insights into a SOC workflow:
- Where alerts originate
- Who investigates them
- What information is required next
- Where uncertainty remains

This transition moves the project from analysis to operational thinking.
