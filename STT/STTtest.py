import os
from google.cloud import speech_v1p1beta1
import io

client = speech_v1p1beta1.SpeechClient.from_service_account_json('texttospeeh-342906-90f7d29050b0.json')

file_name = "audio file.mp3"

with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()

audio = speech_v1p1beta1.RecognitionAudio(content=content)
config = speech_v1p1beta1.RecognitionConfig(
    encoding=speech_v1p1beta1.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)

response = client.recognize(config=config, audio=audio)

# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print(u"Transcript: {}".format(result.alternatives[0].transcript))