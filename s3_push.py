import boto
from boto.s3 import connect_to_region
from boto.s3.key import Key
from boto.exception import S3ResponseError
from credentials import *

BUCKET_NAME = 'mark-public-files'
TEST_FILE = "index.html"

s3 = connect_to_region("eu-west-1", aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET)

def get_or_create_bucket(s3, bucket_name):
	bucket = None
	try:
		bucket = s3.get_bucket(bucket_name)
	except S3ResponseError:
		bucket = s3.create_bucket(bucket_name, location='EU')
	return bucket

def upload_file(bucket, file_name):
	k = bucket.new_key(file_name)
	k.set_contents_from_filename(file_name)
	k.make_public()

bucket = get_or_create_bucket(s3, BUCKET_NAME)
upload_file(bucket, TEST_FILE)
print("Aplication is created. Last Index uploaded.")




