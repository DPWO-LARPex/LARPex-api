from sqlalchemy.orm import Session
from models.event_status_model import EventStatusModel
from models.event_model import EventModel
from schemas.event_status.event_status_post_schema import EventStatusPostSchema
from config.exceptions import NotFoundException, ObjectAlreadyExistsException

def add_event_status_to_event(event_status: EventStatusPostSchema, db: Session):
    db_EventStatus = EventStatusModel(
        name=event_status.name
   )

    db.add(db_EventStatus)
    db.commit()
    db.refresh(db_EventStatus)

    return db_EventStatus


def delete_event_status_item(event_status_id: int, db: Session):
    db_EventStatus = db.query(EventStatusModel).filter(EventStatusModel.id == event_status_id).first()
    if (db_EventStatus is None):
        raise NotFoundException()
    db.delete(db_EventStatus)
    db.commit()

    return db_EventStatus

def get_event_status_item_by_id(event_status_id: int, db: Session):
    db_EventStatus: EventStatusModel = db.query(EventStatusModel).filter(EventStatusModel.id == event_status_id).first()
    if (db_EventStatus is None):
        raise NotFoundException()
    return db_EventStatus

def get_all_event_statuses(db: Session):
    return db.query(EventStatusModel).all()