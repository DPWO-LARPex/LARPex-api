from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime
from .race_schema import RaceSchema
from .class_schema import ClassSchema

class CharactersSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    character_id : int
    name : str
    bio : str
    #race: RaceSchema
    #class_: ClassSchema
