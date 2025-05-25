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

def create_gis_map(df, metric):
    if df.empty:
        return folium.Map(location=[27.7, 85.3], zoom_start=6)

    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=7)

    min_val = df[metric].min()
    max_val = df[metric].max()
    colormap = folium.LinearColormap(colors=['green', 'yellow', 'red'], vmin=min_val, vmax=max_val)
    colormap.caption = f"{metric} scale"
    colormap.add_to(m)

    for _, row in df.iterrows():
        value = row[metric]
        tooltip = f"{row['District']}<br>{metric}: {round(value, 2)}"
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=6,
            popup=tooltip,
            color=colormap(value),
            fill=True,
            fill_color=colormap(value),
            fill_opacity=0.7
        ).add_to(m)

    return m
