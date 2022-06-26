import json
import boto3
import os


def lambda_handler(event, context):

    input= event['Records']
    print(input)
    message = input[0]["body"]
    filename = input[0]["messageId"]+".txt"
    print("filename : {} ", filename)

    encoded_string = message.encode("utf-8")

    #bucket_name = "sushama-1234"
    bucket_name = os.environ.get('s3bucketName')
    s3_path = "100001/" + filename

    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
