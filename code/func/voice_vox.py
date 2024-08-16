import json
import requests
import wave
import random

class VOICE_VOX:
    def __init__(self):
        self.speaker = 1
        self.host = "localhost"
        self.port = 50021
        self.text = ""
        self.wave_path = "../outputs/out.wav"
        self.speaker_ids = [2, 3, 8, 9, 10, 11, 12, 13, 14, 16, 20, 21, 23, 27, 28, 29, 42, 43, 46, 47, 51, 52, 53, 54, 55, 58]


    def change_voice(self, status, num=None):
        if status == 'random':
            self.speaker = random.choice(self.speaker_ids)
        elif status == 'select':
            speaker_id = int(num)
            self.speaker = self.speaker_ids[self.speaker_ids.index(speaker_id)]
        
        print(self.speaker)

        self.generate_sample()


    def generate_wave(self, text):
        params = (
            ('text', text),
            ('speaker', self.speaker)
        )

        post_response1 = requests.post(
            f'http://{self.host}:{self.port}/audio_query',
            params=params
        )

        header = {'Content-Type': 'application/json',}

        post_response2 = requests.post(
            f'http://{self.host}:{self.port}/synthesis',
            headers=header,
            params=params,
            data=json.dumps(post_response1.json())
        )

        wf = wave.open(self.wave_path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(post_response2.content)
        wf.close()


    def generate_sample(self):
        text = "サンプルボイスです"
        self.generate_wave(text)