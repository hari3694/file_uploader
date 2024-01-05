import os
import logging
import boto3
from botocore.exceptions import ClientError
from .utils import get_config


def upload_files_to_s3(bucket_name, directory, config_file):
    """Upload a file to an S3 bucket

    :param directory: File Directory to upload
    :param bucket_name: Bucket to upload to
    :param config_file: File path to the configuration path
    :return: True if file was uploaded, else False
    """

    aws_access_key = get_config(config_file, section="S3", key="AWS_ACCESS_KEY")
    aws_secret = get_config(config_file, section="S3", key="AWS_SECRET")

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret)

    file_types = get_config(config_file, section="S3", key="S3_FILE_TYPES")
    print(file_types)
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(file)
            if os.path.splitext(file)[1].lower() in file_types:
                file_path = os.path.join(root, file)
                object_name = os.path.basename(file)
                print(object_name, file_path)
                with open(file_path, "rb") as f:
                    try:
                        s3.upload_file(file_path, bucket_name, object_name)

                    except ClientError as e:
                        print(e)
                        logging.error(e)
    return True


if __name__ == "__main__":
    upload_files_to_s3("myfileuploaderbucket", "C:/projects/upload_directory", "./config.ini")
