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
import pyaudio
import wave
from pydub import AudioSegment


def play_audio(file_path):
        chunk = 1024
        wf = wave.open(file_path, 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(chunk)

        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        stream.stop_stream()
        stream.close()
        p.terminate()
def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")

    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3("output.mp3")
    sound.export("output.wav", format="wav")

    play_audio("output.wav")

