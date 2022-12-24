from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Abiodun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id = 'dag_with_catchup_and_backfill_v01',
    default_args = default_args,
    start_date = datetime(2022, 12, 8),
    schedule_interval = '@daily'
)

with DAG(
    dag_id = 'dag_with_catchup_and_backfill_v01',
    
)