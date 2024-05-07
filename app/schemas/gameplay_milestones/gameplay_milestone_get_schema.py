
from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from schemas.milestone.milestone_with_status_schema import MilestoneWithStatusSchema
from schemas.map.map_get_schema import MapGetSchema

class GameplayMilestoneGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    gameplay_id: int
    milestones: list[MilestoneWithStatusSchema]