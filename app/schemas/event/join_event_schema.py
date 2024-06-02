from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime

class JoinEventSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    # firstname : str
    # lastname : str
    #email : str
    user_id: str
    character_id: str
    payment_id: str
