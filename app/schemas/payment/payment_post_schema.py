from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime
from models.payment_gateway.payment_enum import PaymentTargetEnum
    

class PaymentPostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    date: datetime
    amount: int
    payment_method_id: int
    user_id: int
    payment_target: PaymentTargetEnum
    payment_target_id: int