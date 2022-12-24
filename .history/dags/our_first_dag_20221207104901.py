from datetime import datetime,timedelta

from airflow import DAG

default_args={
    'owner': 'abiodun',
    'retries': 5,
    'retries_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='our_first_dag',
    description='This is our first dag that we write',
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily',
) as dag:
    pass