import boto3

s3_client = boto3.client('s3')
dynamo = boto3.resource('dynamodb')
table=dynamo.Table('emp_details')

def lambda_handler(event, context):
    try:
        # TODO: write code...
        bucket_name=event['Records'][0]['s3']['bucket']['name']
        file_name=event['Records'][0]['s3']['object']['key']
        response = s3_client.get_object(Bucket=bucket_name,Key=file_name)
        data=response["Body"].read().decode('utf-8')
        employees=data.split("\n")
        for emp in employees:
            emp=emp.split(",")
            table.put_item(
                Item = {
                    "id": str(emp[0]),
                    "Name": str(emp[1]),
                    "Age": str(emp[2])
                })
    except Exception as err:
        print(">>>>>"+str(err))
