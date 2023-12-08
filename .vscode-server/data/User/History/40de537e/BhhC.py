from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator 



default_args = {
    'owner' : 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 12),
    'email': ['anamsken60@gmail.com'],
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    'weather_dag',
    default_args=default_args,
    schedule_interval = '@daily',
    catchup=False ) as dag:
    
    
    is_api_available = HttpSensor(
        task_id = 'is_api_available',
        http_conn_id='weather_api',
        enpoint='/data/2.5/weather?q=lagos&appid=651503801c76f2776271759bead16f17'
    )