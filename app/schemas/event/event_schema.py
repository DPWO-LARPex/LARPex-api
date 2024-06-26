from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints
from models.player_model import PlayerModel
from schemas.player.player_info_get_schema import PlayerInfoGetSchema
from schemas.user.user_schema import UserSchema
from datetime import datetime

class EventSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int
    icon : str | None
    tech_desc : str
    client_description : str
    players_count : int
    date : datetime
    price_org : float
    price_buy_in : float
    id_status : int
    id_user : int
    id_place : int
    #players: list[] | None
