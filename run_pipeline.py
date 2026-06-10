# run_pipeline.py
# ==========================================================
# PIPELINE MASTER - PROJET OLIST
# ==========================================================
# Ce script permet de vérifier que les principaux éléments
# du projet sont bien présents et fonctionnels :
#
# 1. Vérification de la structure du projet
# 2. Vérification du modèle Machine Learning
# 3. Chargement du modèle sauvegardé en .joblib
# 4. Exécution d'une prédiction test
# 5. Validation du pipeline
#
# Ce fichier ne remplace pas les notebooks EDA / Cleaning / ML.
# Il sert de script master simple pour démontrer que la chaîne
# ML + déploiement est opérationnelle.
# ==========================================================

from pathlib import Path
import joblib
import pandas as pd


# ==========================================================
# 1. CHEMINS PRINCIPAUX DU PROJET
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent

MODEL_PATH = PROJECT_ROOT / "models" / "deployment_satisfaction_model.joblib"

REQUIRED_FILES = [
    PROJECT_ROOT / "app.py",
    PROJECT_ROOT / "streamlit_app.py",
    PROJECT_ROOT / "test_api.py",
    PROJECT_ROOT / "requirements.txt",
    MODEL_PATH,
]


# ==========================================================
# 2. VÉRIFICATION DES FICHIERS
# ==========================================================

def check_project_files():
    """Vérifie que les fichiers essentiels du projet existent."""

    print("\nÉtape 1 - Vérification des fichiers du projet")

    missing_files = []

    for file_path in REQUIRED_FILES:
        if file_path.exists():
            print(f"OK : {file_path.name}")
        else:
            print(f"MANQUANT : {file_path}")
            missing_files.append(file_path)

    if missing_files:
        raise FileNotFoundError(
            "Certains fichiers nécessaires au pipeline sont manquants."
        )

    print("Tous les fichiers essentiels sont présents.")


# ==========================================================
# 3. CHARGEMENT DU MODÈLE
# ==========================================================

def load_model_artifact():
    """Charge l'artefact contenant le modèle et ses métadonnées."""

    print("\nÉtape 2 - Chargement du modèle Machine Learning")

    artifact = joblib.load(MODEL_PATH)

    print("Modèle chargé avec succès.")
    print(f"Modèle retenu : {artifact.get('model_name')}")
    print(f"Variable cible : {artifact.get('target_name')}")
    print(f"Features utilisées : {artifact.get('feature_names')}")

    return artifact


# ==========================================================
# 4. PRÉDICTION TEST
# ==========================================================

def run_test_prediction(artifact):
    """Exécute une prédiction test avec les 10 variables du modèle."""

    print("\nÉtape 3 - Exécution d'une prédiction test")

    model = artifact["model"]
    feature_names = artifact["feature_names"]

    sample_order = {
        "delivery_time_days": 10,
        "estimated_delivery_time_days": 12,
        "delivery_delay_days": 0,
        "is_late": 0,
        "nb_items": 1,
        "total_price": 120.5,
        "total_freight": 15.9,
        "product_weight_g": 800,
        "customer_state": "SP",
        "payment_type": "credit_card",
    }

    input_df = pd.DataFrame([sample_order])
    input_df = input_df[feature_names]

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    label = "Satisfait" if prediction == 1 else "Non satisfait"

    print(f"Prédiction : {label}")
    print(f"Probabilité de satisfaction : {probability:.2%}")

    return prediction, probability


# ==========================================================
# 5. PIPELINE PRINCIPAL
# ==========================================================

def main():
    """Exécute toutes les étapes du pipeline."""

    print("==================================================")
    print("DÉMARRAGE DU PIPELINE OLIST")
    print("==================================================")

    check_project_files()

    artifact = load_model_artifact()

    run_test_prediction(artifact)

    print("\n==================================================")
    print("PIPELINE TERMINÉ AVEC SUCCÈS")
    print("==================================================")


if __name__ == "__main__":
    main()
