from fastapi import APIRouter
from app.schemas.input_schema import InputFeatures
from app.model.model_loader import load_lille_model
from app.utils.utils import predict_price

router = APIRouter()

model_dict = load_lille_model()

@router.post("/predict/lille")
def predict_lille(features: InputFeatures):
    try:
        prediction = predict_price(model_dict, features, ville="lille")
        bien_type = features.type_local
        if bien_type.lower() == "maison":
            model_name = type(model_dict["best_model_maison"]).__name__
        else:
            model_name = type(model_dict["best_model_appart"]).__name__
        return {
            "prix_m2_estime": prediction,
            "ville_modele": "Lille",
            "model": model_name,
            "note": "Modèle entraîné et évalué sur Lille"
        }
    except Exception as e:
        return {"error": str(e)}
