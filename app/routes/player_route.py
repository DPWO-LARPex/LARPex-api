from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.player.player_info_get_schema import PlayerInfoGetSchema
from services.player_service import get_player_by_user_id, get_player_info_by_user_id
from config.database import get_db
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/player")

@router.get("/info-by-uid/{user_id}", response_model=PlayerInfoGetSchema)
async def get_player_info_by_uid_route(user_id: int, db: Session = Depends(get_db)):
    return get_player_info_by_user_id(user_id, db)
