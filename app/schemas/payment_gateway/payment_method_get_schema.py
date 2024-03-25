from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class PaymentMethodGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    payment_name: str