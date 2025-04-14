#example code to test the model using a Flask API
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import os
import dill

def normalize_data(df):
    normalized_df = df.copy()
    #normalize all numeric columns
    columns_to_plot = df.select_dtypes(include=[np.number]).columns.tolist()
    for column in columns_to_plot:
        # Normalize each column of the DataFrame between 0 and 1
        min_value = normalized_df[column].min()
        max_value = normalized_df[column].max()
        if min_value == max_value:
            # If all values are the same, set to that value
            normalized_df[column] = min_value
        else:
            normalized_df[column] = (normalized_df[column] - min_value) / (max_value - min_value)
    return normalized_df

current_dir = os.path.dirname(os.path.abspath(__file__))
model_location = os.path.join(current_dir, "model", "svm_model.dill")
app = Flask(__name__)
correlated_columns = ['TWF', 'HDF', 'PWF', 'OSF']


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load the model from the specified location
        if not os.path.exists(model_location):
            return jsonify({"error": "Model file not found"}), 500
        with open(model_location, 'rb') as file:
            model_pipeline = dill.load(file)
        # Read the input data from the request
        data = request.get_json(force=True)
        df = pd.DataFrame(data)
        df = df[correlated_columns]
        df = normalize_data(df.astype(float))
        predictions = model_pipeline.predict(df)
        #convert 1 to failure and 0 to normal
        predictions_text = ["failure" if pred == 1 else "No Failure" for pred in predictions]
        #create a jason output with the float and text predictions
        json_str = jsonify({"prediction_values": predictions.tolist(),"prediction_text": predictions_text})
        return json_str, 200
    except Exception as e:
        # return error code and message in JSON format
        return jsonify({"error": "Invalid input", "description": str(e)}), 400


if __name__ == "__main__":
    #model_pipeline = joblib.load(model_location)
    app.run(host="0.0.0.0", port=5000)