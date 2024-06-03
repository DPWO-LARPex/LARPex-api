from sqlalchemy.orm import Session
from models.event_model import EventModel
from models.user import User
from models.question_model import QuestionModel
from schemas.question.event_question_schema import EventQuestionSchema
from config.exceptions import NotFoundException, ObjectAlreadyExistsException

def add_event_question(question: EventQuestionSchema, db: Session):
    db_Event = db.query(EventModel).filter(EventModel.id == question.event_id).first()
    if (db_Event is None):
        raise NotFoundException(detail="Wydarzenie o podanym ID nie istnieje")
    
    db_User = db.query(User).filter(User.user_id == question.user_id).first()
    if (db_User is None):
        raise NotFoundException(detail="Osoba o podanym ID nie istnieje")
    
    db_Question = QuestionModel(
        event_id = question.event_id,
        user_id = question.user_id,
        content = question.content
        )
    db.add(db_Question)
    db.commit()
    db.refresh(db_Question)
    return db_Question

def get_event_questions(event_id: int, db: Session):
    return db.query(QuestionModel).filter(QuestionModel.event_id == event_id).all()
