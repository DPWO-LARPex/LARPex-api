from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class UserPostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    firstname: str
    lastname: str
    email: str