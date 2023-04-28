from datetime import timedelta

# DAG defaults args
OWNER = 'kienlc'
EMAIL = 'kien291220@gmail.com'
RETRY_DELAY = timedelta(seconds=60)
RETRIES = 2
TIMEOUT = 300000

# GCP configs
PROJECT_ID = 'future-glider-383316'
GS_PATH = 'english_football'
BUCKET_NAME = 'english_football_bucket'
STAGING_DATASET = 'staging_football_dataset'
DATASET = 'football_dataset'
LOCATION = 'asia-southeast1'

# Query sources
QUERIES_SRC = './queries'
