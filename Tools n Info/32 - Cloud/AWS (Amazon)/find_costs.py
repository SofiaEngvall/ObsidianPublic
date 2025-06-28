import boto3
from botocore.exceptions import ClientError


def list_ec2_instances():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    for res in instances['Reservations']:
        for inst in res['Instances']:
            print(f"EC2 Instance: {inst['InstanceId']} in {inst['Placement']['AvailabilityZone']}")

def list_ebs_volumes():
    ec2 = boto3.client('ec2')
    vols = ec2.describe_volumes()
    for vol in vols['Volumes']:
        print(f"EBS Volume: {vol['VolumeId']} ({vol['Size']} GiB)")

def list_elastic_ips():
    ec2 = boto3.client('ec2')
    addresses = ec2.describe_addresses()
    for addr in addresses['Addresses']:
        print(f"Elastic IP: {addr.get('PublicIp')}")

def list_s3_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    for b in buckets['Buckets']:
        print(f"S3 Bucket: {b['Name']}")

def list_rds_instances():
    rds = boto3.client('rds')
    instances = rds.describe_db_instances()
    for db in instances['DBInstances']:
        print(f"RDS Instance: {db['DBInstanceIdentifier']} ({db['DBInstanceClass']})")

def list_lambda_functions():
    lam = boto3.client('lambda')
    funcs = lam.list_functions()
    for f in funcs['Functions']:
        print(f"Lambda Function: {f['FunctionName']}")

def list_elbs():
    elb = boto3.client('elb')
    res = elb.describe_load_balancers()
    for lb in res['LoadBalancerDescriptions']:
        print(f"ELB: {lb['LoadBalancerName']}")

def list_albs():
    elbv2 = boto3.client('elbv2')
    res = elbv2.describe_load_balancers()
    for lb in res['LoadBalancers']:
        print(f"ALB/NLB: {lb['LoadBalancerName']}")

def list_cloudfront_distributions():
    cf = boto3.client('cloudfront')
    dists = cf.list_distributions()
    for item in dists.get('DistributionList', {}).get('Items', []):
        print(f"CloudFront Distribution: {item['Id']}")

def list_nat_gateways():
    ec2 = boto3.client('ec2')
    res = ec2.describe_nat_gateways()
    for gw in res['NatGateways']:
        print(f"NAT Gateway: {gw['NatGatewayId']}")

def list_dynamodb_tables():
    db = boto3.client('dynamodb')
    tables = db.list_tables()
    for name in tables['TableNames']:
        print(f"DynamoDB Table: {name}")

def main():
    print("=== Cost-Related AWS Resources ===")
    try:
        list_ec2_instances()
        list_ebs_volumes()
        list_elastic_ips()
        list_s3_buckets()
        list_rds_instances()
        list_lambda_functions()
        list_elbs()
        list_albs()
        list_cloudfront_distributions()
        list_nat_gateways()
        list_dynamodb_tables()
    except ClientError as e:
        print(f"AWS error: {e}")

if __name__ == "__main__":
    main()
