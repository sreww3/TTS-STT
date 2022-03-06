import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'texttospeeh-342906-d2e1e23d9aec.json'

client = texttospeech_v1.TextToSpeechClient()

text = 'Hi, this is test texts to confirm text to speech is working as well'

synthesis_input = texttospeech_v1.SynthesisInput(text = text)

voice = texttospeech_v1.VoiceSelectionParams(
    language_code = 'en-US',
    ssml_gender = texttospeech_v1.SsmlVoiceGender.MALE
)

""" output """

audio_config = texttospeech_v1.AudioConfig(
    audio_encoding = texttospeech_v1.AudioEncoding.MP3
)

response1 = client.synthesize_speech(
    input = synthesis_input,
    voice = voice,
    audio_config = audio_config
)

with open('audio file.mp3', 'wb') as output:
    output.write(response1.audio_content)

