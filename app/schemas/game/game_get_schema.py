from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from schemas.map.map_get_schema import MapGetSchema

class GameGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    game_id: int
    user_id: int
    name: str
    description: str
    max_players_number: int
    state: str
    difficulty: str
    scenario: str
    maps: list[MapGetSchema]
