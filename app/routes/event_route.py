from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.event.create_event_schema import CreateEventSchema
from schemas.event.event_schema import EventSchema
from schemas.event.event_status_schema import EventStatusSchema
from schemas.event.event_sign_up_schema import EventSignUpSchema
from services.event_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/event")

@router.get("/")
async def get_events(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{event_id}", response_model=EventSchema)
async def get_event(event_id: int, db: Session = Depends(get_db)):
    return get_by_id(event_id, db)

@router.post("/")
async def create_event(event: CreateEventSchema, db: Session = Depends(get_db)):
    return create(event, db)

@router.post("/{event_id}/sign_up", response_model=EventSignUpResponseSchema)
async def sign_up_for_event(event_id: int, event: EventSignUpSchema, db: Session = Depends(get_db)):
    return sign_up(event_id, event, db)

@router.post("/{event_id}/join_event")
async def join_event(event_id: int, event_join: EventJoinSchema, db: Session = Depends(get_db)):
    return join(event_id, event_join, db)

@router.put("/{event_id}", response_model=EventSchema)
async def edit_event(event_id: int, event: CreateEventSchema, db: Session = Depends(get_db)):
    return edit(event_id, event, db)

@router.delete("/{event_id}", response_model=EventSchema)
async def delete_event(event_id: int, db: Session = Depends(get_db)):
    return delete(event_id, db)

@router.post("/{event_id}/launch")
async def launch_event(event_id: int, db: Session = Depends(get_db)):
    return launch(event_id, db)

@router.post("/{event_id}/end")
async def end_event(event_id: int, db: Session = Depends(get_db)):
    return end(event_id, db)

@router.get("/{event_id}/status", response_model=EventStatusSchema)
async def get_event_status(event_id: int, db: Session = Depends(get_db)):
    return get_status(event_id, db)

@router.get("/get-events-by-uid/{user_id}", response_model=list[EventSchema])
async def get_events_by_user_id_route(user_id: int, db: Session = Depends(get_db)):
    return get_events_by_user_id(user_id, db)

# @router.post("/question")
# async def send_question(question: EventQuestionSchema, db: Session = Depends(get_db)):
#     return add_event_question(question, db)

# @router.get("/{event_id}/questions")
# async def get_questions(event_id: int, db: Session = Depends(get_db)):
#     return get_event_questions(event_id, db)

@router.get("/{event_id}/users")
async def get_event_users(event_id: int, db: Session = Depends(get_db)):
    return get_players(event_id, db)