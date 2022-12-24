from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.models.xcom import XCom


default_args = {
    'owner': 'Abiodun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(age, ti):
    name = ti.xcom_pull(task_ids='get_name')
    print(f"Hello world!, my name is {name}, "
          f"and I am {age} years old!")


def get_name():
    return 'Muhammad'


with DAG(
        default_args = default
        dag_id='our_dag_with_python_operator_v04',
        description='Our first dag using Python operator',
        start_date=datetime(2022, 12, 8),
        schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'age': 15}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable='get_name'
    )

    # task1

    task2 >> task1
