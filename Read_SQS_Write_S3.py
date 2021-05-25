import boto3
import time;
import calendar;

def lambda_handler(event, context):
    
    # reading message from event triggered by SQS
    messageId=event['Records'][0]['messageId']
    messageBody=event['Records'][0]['body']
    
    # constructing dynamic file name
    ts = calendar.timegm(time.gmtime())
    path="/tmp/"
    fileName="Data_{}.json".format(ts)
    pathWithfileName=path+fileName
    
    # Writing the retreived SQS message into the file
    f = open(pathWithfileName, "w")
    f.write(messageId+"\n"+messageBody)
    f.close()
    
    #Initialzing S3 client and uploading the file into S3 bucket
    client = boto3.client('s3')
    s3 = boto3.resource('s3')
    s3BucketName="livebucket2021"
    s3.meta.client.upload_file(pathWithfileName, s3BucketName, fileName)
