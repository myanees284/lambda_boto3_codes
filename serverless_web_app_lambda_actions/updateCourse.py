import boto3

dynamo = boto3.resource('dynamodb')
table=dynamo.Table('courses')

def lambda_handler(event, context):
    tempid=event['id']
    
    titleVal=event['title']
    watchHrefVal=event['watchHref']
    authorIdVal=event['authorId']
    lenghtVal=event['length']
    categoryVal=event['category']
    try:
        response=table.put_item(
                Item = {
                    "id": tempid,
                    "title": titleVal,
                    "watchHref": watchHrefVal,
                    "authorId": authorIdVal,
                    "length": lenghtVal,
                    "category": categoryVal
                })
        response={ "id": tempid, "title": titleVal, "watchHref": watchHrefVal, "authorId": authorIdVal, "length": lenghtVal, "category": categoryVal }
        return response
    except Exception as e:
        print(">>>>>>"+str(e))