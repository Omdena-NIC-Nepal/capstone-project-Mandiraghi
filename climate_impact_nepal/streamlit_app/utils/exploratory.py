import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import folium
from streamlit_folium import folium_static


""" Load Raw Climate Dataset
""" 
def load_raw_data():
    df = pd.read_csv('data/processed/sampled_dataset.csv', parse_dates=['Date'], dayfirst=True)
    return df

""" 
Basic Dataset Summary
"""
def get_dataset_info(df):
    info = {
        "shape": df.shape,
        "columns": list(df.columns),
        "nulls": df.isnull().sum(),
        "describe": df.describe()
    }
    return info


"""
Rainfall Outliers
"""
def get_rainfall_outliers(df):
    Q1 = df['Precip'].quantile(0.25)
    Q3 = df['Precip'].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df['Precip'] < Q1 - 1.5 * IQR) | (df['Precip'] > Q3 + 1.5 * IQR)]
    return outliers[['Date', 'District', 'Precip']]


"""
Top 5 Hottest Days
"""
def get_hottest_days(df):
    return df[['Date', 'District', 'MaxTemp_2m']].sort_values(by='MaxTemp_2m', ascending=False).head(5)


"""
 Top 5 Coldest Days
"""
def get_coldest_days(df):
    return df[['Date', 'District', 'MinTemp_2m']].sort_values(by='MinTemp_2m', ascending=True).head(5)

# Direction to save plots locally
SAVE_DIR = "reports/figures"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_plot(fig, filename):
    fig.savefig(f"{SAVE_DIR}/{filename}", bbox_inches='tight')


"""
Temperature of Map
"""
def plot_show_map(df):
    m = folium.Map(location=[28.3949, 84.1240], zoom_start=6)
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5,
            popup=f"{row['District']} - Temp: {row['Temp_2m']}°C",
            color='red' if row['Temp_2m'] > 35 else 'blue'
        ).add_to(m)
    folium_static(m)


"""
 Precipitation Distribution Plot
"""
def plot_precip_distribution(df, save = False):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['Precip'], bins=40, kde=True, ax=ax)
    ax.set_title("Distribution of Daily Precipitation")
    if save:
        save_plot(fig, "precip_distribution.png")
    return fig


"""
Temperature Distribution Plot
"""
def plot_temp_distribution(df, save = False):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df['Temp_2m'], bins=40, kde=True, ax=ax)
    ax.set_title("Distribution of Temperature")
    if save:
        save_plot(fig, "temperature_distribution.png")
    return fig


"""
Daily Temperature Trends Plot
"""
def plot_daily_temperature_trend(df, save = False):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.lineplot(data=df, x='Date', y='MaxTemp_2m', label='Max Temp', ax=ax)
    sns.lineplot(data=df, x='Date', y='MinTemp_2m', label='Min Temp', ax=ax)
    ax.set_title("Daily Temperature Trends in Nepal")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True)
    ax.legend()
    if save:
        save_plot(fig, "temperature_trend.png")
    return fig


"""
 Top 10 Hottest Districts Plot
"""
def plot_top_hot_districts(df, save = False):
    district_avg_temp = df.groupby('District')['Temp_2m'].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=district_avg_temp.values, y=district_avg_temp.index, ax=ax)
    ax.set_title("Top 10 Hottest Districts (Avg Temp)")
    ax.set_xlabel("Temperature (°C)")
    if save:
        save_plot(fig, "top_10_hottest_districts.png")
    return fig


"""
Rainfall Trend Over Time Plot
"""
def plot_rainfall_trend(df, save = False):
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.lineplot(data=df, x='Date', y='Precip', ax=ax)
    ax.set_title("Rainfall Trend Over Time")
    ax.grid(True)
    if save:
        save_plot(fig, "rainfall_trend.png")
    return fig


"""
 Wind Speed Trend Plot
"""
def plot_wind_speed_trend(df, save = False):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.lineplot(data=df, x='Date', y='WindSpeed_10m', label='10m Wind', ax=ax)
    sns.lineplot(data=df, x='Date', y='WindSpeed_50m', label='50m Wind', ax=ax)
    ax.set_title("Wind Speed Trends (10m vs 50m)")
    ax.set_ylabel("Wind Speed (m/s)")
    ax.legend()
    ax.grid(True)
    if save:
        save_plot(fig, "wind_speed_trend.png")
    return fig


""" 
Correlation Heatmap 
"""
def plot_correlation_heatmap(df, save = False):
    numerical_df = df[[
        "MaxTemp_2m", "MinTemp_2m", "Humidity_2m", "Precip",
        "WindSpeed_10m", "WindSpeed_50m", "EarthSkinTemp"
    ]].dropna()
    sample_size= min(1000, len(numerical_df))
    if sample_size == 0:
        raise ValueError("No data available for correlation heatmap.")

    numerical_df = numerical_df.sample(n=sample_size, random_state=42)


    fig, ax = plt.subplots(figsize=(14, 10))
    sns.heatmap(numerical_df.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap of Climate Variables")
    if save:
        save_plot(fig, "correlation_heatmap.png")
    return fig


"""
    Create a pair plot for selected climate variables.
"""
def plot_pairplot(df, save=False):
    numerical_df = df[[
        "MaxTemp_2m", "MinTemp_2m", "Humidity_2m", "Precip",
        "WindSpeed_10m", "WindSpeed_50m", "EarthSkinTemp"
    ]].dropna()

    sample_size = min(1000, len(numerical_df))
    if sample_size == 0:
        raise ValueError("No data available for pair plot.")

    numerical_df = numerical_df.sample(n=sample_size, random_state=42)

    fig = sns.pairplot(numerical_df)
    if save:
        fig.savefig("pairplot.png")
    return fig



"""
    Seasonal Plots over time
"""
def plot_seasonal(df, column, save=False):

    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    pivot_table = df.pivot_table(values=column, index='Month', columns='Year')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=pivot_table, ax=ax)
    ax.set_title(f'Seasonal Plot of {column}')
    ax.set_xlabel('Month')
    ax.set_ylabel(column)
    if save:
        save_plot(fig, f"{column}_seasonal.png")
    return fig


#Saving the figures locally 
if __name__ == "__main__":
    df = load_raw_data()

    plot_temp_distribution(df, save=True)
    plot_precip_distribution(df, save=True)
    plot_daily_temperature_trend(df, save=True)
    plot_top_hot_districts(df, save=True)
    plot_rainfall_trend(df, save=True)
    plot_wind_speed_trend(df, save=True)
    plot_correlation_heatmap(df, save=True)
    plot_pairplot(df, save=True)
    plot_seasonal(df, save=True)


    print(" All plots saved to reports/figures/")

