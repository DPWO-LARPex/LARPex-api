
from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from schemas.map.map_get_schema import MapGetSchema

class GameStateGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    game_id: int
    state: str