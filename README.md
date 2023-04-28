## Introduction
This ETL pipeline is a process that extracts the english football datasets from Google Cloud Storage (GCS), transforms it, and then loads these data into Google BigQuery (BQ) using Airflow on Google Cloud Composer.

## Requirements
To build this pipeline, you will need the following:
* A Google Cloud Platform (GCP) account with access to GCS, BQ, Google Cloud Composer
* Apache Airflow
* Python

## Steps:
* The first step is to extract the data from GCS.
* After extracted the data, you will create and load these extracted data into a staging area on BQ.
* Once the data is in the staging area, you need to transform it depend on your business.
* Then design task flows to load these transform data into BQ by using Airflow.

## Conclusion:
In summary, building an ETL data pipeline that extracts data from GCS, transforms it, and loads it into BQ requires a GCP account, Airflow, and Python. With this pipeline, you can move data from GCS into BQ for analysis and reporting.
