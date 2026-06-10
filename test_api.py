# ==========================================================
# TEST_API.PY
# ==========================================================
# Ce script permet de tester automatiquement notre API FastAPI.
#
# Il vérifie :
# 1. Que l'API est accessible.
# 2. Que l'endpoint "/" fonctionne correctement.
# 3. Que l'endpoint "/predict" renvoie une prédiction.
#
# Auteur : Mehdi Azouaou
# Projet : Analyse des ventes et prédiction de la satisfaction
#          client sur la plateforme e-commerce Olist
# ==========================================================

# Import de la bibliothèque requests.
# Elle permet d'envoyer des requêtes HTTP à notre API.
import requests


# ==========================================================
# URL DE L'API
# ==========================================================
# L'API tourne localement sur le port 8000.
# Si l'API est déployée plus tard sur Render ou HuggingFace,
# cette URL devra être remplacée.
BASE_URL = "http://127.0.0.1:8000"


# ==========================================================
# DONNÉES DE TEST
# ==========================================================
# Exemple d'une commande Olist utilisée pour tester
# la prédiction de satisfaction.
#
# Ces variables correspondent exactement aux 10 variables
# utilisées pour entraîner le modèle Machine Learning.
payload = {
    "delivery_time_days": 10,
    "estimated_delivery_time_days": 12,
    "delivery_delay_days": 0,
    "is_late": 0,
    "nb_items": 1,
    "total_price": 120.5,
    "total_freight": 15.9,
    "product_weight_g": 800,
    "customer_state": "SP",
    "payment_type": "credit_card"
}


# ==========================================================
# TEST DE L'ENDPOINT HOME
# ==========================================================
def test_home():
    """
    Vérifie que l'API est bien accessible.

    Endpoint testé :
    GET /

    Résultat attendu :
    Code HTTP = 200
    """

    # Envoi d'une requête GET à l'API.
    response = requests.get(f"{BASE_URL}/")

    # Affichage des informations retournées.
    print("====================================")
    print("TEST 1 : Endpoint Home")
    print("====================================")

    print("Status code :", response.status_code)
    print("Réponse :", response.json())

    # Vérification que le code HTTP est bien 200.
    assert response.status_code == 200


# ==========================================================
# TEST DE L'ENDPOINT PREDICT
# ==========================================================
def test_predict():
    """
    Vérifie que l'API renvoie une prédiction.

    Endpoint testé :
    POST /predict

    Résultat attendu :
    Code HTTP = 200
    Une prédiction est renvoyée.
    """

    # Envoi d'une requête POST contenant les données de test.
    response = requests.post(
        f"{BASE_URL}/predict",
        json=payload
    )

    # Affichage des résultats.
    print("\n====================================")
    print("TEST 2 : Endpoint Predict")
    print("====================================")

    print("Status code :", response.status_code)
    print("Réponse :", response.json())

    # Vérification que l'appel s'est bien déroulé.
    assert response.status_code == 200

    # Vérification de la présence des champs attendus.
    assert "prediction" in response.json()

    assert "prediction_label" in response.json()

    assert "satisfaction_probability" in response.json()


# ==========================================================
# EXECUTION DES TESTS
# ==========================================================
# Ce bloc s'exécute uniquement lorsque le fichier
# est lancé directement avec :
#
# python test_api.py
#
# Il ne s'exécute pas si le fichier est importé.
# ==========================================================
if __name__ == "__main__":

    print("\nDémarrage des tests API...\n")

    # Test de l'endpoint Home.
    test_home()

    # Test de l'endpoint Predict.
    test_predict()

    print("\n✅ Tous les tests API sont passés avec succès.")