# Data Analytics Essentials – Projects & Data Gathering

## What is a Data Analytics Project
A data analytics project aims to answer a specific question using data.
The focus is on insight and decision-making, not tools.

## Project Lifecycle
1. Define the problem
2. Identify required data
3. Collect data
4. Clean and prepare data
5. Analyze using statistics
6. Communicate insights

## Common Failure Points
- Poor problem definition
- Low-quality or biased data
- Overreliance on tools
- Ignoring data limitations

## Data Gathering
Data can come from:
- Databases
- Files (CSV, Excel)
- Logs
- APIs
- Sensors

Cybersecurity data is often log-based and semi-structured.

## Data Quality Dimensions
- Accuracy
- Completeness
- Consistency
- Timeliness
- Relevance

## Key Insight
Asking the right questions about data is more important than using advanced tools.


## Data Cleaning and Preparation

Data cleaning is the process of fixing missing values, duplicates,
incorrect formats, and inconsistencies before analysis.

### Common Issues
- Missing values
- Duplicates
- Incorrect data types
- Inconsistent formats
- Outliers

### Handling Missing Data
Options include removing rows, filling with statistical values,
or using domain-specific defaults.

### Outliers
Outliers should be investigated before removal, especially in
security datasets where rare events may indicate attacks.

## Data Transformation Concepts

Transformation prepares data for analysis through:
- Aggregation
- Normalization
- Feature creation
- Filtering and sorting

Excel transformations represent logical operations that later
map to Python-based workflows.

## Statistics in Data Analytics

Statistical measures help summarize and interpret data distributions.
In skewed datasets, median and variance are often more informative than mean.

Security datasets are typically imbalanced, making naive accuracy misleading.
