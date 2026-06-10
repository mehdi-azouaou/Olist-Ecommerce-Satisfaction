# Analyse des ventes et prédiction de la satisfaction client sur la plateforme e-commerce Olist

## Membres du groupe

* Mehdi AZOUAOU
* Junior VIERA
* Gaetan DE BEYSSAC

---

## Contexte du projet

Dans le cadre de notre formation Data Analyst Full Stack, nous avons réalisé un projet d'analyse de données et de Machine Learning à partir du dataset public **Brazilian E-Commerce Public Dataset by Olist**.

L'objectif principal est d'analyser les performances de la plateforme e-commerce Olist et de développer un modèle permettant de prédire la satisfaction des clients à partir des caractéristiques d'une commande.

---

## Objectifs du projet

Les objectifs du projet sont les suivants :

* Comprendre la structure et la qualité des données.
* Réaliser une analyse exploratoire des données (EDA).
* Nettoyer et préparer les données.
* Construire un modèle de Machine Learning.
* Comparer plusieurs algorithmes de classification.
* Sélectionner le modèle le plus performant.
* Déployer le modèle sous forme d'API FastAPI.
* Créer une interface utilisateur Streamlit permettant de réaliser des prédictions.

---

## Description des données

Le projet repose sur les données publiques d'Olist regroupant :

* Clients
* Commandes
* Produits
* Paiements
* Avis clients
* Vendeurs
* Géolocalisation

Les données couvrent plusieurs centaines de milliers de commandes réalisées au Brésil.

---

## Architecture du projet

data/
├── raw/
├── processed/

models/
├── best_model.pkl

notebooks/
├── EDA_Olist.ipynb
├── Cleaning_Olist.ipynb
├── ML_Olist_V1.ipynb

src/

app.py
streamlit_app.py
test_api.py
requirements.txt

---

## Méthodologie

### 1. Analyse exploratoire

* Analyse des distributions
* Recherche des valeurs manquantes
* Recherche des doublons
* Analyse des délais de livraison
* Analyse des avis clients

### 2. Préparation des données

* Nettoyage des données
* Encodage des variables catégorielles
* Création des variables métiers
* Sélection des variables pertinentes

### 3. Modélisation

Trois modèles ont été comparés :

* Logistic Regression
* Random Forest
* Gradient Boosting

---

## Résultats

| Modèle              | ROC AUC |
| ------------------- | ------- |
| Logistic Regression | 0.686   |
| Random Forest       | 0.708   |
| Gradient Boosting   | 0.725   |

Le modèle Gradient Boosting a obtenu les meilleures performances et a été retenu pour le déploiement.

---

## Déploiement

Le modèle a été déployé sous la forme :

* d'une API REST avec FastAPI ;
* d'une interface utilisateur avec Streamlit.

L'utilisateur peut renseigner les caractéristiques d'une commande et obtenir :

* la prédiction de satisfaction ;
* la probabilité associée.

---

## Conclusion

Ce projet nous a permis de mettre en pratique l'ensemble de la chaîne de valeur d'un projet Data :

* préparation des données ;
* analyse exploratoire ;
* modélisation ;
* évaluation ;
* déploiement ;
* création d'une interface utilisateur.

Les résultats montrent qu'il est possible de prédire la satisfaction client avec une performance satisfaisante à partir des informations disponibles avant la livraison.
