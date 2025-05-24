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
    st.write("Shape of the data:", df.shape)

    st.markdown("===========================================================")

    st.write("First 5 rows of the dataset:")
    st.dataframe(df.head())

    st.markdown("============================================================")

    st.write("Missing values:")
    st.dataframe(df.isnull().sum())

    st.markdown("============================================================")

    """Display Rainfall Outliers
    """
    st.subheader("Rainfall Outliers")
    outliers = exploratory.get_rainfall_outliers(df)
    st.dataframe(outliers.head())

    st.markdown("==============================================================")

    """Display hottest and coldest Days
    """
    st.subheader("Top 5 Hottest Days")
    st.dataframe(exploratory.get_hottest_days(df))

    st.markdown("==============================================================")

    st.subheader("Top 5 Coldest Days")
    st.dataframe(exploratory.get_coldest_days(df))

    st.markdown("===============================================================")

    """Temperature on Map
    """
    st.subheader("Temperature across the districts")
    fig_map = exploratory.plot_show_map(df)
    st.pyplot(fig_map)
    st.markdown("===============================================================")



    """Plot temperature distribution
    """
    st.subheader("Temperature Distribution")
    fig1 = exploratory.plot_temp_distribution(df)
    st.pyplot(fig1)

    st.markdown("=================================================================")

    st.subheader("Precipitation Distribution")
    fig2 = exploratory.plot_precip_distribution(df)
    st.pyplot(fig2)

    st.markdown("====================================================================")


    """Plot temperature distribution
    """
    st.subheader("Daily Temperature Trends")
    fig3 = exploratory.plot_daily_temperature_trend(df)
    st.pyplot(fig3)

    st.markdown("=================================================================")

    """Plot Hottest districts
    """
    st.subheader("Top 10 Hottest Districts")
    fig4 = exploratory.plot_top_hot_districts(df)
    st.pyplot(fig4)

    st.markdown("==================================================================")

    """Plot time series and Trends
    """
    st.subheader("Rainfall Over Time")
    fig5 = exploratory.plot_rainfall_trend(df)
    st.pyplot(fig5)

    st.markdown("=======================================================================")

    st.subheader("Wind Speed Trends")
    fig6 = exploratory.plot_wind_speed_trend(df)
    st.pyplot(fig6)

    st.markdown("===================================================================")

    """
      Correlation 
    """

    st.subheader(" Correlation Between Variables")
    fig_corr7 = exploratory.plot_correlation_heatmap(df)
    st.pyplot(fig_corr7)

    st.markdown("======================================================================")

    """
      Pair Plot 
    """
    st.subheader("Pair Plot of Selected Climate Variables")
    fig_pair8 = exploratory.plot_pairplot(df)
    st.pyplot(fig_pair8)

    st.markdown("======================================================================")

    """
    Seasonal Plots
    """
    st.subheader("Seasonal Plot of Temperature") 
    fig_seasonal9 = exploratory.plot_seasonal(df.copy(), 'Temp_2m')
    st.pyplot(fig_seasonal9)
    

