from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCheckOperator, BigQueryExecuteQueryOperator
from configs import OWNER, EMAIL, RETRIES, RETRY_DELAY, TIMEOUT, BUCKET_NAME, PROJECT_ID, GS_PATH, STAGING_DATASET, DATASET, LOCATION, QUERIES_SRC
from schema_fields import TEAM_SCHEMA_FIELDS, SEASON_SCHEMA_FIELDS, STANDING_SCHEMA_FIELDS, MATCH_SCHEMA_FIELDS

default_args = {
    'owner': OWNER,
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email_on_failure': EMAIL,
    'email_on_retry': EMAIL,
    'retries': RETRIES,
    'retry_delay': RETRY_DELAY,
    'timeout_seconds': TIMEOUT,
}

with DAG('gcs_to_bigquery', default_args=default_args, schedule_interval="@once") as dag:

    init_pipeline = DummyOperator(task_id='initial_pipeline', dag=dag)

    # Loading staging datasets from GCS to staging areas
    load_staging_dataset = DummyOperator(
        task_id='load_staging_dataset', dag=dag)

    load_staging_teams = GCSToBigQueryOperator(
        task_id='load_teams',
        bucket=BUCKET_NAME,
        source_objects=[f'{GS_PATH}/teams.csv'],
        destination_project_dataset_table=f'{PROJECT_ID}.{STAGING_DATASET}.staging_teams',
        source_format='csv',
        write_disposition='WRITE_TRUNCATE',
        skip_leading_rows=1,
        allow_quoted_newlines='true',
        schema_fields=TEAM_SCHEMA_FIELDS)

    load_staging_seasons = GCSToBigQueryOperator(
        task_id='load_seasons',
        bucket=BUCKET_NAME,
        source_objects=[f'{GS_PATH}/seasons.csv'],
        destination_project_dataset_table=f'{PROJECT_ID}.{STAGING_DATASET}.staging_seasons',
        source_format='csv',
        write_disposition='WRITE_TRUNCATE',
        skip_leading_rows=1,
        allow_quoted_newlines='true',
        schema_fields=SEASON_SCHEMA_FIELDS)

    load_staging_standings = GCSToBigQueryOperator(
        task_id='load_standings',
        bucket=BUCKET_NAME,
        source_objects=[f'{GS_PATH}/standings.csv'],
        destination_project_dataset_table=f'{PROJECT_ID}.{STAGING_DATASET}.staging_standings',
        source_format='csv',
        write_disposition='WRITE_TRUNCATE',
        skip_leading_rows=1,
        allow_quoted_newlines='true',
        schema_fields=STANDING_SCHEMA_FIELDS)

    load_staging_matches = GCSToBigQueryOperator(
        task_id='load_matches',
        bucket=BUCKET_NAME,
        source_objects=[f'{GS_PATH}/matches.csv'],
        destination_project_dataset_table=f'{PROJECT_ID}.{STAGING_DATASET}.staging_matches',
        source_format='csv',
        write_disposition='WRITE_TRUNCATE',
        skip_leading_rows=1,
        allow_quoted_newlines='true',
        schema_fields=MATCH_SCHEMA_FIELDS)

    check_staging_teams = BigQueryCheckOperator(
        task_id='check_staging_teams',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'SELECT COUNT(*) FROM {PROJECT_ID}.{STAGING_DATASET}.staging_teams'
    )

    check_staging_seasons = BigQueryCheckOperator(
        task_id='check_staging_seasons',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'SELECT COUNT(*) FROM {PROJECT_ID}.{STAGING_DATASET}.staging_seasons'
    )

    check_staging_standings = BigQueryCheckOperator(
        task_id='check_staging_standings',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'SELECT COUNT(*) FROM {PROJECT_ID}.{STAGING_DATASET}.staging_standings'
    )

    check_staging_matches = BigQueryCheckOperator(
        task_id='check_staging_matches',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'SELECT COUNT(*) FROM {PROJECT_ID}.{STAGING_DATASET}.staging_matches'
    )

    # Create dim and fact tables from staging areas
    create_dim_table = DummyOperator(task_id='create_dim_table', dag=dag)

    create_dim_teams = BigQueryExecuteQueryOperator(
        task_id='create_dim_teams',
        destination_dataset_table=f'{PROJECT_ID}.{DATASET}.dim_teams',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_TRUNCATE',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'{QUERIES_SRC}/dim_teams.sql'
    )

    create_dim_seasons = BigQueryExecuteQueryOperator(
        task_id='create_dim_seasons',
        destination_dataset_table=f'{PROJECT_ID}.{DATASET}.dim_seasons',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_TRUNCATE',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'{QUERIES_SRC}/dim_seasons.sql'
    )

    check_dim_teams = BigQueryCheckOperator(
        task_id='check_dim_teams',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'SELECT COUNT(*) FROM {PROJECT_ID}.{DATASET}.dim_teams'
    )

    check_dim_seasons = BigQueryCheckOperator(
        task_id='check_dim_seasons',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'SELECT COUNT(*) FROM {PROJECT_ID}.{DATASET}.dim_seasons')

    create_fact_table = DummyOperator(task_id='create_fact_table', dag=dag)

    create_fact_matches = BigQueryExecuteQueryOperator(
        task_id='create_fact_matches',
        destination_dataset_table=f'{PROJECT_ID}.{DATASET}.fact_matches',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_TRUNCATE',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'{QUERIES_SRC}/fact_matches.sql'
    )

    create_fact_goals = BigQueryExecuteQueryOperator(
        task_id='create_fact_goals',
        destination_dataset_table=f'{PROJECT_ID}.{DATASET}.fact_goals',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_TRUNCATE',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'{QUERIES_SRC}/fact_goals.sql'
    )

    create_fact_standings = BigQueryExecuteQueryOperator(
        task_id='create_fact_standings',
        destination_dataset_table=f'{PROJECT_ID}.{DATASET}.fact_standings',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_TRUNCATE',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'{QUERIES_SRC}/fact_standings.sql'
    )

    check_fact_matches = BigQueryCheckOperator(
        task_id='check_fact_matches',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'SELECT COUNT(*) FROM {PROJECT_ID}.{DATASET}.fact_matches'
    )

    check_fact_goals = BigQueryCheckOperator(
        task_id='check_fact_goals',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'SELECT COUNT(*) FROM {PROJECT_ID}.{DATASET}.fact_goals'
    )

    check_fact_standings = BigQueryCheckOperator(
        task_id='check_fact_standings',
        use_legacy_sql=False,
        location=LOCATION,
        sql=f'SELECT COUNT(*) FROM {PROJECT_ID}.{DATASET}.fact_standings'
    )

# Design workflows
finish_pipeline = DummyOperator(task_id='finish_pipeline', dag=dag)

init_pipeline >> load_staging_dataset

load_staging_dataset >> load_staging_teams >> check_staging_teams
check_staging_teams >> load_staging_seasons >> check_staging_seasons

check_staging_seasons >> [load_staging_standings, load_staging_matches]
load_staging_standings >> check_staging_standings
load_staging_matches >> check_staging_matches

[check_staging_standings, check_staging_matches] >> create_dim_table
create_dim_table >> [create_dim_teams, create_dim_seasons]
create_dim_teams >> check_dim_teams
create_dim_seasons >> check_dim_seasons

[check_dim_teams, check_dim_seasons] >> create_fact_table
create_fact_table >> [create_fact_matches,
                      create_fact_goals, create_fact_standings]
create_fact_matches >> check_fact_matches
create_fact_goals >> check_fact_goals
create_fact_standings >> check_fact_standings

[check_fact_matches, check_fact_goals, check_fact_standings] >> finish_pipeline
