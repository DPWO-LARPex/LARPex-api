from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class QrGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    qr_id: int
    icon: str
