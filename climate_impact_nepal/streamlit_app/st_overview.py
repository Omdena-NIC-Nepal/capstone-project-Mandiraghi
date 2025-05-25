import streamlit as st

def show_overview():
    st.title("🌍 Nepal Climate Impact Dashboard")

    st.markdown("""
    This dashboard is developed as part of a comprehensive capstone project focused on understanding and assessing 
    the impacts of climate change in Nepal. Combining structured climate data and unstructured textual sources, 
    this tool enables users to analyze trends, make predictions, visualize spatial patterns, and extract insights 
    from climate-related documents.
    """)

    st.subheader("📌 Project Motivation")
    st.markdown("""
    Nepal, a country situated in the Himalayas, is highly vulnerable to the impacts of climate change. From glacial
    retreat and extreme weather events to shifts in agricultural patterns and ecosystem degradation, the country faces
    mounting environmental and socioeconomic challenges. The goal of this dashboard is to provide a data-driven 
    platform to support:

    - Climate research and awareness
    - Evidence-based policy making
    - Disaster preparedness and risk reduction
    - Academic and community engagement
    """)

    st.subheader("📊 Key Features")
    st.markdown("""
    **🔍 Exploratory Data Analysis (EDA)**
    - Analyze multivariate climate data across Nepal
    - Identify outliers and extreme events
    - Examine district-wise comparisons and seasonal patterns

    **🤖 Machine Learning Model Training**
    - Choose from Random Forest, SVM, Linear, Lasso, and Ridge Regression
    - Evaluate models using RMSE, MAE, and R² Score
    - Customize thresholds and feature selections

    **📈 Climate Forecasting**
    - Predict future climate conditions
    - Run simulations for planning and adaptation strategies

    **🗺️ GIS Climate Visualization**
    - Interactive maps to visualize temperature, rainfall, humidity, and wind by district and time

    **📚 Climate Text Analysis (NLP)**
    - Extract and analyze text from documents
    - Sentiment and emotion analysis
    - Named entity and aspect-based insights
    """)
    st.image("assets/Daily_temperature_trends_over_years.png", caption="Temperature Trends Over Years")

    st.subheader("📂 Data Sources")
    st.markdown("""
    - Historical climate data from Nepal's Department of Hydrology and Meteorology
    - Processed CSV datasets of temperature and precipitation trends
    - Research papers and climate reports for NLP

    Note: The original dataset (~116 MB) has been reduced to <100 MB for performance and web deployment.
    """)

    st.subheader("🧰 Tools & Technologies")
    st.markdown("""
    - Python, pandas, scikit-learn, matplotlib, seaborn for analysis and modeling
    - Streamlit for dashboard interface
    - Folium and Geopandas for GIS mapping
    - spaCy, TextBlob, and NLTK for NLP capabilities
    """)

    st.subheader("📌 How to Use")
    st.markdown("""
    Use the **sidebar** to navigate through the modules:
    - Overview
    - Exploratory Data Analysis
    - Model Training
    - Make Predictions
    - GIS Visualization
    - Text Analysis
    - About
    """)

