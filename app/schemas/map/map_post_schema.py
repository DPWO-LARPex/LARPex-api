from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class MapPostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    game_id: int
