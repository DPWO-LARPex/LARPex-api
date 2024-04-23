from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime

from schemas.item.item_get_schema import ItemGetSchema

class InventoryGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    inventory_id: int
    capacity: int
    character_id: int
    items: list[ItemGetSchema]

