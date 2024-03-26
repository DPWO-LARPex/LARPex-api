from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.game.game_get_schema import GameGetSchema
from services.game_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/user")

@router.get("/{user_id}/games", response_model=list[GameGetSchema])
async def get_games_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return get_games_items_by_user_id(user_id, db)
