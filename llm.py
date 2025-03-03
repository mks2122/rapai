from transformers import pipeline
def llm(message):

    messages = [
        {"role": "system", "content": """ " Battery Health": "85% (Good condition)",
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
            "Connectivity Status": "4G LTE Connected" this is the diagnostics of the car. answer the following questions based on this information, if asked:"""},
        {"role": "user", "content": message}
    ]
    pipe = pipeline("text-generation", model="Qwen/Qwen2-3B", device=0) 
    return pipe(messages)