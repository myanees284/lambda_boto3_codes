import boto3

dynamo = boto3.resource('dynamodb')
table=dynamo.Table('courses')

def lambda_handler(event, context):
    tempid=event['title']
    id=tempid.replace(" ", "-").lower()
    
    titleVal=tempid
    watchHrefVal="http://www.pluralsight.com/courses/{}".format(id)
    authorIdVal=event['authorId']
    lenghtVal=event['length']
    categoryVal=event['category']
    try:
        table.put_item(
                Item = {
                    "id": id,
                    "title": titleVal,
                    "watchHref": watchHrefVal,
                    "authorId": authorIdVal,
                    "length": lenghtVal,
                    "category": categoryVal
                })
        return 'Data persisted successfully'
    except Exception as e:
        print(">>>>>>"+str(e))