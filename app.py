from flask import Flask, jsonify
import random

app = Flask(_name_)

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

def generate_ev_diagnostics():
    return {
        "Battery Health": "85% (Good condition)",
        "Battery Temperature": "32°C",
        "State of Charge (SOC)": "68%",
        "Charging Status": "Charging (Fast mode)",
        "Charging Power": "50 kW",
        "Estimated Range": "320 km",
        "Motor Temperature": "45°C",
        "Inverter Status": "Operational",
        "Regenerative Braking Efficiency": "78%",
        "Tire Pressure": "35 PSI (Optimal)",
        "Brake Pad Wear": "20% worn",
        "Cabin Temperature": "22°C",
        "Coolant Temperature": "38°C",
        "Energy Consumption Rate": "14 kWh/100km",
        "Odometer Reading": "15,000 km",
        "Drive Mode": "Eco Mode",
        "Auxiliary Battery Voltage": "12.8V",
        "Headlight Status": "On (Auto Mode)",
        "GPS Signal Strength": "Strong",
        "Connectivity Status": "4G LTE Connected"
    }

@app.route('/random_sms', methods=['GET'])
def get_random_sms():
    random_sms = random.choice(sms_messages)
    random_name = random.choice(names)
    return f"{random_name} sent a message saying {random_sms}\n <br>{random_name}"

@app.route('/random_call', methods=['GET'])
def get_random_call():
    random_name = random.choice(names)
    return f"{random_name} is trying to call you..."

@app.route('/ev_diagnostics', methods=['GET'])
def get_ev_diagnostics():
    return jsonify(generate_ev_diagnostics())


if _name_ == '_main_':
    app.run(debug=True)