from airflow import DAG


with DAG(
    dag_id='our_first_dag',
    description='This is our first DAG'
) as dag:
    pass