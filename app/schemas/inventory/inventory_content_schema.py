from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime

from schemas.item.item_get_schema import ItemGetSchema

class InventoryContentSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    item: ItemGetSchema

