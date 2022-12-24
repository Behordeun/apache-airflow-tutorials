from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Abiodun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id = 'dag_with_cron_expression_v03',
    default_args = default_args,
    start_date = datetime(2022, 12, 11),
    schedule_interval = '20 12 * * Sun',
    catchup = False
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command = 'echo dag with cron expression!'
    )
    
    