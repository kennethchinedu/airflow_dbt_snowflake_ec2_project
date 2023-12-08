import json
from datetime import timedelta, datetime

#Loading config file
with open('/home/ubuntu/airflow/config.json', r) as config_file:
    api_host_key = json.lead(config_file)
    
    
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
    
    with open(file_path,'w') as output_file:
        json.dump(response_data, output_file, indent=4)
    output_list = [Output_file_path, file_str]
    return output_list
