from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from schemas.map.map_get_schema import MapGetSchema

class PlayerInfoGetSchema(BaseModel):
    username: str
    surname: str
    nickname: str
    rank: str
    character_id: int
    user_id: int