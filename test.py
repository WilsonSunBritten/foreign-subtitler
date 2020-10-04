from uploader import Uploader
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
uploader = Uploader()
uploader.upload_blob(bucket_name='kerphi-video-bucket', source_file_name='./README.md', destination='sample-project-README.md')