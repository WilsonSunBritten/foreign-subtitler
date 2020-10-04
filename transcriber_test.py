import os
from transcriber import Transcriber


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
os.environ['BUCKET_NAME'] = 'kerphi-video-bucket'

transcriber = Transcriber()
transcriber.extract_text('ja-JP', './video.mp4')
