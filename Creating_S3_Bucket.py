import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Create a new bucket
bucket_name = "cloud-architecture-demo-bucket"

region = "us-east-1" #near user (person,another service)

try:
	
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print("Error:", e)

