#%% Libraries
import boto3
from botocore.exceptions import NoCredentialsError


#%% Load keys from config.py file
from config import ACCESS_KEY, SECRET_KEY


#%% Define function to upload files to s3 bucket
def upload_to_aws(local_file, bucket, s3_file):
    """
    Upload file to S3 bucket. Returns True if no errors are encountered.

    Inputs:
    ------
        local_file : file name/path to upload
        bucket     : Target S3 bucket name
        s3_file    : Name for the file in the bucket
    """
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    # Try to upload the file, handling errors
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
