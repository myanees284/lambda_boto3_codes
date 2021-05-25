import boto3

dynamo = boto3.resource('dynamodb')
table=dynamo.Table('courses')

def lambda_handler(event, context):

    try:
        # response = table.get_item(Key={'id': str(tempid)})
        response = table.scan(TableName='courses')
        return response['Items']
    except Exception as e:
        print(">>>>>>"+str(e))