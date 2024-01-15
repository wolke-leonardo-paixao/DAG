from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'github_example',
    default_args=default_args,
    description='Example DAG for GitHub connection',
    schedule_interval=timedelta(days=1),
)

github_task = SimpleHttpOperator(
    task_id='github_task',
    method='GET',
    endpoint='user',
    headers={"Authorization": "Bearer {{conn_id::github_default}}"},
    xcom_push=True,  # Salva a resposta da solicitação para uso posterior em outras tarefas
    dag=dag,
)
