from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.event.event_post_schema import EventPostSchema
from schemas.event.event_get_schema import EventGetSchema
from services.event_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/event")

@router.get("/", response_model=list[EventGetSchema])
async def get_all_events_route(db: Session = Depends(get_db)):
    return get_all_events(db)

@router.get("/{event_id}", response_model=EventGetSchema)
async def get_event_by_id(event_id: int, db: Session = Depends(get_db)):
    return get_event_item_by_id(event_id, db)

@router.post("/")
async def add_event(event: EventPostSchema, db: Session = Depends(get_db)):
    return add_event_item(event, db)

@router.put("/{event_id}", response_model=EventGetSchema)
async def edit_event(event_id: int, event: EventPostSchema, db: Session = Depends(get_db)):
    return edit_event_item(event_id, event, db)

@router.delete("/{event_id}", response_model=EventGetSchema)
async def delete_event(event_id: int, db: Session = Depends(get_db)):
    return delete_event_item(event_id, db)