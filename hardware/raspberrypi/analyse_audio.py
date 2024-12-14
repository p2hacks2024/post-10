import base64

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class CryOfSoul():
    def __init__(self, text, intensity_of_emotion):
        self.message = text
        self.intensity_of_emotion = intensity_of_emotion

    def __str__(self):
        return f"Message: {self.message}\nIntensity of Emotion: {self.intensity_of_emotion}"

class AnalyseAudio():
    def __init__(self):
        self.client = OpenAI()

        self.prompt = """
        日頃の不満や悩みをぶちまけた音声が渡されます．
        まず，その音声の内容をテキストに起こしてください．
        次に，その内容が日本語として破綻している箇所があれば修正してください．
        最後に，その内容について，感情の強度(Intensity of Emotion)を0~9のスケールで評価してください．

        出力は次の形式に従ってください．
        文字起こし: ここにテキストを入力
        感情の強度: ここに数値を入力
        """


    def analyse(self, audio_path: str) -> CryOfSoul:
        with open(audio_path, "rb") as audio_file:
            wav_data = audio_file.read()
        encoded_string = base64.b64encode(wav_data).decode('utf-8')

        completion = self.client.chat.completions.create(
            model="gpt-4o-audio-preview",
            modalities=["text"],
            audio={"voice": "alloy", "format": "wav"},
            messages=[
                {
                    "role": "system",
                    "content": [{
                        "type": "text",
                        "text": self.prompt
                    }]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_audio",
                            "input_audio": {
                                "data": encoded_string,
                                "format": "wav"
                            }
                        }
                    ]
                },
            ],
            temperature=0.0,
        )

        return self._parse_text(completion.choices[0].message.content)

    
    def _parse_text(self, text: str) -> CryOfSoul:
        text = text.split("\n")
        text = [line.split(": ")[1] for line in text]

        return CryOfSoul(text[0], int(text[1]))

if __name__ == "__main__":
    analyse_audio = AnalyseAudio()
    print(analyse_audio.analyse('sample.wav'))
