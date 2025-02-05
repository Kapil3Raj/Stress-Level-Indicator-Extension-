import os
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Define dataset path dynamically
dataset_path = os.path.join(os.getcwd(), 'server', 'dataset', 'stress_dataset.csv')

# Load dataset
df = pd.read_csv(dataset_path)
print("📊 Dataset loaded successfully!")

# Train/Test Split
X = df[["typing_speed", "hesitation_time", "mouse_speed"]]
y = df["stress_label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
print("🧠 Training model...")
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R² score: {r2}")

# Save model to 'server/models/'
model_dir = os.path.join(os.getcwd(), 'server', 'models')
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, "stress_model.pkl")
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"📁 Model saved at {model_path}!")
