from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.game.game_get_schema import GameGetSchema
from schemas.user.user_get_schema import UserGetSchema
from schemas.user.user_post_schema import UserPostSchema
from schemas.bought_item.bought_item_get_schema import BoughtItemGetSchema
from services.game_service import *
from services.user_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/user")

@router.get("/{user_id}/games", response_model=list[GameGetSchema])
async def get_games_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return get_games_items_by_user_id(user_id, db)

@router.post("/")
async def add_user(simple: UserPostSchema, db: Session = Depends(get_db)):
    return add_user(simple, db)

@router.get("/{user_id}", response_model=UserGetSchema)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return get_game_user_by_id(user_id, db)

@router.get("/{user_id}/bought_items", response_model=list[BoughtItemGetSchema])
async def get_bought_items_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return get_game_bought_items_by_user_id(user_id, db)