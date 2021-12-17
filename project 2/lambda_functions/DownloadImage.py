import boto3

def download_data(input_bucket, input_object, file_name):
    s3 = boto3.client('s3')
    s3.download_file(input_bucket, input_object, file_name)
    return file_name