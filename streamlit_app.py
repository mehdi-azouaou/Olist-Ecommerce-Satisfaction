import requests
import streamlit as st

# ────────────────────────────────────────────────
# ⚙️ Configuration
# ────────────────────────────────────────────────
API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Olist Satisfaction Predictor",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Olist Customer Satisfaction Predictor")
st.write(
    "Renseignez les informations principales d'une commande, "
    "puis cliquez sur **Prédire** pour estimer si le client sera satisfait."
)


# ────────────────────────────────────────────────
# 📡 Appel à l'API FastAPI
# ────────────────────────────────────────────────
def get_prediction(payload: dict) -> dict:
    """Envoie les données de commande à l'API FastAPI et renvoie la prédiction."""
    response = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
    response.raise_for_status()
    return response.json()


# ────────────────────────────────────────────────
# 📝 Formulaire utilisateur
# ────────────────────────────────────────────────
st.subheader("Informations de la commande")

col1, col2 = st.columns(2)

with col1:
    delivery_time_days = st.number_input("Délai réel de livraison (jours)", min_value=0, value=10, step=1)
    estimated_delivery_time_days = st.number_input("Délai estimé de livraison (jours)", min_value=0, value=12, step=1)
    delivery_delay_days = st.number_input("Retard de livraison (jours)", min_value=0, value=0, step=1)
    is_late = st.selectbox("Commande en retard ?", options=[0, 1], format_func=lambda x: "Non" if x == 0 else "Oui")
    nb_items = st.number_input("Nombre d'articles", min_value=1, value=1, step=1)

with col2:
    total_price = st.number_input("Prix total de la commande", min_value=0.0, value=120.5, step=1.0)
    total_freight = st.number_input("Frais de livraison", min_value=0.0, value=15.9, step=1.0)
    product_weight_g = st.number_input("Poids du produit (grammes)", min_value=0.0, value=800.0, step=100.0)

    customer_state = st.selectbox(
        "État du client",
        options=[
            "SP", "RJ", "MG", "RS", "PR", "SC", "BA", "DF", "GO", "ES",
            "PE", "CE", "PA", "MT", "MA", "MS", "PB", "PI", "RN", "AL",
            "SE", "TO", "RO", "AM", "AC", "AP", "RR"
        ]
    )

    payment_type = st.selectbox(
        "Type de paiement",
        options=["credit_card", "boleto", "voucher", "debit_card", "unknown"]
    )


# ────────────────────────────────────────────────
# 📦 Payload envoyé à l'API
# ────────────────────────────────────────────────
payload = {
    "delivery_time_days": delivery_time_days,
    "estimated_delivery_time_days": estimated_delivery_time_days,
    "delivery_delay_days": delivery_delay_days,
    "is_late": is_late,
    "nb_items": nb_items,
    "total_price": total_price,
    "total_freight": total_freight,
    "product_weight_g": product_weight_g,
    "customer_state": customer_state,
    "payment_type": payment_type
}


# ────────────────────────────────────────────────
# 🔮 Prédiction
# ────────────────────────────────────────────────
if st.button("Prédire la satisfaction", type="primary"):
    try:
        result = get_prediction(payload)

        prediction_label = result.get("prediction_label")
        probability = result.get("satisfaction_probability")

        if result.get("prediction") == 1:
            st.success(f"✅ Prédiction : **{prediction_label}**")
        else:
            st.error(f"❌ Prédiction : **{prediction_label}**")

        st.metric(
            label="Probabilité de satisfaction",
            value=f"{probability * 100:.2f}%"
        )

        with st.expander("Voir les données envoyées à l'API"):
            st.json(payload)

        with st.expander("Voir la réponse complète de l'API"):
            st.json(result)

    except requests.exceptions.ConnectionError:
        st.error(
            "❌ Impossible de joindre l'API. "
            "Vérifie que FastAPI tourne avec : `python -m uvicorn app:app --reload`"
        )

    except requests.exceptions.HTTPError as e:
        st.error(f"❌ Erreur API : {e.response.status_code} — {e.response.text}")

    except Exception as e:
        st.error(f"❌ Erreur inattendue : {e}")
