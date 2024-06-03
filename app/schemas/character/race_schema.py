from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime

class RaceSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    race_id : int
    name : str
    description : str
