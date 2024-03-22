from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class SimpleItemPostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    text: str
    count: int
