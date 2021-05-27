import boto3

ec2 = boto3.client('ec2')
#listing all the unused volumes available in current region and deleting it.
response = ec2.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'available',
            ]
        },
    ]
)
for v in response['Volumes']:
    print(v['VolumeId'],v['AvailabilityZone'])
    ec2.delete_volume(
        VolumeId=v['VolumeId']
    ) 
