from pydantic import BaseModel, Field

class InputFeatures(BaseModel):
    surface_bati: float = Field(..., gt=0)
    nombre_pieces: int = Field(..., gt=0)
    type_local: str
    surface_terrain: float = Field(..., ge=0)
    nombre_lots: int = Field(..., ge=0)

class PredictRequest(BaseModel):
    ville: str
    features: InputFeatures
