import streamlit as st
from streamlit_app.utils import exploratory

def show_analysis(df):
    st.title("Exploratory Climate Data Analysis")

    """Display exploratory data analysis
    """
    st.subheader("Basic Dataset Info")
    st.write("Shape of the data:", df.shape)
    st.write("First 5 rows of the dataset:")
    st.dataframe(df.head())

    st.write("Missing values:")
    st.dataframe(df.isnull().sum())

    """Display Rainfall Outliers
    """
    st.subheader("Rainfall Outliers")
    outliers = exploratory.get_rainfall_outliers(df)
    st.dataframe(outliers.head())

    """Display hottest and coldest Days
    """
    st.subheader("Top 5 Hottest Days")
    st.dataframe(exploratory.get_hottest_days(df))

    st.subheader("Top 5 Coldest Days")
    st.dataframe(exploratory.get_coldest_days(df))

    """Plot temperature distribution
    """
    st.subheader("Temperature Distribution")
    fig1 = exploratory.plot_temp_distribution(df)
    st.pyplot(fig1)

    st.subheader("Precipitation Distribution")
    fig2 = exploratory.plot_precip_distribution(df)
    st.pyplot(fig2)

    """Plot temperature distribution
    """
    st.subheader("Daily Temperature Trends")
    fig3 = exploratory.plot_daily_temperature_trend(df)
    st.pyplot(fig3)

    """Plot Hottest districts
    """
    st.subheader("Top 10 Hottest Districts")
    fig4 = exploratory.plot_top_hot_districts(df)
    st.pyplot(fig4)

    """Plot time series and Trends
    """
    st.subheader("Rainfall Over Time")
    fig5 = exploratory.plot_rainfall_trend(df)
    st.pyplot(fig5)

    st.subheader("Wind Speed Trends")
    fig6 = exploratory.plot_wind_speed_trend(df)
    st.pyplot(fig6)

    """
      Correlation 
    """

    st.subheader(" Correlation Between Variables")
    fig_corr7 = exploratory.plot_correlation_heatmap(df)
    st.pyplot(fig_corr7)
