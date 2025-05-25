import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
from utils import exploratory


def show_analysis(df):
    st.title("EDA")

    """Display exploratory data analysis
    """
    st.subheader("Basic Dataset Info")
    st.markdown("""Provides a quick overview of the dataset,
                 including its shape and the first few rows to understand the structure.""")
    st.write("Shape of the data:", df.shape)

    st.markdown("================================________======================================")

    st.write("First 5 rows of the dataset:")
    st.dataframe(df.head())

    st.markdown("================================________========================================")

    st.write("Missing values:")
    st.markdown("""Shows how many values are missing in each column to assess data completeness.""")
    st.dataframe(df.isnull().sum())

    st.markdown("================================________========================================")

    """Display Rainfall Outliers
    """
    st.subheader("Rainfall Outliers")
    st.markdown("""Identifies data points with extreme or unusual precipitation values for further inspection.""")
    outliers = exploratory.get_rainfall_outliers(df)
    st.dataframe(outliers.head())

    st.markdown("================================________=========================================")

    """Display hottest and coldest Days
    """
    st.subheader("Top 5 Hottest Days")
    st.markdown("""Displays the five days with the highest recorded temperatures in the dataset.""")
    st.dataframe(exploratory.get_hottest_days(df))

    st.markdown("=================================________==========================================")

    st.subheader("Top 5 Coldest Days")
    st.markdown("""Displays the five days with the lowest recorded temperatures in the dataset.""")
    st.dataframe(exploratory.get_coldest_days(df))

    st.markdown("==================================________=========================================")

    """Temperature on Map
    """
    st.subheader("Temperature across the districts")
    st.markdown("""Visualizes temperature distribution across different districts in Nepal.""")
    fig_map = exploratory.plot_show_map(df)
    st.pyplot(fig_map)
    st.markdown("==================================________==========================================")



    """Plot temperature distribution
    """
    st.subheader("Temperature Distribution")
    st.markdown("""Plots the distribution of temperature values across the dataset.""")
    fig1 = exploratory.plot_temp_distribution(df)
    st.pyplot(fig1)

    st.markdown("==================================________===========================================")

    st.subheader("Precipitation Distribution")
    st.markdown("""Plots the distribution of precipitation values across the dataset.""")
    fig2 = exploratory.plot_precip_distribution(df)
    st.pyplot(fig2)

    st.markdown("==================================________===========================================")


    """Plot temperature distribution
    """
    st.subheader("Daily Temperature Trends")
    st.markdown("""A line plot showing how temperature fluctuates daily over time, helping to spot seasonal or long-term trends.""")
    fig3 = exploratory.plot_daily_temperature_trend(df)
    st.pyplot(fig3)

    st.markdown("=====================================________=========================================")

    """Plot Hottest districts
    """
    st.subheader("Top 10 Hottest Districts")
    st.markdown("""Shows the top 10 districts with the highest average temperatures.""")
    fig4 = exploratory.plot_top_hot_districts(df)
    st.pyplot(fig4)

    st.markdown("========================================________======================================")

    """Plot time series and Trends
    """
    st.subheader("Rainfall Over Time")
    st.markdown("""A line plot showing how rainfall fluctuates over time, helping to spot seasonal or long-term trends.""")
    fig5 = exploratory.plot_rainfall_trend(df)
    st.pyplot(fig5)

    st.markdown("====================================________===========================================")

    st.subheader("Wind Speed Trends")
    st.markdown("""A line plot showing how wind speed fluctuates over time, helping to spot seasonal or long-term trends.""")
    fig6 = exploratory.plot_wind_speed_trend(df)
    st.pyplot(fig6)

    st.markdown("======================================________==========================================")

    """
      Correlation 
    """

    st.subheader(" Correlation Between Variables")
    st.markdown("""A heatmap showing the correlation between different variables in the dataset.""")
    fig_corr7 = exploratory.plot_correlation_heatmap(df)
    st.pyplot(fig_corr7)

    st.markdown("========================================________===========================================")

    """
      Pair Plot 
    """
    st.subheader("Pair Plot of Selected Climate Variables")
    st.markdown("""A pair plot showing the relationship between different climate variables.""")
    fig_pair8 = exploratory.plot_pairplot(df)
    st.pyplot(fig_pair8)

    st.markdown("========================================________============================================")

    """
    Seasonal Plots
    """
    st.subheader("Seasonal Plot of Temperature") 
    st.markdown("""A seasonal plot showing how temperature fluctuates over time, helping to spot seasonal or long-term trends.""")
    fig_seasonal9 = exploratory.plot_seasonal(df.copy(), 'Temp_2m')
    st.pyplot(fig_seasonal9)
    

