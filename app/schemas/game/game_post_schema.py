from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict

class GamePostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    name: str
    description: str
    max_players_number: int
    state: str
    difficulty: str
    scenario: str
