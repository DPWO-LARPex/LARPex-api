from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class MapGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    map_id: int
    game_id: int
