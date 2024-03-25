from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.gra.gra_get_schema import GraGetSchema
from schemas.gra.gra_post_schema import GraPostSchema
from services.gra_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/gry")

@router.get("/", response_model=list[GraGetSchema])
async def get_games(db: Session = Depends(get_db)):
    return get_all_gra_items(db)

@router.get("/{id_gry}", response_model=GraGetSchema)
async def get_game_by_id(id_gry: int, db: Session = Depends(get_db)):
    return get_gra_item_by_id(id_gry, db)

@router.post("/")
async def add_game(simple: GraPostSchema, db: Session = Depends(get_db)):
    return add_gra_item(simple, db)

@router.put("/{id_gry}", response_model=GraGetSchema)
async def edit_game(id_gry: int, game: GraPostSchema, db: Session = Depends(get_db)):
    return edit_gra_item(id_gry, game, db)

@router.delete("/{id_gry}", response_model=GraGetSchema)
async def delete_game(id_gry: int, db: Session = Depends(get_db)):
    return delete_gra_item(id_gry, db)