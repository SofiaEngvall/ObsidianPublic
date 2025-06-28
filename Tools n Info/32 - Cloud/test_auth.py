import boto3

# Put your AWS credentials here (use IAM user with least privilege for your tasks)
AWS_ACCESS_KEY = 'AKIART7Y2ZUTNFS3WWGA'
AWS_SECRET_KEY = 'YOUR_SECRET_KEY' in file script_read_access.key
AWS_REGION = 'eu-west-1'  # or your preferred region

# Create clients with explicit credentials
ec2 = boto3.client(
    'ec2',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

# Example: list EC2 instances
def list_ec2_instances():
    res = ec2.describe_instances()
    for r in res['Reservations']:
        for i in r['Instances']:
            print(f"Instance ID: {i['InstanceId']}")

if __name__ == '__main__':
    list_ec2_instances()
