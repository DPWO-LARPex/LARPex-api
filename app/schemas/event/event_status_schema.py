from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime

class EventStatusSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int
    name : str
