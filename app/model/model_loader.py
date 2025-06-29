import os
import pickle

def load_lille_model():
    """Charge le bundle Lille avec les meilleurs modèles et scalers"""
    lille_path = os.path.join("models", "model_lille_best.pkl")
    
    with open(lille_path, 'rb') as f:
        lille_bundle = pickle.load(f)
    
    return {
        'best_model_appart': lille_bundle['model_appart'],
        'best_model_maison': lille_bundle['model_maison'],
        'scaler_X_appart': lille_bundle['scaler_X_appart'],
        'scaler_y_appart': lille_bundle['scaler_y_appart'],
        'scaler_X_maison': lille_bundle['scaler_X_maison'],
        'scaler_y_maison': lille_bundle['scaler_y_maison'],
        'features': lille_bundle['features']
    }

def load_bordeaux_model():
    """Charge le bundle Bordeaux avec les 2 meilleurs modèles"""
    bordeaux_path = os.path.join("models", "model_bordeaux_best_2.pkl")
    
    with open(bordeaux_path, 'rb') as f:
        bordeaux_bundle = pickle.load(f)
    
    return {
        'best_model_appart': bordeaux_bundle['best_model_appart'],
        'best_model_maison': bordeaux_bundle['best_model_maison'],
        'scaler_X_appart_lille': bordeaux_bundle['scaler_X_appart_lille'],
        'scaler_X_maison_lille': bordeaux_bundle['scaler_X_maison_lille'],
        'scaler_X_appart_bx': bordeaux_bundle['scaler_X_appart_bx'],
        'scaler_y_appart_bx': bordeaux_bundle['scaler_y_appart_bx'],
        'scaler_X_maison_bx': bordeaux_bundle['scaler_X_maison_bx'],
        'scaler_y_maison_bx': bordeaux_bundle['scaler_y_maison_bx'],
        'features': bordeaux_bundle['features']
    }

