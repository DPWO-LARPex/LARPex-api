

from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from schemas.map.map_get_schema import MapGetSchema

class MilestoneWithStatusSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    milestone_id: int
    name: str
    description: str
    is_reached: bool