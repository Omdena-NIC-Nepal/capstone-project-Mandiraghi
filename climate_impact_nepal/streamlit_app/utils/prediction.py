import pandas as pd 
import joblib 
import os


""" 
Load a saved model from the models/ directory
"""

def load_model(target_column, model_type="RandomForest"):
    model_path = f"models/model_{target_column}_{model_type}.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        raise FileNotFoundError(f"No model found for {target_column} with {model_type}")

"""
 Prepare input data and make prediction
"""

def make_prediction(model, user_inputs, feature_list):
    """
    user_inputs: dict of {feature_name: value}
    feature_list: list of features the model was trained on
    """
    input_data = pd.DataFrame([user_inputs])  # 1-row DataFrame
    input_data = input_data[feature_list]     # For correct order/columns
    prediction = model.predict(input_data)[0] # to get single prediction value
    return prediction

