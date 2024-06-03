from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class QrPostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    icon: str