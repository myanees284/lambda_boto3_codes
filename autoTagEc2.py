import boto3
import json

ec2 = boto3.client('ec2')
# tags to attach to EC2 instances
tags=[
        {
            'Key': 'ClientName',
            'Value': 'SuperNova',
        },
        {
            'Key': 'CostCenter',
            'Value': 'SN19191',
        }
    ]

def lambda_handler(event, context):
   #Parsing the event response to collect the instance ids and adding them into list
    items=event['detail']['responseElements']['instancesSet']['items']
    instance_ids=[]
    for item in items:
        instance_ids.append(item['instanceId'])
    #using ec2  boto3 function to create tag against each instance id
    ec2.create_tags(
        Resources=instance_ids,
        Tags=tags,
        )
    
