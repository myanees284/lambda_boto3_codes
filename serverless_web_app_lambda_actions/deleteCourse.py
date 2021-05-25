import boto3

dynamo = boto3.resource('dynamodb')
table=dynamo.Table('courses')

def lambda_handler(event, context):
    tempid=event['id']
    print(tempid)
    try:
        response = table.delete_item(Key={'id': str(tempid)})
        return response
    except Exception as e:
        print(">>>>>>"+str(e))