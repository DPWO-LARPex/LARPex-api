
from fastapi import APIRouter, Depends
from services.gameplay_service import get_gameplay_status_by_game_id
from config.database import get_db
from config.exceptions import NotFoundExceptionModel
from services.inventory_service import get_character_inventory_by_user_id

router = APIRouter(prefix="/gameplay")

@router.get("/character-inventory-by-uid/{user_id}")
async def get_character_inventory_by_user_id_route(user_id: int, db = Depends(get_db)):
    return get_character_inventory_by_user_id(db, user_id)

@router.get("/status-by-game-id/{game_id}")
async def get_gameplay_status_by_game_id_route(game_id: int, db = Depends(get_db)):
    return get_gameplay_status_by_game_id(game_id, db)
