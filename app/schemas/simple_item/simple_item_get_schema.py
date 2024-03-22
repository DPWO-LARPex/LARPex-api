from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class SimpleItemGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    text: str
    count: int

        