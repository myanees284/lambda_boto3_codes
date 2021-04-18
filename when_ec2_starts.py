import boto3

client = boto3.client('sns')

def lambda_handler(event, context):
  
    instance_id=event['detail']['instance-id']
    state_name=event['detail']['state']
    message="Hello Team instance with id {} has been {}".format(instance_id,state_name)
    client.publish(TopicArn='<your ARN ID>',
                   Message=message)
