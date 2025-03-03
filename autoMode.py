import pandas as pd
import numpy as np
import joblib
from terrainBasedModes.fetchData import fetchData 
from sklearn.preprocessing import LabelEncoder

model = joblib.load('random_forest_model.joblib')
lat, lon = 12.680049486037065, 79.95818724550932
data = fetchData(lat,lon)  

data = data.drop(columns=["maxspeed"])  

le = LabelEncoder()
data["road_type"] = le.fit_transform(data["road_type"].astype(str))
data["junction"] = data["junction"].map({"no": 0, "yes": 1})

X_new = data.drop("label", axis=1)  


predictions = model.predict(X_new)

data['predictions'] = predictions
data['predictions'] = data['predictions'].map({0: 'Eco', 1: 'Normal', 2: 'Sport'})
# print(data[['road_type', 'junction', 'predictions']]) 
print(data['predictions'][0])

