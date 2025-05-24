import streamlit as st
import pandas as pd
from utils.model_training import train_model

def show_model_trainer(df):
    st.title("Model Training")

    st.markdown("""
    ### Select Target Variable
    Choose the climate-related variable you want to predict.
    """)
    target_column = st.selectbox("Choose a target column:", [
        "MaxTemp_2m", "MinTemp_2m", "Precip", "WindSpeed_10m",
        "WindSpeed_50m", "Humidity_2m", "EarthSkinTemp"
    ])

    st.markdown("""
    ### Select Model Type
    Choose a machine learning model to train.
    """)
    model_type = st.selectbox("Choose a model:", [
        "LinearRegression", "Lasso", "Ridge", "SVM", "RandomForest"
    ])

    st.markdown("""
    ### Optional Hyperparameter Configuration
    Tune the hyperparameters for your selected model.
    """)
    hyperparams = {}

    if model_type == "Lasso" or model_type == "Ridge":
        alpha = st.slider("Alpha (Regularization Strength)", min_value=0.01, max_value=10.0, value=1.0, step=0.01)
        hyperparams['alpha'] = alpha
    elif model_type == "SVM":
        C = st.slider("C (Penalty Parameter)", min_value=0.01, max_value=10.0, value=1.0, step=0.01)
        epsilon = st.slider("Epsilon (Tube Size)", min_value=0.01, max_value=1.0, value=0.2, step=0.01)
        hyperparams['C'] = C
        hyperparams['epsilon'] = epsilon
    elif model_type == "RandomForest":
        max_depth = st.slider("Max Depth", min_value=2, max_value=20, value=10, step=1)
        n_estimators = st.slider("Number of Trees", min_value=10, max_value=300, value=100, step=10)
        hyperparams['max_depth'] = max_depth
        hyperparams['n_estimators'] = n_estimators

    st.markdown("""
    ### 🔍 Select Features for Model Training
    Choose the input features that should be used to predict the selected target.
    """)
    drop_cols = ['Date', 'District', 'Latitude', 'Longitude', 'YearMonth', target_column, 'Year', 'Month']
    all_features = [col for col in df.columns if col not in drop_cols]
    selected_features = st.multiselect("Select features:", options=all_features, default=all_features)

    st.markdown("---")
    if st.button("Train Model"):
        with st.spinner("Training in progress..."):
            model, metrics, features = train_model(
                df=df,
                target_column=target_column,
                model_type=model_type,
                selected_features=selected_features,
                save_model=True,
                hyperparams=hyperparams
            )

        st.success(f"Model trained and saved as: model_{target_column}_{model_type}.pkl")

        st.subheader("📊 Evaluation Metrics")
        st.write(f"**Train RMSE**: {metrics['Training_RMSE']:.2f}")
        st.write(f"**Train MAE**: {metrics['Training_MAE']:.2f}")
        st.write(f"**Train R² Score**: {metrics['Training_R2_Score']:.2f}")
        st.write(f"**Test RMSE**: {metrics['Test_RMSE']:.2f}")
        st.write(f"**Test MAE**: {metrics['Test_MAE']:.2f}")
        st.write(f"**Test R² Score**: {metrics['Test_R2_Score']:.2f}")

        st.subheader("🔍 Features Used")
        st.write(features)
