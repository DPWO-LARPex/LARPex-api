from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class EventStatusPostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


