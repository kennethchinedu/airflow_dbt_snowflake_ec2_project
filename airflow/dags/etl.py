from airflow import DAG
from datetime import timedelta, datetime
import json, requests
from airflow.operators.python import PythonOperator 
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.bash_operator import BashOperator 
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor



# from functions.functions import extract_data 

now = datetime.now()
dt_now_string = now.strftime('%d%m%Y%H%M%S')



#Loading config file
with open('/home/ubuntu/airflow/config.json', 'r') as config_file:
    api_host_key = json.load(config_file)
    
    
now = datetime.now()
dt_now_string = now.strftime("%d%m%Y%H%M%S")

def extract_data(**kwargs):
    url = kwargs['url']
    headers = kwargs['headers']
    querystring = kwargs['querystring']
    dt_string = kwargs['date_string']
    # return headers
    response = requests.get(url, headers=headers, params=querystring)
    response_data = response.json()
        
    # Create the full path to the json file
    output_file_path = f'/home/ubuntu/response_data_{dt_string}.json'
    file_str = f'response_data_{dt_string}.csv'
    
    with open(output_file_path,'w') as output_file:
        json.dump(response_data, output_file, indent=4)
    output_list = [output_file_path, file_str]
    return output_list


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
    'Zillow_Dag',
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
        op_kwargs={'url':'https://zillow56.p.rapidapi.com/search', 'querystring':{'location':'lagos, tx'}, 'headers':api_host_key ,'date_string': dt_now_string}
    )
    
    load_file_to_s3 = BashOperator(
        task_id="load_file_to_s3",
        bash_command= 'aws s3 mv {{ti.xcom_pull("extract_data_task")[0]}} s3://zillow-analytics-ec2/lagos/',
        
    )
    
    is_csv_file_available_in_bucket = S3KeySensor(
        task_id = 'is_csv_file_available_in_bucket',
        
    )
   
is_api_available >> extract_data_task >> load_file_to_s3