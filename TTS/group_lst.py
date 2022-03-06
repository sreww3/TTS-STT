import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1
import pandas as pd
import numpy as np
"""
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'texttospeeh-342906-d2e1e23d9aec.json'

client = texttospeech_v1.TextToSpeechClient()
"""

recipe = pd.read_csv("recipe.csv", index_col='index')
df = pd.DataFrame(recipe)
recipe = df.iloc[:,4][0].split(':')

for i in recipe:
    print(i)
"""
    synthesis_input = texttospeech_v1.SynthesisInput(text = i)

    voice = texttospeech_v1.VoiceSelectionParams(
        language_code = 'ko-KR',
        ssml_gender = texttospeech_v1.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding = texttospeech_v1.AudioEncoding.MP3
    )

    response1 = client.synthesize_speech(
        input = synthesis_input,
        voice = voice,
        audio_config = audio_config
    )

    with open(str(cnt)+'.mp3','wb') as output:
        output.write(response1.audio_content)
    cnt += 1
"""