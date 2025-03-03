import requests
import json
import pandas as pd





def fetchData(x =12.899138982066853 ,y =80.227867302601):
    query = f"""
    [out:json];
    way(around:50, {x}, {y})["highway"];
    out body;
    """
    url = "http://overpass-api.de/api/interpreter"
    response = requests.get(url, params={'data': query})
    data = response.json()

    road_data = []
    for way in data.get("elements", []):
        tags = way.get("tags", {})
        road_data.append({
            "latitude": x,
            "longitude": y,
            "road_type": tags.get("highway", "unknown"),
            "lanes": tags.get("lanes", 1),
            "maxspeed": tags.get("maxspeed", "unknown"),
            "junction": tags.get("junction", "no"),
        })

    df = pd.DataFrame(road_data)
    df["label"] = df.apply(lambda row: 1 if row["road_type"] == "residential" and row["lanes"] < 2 else (0 if row["road_type"] == "residential" and row["lanes"] >= 2 else 2), axis=1)
    # print(df["label"])
    return df
