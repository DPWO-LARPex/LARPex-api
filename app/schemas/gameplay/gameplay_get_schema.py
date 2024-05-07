
from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from schemas.map.map_get_schema import MapGetSchema

class GameplayGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    gameplay_id: int
    game_id: int
    player_id: int
    points: int
    time: int
    players_placement: str

