from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class BoughtItemGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    is_premium: bool
    virtual_currency: float