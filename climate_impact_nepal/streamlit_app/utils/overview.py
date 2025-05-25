import streamlit as st

def show_overview():
    st.title("📊 Nepal Climate Impact Dashboard Overview")

    st.markdown("""
    Welcome to the **Nepal Climate Impact Dashboard**, an integrated analytical platform developed to monitor, analyze, and forecast climate trends and their socioeconomic impacts across Nepal.

    This dashboard is the result of an interdisciplinary capstone project focused on climate vulnerability, using a combination of structured meteorological data and unstructured text analysis to derive insights.
    """)

    st.subheader("🔍 Exploratory Data Analysis")
    st.markdown("""
    - Explore key statistics, trends, and anomalies in historical climate data.
    - Analyze temperature variations, rainfall distributions, wind trends, and correlation patterns.
    - Includes outlier detection, seasonal trends, and district-level comparisons.
    """)

    st.subheader("🤖 Machine Learning Model Training")
    st.markdown("""
    - Train various regression models including Linear Regression, Ridge, Lasso, Random Forest, and SVM.
    - Users can select specific features, target variables, and view performance metrics such as RMSE, MAE, and R².
    - Supports reproducibility through saved model files.
    """)

    st.subheader("📈 Make Climate Predictions")
    st.markdown("""
    - Predict future climate variables such as temperature, humidity, precipitation, and wind speeds.
    - Enables scenario simulation using trained models.
    - Input custom values to generate on-the-fly forecasts.
    """)

    st.subheader("🗺️ GIS Visualization")
    st.markdown("""
    - View spatial distribution of climate metrics over Nepal.
    - Interactive map lets you filter by district, year, and month.
    - Highlighted features: temperature, wind speed, humidity, and rainfall.
    """)

    st.subheader("📚 Climate Text Analysis")
    st.markdown("""
    - Upload and analyze climate-related reports, articles, or documents.
    - Perform sentiment and emotion classification, named entity recognition, and aspect-based sentiment analysis.
    - Visual and interpretable results for policy insights and awareness.
    """)

    st.subheader("🎯 Why This Matters")
    st.markdown("""
    - Nepal is highly vulnerable to climate change impacts due to its topography and socioeconomic conditions.
    - This dashboard empowers data-driven decision-making and community engagement.
    - It bridges technical data science with actionable climate resilience.
    """)

    st.subheader("📂 Dataset Summary")
    st.markdown("""
    - Primary dataset is a downsampled version of historical daily climate metrics from 1981–2020.
    - Columns include temperature, precipitation, wind speed, humidity, earth skin temperature, and location identifiers.
    - Downsampling was applied to reduce file size under 100MB for optimal performance and deployment.
    """)

    st.info("Use the left sidebar to explore each feature in detail.")
