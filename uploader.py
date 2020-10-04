from google.cloud import storage
import os


class Uploader:
    def __init__(self):
        self.storage_client = storage.Client()
        self.bucket_name = os.environ['BUCKET_NAME']

    def upload_blob(self, source_file_name: str, destination: str):
        """Uploads a file to the designated bucket"""
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(destination)
        print(f'Initiating upload to blob: {blob}')
        # timeout of 5 minutes
        blob.upload_from_filename(source_file_name, timeout=300)

        print(f'File {source_file_name} uploaded to {destination}')
        return f'gs://{self.bucket_name}/{destination}'