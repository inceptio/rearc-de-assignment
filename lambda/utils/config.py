# config.py

BLS_BASE_URL = "https://download.bls.gov/pub/time.series/pr/"

DATA_FILE = "pr.data.1.AllData"



DATAUSA_BSA_URL = "https://honolulu-api.datausa.io/tesseract"

OTHER_FILES = [
    "pr.series",
    "pr.class",
    "pr.measure",
    "pr.period",
    "pr.sector",
    "pr.duration",
    "pr.seasonal",
    "pr.footnote",
    "pr.contacts",
    "pr.txt",
]

BUCKET_NAME = "rearc-assignment-bls"
RAW_PREFIX = "raw/bls/pr/"
CURATED_PREFIX = "curated/bls/pr/"

S3_REGION = "us-east-1"
HEADERS = {
    "User-Agent": "BLS-Data-Engineering/1.0 (contact: your-email@example.com)"
}
