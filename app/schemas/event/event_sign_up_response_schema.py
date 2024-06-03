from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime

class EventSignUpResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    player_id: int
    event_id: int