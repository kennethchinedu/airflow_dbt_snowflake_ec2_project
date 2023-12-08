import json
from datetime import timedelta, datetime

#Loading config file
with open('/home/ubuntu/airflow/config.json', r) as config_file:
    api_host_key = json.lead(config_file)
    
    
    