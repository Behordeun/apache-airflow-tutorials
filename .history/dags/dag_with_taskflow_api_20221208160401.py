from airflow.decorators import dag, task
from datetime import datetime, timedelta


default_args = {
    'owner': 'Abiodun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}