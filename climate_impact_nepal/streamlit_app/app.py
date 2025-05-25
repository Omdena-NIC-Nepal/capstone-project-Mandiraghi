import numpy as np
import pandas as pd 
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt 

from utils.preprocess import load_data
import st_overview
import st_exploratory
import st_model_training
import st_prediction
import st_gis_visualization 
import st_text_analysis

#Set up Page Configuration 
st.set_page_config(
    page_title = "Nepal Climate Impact Dashboard",
    layout = "wide"
)

# Inject custom CSS for background color and spacing
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F0F8FF;
    }
    .block-container {
        padding: 2rem 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# App title and description 
st.title("Nepal Climate Trends & Analytics Portal ")


#Setting a sidebar 
st.sidebar.title("Navigation Page")
page = st.sidebar.radio("Go to",
                         ["Overview of the Dashboard",
                           "Exploratory Data Analysis",
                           "GIS Visualization", 
                           "Model Training", 
                           "Make Predictions",
                           "Text Analysis",
                           "About the Project"])

data_path = "capstone-project-Mandiraghi/climate_impact_nepal/data/sampled_dataset.csv"
df = load_data()


# Page Content
if page == "Overview of the Dashboard":
    st_overview.show_overview()
    
elif page == "Exploratory Data Analysis":
    st.title("🔍 Exploratory Data Analysis")
    st.markdown("""
        In this section, you can visualize and explore the historical trends and distributions of climate metrics across Nepal.

        - Filter by year, district, or metric.
        - Analyze monsoon trends, seasonal shifts, or average values.
        - Identify anomalies, outliers, or potential data gaps.
    """)
    st_exploratory.show_analysis(df)

elif page == "GIS Visualization":
    st.title("🗺️ GIS-Based Visualization")
    st.markdown("""
        This section provides geospatial insights into Nepal’s climate data.

        - Visualize climate metrics across different districts.
        - Filter by year, month, and region.
        - See hotspots or cool zones and analyze spatial variability.
    """)
    st_gis_visualization.show_gis_visualization_ui(df)

elif page == "Model Training":
    st.title("🤖 Train a Climate Prediction Model")
    st.markdown("""
        Select a climate target variable (e.g., MaxTemp, Precipitation) and train a model of your choice.

        - Choose from Linear Regression, Random Forest, or SVM.
        - Customize feature selection.
        - Automatically evaluates model accuracy using RMSE and R².
    """)
    st_model_training.show_model_trainer(df)

elif page == "Make Predictions":
    st.title("📊 Predict Climate Metrics")
    st.markdown("""
        Use a trained model to make predictions for specific climate variables.

        - Select the model and variable you want to predict.
        - Adjust input sliders for features used during training.
        - Get an instant forecasted value based on your inputs.
    """)
    st_prediction.show_prediction_ui(df)


elif page == "Text Analysis":
    st.title("Insights on Climate Change")
    st.markdown("""
        Upload and analyze climate-related PDFs or TXT files.

        - Perform sentiment analysis (positive/negative/neutral).
        - Extract named entities (people, locations, organizations).
        - Tokenize and analyze keywords and trends.
    """)
    st_text_analysis.show_text_analysis_ui()

else:
    st.title("ℹ️ About This Project ")
    st.markdown("""
        This interactive dashboard was developed as a capstone project for the **Omdena NIC Nepal Local Chapter** with the aim of analyzing and predicting climate change impacts in **Nepal**. It combines geospatial, statistical, and natural language processing (NLP) techniques to offer a comprehensive perspective on climate patterns, risks, and perceptions.

        ### 🔍 Key Capabilities:
        - **Exploratory Data Analysis:** Visualizing climate variables such as temperature, rainfall, humidity, and wind speed over time and region.
        - **Predictive Modeling:** Training machine learning models (Linear Regression, Random Forest, SVM, Ridge, Lasso) to forecast key climate variables.
        - **GIS Visualization:** Mapping spatial distribution of climate metrics across districts using Folium and Streamlit-Folium.
        - **Text Analysis:** Extracting and analyzing public climate perception from PDFs using sentiment analysis, emotion classification, and named entity recognition.

        ### 🛠 Tools & Technologies:
        - **Python** for scripting and data pipelines
        - **Streamlit** for front-end dashboard
        - **scikit-learn**, **xgboost** for modeling
        - **nltk**, **spaCy**, **TextBlob** for NLP
        - **folium**, **geopandas**, **rasterio** for spatial analysis
        - **matplotlib**, **seaborn**, **plotly** for visualization

        ### 👤 Project Author:
        **Mandira Ghimire**  (Omdena Student)
        - [GitHub Profile](https://github.com/Mandiraghi)  
        - [LinkedIn Profile](https://www.linkedin.com/in/mandirag/)

       """)




