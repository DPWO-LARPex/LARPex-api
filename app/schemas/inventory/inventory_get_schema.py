from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime

from schemas.inventory.inventory_content_schema import InventoryContentSchema

class InventoryGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    inventory_id: int
    capacity: int
    player_id: int
    items: list[InventoryContentSchema]

