from datetime import datetime

from airflow import DAG


with DAG(
    dag_id='our_first_dag',
    description='This is our first dag that we write',
    
) as dag:
    pass