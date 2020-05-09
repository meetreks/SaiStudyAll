import boto3
#either set configure settings here or use aws configure
sqs = boto3.resource('sqs')
ssm = boto3.resource('ssm')
queue = sqs.get_queue_by_name(QueueName='kisicox')
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
response = queue.send_message(MessageBody='world')
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))
