from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator 
from airflow.providers.http.sensors.http import HttpSensor



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
    
    # simplehttp_task = SimpleHttpOperator(
    #     task_id="simplehttp_task",
    #     http_conn_id="http_conn",
    #     endpoint='post',
    #     data=json.dumps({"priority": 5}),
    #     headers={"Content-Type": "application/json"},
    #     # response_check=lambda response: response.json()['json']['priority'] == 5,
    #     # response_filter=lambda response: json.loads(response.text),
    #     # extra_options: Optional[Dict[str, Any]] = None,
    #     # log_response: bool = False,
    #     # auth_type: Type[AuthBase] = HTTPBasicAuth,
    # )
        
    is_api_available =  HttpSensor(
        task_id = 'is_api_available',
        http_conn_id ='weather_api',
        enpoint = '/data/2.5/weather?q=lagos&appid=651503801c76f2776271759bead16f17'
    )