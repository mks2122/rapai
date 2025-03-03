import requests

# Define Latitude & Longitude
lat, lon = 12.775805023619611, 80.24880282662333  # Example (Bangalore)

# Overpass API Query (Get Road Data at Given Location)
query = f"""
[out:json];
way(around:50,{lat},{lon})["highway"];
out tags;
"""
url = "http://overpass-api.de/api/interpreter"
response = requests.get(url, params={'data': query})
data = response.json()

# Extract Road Type
road_types = [way['tags'].get('highway', 'Unknown') for way in data.get('elements', [])]

# Check if the Road is in the City or Highway
if any(rt in ['motorway', 'trunk', 'motorway_link', 'trunk_link'] for rt in road_types):
    print("🛣️ Highway Detected - Maintain High Performance!")
elif any(rt in ['primary', 'secondary', 'tertiary', 'residential', 'service'] for rt in road_types):
    print("🏙️ City Road Detected - Reduce Performance!")
else:
    print("Unknown Road Type - Use Default Mode.")
