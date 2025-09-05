import boto3

# Create an S3 resource
s3 = boto3.resource('s3')

# # Get all buckets
# for bucket in s3.buckets.all():
#     print(bucket.name)

# Create a new bucket
# s3.create_bucket(Bucket='uk-new-s3bucket', CreateBucketConfiguration={'LocationConstraint': 'ca-central-1'}) 

# Delete a bucket
# s3.Bucket('uk-new-s3bucket').delete()

# Delete all buckets
# for bucket in s3.buckets.all():

# Upload a new file
# s3.Bucket('uk-new-s3bucket').upload_file('app.py', 'app.py')

# Download a file
# s3.Bucket('uk-new-s3bucket').download_file('app.py', 'downloaded_app.py')

# Delete a file
# s3.Object('uk-new-s3bucket', 'app.py').delete()

# Read a file
obj = s3.Object('uk-new-s3bucket', 'app.py')
print(obj.get()['Body'].read().decode('utf-8'))