from typing import List
from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.place.place_post_schema import PlacePostSchema
from schemas.place.place_get_schema import PlaceGetSchema
from services.place_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/place")


@router.post("/")
async def add_place(place: PlacePostSchema, db: Session = Depends(get_db)):
    return add_place_to_event(place, db)

@router.delete("/{place_id}", response_model=PlaceGetSchema)
async def delete_place(place_id: int, db: Session = Depends(get_db)):
    return delete_place_item(place_id, db)

@router.get("/{place_id}", response_model=PlaceGetSchema)
async def get_place(place_id: int, db: Session = Depends(get_db)):
    return get_place_item_by_id(place_id, db)

@router.get("/", response_model=List[PlaceGetSchema])
async def get_places(db: Session = Depends(get_db)):
    return get_all_places(db)