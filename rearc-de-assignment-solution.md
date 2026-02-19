### Project Structure
rearc-de-assignment/
│
├── lambda/
│   ├── main.py
│   ├── extract_service/
│   ├── utils/
│   └── requirements.txt
│
├── terraform/
│   ├── provider.tf
│   ├── iam.tf
│   ├── lambda.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── s3.tf
├── data_analysis/
│   └── rearc_data_analysis.ipynb


### Architecture Overview

Extract BLS raw time-series files
Transform into partitioned Parquet
Upload to S3 (raw zone)
Fetch US population data from DataUSA API
Upload JSON to S3
All logic executed inside AWS Lambda
Infrastructure deployed using Terraform