import os
from google.cloud import speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'texttospeeh-342906-90f7d29050b0.json'
speech_client = speech.SpeechClient()

example_mp3 = "audio file.mp3"

with open(example_mp3, 'rb') as f:
    content = f.read()

audio_mp3 = speech.RecognitionAudio(content=content)

config_mp3 = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz = 44100,
    language_code ="en-US",
    audio_channel_count = 2
)

response_standard_mp3 = speech_client.recognize(
    config=config_mp3,
    audio=audio_mp3
)

print(response_standard_mp3)