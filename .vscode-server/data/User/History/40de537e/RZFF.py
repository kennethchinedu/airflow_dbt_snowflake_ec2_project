from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator 
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from functions.functions import extract_data 

now = datetime.now()
dt_now_string = now.strftime('%d%m%Y%H%M%S')

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
    
    is_api_available = SimpleHttpOperator(
        task_id="is_api_available",
        http_conn_id="weather_api",
        endpoint='/data/2.5/weather?q=lagos&appid=651503801c76f2776271759bead16f17'
    )
    
    
    extract_data_task = PythonOperator(
        task_id="extract_data_task",
        python_callable= extract_data,
        op_kwargs={'url':'https://zillow56.p.rapidapi.com/search', 'querystring':{'location':'houston, tx'}, 'headers':api_host_key ,'date_string': dt_now_string}
    )
   
is_api_available > extract_data_task