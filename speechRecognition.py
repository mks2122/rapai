import speech_recognition as sr
import time

def record_speech(timeout=2, phrase_time_limit=10):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening... Speak now!")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("Processing...")
            text = recognizer.recognize_google(audio)  
            return text
        except sr.WaitTimeoutError:
            print(" No speech detected. Stopping...")
            return None
        except sr.UnknownValueError:
            print(" Could not understand audio.")
            return None
        except sr.RequestError:
            print(" Error with the recognition service.")
            return None

if __name__ == "__main__":
    speech_text = record_speech()
    if speech_text:
        print(f" Recognized Speech: {speech_text}")
    else:
        print("No valid speech detected.")
