from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime

class ClassSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    class_id : int
    name : str
    description : str
