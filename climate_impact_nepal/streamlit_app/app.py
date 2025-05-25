import numpy as np
import pandas as pd 
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt 

from utils.preprocess import load_data
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
                         [
                           "Overview",
                           "Exploratory Data Analysis", 
                           "Model Training", 
                           "Make Predictions",
                           "GIS Visualization",
                           "Text Analysis",
                           "About"])

data_path = "capstone-project-Mandiraghi/climate_impact_nepal/data/sampled_dataset.csv"
df = load_data()


# Page Content
if page == "Overview":
    st.subheader("Welcome to the Nepal Climate Impact Dashboard 🌏")
    st.markdown("""
        This interactive dashboard helps you explore, analyze, and understand climate change trends and their potential impacts across Nepal.

        🔍 Use Exploratory Data Analysis to uncover patterns and distributions.

        🤖 Train predictive machine learning models on climate features such as temperature, precipitation, humidity, and wind.

        📈 Use trained models to make predictions and evaluate scenarios.

        🗺️ Explore spatial patterns using GIS visualizations by district, year, and climate metrics.

        📚 Analyze climate-related text documents for sentiment, emotion, and insights using NLP techniques.

        Please use the sidebar to explore each functionality in detail.
    """)
    # Add image (place your image in a relative path like 'assets/overview_banner.png')
    st.image("capstone-project-Mandiraghi/climate_impact_nepal/data/Daily_temperature_trends_over_years.png", use_column_width=True)

elif page == "Exploratory Data Analysis":
    st.title("🔍 Exploratory Data Analysis")
    st.markdown("""
        In this section, you can visualize and explore the historical trends and distributions of climate metrics across Nepal.

        - Filter by year, district, or metric.
        - Analyze monsoon trends, seasonal shifts, or average values.
        - Identify anomalies, outliers, or potential data gaps.
    """)
    st_exploratory.show_analysis(df)

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

elif page == "GIS Visualization":
    st.title("🗺️ GIS-Based Visualization")
    st.markdown("""
        This section provides geospatial insights into Nepal’s climate data.

        - Visualize climate metrics across different districts.
        - Filter by year, month, and region.
        - See hotspots or cool zones and analyze spatial variability.
    """)
    st_gis_visualization.show_gis_visualization_ui(df)

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
    st.title("ℹ️ About This Dashboard")
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

        This dashboard is part of a broader initiative to integrate data science with sustainability and policy-making for climate resilience in vulnerable regions like Nepal.
    """)




