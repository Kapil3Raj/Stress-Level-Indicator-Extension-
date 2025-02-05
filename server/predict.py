import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow requests from Chrome extension

# Absolute path for the model file
model_path = os.path.join(os.getcwd(), 'server', 'models', 'stress_model.pkl')

try:
    model = pickle.load(open(model_path, "rb"))
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", str(e))

@app.route("/predict", methods=["POST"])
def predict_stress():
    try:
        # Getting the input JSON data from the request
        data = request.get_json()
        print("Received data:", data)  # Debugging input data

        # Get the input values for typing_speed, hesitation_time, and mouse_speed
        typing_speed = data.get("typing_speed", 50)  # Default to 50 if not provided
        hesitation_time = data.get("hesitation_time", 1.5)  # Default to 1.5 if not provided
        mouse_speed = data.get("mouse_speed", 40)  # Default to 40 if not provided

        # Create the feature array for prediction
        features = np.array([[typing_speed, hesitation_time, mouse_speed]])
        print("Input to model:", features)  # Debugging model input

        # Predict stress level (continuous output between 1 and 10)
        stress_level = model.predict(features)[0]

        # Ensure the stress level is within the range of 1-10
        stress_level = max(1, min(10, round(stress_level, 1)))  # Clamping the value to stay within the range 1-10

        # Prepare the response with the predicted stress level
        response = {"stress_level": stress_level}
        print("Response:", response)  # Debugging output response

        # Return the JSON response
        return jsonify(response)

    except Exception as e:
        # Handle any errors and provide the error message in the response
        print("Error during prediction:", str(e))
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
