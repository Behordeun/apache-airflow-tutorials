from airflow import DAG


with DAG(
    dag_id='our_first_dag',
    description='This is our '
) as dag:
    pass