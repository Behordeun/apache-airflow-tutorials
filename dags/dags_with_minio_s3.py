from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args = {
    'owner': 'Abiodun',
    'retries': 5,
    'retry_delay': timedelta(minutes=10)
}

with DAG(
    default_args = default_args,
    dag_id='dag_with_minio_s3_V01',
    description='Dag with Minio S3',
    start_date= datetime(2022, 12, 21),
    schedule='@daily'
) as dag:
    task1 = S3KeySensor(
        task_id='sens_minio_s3',
        bucket_name='airflow',
        bucket_key='data.csv',
        aws_conn_id=''
    )
