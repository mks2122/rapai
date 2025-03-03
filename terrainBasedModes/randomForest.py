import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from fetchData import fetchData
import joblib

data = fetchData()
print(data.head())
# Drop the maxspeed column
data = data.drop(columns=["maxspeed",])


# Encode categorical features
le = LabelEncoder()
data["road_type"] = le.fit_transform(data["road_type"].astype(str))
data["junction"] = data["junction"].map({"no": 0, "yes": 1})  # Convert labels to numbers

# Split into Train/Test
X = data.drop("label", axis=1)
y = data["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
# Export the model
joblib.dump(model, 'random_forest_model.pkl')
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
