import pandas as pd
import folium
import matplotlib.pyplot as plt

# Load the data
def load_gis_data(path):
    df = pd.read_csv(path, parse_dates=['Date'])
    return df

# Filter the data based on selections
def filter_data(df, metric, districts, year, month):
    if districts:
        df = df[df['District'].isin(districts)]
    if year:
        df = df[df['Year'] == year]
    if month:
        df = df[df['Month'] == month]
    return df[['Latitude', 'Longitude', 'District', metric]]

# Create the map
def create_gis_map(df, metric):
    if df.empty:
        return folium.Map(location=[27.7, 85.3], zoom_start=6)

    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=7)
    
    for _, row in df.iterrows():
        value = round(row[metric], 2)
        tooltip = f"{row['District']}<br>{metric}: {value}"
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=6,
            popup=tooltip,
            color='blue',
            fill=True,
            fill_opacity=0.6
        ).add_to(m)
    return m

