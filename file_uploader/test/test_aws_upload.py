import os
import logging
import pytest
import boto3
from unittest.mock import patch
from botocore.exceptions import ClientError
from file_uploader.src.aws_upload import upload_files_to_s3, get_config

