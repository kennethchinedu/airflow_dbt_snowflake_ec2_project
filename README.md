# Real Estate Analytics Data Engineering Pipeline

## Overview
Welcome to my portfolio project showcasing an end-to-end data engineering pipeline designed to fetch Zillow Analytics real estate data, process it, and store valuable insights. 
This project shows  my fundamental understanding of AWS services, including EC2 and Lambda functions, as well as data engineering tools such as Airflow, Snowflake, and dbt (data build tool).

Features
### 1. AWS Infrastructure
The project is hosted on an EC2 instance, providing a robust and scalable environment for running the data engineering pipeline. The EC2 instance serves as the server for executing the pipeline tasks.

### 2. Airflow DAGs
Airflow is utilized to orchestrate the data pipeline. Directed Acyclic Graphs (DAGs) have been implemented to schedule and manage the workflow. These DAGs fetch Zillow Analytics real estate data and efficiently load it into an S3 bucket.

### 3. Lambda Function
A Lambda function is employed to create a duplicate copy of the loaded data in another S3 bucket. This redundancy ensures data durability and provides an additional layer of storage.

### 4. Snowflake Integration
The loaded data is picked up by a Snowflake pipe, facilitating its seamless transfer to a Snowflake stage. This integration ensures a secure and optimized storage solution in the cloud.

### 5. dbt Processing
dbt (data build tool) is leveraged to transform the data within Snowflake. Two-dimensional models are created:

Featured Home Model: Extracting insights related to featured properties.
Home Location Model: Analyzing and categorizing data based on geographical attributes.


#### I did not go further writing dbt test at the time of this project
