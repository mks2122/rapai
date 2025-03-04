
from groq import Groq

def llm(msg):
    client = Groq()
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
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
            "Connectivity Status": "4G LTE Connected" 
            this is the diagnostics of the car. answer the following questions based on this information, if asked about any of these:"""},
        
            {"role": "user", "content": msg}
        ],
        temperature=1,
        max_completion_tokens=460,
        top_p=1,
        stream=True,
        stop=None,
    )
    result=""
    for chunk in completion:
        # print(chunk.choices[0].delta.content or "", end="")
        result+=chunk.choices[0].delta.content or ""
    return result