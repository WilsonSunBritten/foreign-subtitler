from pydub.utils import mediainfo
import subprocess


class VideoAnalyzer:

    @staticmethod
    def extract_media_info(video_filepath: str):
        complete_media_info = mediainfo(video_filepath)
        channel_count = complete_media_info['channels']
        bit_rate = complete_media_info['bit_rate']
        sample_rate = complete_media_info['sample_rate']

        return channel_count, bit_rate, sample_rate

    @staticmethod
    def convert_to_audio(video_filepath: str) -> str:
        channel_count, bit_rate, sample_rate = VideoAnalyzer.extract_media_info(video_filepath)
        # audio file name is video without extension + _audio.wav
        audio_filename = video_filepath.rsplit('.', 1)[0] + '_audio.wav'
        audio_convert_command = f'ffmpeg -i {video_filepath} -b:a {bit_rate} -ac {channel_count} -ar {sample_rate} -vn {audio_filename}'
        subprocess.call(audio_convert_command, shell=True)
        return audio_filename
