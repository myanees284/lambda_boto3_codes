import boto3

dynamo = boto3.resource('dynamodb')
table=dynamo.Table('authors')

def lambda_handler(event, context):
    # TODO implement
    response=table.scan(
        TableName='authors')
    formattedresponse=response['Items']
    # print(formattedresponse)
    return formattedresponse