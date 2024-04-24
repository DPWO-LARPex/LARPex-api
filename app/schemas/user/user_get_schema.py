from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class UserGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    firstname: str
    lastname: str