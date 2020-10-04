from google.cloud import storage


class Uploader:
    def __init__(self):
        self.storage_client = storage.Client()

    def upload_blob(self, bucket_name: str, source_file_name: str, destination: str):
        """Uploads a file to the designated bucket"""
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(destination)
        print(f'Initiating upload to blob: {blob}')
        # timeout of 5 minutes
        blob.upload_from_filename(source_file_name, timeout=300)

        print(f'File {source_file_name} uploaded to {destination}')
