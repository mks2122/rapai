# from TTS.api import TTS

# def text_to_speech(text, output_path):
#     tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
#     tts.tts_to_file(text=text, file_path=output_path)

# if __name__ == "__main__":
#     text = "Hello, this is a test for text to speech conversion using Coqui TTS."
#     output_file = "output.wav"
#     text_to_speech(text, output_file)
#     print(f"Speech saved to {output_file}")


from gtts import gTTS
import os

text = "Hello, this is a text-to-speech test!"
tts = gTTS(text=text, lang="en")
tts.save("output.mp3")

# Play the generated speech
os.system("start output.mp3")  # Windows
# os.system("mpg321 output.mp3")  # Linux
