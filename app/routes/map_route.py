from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.map.map_post_schema import MapPostSchema
from schemas.map.map_get_schema import MapGetSchema
from services.map_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/maps")

@router.post("/")
async def add_Map(map: MapPostSchema, db: Session = Depends(get_db)):
    return add_map_item_to_game(map, db)

@router.delete("/{map_id}", response_model=MapGetSchema)
async def delete_map(map_id: int, db: Session = Depends(get_db)):
    return delete_map_item(map_id, db)