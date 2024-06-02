from sqlalchemy.orm import Session
from models.event_model import EventModel
from models.event_status_model import EventStatusModel
from schemas.event.create_event_schema import CreateEventSchema
from models.user import User
from models.place_model import PlaceModel
from models.question_model import QuestionModel
from schemas.event.event_schema import EventSchema
from schemas.event.join_event_schema import JoinEventSchema
from schemas.event.event_question_schema import EventQuestionSchema
from config.exceptions import NotFoundException, ObjectAlreadyExistsException


def get_by_id(event_id: int, db: Session):
    db_Event: EventModel = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException()
    return db_Event


def create(event: CreateEventSchema, db: Session):

    #TODO: dodac walidacje id_user, id_place, id_status
    db_status = db.query(EventStatusModel).filter(EventStatusModel.id == event.id_status).first()
    if (db_status is None):
        raise NotFoundException(detail="Nie istnieje status o podanym id")
    
    db_user = db.query(User).filter(User.user_id == event.id_user).first()
    if (db_user is None):
        raise NotFoundException(detail="Nie istnieje user o podanym id")
    
    db_place = db.query(PlaceModel).filter(PlaceModel.id == event.id_place).first()
    if (db_place is None):
        raise NotFoundException(detail="Nie istnieje miejsce o podanym id")

    db_Event = EventModel(
        icon=event.icon,
        tech_desc=event.tech_desc,
        client_description=event.client_description,
        players_count=event.players_count,
        date=event.date,
        price_org=event.price_org,
        price_buy_in=event.price_buy_in,
        id_status=event.id_status,
        id_user=event.id_user,
        id_place=event.id_place
        )
    db.add(db_Event)
    db.commit()
    db.refresh(db_Event)
    return db_Event


def get_all(db: Session):
    return db.query(EventModel).all()


def edit(event_id: int, event: CreateEventSchema, db: Session):
    db_Event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException()
    
    #TODO: dodac walidacje id_user, id_place, id_status

    db_Event.icon = event.icon,
    db_Event.tech_desc = event.tech_desc,
    db_Event.client_description = event.client_description,
    db_Event.players_count = event.players_count,
    db_Event.date = event.date,
    db_Event.price_org = event.price_org,
    db_Event.price_buy_in = event.price_buy_in,
    db_Event.id_status = event.id_status,
    db_Event.id_user = event.id_user,
    db_Event.id_place = event.id_place

    db.commit()
    db.refresh(db_Event)
    return db_Event


def delete(event_id: int, db: Session):
    db_Event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException()
    db.delete(db_Event)
    db.commit()
    return db_Event

def sign_up(event_id: int, join_event: JoinEventSchema, db:Session):
    db_Event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException(detail="Event not found")
    
    db_User = db.query(User).filter(User.user_id == join_event.user_id).first()
    if (db_User is None):
        raise NotFoundException(detail="User not found")
    
    #TODO: dokonczyc walidacje id_character, id_payment

    
    # db_User = db.query(User).filter(User.email == join_event.email).first()
    # if (db_Event is None):
    #     db_User = User(
    #         firstname=join_event.firstname,
    #         lastname=join_event.lastname,
    #         email=join_event.email
    #     )

    #     db.add(db_User)
    #     db.commit()
    #     db.refresh(db_User)

    # if (db_Event not in db_User.events):
    #     db_User.events.append(db_Event)
    #     db.commit()

    return

def end(event_id: int, db:Session):
    db_Event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException()
    db_Event.id_status=3
    db.commit()

    return

def launch(event_id: int, db:Session):
    db_Event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException()
    
    db_Event.id_status=1
    db.commit()

    return

def get_status(event_id: int, db:Session):
    db_Event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException()
    
    return db.query(EventStatusModel).filter(EventStatusModel.id == db_Event.id_status).first()

# def add_event_question(question: EventQuestionSchema, db: Session):
#     db_Event = db.query(EventModel).filter(EventModel.id == question.event_id).first()
#     if (db_Event is None):
#         raise NotFoundException(detail="Wydarzenie o podanym ID nie istnieje")
    
#     db_User = db.query(User).filter(User.user_id == question.user_id).first()
#     if (db_User is None):
#         raise NotFoundException(detail="Osoba o podanym ID nie istnieje")
    
#     db_Question = QuestionModel(
#         event_id = question.event_id,
#         user_id = question.user_id,
#         content = question.content
#         )
#     db.add(db_Question)
#     db.commit()
#     db.refresh(db_Question)
#     return db_Question

# def get_event_questions(event_id: int, db: Session):
#     return db.query(QuestionModel).filter(QuestionModel.event_id == event_id).all()

def get_users(event_id: int, db: Session):
    db_Event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException()

    return db_Event.users