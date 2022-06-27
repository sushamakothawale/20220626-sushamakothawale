# 20220626-sushamakothawale

This repo contains cloudformation templates and lamda code required for deployemnt.

# Assignment details:
1 . An SQS queue which subscribes to a SNS topic based on a particular message type
2. A lambda function which is listening to the SQS Queue (in point 1) events and writing the
messages body to s3
3. S3 bucket configured with versioning and lifecycle polices for that data
4 Necessary policies and roles required for this use-case

# Assignment solution:
Based on the details, implemented the assignment in two different ways:
1. Filterpolcy based topic subscription
2. TagBased topic subscription

# Filterpolcy based topic subscription
  IAC-Template-Artifacts/createLambda_withFilter.yaml is the main cloudfomation template to implement the solution
  Below the are details:
  1. Create sampleQueue [Queuname paramterised]
  2. Add QueuePolicy to sampleQueue for sending/reciving messages on the queue
  3. Create sampleTopic with tag "createdBY:Sushama" [Topicname paramterised]
  4. Add SNS subscription to the samplequeue and it has filter based policy. If message attribute has "action: create" key then message will be consumed/received.
  5. LamdaFunction SqsMessageReader_3, it has the logic to get the messages/message_body from samplequeue and write them back to s3 bucket.
  6. Creating IAM role with required policies for lambda execution
  7. EventSourceMapping for Lambda trigger on event i.e. record/messages on queue.
  8. S3 bucket where the message body files will get saved. bucket versioning is enabled + added lifecycle policy to expire after 90 days and Moving objects to a cheaper storage class  after 30 days. [Bucketname is paramterised]

# TagBased topic subscription
  IAC-Template-Artifacts/createLambda.yaml is the main cloudfomation template to implement the solution
  Below the are details:
  1. Create sampleQueue [Queuname paramterised]
  2. Add QueuePolicy to sampleQueue for sending/reciving messages on the queue
  3. Create sampleTopic with tag "createdBY:Sushama" [Topicname paramterised]
  4. Add SNS subscription to the samplequeue.
  5. LamdaFunction SqsMessageReader_3, it has the logic to get the messages/message_body from samplequeue and write them back to s3 bucket.
  6. Creating IAM role with required policies for lambda execution
  7. EventSourceMapping for Lambda trigger on event i.e. record/messages on queue.
  8.  S3 bucket where the message body files will get saved. bucket versioning is enabled + added lifecycle policy to expire after 90 days and Moving objects to a cheaper storage class  after 30 days. [Bucketname is paramterised]
  9. LamdaFunction SNSListner_3, it has the logic to listen to SNS topic list and fetch the tags of topics. If topic has "createdBy:Sushama" tag then subscription of the topic will get added to sampleQueue
  10. Eventbridge rule to invoke rule after 5 minutes to check new topics and their tags.
  11. LambdaInvokePermissionCloudwatchEventsLambda LambdaInvole Permisiions from cloudwatch Event rule.

# NOTES:
  1. IAC-Template-Artifacts/createLambda_withFilter.yaml is the main cloudfomation template to implement the  Filterpolcy based topic subscription.
  2. IAC-Template-Artifacts/createLambda.yaml is the main cloudfomation template to implement the TagBased topic subscription
  3. Lambda code is stored IAC-Template-Artifacts/lambda-artifacts/ folder
  4. SQSMessageReader - it has Filterpolcy based topic subscription lamda code.
  5. SNSListener- it has tag Based topic subscription code.
  6. To execute the code you need to compress the lamda code i. .zip file and store that in s3 bucket named lambda-artifacts-june. There are already parametrised in CFN template.
