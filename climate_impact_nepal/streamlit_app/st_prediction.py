import streamlit as st
import pandas as pd
from utils.prediction import load_model, make_prediction
from utils.model_training import train_model

def show_prediction_ui(df):
    st.title("Prediction")

    st.markdown("___________")

    """  Select Target and Model
    """ 
   
    target_column = st.selectbox("Select variable to predict", [
        "MaxTemp_2m", "MinTemp_2m", "Precip", "WindSpeed_10m",
        "Humidity_2m", "EarthSkinTemp"
    ])

    model_type = st.selectbox("Select model to use", ["RandomForest", "LinearRegression", "SVM"])

    """Load Model
    """
    try:
        model = load_model(target_column, model_type)
    except FileNotFoundError as e:
        st.warning(str(e))
        return

    """
     Get Features used in model
    """

    # Retrain model to extract feature names only 
    _, _, features = train_model(df, target_column, model_type, save_model=False)

    st.subheader("Enter Input Values")

    user_inputs = {}
    for feature in features:
        # Guess range based on column stats
        min_val = float(df[feature].min())
        max_val = float(df[feature].max())
        default_val = float(df[feature].mean())
        user_inputs[feature] = st.slider(f"{feature}", min_value=round(min_val, 2), max_value=round(max_val, 2), value=round(default_val, 2))


    st.markdown("___________")

    """ Predict
    """ 
    
    if st.button(" Predict"):
        result = make_prediction(model, user_inputs, features)
        st.markdown("__________")
        st.success(f"Predicted {target_column}: **{round(result, 2)}**")
