import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib 
import os


# Training a model for target columns 
"""Target Columns are :
    "MaxTemp_2m",
    "MinTemp_2m",
    "Precip",
    "WindSpeed_10m",
    "WindSpeed_50m",
    "Humidity_2m",
    "EarthSkinTemp",
    "Temp_2m 
"""

def train_model (df, target_column = "MaxTemp_2m", model_type ="Linear Regression", save_model = True):
    drop_cols = ['Date', 'District', 'Latitude', 'Longitude', 'YearMonth']
    features = [col for col in df.columns if col not in drop_cols + [target_column]]

    X = df[features]
    Y = df[target_column]

    # Split the train and test model 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    #Model Selection for each target variables case 
    if model_type == "RandomForest":
        model = RandomForestRegressor(n_estimators = 100, random_state = 42)
    elif model_type == "LinearRegression":
        model = LinearRegression()
    else: 
        raise ValueError(f"Unsupported model type: {model_type}")
    
    #Train the model 
    model.fit(X_train, y_train)

    #Test / Predict the model 
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    #Evaluation 

    training_rmse = mean_squared_error(y_train, y_pred_train, squared = False)
    training_r2 = r2_score(y_train, y_pred_train)
    test_rmse = mean_squared_error(y_test, y_pred_test, squared = False)
    test_r2 = r2_score(y_test, y_pred_test)

    metrics = { 
        "Training RMSE " : training_rmse, 
        "Training R2_Score " : training_r2,
        "Test RMSE " : test_rmse, 
        "Test R2_Score " : test_r2
    }

    # Save the Model 
    if save_model:  
        model_dir = "/Users/mandiraghimire/Desktop/MghiGitManu/capstone-project-Mandiraghi/climate_impact_nepal/models"
        os.makedirs(model_dir, exist_ok= True)
        model_path = f"{model_dir}/model_{target_column}_{model_type}.pkl"
        joblib.dump(model, model_path)

    return model, metrics, features 


# To load previously saved models 
def load_model(target_column="MaxTemp_2m", model_type="RandomForest"):
    model_path = f"models/model_{target_column}_{model_type}.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        raise FileNotFoundError(f"Model not found at {model_path}")
    

