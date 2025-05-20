import numpy as np
import pandas as pd 
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt 

from utils.preprocess import load_data
from streamlit_app import st_exploratory
from streamlit_app import st_model_training
from streamlit_app import st_prediction


#Set up Page Configuration 
st.set_page_config(
    page_title = "Nepal Climate Impact Dashboard",
    layout = "wide"
)

# App title and description 
st.title("Climate Trend and Changes Analysis and Predictor")

st.markdown("Historical Temperature and Predict Trend Analysis")


#Setting a sidebar 
st.sidebar.title("Navigation Page")
page = st.sidebar.radio("Navigate", ["Exploratory Data Analysis", "Model Training", "Make Predictions"])

df = load_data()

if page == "Exploratory Data Analysis":
    st_exploratory.show_analysis(df)

elif page == "Model Training":
    st_model_training.show_model_trainer(df)

elif page == "Make Prediction":
    st_prediction.show_prediction_ui(df)

else:
    print("No Prediction to Display")



