# main.py

from utils.config import RAW_PREFIX, CURATED_PREFIX, DATA_FILE, BUCKET_NAME
from extract_service.extract_bls import download_raw_files, transform_to_partitioned_parquet
from utils.s3_utils import  write_df_to_s3, upload_json_to_s3
from extract_service.extract_census import fetch_datausa_population

def main():

    raw_files = download_raw_files()

    parquet_df = transform_to_partitioned_parquet(
        raw_files[DATA_FILE]
    )

    write_df_to_s3(parquet_df,
                   bucket_name=BUCKET_NAME,
                   s3_prefix_key="raw/bls_data",
                   output_format="parquet")

    data = fetch_datausa_population()

    upload_json_to_s3(
        data=data,
        bucket_name=BUCKET_NAME,
        s3_prefix_key="raw/datausa/population.json",
    )


# if __name__ == "__main__":
#     main()

def lambda_handler(event, context):
    main()
    return { "statusCode": 200, "body": "Pipeline executed successfully" }