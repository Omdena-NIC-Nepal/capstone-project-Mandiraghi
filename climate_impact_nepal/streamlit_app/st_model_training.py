import streamlit as st
import pandas as pd
from streamlit_app.utils.model_training import train_model

def show_model_trainer(df):
    st.title("Train Climate Prediction Models")
    
    """ Model Target Selection
   """ 
    
    st.subheader(" Select Target Variable to Predict")
    target_column = st.selectbox("Choose a target column:", [
        "MaxTemp_2m", "MinTemp_2m", "Precip", "WindSpeed_10m",
        "Humidity_2m", "EarthSkinTemp"
    ])
    
    
    """ Model Type Selection
   """ 
    
    st.subheader(" Select Model Type")
    model_type = st.selectbox("Choose a model:", ["RandomForest", "LinearRegression"])


    """ Train Model 
   """ 
    
    if st.button("Train Model"):
        with st.spinner("Training in progress..."):
            model, metrics, features = train_model(
                df=df,
                target_column=target_column,
                model_type=model_type,
                save_model=True
            )
        
        st.success(f"Model trained and saved as: model_{target_column}_{model_type}.pkl")
        
        """Show Results
        """

        st.subheader(" Evaluation Metrics")
        st.write(f"**Train RMSE**: {metrics['Training RMSE']:.2f}")
        st.write(f"**Test RMSE**: {metrics['Test RMSE']:.2f}")
        st.write(f"**Train R² Score**: {metrics['Training R2_Score']:.2f}")
        st.write(f"**Test R² Score**: {metrics['Test R2_Score']:.2f}")

        st.subheader("Features Used")
        st.write(features)

