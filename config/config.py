import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    REGION_NAME = os.getenv('REGION_NAME')
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
    LOCAL_DOWNLOAD_PATH = os.getenv('LOCAL_DOWNLOAD_PATH')
