import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
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
    "Temp_2m" 
"""

def train_model(df, target_column="MaxTemp_2m", model_type="LinearRegression", selected_features=None, save_model=True, hyperparams=None):
    drop_cols = ['Date', 'District', 'Latitude', 'Longitude', 'YearMonth', 'Year', 'Month']
    # Add target leakage protection
    if target_column == "MaxTemp_2m":
        drop_cols += ["Temp_Diff"]
    elif target_column == "MinTemp_2m":
        drop_cols += ["Temp_Diff"]
    elif target_column == "Temp_2m":
        drop_cols += ["Temp_Diff", "TempRange_2m"]

    if selected_features:
        features = [f for f in selected_features if f in df.columns]
    else:
        features = [col for col in df.columns if col not in drop_cols + [target_column]]

    X = df[features]
    y = df[target_column]

    # Split the train and test model 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model Selection with optional hyperparameters
    hyperparams = hyperparams or {}

    if model_type == "RandomForest":
        model = RandomForestRegressor(
            n_estimators=hyperparams.get("n_estimators", 100),
            max_depth=hyperparams.get("max_depth", None),
            random_state=42
        )
    elif model_type == "LinearRegression":
        model = LinearRegression()
    elif model_type == "Lasso":
        model = Lasso(alpha=hyperparams.get("alpha", 0.1))
    elif model_type == "Ridge":
        model = Ridge(alpha=hyperparams.get("alpha", 1.0))
    elif model_type == "SVM":
        model = SVR(
            kernel=hyperparams.get("kernel", "rbf"),
            C=hyperparams.get("C", 1.0),
            epsilon=hyperparams.get("epsilon", 0.2)
        )
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

    # Train the model 
    model.fit(X_train, y_train)

    # Test / Predict the model 
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Evaluation 
    training_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train, squared=False))
    training_r2 = r2_score(y_train, y_pred_train)
    training_mae = mean_absolute_error(y_train, y_pred_train)

    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test, squared=False))
    test_r2 = r2_score(y_test, y_pred_test)
    test_mae = mean_absolute_error(y_test, y_pred_test)

    metrics = {
        "Training_RMSE": training_rmse,
        "Training_MAE": training_mae,
        "Training_R2_Score": training_r2,
        "Test_RMSE": test_rmse,
        "Test_MAE": test_mae,
        "Test_R2_Score": test_r2
    }

    # Save the Model 
    if save_model:  
        model_dir = "climate_impact_nepal/models"
        os.makedirs(model_dir, exist_ok=True)
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
