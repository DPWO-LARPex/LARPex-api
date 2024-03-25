from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.game.game_post_schema import GamePostSchema
from schemas.game.game_get_schema import GameGetSchema
from services.game_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/games")

@router.get("/", response_model=list[GameGetSchema])
async def get_game(db: Session = Depends(get_db)):
    return get_all_games(db)

@router.get("/{game_id}", response_model=GameGetSchema)
async def get_game_by_id(game_id: int, db: Session = Depends(get_db)):
    return get_game_by_id(game_id, db)

@router.post("/")
async def add_game(simple: GamePostSchema, db: Session = Depends(get_db)):
    return add_game(simple, db)

@router.put("/{game_id}", response_model=GameGetSchema)
async def edit_game(game_id: int, game: GamePostSchema, db: Session = Depends(get_db)):
    return edit_game(game_id, game, db)

@router.delete("/{game_id}", response_model=GameGetSchema)
async def delete_game(game_id: int, db: Session = Depends(get_db)):
    return delete_game(game_id, db)