from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints


class EventStatusGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

