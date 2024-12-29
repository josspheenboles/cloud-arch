import boto3

# Initialize EC2 client
ec2 = boto3.resource('ec2')

# Launch an EC2 instance
try:
    instance = ec2.create_instances(
        ImageId='ami-0c2b8ca1dad447f8a',  # Replace with a valid AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='my-key-pair'  # Replace with your key pair name
    )
    print(f"Instance launched with ID: {instance[0].id}")
except Exception as e:
    print("Error:", e)

