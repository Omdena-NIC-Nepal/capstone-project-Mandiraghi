# Climate Impact Assessment and Prediction System for Nepal

## Project Overview

This project presents an integrated data analysis system focused on monitoring, analyzing, and forecasting the impacts of climate change in Nepal. Designed as a full-cycle solution, it leverages exploratory data analysis (EDA), machine learning (ML), geospatial visualization (GIS), and natural language processing (NLP) to provide information to data science studnets and ethusiasts about emerging climate risks and patterns in Nepal's vulnerable regions.

## Objective

To create an end-to-end analytical platform that combines quantitative climate metrics and unstructured textual insights to:

* Identify key climate trends and vulnerabilities in Nepal.
* Train predictive models for future temperature, precipitation, and other key climate indicators.
* Visualize geospatial distribution of climate variables.
* Analyze climate-related public discourse using NLP.

## Key Features

### 1. Exploratory Data Analysis

* Regional analysis of temperature, precipitation, wind speed, and humidity trends.
* Monsoon season behavior and extreme weather variability.
* Interactive data visualizations using Streamlit.

### 2. Machine Learning Modeling

* Supports Random Forest, SVM, Linear Regression, Lasso, and Ridge Regression.
* Dynamic feature selection via multiselect interface.
* Model evaluation includes RMSE, MAE, and R2 metrics.
* Configurable thresholds and regularization parameters.

### 3. GIS Visualization

* Folium-based district-wise mapping of selected climate metrics.
* Filters for district, year, and month.
* Outputs interactive spatial heatmaps for climate monitoring.

### 4. Text Analysis (NLP)

* Upload and process PDF/TXT climate articles.
* Sentiment analysis (polarity, subjectivity) of public narratives.
* Named Entity Recognition (NER) for location and event extraction.
* Aspect-based sentiment classification (e.g., rainfall, government response).

## Tools and Technologies

* **Frontend**: Streamlit
* **ML**: scikit-learn (Linear Regression, RandomForest, SVM, Lasso, Ridge)
* **Visualization**: Matplotlib, Seaborn, Folium
* **NLP**: spaCy, TextBlob
* **GIS**: streamlit-folium, Leaflet
* **PDF Processing**: PyMuPDF (fitz)

## Dataset Sources

* Custom climate dataset (daily temperature, wind, humidity, precipitation) for Nepal.
* Textual documents related to climate change collected from reports and publications.
* Source:  https://www.kaggle.com/code/sanjipmahat/nepal-daily-climate 

## Dataset Optimization

To ensure app performance and ease of sharing via GitHub:

* The original raw climate files exceeded 100MB and were unsuitable for upload to GitHub.
* We extracted a representative sample (sampled\_dataset.csv) containing balanced observations across different districts, years, and climate metrics.
* This reduced file is still robust enough for training, predictions, visualization, and text analysis workflows.

## Folder Structure

```
climate_impact_nepal/
├── data/                   # Raw, processed, and uploaded datasets
├── models/                # Saved machine learning models
├── notebooks/             # Jupyter notebooks for EDA and feature engineering
├── reports/               # Generated analysis reports
├── streamlit_app/         # Streamlit pages and utils
│   ├── app.py             # Main dashboard script
│   ├── st_model_training.py
│   ├── st_prediction.py
│   ├── st_gis_visualization.py
│   ├── st_text_analysis.py
│   └── utils/
├── requirements.txt       # Python dependencies
└── README.md              # Project overview and setup
```

## How to Run

1. Clone this repository.
2. Create a virtual environment and activate it:

   ```bash
   conda create -n airish_env python=3.9
   conda activate airish_env
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   python -m textblob.download_corpora
   ```
4. Run the Streamlit app:

   ```bash
   streamlit run streamlit_app/app.py
   ```

## Future Directions

* Integration with real-time IoT sensors.
* Improved NLP pipeline with multilingual support for Nepali.
* Advanced modeling using XGBoost or Deep Learning (LSTM for climate series).
* Mobile-ready dashboard deployment.
* Cross-border data collaboration (e.g., Himalayan region).

## Contributors

* Mandira Ghimire (Omdena Student)

