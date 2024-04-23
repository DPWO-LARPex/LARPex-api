from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from schemas.map.map_get_schema import MapGetSchema

class MicrostoreItemGetSchema(BaseModel):
    id: int
    name: str
    description: str
    price: float
