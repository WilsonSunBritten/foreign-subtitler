from google.cloud import speech_v1
from uploader import Uploader
from video_analyzer import VideoAnalyzer
import random

class Transcriber:
    def __init__(self):
        self.client = speech_v1.SpeechClient()
        self.uploader = Uploader()
        self.base_config = {
            "encoding": speech_v1.enums.RecognitionConfig.AudioEncoding.LINEAR16,
            "enable_word_time_offsets": True,
            "profanity_filter": False,
            "model": "default",
            "enable_automatic_punctuation": True
        }

    def extract_text(self, language: str, video_path: str):
        audio_filepath, channel_count, sample_rate = VideoAnalyzer.convert_to_audio(video_path)

        complete_config = self.base_config.copy()
        complete_config['sample_rate_hertz'] = int(sample_rate)
        complete_config['audio_channel_count'] = int(channel_count)
        complete_config['language_code'] = language

        upload_path = f'audio/audio_{random.randint(0,9999999)}.{audio_filepath.split(".")[-1]}'
        bucket_path = self.uploader.upload_blob(audio_filepath, upload_path)

        print('beginning long_running_recognize')
        recognition = self.client.long_running_recognize(complete_config, {'uri': bucket_path})

        print(u'Waiting for recognition process to finish')
        response = recognition.result()
        print('completed recognition')
        return response
