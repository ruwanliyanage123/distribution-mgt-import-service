import shutil

from config.config import Config
from service.s3_service import S3Service

if __name__ == "__main__":
    bucket_name = Config.S3_BUCKET_NAME
    object_keys = ['fruits/apple.jpeg']
    download_path = 'images'
    upload_s3_key = 'in-progress'
    prefix = 'in_progress'
    s3_service = S3Service()
    s3_service.download_s3_objects(bucket_name, object_keys, download_path)
    renamed_files = s3_service.rename_files(download_path, prefix)
    s3_service.upload_files(bucket_name, download_path, upload_s3_key)
    shutil.rmtree(download_path)