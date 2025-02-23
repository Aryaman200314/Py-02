
import boto3
iam_client = boto3.client('iam')

def list_admin_roles():
    paginator = iam_client.get_paginator('list_roles')
    for page in paginator.paginate():
        roles = page['Roles']
        for role in roles:
            if 'admin' in role['RoleName']:  
                print(role['RoleName'])

list_admin_roles()
