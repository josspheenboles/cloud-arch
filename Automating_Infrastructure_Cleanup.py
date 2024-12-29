# Delete S3 bucket
def delete_s3_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except Exception as e:
        print("Error:", e)

# Terminate EC2 instances
def terminate_ec2_instances():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        if instance.state['Name'] == 'running':
            print(f"Terminating instance {instance.id}...")
            instance.terminate()

delete_s3_bucket("cloud-architecture-demo-bucket")
terminate_ec2_instances()

