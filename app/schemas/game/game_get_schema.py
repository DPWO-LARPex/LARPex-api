from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class GameGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    author_id: int
    name: str
    description: str
    max_players_count: int
    min_players_count: int
    state: bool
