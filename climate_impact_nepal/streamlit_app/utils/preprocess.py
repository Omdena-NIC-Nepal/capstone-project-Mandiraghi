import pandas as pd 


# Loading datasets and reading the data 

import pandas as pd
import os

def load_data(filepath=None):
    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__), "../../data/sampled_dataset.csv")
    df = pd.read_csv(filepath, parse_dates=['Date'])
    return df



# Feature engineering
def for_ML_model_features(df):
    # Average Wind Speed
    df['Wind_Avg'] = (df['WindSpeed_10m'] + df['WindSpeed_50m']) / 2

    # Monsoon Season Indicator
    df['Is_Monsoon'] = df['Month'].apply(lambda x: 1 if x in [6, 7, 8, 9] else 0)

    # Temperature Difference
    df['Temp_Diff'] = df['MaxTemp_2m'] - df['MinTemp_2m']

    # Wind Speed Total
    wind_cols = ['WindSpeed_10m', 'MaxWindSpeed_10m', 'MinWindSpeed_10m',
                 'WindSpeed_50m', 'MaxWindSpeed_50m', 'MinWindSpeed_50m']
    df['WindSpeed_Total'] = df[wind_cols].sum(axis=1)

    return df



# Saving the processed and updaed data 
def save_updated_data(df, out_path):
    df.to_csv(out_path, index = False)


if __name__ == "__main__":
    input_path = "capstone-project-Mandiraghi/climate_impact_nepal/data/sampled_dataset.csv"
    output_path = "capstone-project-Mandiraghi/climate_impact_nepal/data/processed/nepal_daily_climate_engineered.csv"

    df = load_data(input_path)
    df = for_ML_model_features(df)
    save_updated_data(df, output_path)

