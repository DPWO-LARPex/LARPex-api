from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime


class PaymentPostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    date: datetime
    amount: int
    payment_method_id: int
    person_id: int
    event_id: int