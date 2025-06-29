from fastapi import APIRouter
from app.schemas.input_schema import PredictRequest, InputFeatures
from app.model.model_loader import load_lille_model, load_bordeaux_model
from app.utils.utils import predict_price

router = APIRouter()

# Charger les modèles une seule fois
lille_model_dict = load_lille_model()
bordeaux_model_dict = load_bordeaux_model()

@router.post("/predict")
def predict(request: PredictRequest):
    ville = request.ville.strip().lower()
    features = request.features
    if ville == "lille":
        model_dict = lille_model_dict
    elif ville == "bordeaux":
        model_dict = bordeaux_model_dict
    else:
        return {"error": f"Ville inconnue : {request.ville}. Choisissez 'lille' ou 'bordeaux'."}
    try:
        prediction = predict_price(model_dict, features, ville=ville)
        bien_type = features.type_local
        if bien_type.lower() == "maison":
            model_name = type(model_dict["best_model_maison"]).__name__
        else:
            model_name = type(model_dict["best_model_appart"]).__name__
        return {
            "prix_m2_estime": prediction,
            "ville_modele": ville.capitalize(),
            "model": model_name
        }
    except Exception as e:
        return {"error": str(e)} 