from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.question.event_question_schema import EventQuestionSchema
from services.questions_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/question")

@router.post("/")
async def send_question(question: EventQuestionSchema, db: Session = Depends(get_db)):
    return add_event_question(question, db)

@router.get("/{event_id}")
async def get_questions(event_id: int, db: Session = Depends(get_db)):
    return get_event_questions(event_id, db)
