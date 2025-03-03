import whisper

def speech_to_text(audio_path):
    model = whisper.load_model("small")  # Load the Whisper Small model
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__":
    audio_file = "./output.mp3"  
    text = speech_to_text(audio_file)
    print("Transcribed Text:", text)
