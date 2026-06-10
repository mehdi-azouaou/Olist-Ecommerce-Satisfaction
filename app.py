from fastapi import FastAPI
import pandas as pd
import joblib

# ==========================
# Chargement de l'artefact
# ==========================

artifact = joblib.load("models/deployment_satisfaction_model.joblib")

model = artifact["model"]
feature_names = artifact["feature_names"]

# ==========================
# API
# ==========================

app = FastAPI(
    title="Olist Customer Satisfaction API",
    description="Predict customer satisfaction on Olist",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Olist Customer Satisfaction Prediction API",
        "model": artifact["model_name"],
        "target": artifact["target_name"]
    }


@app.post("/predict")
def predict(data: dict):

    # Création DataFrame
    df = pd.DataFrame([data])

    # Réorganisation des colonnes
    df = df[feature_names]

    # Prédiction
    prediction = model.predict(df)[0]

    # Probabilité d'être satisfait
    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "prediction_label": (
            artifact["classes"][1]
            if prediction == 1
            else artifact["classes"][0]
        ),
        "satisfaction_probability": round(float(probability), 4)
    }