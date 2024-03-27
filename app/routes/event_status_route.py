from typing import List
from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.event_status.event_status_post_schema import EventStatusPostSchema
from schemas.event_status.event_status_get_schema import EventStatusGetSchema
from services.event_status_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/event_status")


@router.post("/")
async def add_event_status(event_status: EventStatusPostSchema, db: Session = Depends(get_db)):
    return add_event_status_to_event(event_status, db)

@router.delete("/{event_status_id}", response_model=EventStatusGetSchema)
async def delete_event_status(event_status_id: int, db: Session = Depends(get_db)):
    return delete_event_status_item(event_status_id, db)

@router.get("/{event_status_id}", response_model=EventStatusGetSchema)
async def get_event_status(event_status_id: int, db: Session = Depends(get_db)):
    return get_event_status_item_by_id(event_status_id, db)

@router.get("/", response_model=List[EventStatusGetSchema])
async def get_event_statuses(db: Session = Depends(get_db)):
    return get_all_event_statuses(db)