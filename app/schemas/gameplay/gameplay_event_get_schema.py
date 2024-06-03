

from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from schemas.event.event_schema import EventSchema
from schemas.game.game_get_schema import GameGetSchema
from schemas.gameplay.gameplay_get_schema import GameplayGetSchema
from schemas.map.map_get_schema import MapGetSchema

class GameplayEventGetSchema(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)

    gameplay: GameplayGetSchema
    event: EventSchema