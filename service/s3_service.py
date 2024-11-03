import boto3
import os
from config.config import Config

class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=Config.AWS_ACCESS_KEY,
            aws_secret_access_key=Config.AWS_SECRET_KEY,
            region_name=Config.REGION_NAME
        )

    def download_s3_objects(self, bucket_name, object_keys, download_path):
        os.makedirs(download_path, exist_ok=True)
        for key in object_keys:
            file_name = os.path.join(download_path, key.split('/')[-1])
            self.s3_client.download_file(bucket_name, key, file_name)
            print(f"Downloaded {key} to {file_name}")

    def rename_files(self, download_path, prefix):
        renamed_files = []
        for file_name in os.listdir(download_path):
            if os.path.isfile(os.path.join(download_path, file_name)):
                new_name = f"{prefix}_{file_name}"
                os.rename(os.path.join(download_path, file_name), os.path.join(download_path, new_name))
                renamed_files.append(new_name)
                print(f"Renamed {file_name} to {new_name}")
        return renamed_files

    def upload_files(self, bucket_name, folder_path, s3_folder_key):
        try:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    s3_key = os.path.join(s3_folder_key, file)
                    self.s3_client.upload_file(file_path, bucket_name, s3_key)
                    print(f"Uploaded {file_path} to {bucket_name}/{s3_key}")
        except Exception as exception:
            print(f"Failed to upload files due to: {exception}")