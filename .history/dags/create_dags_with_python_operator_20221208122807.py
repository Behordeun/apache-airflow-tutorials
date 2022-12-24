from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Abiodun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(age, ti):
    first_name = ti.xcom_pull(task_ids='get_name')
    print(f"Hello world!, my name is {name}, "
          f"and I am {age} years old!")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Muhammad')
    ti.xcom_push(key='middle_name', value='Abiodun')
    ti.xcom_push(key='last_name', value='Sulaiman')


with DAG(
        dag_id='our_dag_with_python_operator_v05',
        default_args = default_args,
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
        python_callable = get_name
    )

    # task1

    task2 >> task1
