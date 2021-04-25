# Clean up all the resources which cost money



import boto3



def lambda_handler(event, context):

    ec2 = boto3.client('ec2')

    

    # Get list of regions

    regions = ec2.describe_regions().get('Regions',[] )



    # Iterate over regions

    for region in regions:

        

        # Running following for a particular region

        print ("*************** Checking region  --   %s " % region['RegionName'])

        reg=region['RegionName']

        

        

        ################################ Auto Scaling Groups ASG ####################################

        print ("+++++++++++++ Starting Auto Scaling Group now -----------------")

        clientAS = boto3.client('autoscaling', region_name=reg)

        result = clientAS.describe_auto_scaling_groups()

       

        

        for asg1 in result['AutoScalingGroups']:

            print ("About to delete %s | in %s" % (asg1['AutoScalingGroupName'], region['RegionName']))

        

            result = clientAS.delete_auto_scaling_group(AutoScalingGroupName=asg1['AutoScalingGroupName'], ForceDelete= True)

            # Notice the ForceDelete part

        

        

        ################################ Load Balancers ####################################    

        print ("+++++++++++++ Starting LoadBalancers now [NLB & ALB] -----------------")

        client = boto3.client('elbv2', region_name=reg)

        response = client.describe_load_balancers()

        

        for lb1 in response['LoadBalancers']:

            print ("About to delete %s | in %s" % (lb1['LoadBalancerArn'], region['RegionName']))

            response  = client.delete_load_balancer(LoadBalancerArn=lb1['LoadBalancerArn'])

            

            

        print ("+++++++++++++ Starting LoadBalancers now [Classic LB] -----------------")

        client = boto3.client('elb', region_name=reg)

        response = client.describe_load_balancers()

        

        for lb1 in response['LoadBalancerDescriptions']:

            print ("About to delete %s | in %s" % (lb1['LoadBalancerName'], region['RegionName']))

            response = client.delete_load_balancer(LoadBalancerName=lb1['LoadBalancerName'])

            

        

        print ("+++++++++++++ Starting Target Groups now -----------------")    

        client = boto3.client('elbv2', region_name=reg)

        response = client.describe_target_groups()

        

        for tg1 in response['TargetGroups']:

            print ("About to delete %s | in %s" % (tg1['TargetGroupArn'], region['RegionName']))

            response = client.delete_target_group(TargetGroupArn=tg1['TargetGroupArn'])

            

        

        ################################ VPC Components #################################### 

        print ("+++++++++++++ Starting NAT Gateways now -----------------") 

        client = boto3.client('ec2', region_name=reg)

        response = client.describe_nat_gateways()

        

        for ng1 in response['NatGateways']:

            print ("About to delete %s | in %s" % (ng1['NatGatewayId'], region['RegionName']))

            response = client.delete_nat_gateway(NatGatewayId=ng1['NatGatewayId'])

            

            

        ################################ EC2 & EBS ####################################

        print ("+++++++++++++ Starting EC2 Instances now -----------------") 

        client = boto3.client('ec2', region_name=reg)

        response = client.describe_instances()

        

        for reservation in response["Reservations"]:

            for instance in reservation["Instances"]:

                print ("About to delete %s | in %s" % (instance['InstanceId'], region['RegionName']))

                response = client.terminate_instances(InstanceIds=[instance['InstanceId']])

                

        

        print ("+++++++++++++ Starting EBS Volumes now -----------------") 

        client = boto3.client('ec2', region_name=reg)

        response = client.describe_volumes()

        

        for volume in response["Volumes"]:

            print ("About to delete %s | in %s" % (volume['VolumeId'], region['RegionName']))

            response = client.delete_volume(VolumeId=volume['VolumeId'])

        
