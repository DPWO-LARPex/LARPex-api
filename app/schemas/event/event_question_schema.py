from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime

class EventQuestionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    event_id : int
    user_id : int
    content : str
