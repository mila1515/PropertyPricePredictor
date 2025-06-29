# Property Price Predictor

Ce projet propose une API de prédiction du prix immobilier (prix au m²) pour différentes villes (Lille, Bordeaux.) à partir de caractéristiques du bien. Il utilise FastAPI, des modèles de machine learning entraînés, et des notebooks d'analyse.

## Fonctionnalités principales
- Prédiction du prix au m² pour un bien immobilier (appartement ou maison)
- API REST (FastAPI) avec endpoints dédiés par ville
- Modèles ML pré-entraînés et scalers sauvegardés
- Notebooks d'analyse et d'entraînement

## Structure du projet
```
app/
  main.py                # Point d'entrée FastAPI
  model/                 # Chargement des modèles/scalers
  routes/                # Endpoints API (ex: predict_lille.py, predict_bordeaux.py)
  schemas/               # Schémas Pydantic pour validation
  utils/                 # Fonctions utilitaires
models/                  # Modèles et scalers sauvegardés (.pkl, .joblib)
data/                    # Données brutes ou nettoyées (non versionnées)
notebooks/               # Notebooks d'analyse et d'entraînement
requirements.txt         # Dépendances Python
README.md                # Ce fichier
```

## Installation
1. **Cloner le dépôt**
```bash
git clone https://github.com/mila1515/PropertyPricePredictor.git
cd test_PropertyPricePredictor
```
2. **Créer un environnement virtuel et installer les dépendances**
```bash
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sous Windows
pip install -r requirements.txt
```

## Lancer l'API
```bash
uvicorn app.main:app --reload
```
L'API sera accessible sur [http://localhost:8000](http://localhost:8000)

## Exemple d'utilisation de l'API
### Endpoint de prédiction (ex: Lille)
- **POST** `/predict/lille`
- **Body JSON exemple :**
```json
{
    "surface_bati": 100,
    "nombre_pieces": 4,
    "type_local": "Appartement",
    "surface_terrain": 0,
    "nombre_lots": 1
}
```
- **Réponse JSON :**
```json
{
  "prix_m2_estime": 7243.19,
  "ville_modele": "Lille",
  "model": "RandomForestRegressor",
  "note": "Modèle entraîné et évalué sur Lille"
}
```

## Notebooks
- Les notebooks d'analyse et d'entraînement sont dans le dossier `notebooks/`.
- Ils permettent d'explorer les données, d'entraîner et d'évaluer les modèles, et de générer les artefacts utilisés par l'API.

## Tests
- Les tests API sont dans le dossier `tests/`.
- Pour lancer les tests :
```bash
pytest
```

## Auteurs
- Projet réalisé par l'équipe Simplon Dev IA.

---
N'hésitez pas à adapter ce README selon vos besoins ou à ajouter des sections (ex: déploiement, contribution, licence, etc.).
