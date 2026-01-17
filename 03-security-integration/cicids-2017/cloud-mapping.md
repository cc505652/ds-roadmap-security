# Phase 4.5 — Cloud Mapping Appendix (Azure + AWS)

This appendix maps the **cloud-agnostic SOC telemetry pipeline** (Phase 4)
to practical implementations on major cloud platforms.

Scope:
- Vendor mapping only (no deployment)
- Focus on SOC telemetry, detection, governance, and investigation flows
- Emphasizes where Phase 3.5 lessons (false positives + context dependency)
  are handled in real cloud architectures

This appendix allows the design to remain platform-neutral while still
showing readiness to translate architecture into cloud-native services.

---

## 1) Pipeline Stages Recap

The Phase 4 pipeline includes:
1) Telemetry Sources
2) Collection & Transport
3) Ingestion Buffer / Stream
4) Parsing + Normalization + Quality Checks
5) Storage (Hot / Cold)
6) Enrichment + Baselines
7) Detection Layer
8) Alerting + Case Management
9) Investigation + Feedback Loop
10) Security Controls & Governance

---

## 2) Azure Mapping (Conceptual)

### 2.1 Stage-by-stage mapping

| Pipeline Stage | Azure Service Mapping (Examples) |
|---|---|
| Telemetry Sources | NSG Flow Logs, Firewall Logs, DNS Logs, Endpoint telemetry (Defender), app/service logs |
| Collection & Transport | Azure Monitor Agent / Data Collection Rules, Syslog connectors |
| Ingestion Buffer / Stream | Event Hubs (stream), Service Bus (queue) |
| Parsing + Normalization | Azure Data Explorer ingestion / Log ingestion pipelines / Function-based parsing |
| Hot Store | Log Analytics Workspace / Azure Data Explorer |
| Cold Store | Azure Storage (Blob) with lifecycle policies + immutability (WORM) |
| Enrichment | Sentinel Watchlists, Logic Apps enrichment, custom enrichment tables in ADX |
| Detection Layer | Microsoft Sentinel analytics rules, KQL queries, scheduled detections |
| Alerting / Case Mgmt | Sentinel incidents + SOAR (Logic Apps) |
| Investigation | Sentinel investigation graphs, hunting queries, workbooks |
| Feedback loop | Incident disposition labels + analytics rule tuning |

---

### 2.2 Why Azure fits SOC workflows well
Azure SOC architectures become simpler because:
- Sentinel integrates detection + case management
- KQL is strong for investigation/hunting
- Identity context is natural via Entra ID logs and Defender telemetry

---

## 3) AWS Mapping (Conceptual)

### 3.1 Stage-by-stage mapping

| Pipeline Stage | AWS Service Mapping (Examples) |
|---|---|
| Telemetry Sources | VPC Flow Logs, CloudTrail, Route53 Resolver logs, ALB logs, endpoint telemetry |
| Collection & Transport | Kinesis Agent / CloudWatch Agent, syslog forwarders |
| Ingestion Buffer / Stream | Kinesis Data Streams / SQS |
| Parsing + Normalization | Lambda for parsing + Glue ETL for normalization |
| Hot Store | OpenSearch (for search), CloudWatch Logs |
| Cold Store | S3 (data lake) + lifecycle policies + Object Lock (WORM) |
| Enrichment | DynamoDB/Glue tables for enrichment + SIEM enrichment workflows |
| Detection Layer | GuardDuty + Security Hub + custom detections via Lambda/OpenSearch |
| Alerting / Case Mgmt | Security Hub findings + EventBridge routing |
| Investigation | Athena queries on S3, OpenSearch dashboards |
| Feedback loop | workflow states in Security Hub + rule tuning iteration |

---

### 3.2 Why AWS SOC pipelines often become “data-lake” first
AWS SOC setups commonly treat S3 as the long-term truth:
- S3 is the immutable evidence store
- Athena queries support investigation at scale
- OpenSearch is used for hot indexing/search

---

## 4) Control Placement (Where Security Belongs)

This section shows where Phase 4 controls (threat model) are enforced.

### 4.1 Integrity + Tamper Resistance
- Azure: Storage immutability policies (WORM), immutable retention
- AWS: S3 Object Lock (WORM), versioning, bucket policies

### 4.2 Identity + Access Governance (RBAC)
- Azure: Azure RBAC + Conditional Access + Privileged Identity Management (PIM)
- AWS: IAM policies + IAM Identity Center + SCPs (Organizations)

### 4.3 Auditability
- Azure: Activity logs + diagnostic logs + Sentinel auditing
- AWS: CloudTrail + Config + Security Hub workflow visibility

Key principle:
> SOC pipeline changes must be auditable, version-controlled, and rollbackable.

---

## 5) Where Phase 3.5 Lessons Are Solved in Cloud Architectures

Phase 3.5 proved:
- false positives dominate naive thresholds
- context dependency is critical

Cloud architectures address this using:

### 5.1 Enrichment (Identity + Asset + Baselines)
- Azure: Sentinel watchlists + enrichment tables + identity integration
- AWS: enrichment tables in DynamoDB/Glue + joinable metadata in Athena/OpenSearch

### 5.2 Baselining (Non-ML + “normal behavior”)
- Azure: KQL baselines per entity/time window
- AWS: Athena-based baselines + scheduled analytics + entity summaries in storage

### 5.3 Alert hygiene (noise reduction)
- deduplication via incident grouping
- severity gating via asset criticality
- routing rules to reduce analyst overload

---

## 6) Failure Modes & Operational Monitoring (Meta-Monitoring)

SOC pipelines must detect failure in the monitoring itself.

### Must-alert conditions
- ingestion lag spikes
- missing telemetry from critical sensors
- schema drift in parsed logs
- alert storms (sudden spike in low-confidence alerts)
- unusual data access (log scraping behavior)
- detection rule/config modification

Cloud-native signals:
- Azure: workspace ingestion health + rule change logs
- AWS: CloudTrail rule changes + Kinesis lag + bucket access anomalies

Key principle:
> Missing logs are themselves a security event.

---

## 7) Minimal “Internship-Ready” Implementation Choice

If implementing a simplified internship-grade version:

### Option A (Azure-first)
- Ingest logs into Log Analytics
- Build a small set of Sentinel analytics rules
- Add watchlist enrichment (asset criticality)
- Use incidents + investigation workflow

### Option B (AWS-first)
- Store telemetry in S3 (data lake)
- Use Athena for queries and baseline summaries
- Use Security Hub for centralized findings
- Index key subsets into OpenSearch for fast search

---

## 8) Summary

This appendix demonstrates that the Phase 4 SOC telemetry pipeline:
- remains cloud-agnostic and architecturally valid
- maps cleanly into Azure and AWS implementations
- preserves SOC-first principles: explainability, governance, integrity
- explicitly addresses Phase 3.5 constraints:
  - false positives
  - context dependency
  - alert fatigue

The core idea remains unchanged across vendors:

> Effective SOC detection is a governed system design problem, not a model score problem.
