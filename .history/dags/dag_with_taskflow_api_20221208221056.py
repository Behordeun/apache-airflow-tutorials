from airflow.decorators import dag, task
from datetime import datetime, timedelta


default_args = {
    'owner': 'Abiodun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id = 'dag_with_taskflow_api_v02',
    default_args = default_args,
    start_date = datetime(2022, 12, 8),
    schedule_interval = '@daily'
)
def hello_world_etl():

    @task()
    def get_name(multiple_outputs=True):
        return {
            'first_name': 'Muhammad',
            'middle_name': 'Abiodun',
            'last_name': 'Sulaiman'
        }

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name, last_name, age):
        print(f'Hello world!, my name is {first_name} {last_name}, and I am {age} years old!')

    name_dict = get_name()
    age = get_age()
    greet(first_name =name_dict['first_name'],
          #middle_name=name_dict['middle_name'],
          last_name=name_dict['last_name'],
          age=age)

greet_dag = hello_world_etl()