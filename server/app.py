from flask import Flask, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows communication between frontend (Chrome extension) and backend

# Load the trained AI model
model = pickle.load(open("models/stress_model.pkl", "rb"))

@app.route("/")
def home():
    return jsonify({"message": "Stress Detection API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json  # Get keyboard/mouse activity data from extension

        # Extract features
        features = np.array([
            data.get("typing_speed", 0),
            data.get("hesitation_time", 0),
            data.get("mouse_speed", 0)
        ]).reshape(1, -1)

        # Predict stress level
        prediction = model.predict(features)[0]  # 0 (low stress) or 1 (high stress)
        stress_score = model.predict_proba(features)[0][1]  # Probability of high stress

        return jsonify({"stress_level": round(stress_score, 2)})  # Return stress score (0-1)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
