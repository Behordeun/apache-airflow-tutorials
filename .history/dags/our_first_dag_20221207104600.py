from datetime import datetime

from airflow import DAG


with DAG(
    dag_id='our_first_dag',
    description='This is our first dag that we write',
    start_date=datetime(2021, 1, 1, 2),
) as dag:
    pass