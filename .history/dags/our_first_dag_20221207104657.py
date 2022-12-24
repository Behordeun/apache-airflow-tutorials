from datetime import datetime

from airflow import DAG

default_args

with DAG(
    dag_id='our_first_dag',
    description='This is our first dag that we write',
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily',
) as dag:
    pass