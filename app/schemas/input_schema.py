from pydantic import BaseModel, Field

class InputFeatures(BaseModel):
    """
    InputFeatures defines the schema for property input features used in price prediction.

    Attributes:
        surface_bati (float): Surface area of the building in square meters. Must be greater than 0.
        nombre_pieces (int): Number of rooms in the property. Must be greater than 0.
        type_local (str): Type of the property (e.g., apartment, house).
        surface_terrain (float): Surface area of the land in square meters. Must be greater than or equal to 0.
        nombre_lots (int): Number of lots associated with the property. Must be greater than or equal to 0.

    Note:
        Cette classe est utilisée pour valider et documenter les données d'entrée nécessaires à la prédiction du prix d'un bien immobilier.
    """
    surface_bati: float = Field(..., gt=0)
    nombre_pieces: int = Field(..., gt=0)
    type_local: str
    surface_terrain: float = Field(..., ge=0)
    nombre_lots: int = Field(..., ge=0)

class PredictRequest(BaseModel):
    ville: str
    features: InputFeatures
