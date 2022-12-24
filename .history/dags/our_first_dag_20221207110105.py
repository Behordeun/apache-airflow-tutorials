from datetime import datetime,timedelta

from airflow import DAG
from airflow.operator.bash import 

default_args={
    'owner': 'abiodun',
    'retries': 5,
    'retries_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2022, 12, 7, 2),
    schedule_interval='@daily',
) as dag:
    pass