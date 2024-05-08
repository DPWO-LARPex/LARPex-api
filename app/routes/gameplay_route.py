
from fastapi import APIRouter, Depends
from schemas.gameplay.gameplay_game_get_schema import GameplayGameGetSchema
from schemas.gameplay_milestones.gameplay_milestone_get_schema import GameplayMilestoneGetSchema
from schemas.gameplay.gameplay_get_schema import GameplayGetSchema
from services.gameplay_service import get_all_gameplays, get_gameplay_by_id, get_gameplay_milestones_by_game_id, get_gameplay_milestones_by_gameplay_id, get_gameplay_status_by_game_id
from config.database import get_db
from config.exceptions import NotFoundExceptionModel
from services.inventory_service import get_character_inventory_by_user_id

router = APIRouter(prefix="/gameplay")

@router.get("/character-inventory-by-uid/{user_id}")
async def get_character_inventory_by_user_id_route(user_id: int, db = Depends(get_db)):
    return get_character_inventory_by_user_id(db, user_id)

@router.get("/", response_model=list[GameplayGetSchema])
async def get_gameplays_route(db = Depends(get_db)):
    return get_all_gameplays(db)

@router.get("/status-by-game-id/{game_id}", response_model=GameplayGetSchema)
async def get_gameplay_status_by_game_id_route(game_id: int, db = Depends(get_db)):
    return get_gameplay_status_by_game_id(game_id, db)

@router.get("/status/{gameplay_id}", response_model=GameplayGetSchema)
async def get_gameplay_status_by_id_route(gameplay_id: int, db = Depends(get_db)):
    return get_gameplay_by_id(gameplay_id, db)

@router.get("/milestones-by-gameplay-id/{gameplay_id}", response_model=GameplayMilestoneGetSchema)
async def get_gameplay_milestones_by_gameplay_id_route(gameplay_id: int, db = Depends(get_db)):
    return get_gameplay_milestones_by_gameplay_id(gameplay_id, db)

@router.get("/milestones-by-game-id/{game_id}", response_model=GameplayMilestoneGetSchema)
async def get_gameplay_milestones_by_game_id_route(game_id: int, db = Depends(get_db)):
    return get_gameplay_milestones_by_game_id(game_id, db)