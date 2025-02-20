import boto3

def list_instance_types():
    ec2_client = boto3.client('ec2')
    paginator = ec2_client.get_paginator('describe_instance_types')
    for page in paginator.paginate():
        for instance_type in page['InstanceTypes']:
            print(f"\nInstance Type: {instance_type['InstanceType']}")

list_instance_types()
