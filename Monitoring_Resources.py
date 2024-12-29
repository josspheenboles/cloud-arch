# List S3 buckets
def list_s3_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    print("S3 Buckets:")
    for bucket in buckets['Buckets']:
        print(f"  - {bucket['Name']}")

# List EC2 instances
def list_ec2_instances():
    ec2 = boto3.resource('ec2')
    print("EC2 Instances:")
    for instance in ec2.instances.all():
        print(f"  - ID: {instance.id}, State: {instance.state['Name']}")

list_s3_buckets()
list_ec2_instances()

