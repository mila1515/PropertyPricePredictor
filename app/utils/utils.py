import pandas as pd
import numpy as np

def predict_price(model_dict, input_data, ville="lille"):
    """
    Calcule la prédiction selon le type de bien immobilier avec scaling.
    """
    bien_type = input_data.type_local.strip().lower()
    
    # Sélection du modèle et scaler selon le type
    if bien_type == "maison":
        model = model_dict.get("best_model_maison")
        if ville.lower() == "lille":
            scaler_X = model_dict.get("scaler_X_maison")
            scaler_y = model_dict.get("scaler_y_maison")
        else:  # bordeaux
            scaler_X = model_dict.get("scaler_X_maison_lille")
            scaler_y = model_dict.get("scaler_y_maison_bx")
    elif bien_type == "appartement":
        model = model_dict.get("best_model_appart")
        if ville.lower() == "lille":
            scaler_X = model_dict.get("scaler_X_appart")
            scaler_y = model_dict.get("scaler_y_appart")
        else:  # bordeaux
            scaler_X = model_dict.get("scaler_X_appart_lille")
            scaler_y = model_dict.get("scaler_y_appart_bx")
    else:
        raise ValueError(f"❌ type_local doit être 'Maison' ou 'Appartement' (reçu : '{input_data.type_local}')")
    
    if not model:
        raise ValueError("❌ Modèle introuvable pour ce type de bien")
    if not scaler_X:
        raise ValueError("❌ Scaler X introuvable pour ce type de bien")
    if not scaler_y:
        raise ValueError("❌ Scaler Y introuvable pour ce type de bien")
    
    # Création du DataFrame avec les features numériques uniquement
    # Les modèles ont été entraînés séparément, donc pas besoin d'encodage one-hot
    X = pd.DataFrame([{
        "Surface reelle bati": input_data.surface_bati,
        "Nombre de lots": input_data.nombre_lots,
        "Surface terrain": input_data.surface_terrain
    }])
    
    # Application du scaler X
    X_scaled = scaler_X.transform(X)
    
    # Prédiction (valeur scalée)
    prediction_scaled = model.predict(X_scaled)[0]
    
    # Conversion en prix réel avec l'inverse du scaler Y
    prediction_real = scaler_y.inverse_transform([[prediction_scaled]])[0][0]
    
    return round(float(prediction_real), 2)