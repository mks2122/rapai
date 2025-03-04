from flask import Flask, jsonify,request, render_template
import random
from whishperAudio import speech_to_text
from tts import speak
from speechRecognition import record_speech
from terrainBasedModes.api import llm
from autoMode import autoMode

app = Flask(__name__,template_folder='./')

# Predefined list of random SMS messages and names
sms_messages = [
    "Hey, how are you?",
    "Don't forget our meeting tomorrow!",
    "Call me when you're free.",
    "Happy Birthday! Have a great day!",
    "Let's catch up soon!"
]

names = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/random_sms', methods=['GET'])
def get_random_sms():
    random_sms = random.choice(sms_messages)
    random_name = random.choice(names)
    speak(f"{random_name} sent a message saying {random_sms}\n {random_name}")
    return record_speech()
    

@app.route('/random_call', methods=['GET'])
def get_random_call():
    random_name = random.choice(names)
    speak(f"{random_name} is trying to call you...")
    return record_speech()

@app.route('/ev_diagnostics', methods=['GET'])
def get_ev_diagnostics():
    speak("What would you like to know about the car?")
    query = record_speech()
    speak(llm(query))
    return 'done'


@app.route('/mode')
def mode():
    # Get the 'lat' and 'lom' query parameters
    lat = 21.1702 
    lom = 72.8311 
    
    return autoMode(lat, lom)
    return f"Latitude: {lat}, Longitude: {lom}"
    # speak(llm(query))
    # return jsonify({"response": llm(query)})


if __name__ == '__main__':
    app.run(debug=True)