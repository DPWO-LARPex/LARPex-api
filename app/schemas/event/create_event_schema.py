from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class CreateEventSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    icon: str
    tech_desc: str
    client_description: str
    players_count: int
    date: datetime
    price_org: float
    price_buy_in: float
    id_status: int
    id_user: int
    id_place: int