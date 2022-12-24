from airflow.decorators import dag, task
from datetime import datetime, timedelta


default_args = {
    'owner': 'Abiodun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id = 'dag_with_taskflow_api_v01',
    default_args = default_args,
    start_date = datetime(2022, 12, 8)
    schedule_interval = '@daily'
)
def hello_world_etl():
    
    
    @task()
    def get_name():
        return 'Muhammad'