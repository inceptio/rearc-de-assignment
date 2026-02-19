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

###
####1. Bls public url via s3 : https://rearc-assignment-bls.s3.us-east-1.amazonaws.com/raw/bls_data/part-0.parquet

####2. json data us saved in s3://rearc-assignment-bls/raw/datausa/population.json

####3. Please find data analysis under data_analysis/rearc_data_analysis.ipynb : https://github.com/inceptio/rearc-de-assignment/blob/main/data_analysis/rearc_data_analysis.ipynb
