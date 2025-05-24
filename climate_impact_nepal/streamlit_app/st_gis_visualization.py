
import pandas as pd
import folium
from streamlit_folium import st_folium
import streamlit as st
import matplotlib.pyplot as plt
from utils.gis_visualization import load_gis_data, filter_data, create_gis_map

def show_gis_visualization_ui(df):
    st.title(" GIS ")

    metric = st.selectbox("Select climate metric to visualize:", [
        "Precip", "Temp_2m", "Humidity_2m", "WindSpeed_10m", "WindSpeed_50m",
        "MaxTemp_2m", "MinTemp_2m", "EarthSkinTemp"
    ])

    all_districts = sorted(df['District'].dropna().unique())
    selected_districts = st.multiselect("Select district(s):", options=all_districts, default=all_districts[:5])

    available_years = sorted(df['Year'].dropna().unique())
    year = st.selectbox("Select Year:", options=available_years)

    available_months = sorted(df['Month'].dropna().unique())
    month = st.selectbox("Select Month:", options=available_months)

    st.markdown("---")
    st.subheader("Map Output")

    filtered_df = filter_data(df, metric, selected_districts, year, month)
    map_obj = create_gis_map(filtered_df, metric)
    st_folium(map_obj, width=700, height=500)

    st.markdown("---")
    st.subheader("Filtered Data")
    st.dataframe(filtered_df)

# For local testing
if __name__ == "__main__":
    df = load_gis_data("../data/processed/sample_nepal_climate.csv")
    show_gis_visualization_ui(df)
