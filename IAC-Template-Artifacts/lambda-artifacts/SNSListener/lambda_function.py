import json
import boto3
import os

def lambda_handler(event, context):
    # TODO implement
   
    tagkey = "createdBy"
    tagValue = "Sushama"
    #sqsARN= "arn:aws:sqs:ap-south-1:872801921732:SampleQueue"
    sqsARN = os.environ.get('queueArn')
      
    c = boto3.client('sns')
   
    paginator = c.get_paginator('list_topics')

    # creating a PageIterator from the paginator
    page_iterator = paginator.paginate().build_full_result()

    topics_list = []
    tag_list = []

    # loop through each page from page_iterator
    for page in page_iterator['Topics']:
        topics_list.append(page['TopicArn'])
        print(page['TopicArn'])
        
    
    for topic in topics_list:
        tag_list = c.list_tags_for_resource(ResourceArn=topic)  
        tagStr = str(tag_list)
        print("tags:", tagStr)
        if tagkey in tagStr and tagValue in tagStr:
          print("Found")
          c.subscribe(
            TopicArn=topic,
            Protocol='sqs',
            Endpoint=sqsARN
          )     
        else:
          print("not found")
          
    
        
     
    
    
    
        
        
   
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
