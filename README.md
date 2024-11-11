[![CI](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml)

# PySpark Data Processing Project
## Project Overview
This project focuses on utilizing PySpark for efficient data processing on the US_birth.csv dataset. The primary objectives are to incorporate Spark SQL queries, perform data transformations, and generate a summary of descriptive statistics. The process involves extracting, transforming, and querying the dataset, followed by creating a formatted summary report.

## Dataset
We use the US_birth.csv dataset, which contains data on U.S. births. This dataset will be processed in a PySpark environment to demonstrate Spark's powerful data processing capabilities on large-scale data.

## Getting Started
### Environment Setup
1. Open Codespaces or your preferred IDE.
2. Wait for the environment setup to complete.

## Output
Spark Output Data: Generated from PySpark transformations.
Summary Markdown File: A summary file containing key statistics and insights from the dataset.
## Code Formatting and Linting
This project follows code quality standards for readability and maintenance.


## Process Overview
Data Extraction: Extracts the dataset using the extract function.
Spark Session: Initializes a Spark session via start_spark.
Data Loading: Loads the dataset into a Spark DataFrame with load_data.
Descriptive Statistics: Generates summary statistics using describe.
Query Execution: Executes a SQL query on the dataset via query.
Data Transformation: Performs additional transformations with example_transform.
End Spark Session: Closes the Spark session with end_spark.
## References
PySpark Template: https://github.com/nogibjj/python-ruff-template
Original Dataset Source: https://github.com/fivethirtyeight/data/tree/master/daily-show-guests
## GitHub Actions
This project includes GitHub Actions for CI/CD, automatically running tests and code formatting checks on each push.
echo "Trigger CI/CD workflow" >> README.md

