from fastapi import APIRouter
from app.schemas.input_schema import InputFeatures
from app.model.model_loader import load_bordeaux_model
from app.utils.utils import predict_price

router = APIRouter()

model_dict = load_bordeaux_model()

@router.post("/predict/bordeaux")
def predict_bordeaux(features: InputFeatures):
    try:
        prediction = predict_price(model_dict, features, ville="bordeaux")
        bien_type = features.type_local
        if bien_type.lower() == "maison":
            model_name = type(model_dict["best_model_maison"]).__name__
        else:
            model_name = type(model_dict["best_model_appart"]).__name__
        return {
            "prix_m2_estime": prediction,
            "ville_modele": "Bordeaux",
            "model": model_name,
            "note": "Modèle entraîné sur Lille, évalué sur Bordeaux"
        }
    except Exception as e:
        return {"error": str(e)}

print("Chargement du modèle Bordeaux OK")