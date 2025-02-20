import boto3

def list_instance_types():
    ec2_client = boto3.client('ec2')
    
    try:
        # Use paginator to handle multiple pages of results
        paginator = ec2_client.get_paginator('describe_instance_types')
        
        for page in paginator.paginate():
            for instance_type in page['InstanceTypes']:
                print(f"\nInstance Type: {instance_type['InstanceType']}")
                
    except Exception as e:
        print(f"Error: {e}")

list_instance_types()
