import json
import boto3 

#setting up s3 client
s3_client = boto3.client('s3')


#This functions is triggerd by s3 and copies the raw file from another s3 bucket
def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
   
    target_bucket = 'copy_of_zillow_raw_data/lagos/'
    copy_source = {'Bucket' :source_bucket, 'Key':object_key}
    
    waiter = s3_client.get_waiter('object_xists')
    s3_client.copy_object(Bucket=target_bucket, Key=object_key, CopySource=copy_source)
    
    return(
        'statuscode' : 200,
        'body': json.dumps('File copy completed successfully')
        )