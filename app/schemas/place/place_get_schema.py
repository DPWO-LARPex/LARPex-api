from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints


class PlaceGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    number: int
    street: str
    city: str

