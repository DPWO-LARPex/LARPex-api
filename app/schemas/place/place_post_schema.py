from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints


class PlacePostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    number: int
    street: str
    city: str

