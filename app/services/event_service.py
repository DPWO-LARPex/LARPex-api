from sqlalchemy.orm import Session
from models.event_model import EventModel
from schemas.event.event_post_schema import EventPostSchema
from schemas.event.event_get_schema import EventGetSchema
from config.exceptions import NotFoundException, ObjectAlreadyExistsException


def get_event_item_by_id(event_id: int, db: Session):
    db_Event: EventModel = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException()
    return db_Event


def add_event_item(event: EventPostSchema, db: Session):

    #TODO: dodac walidacje id_user, id_place, id_status

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


def get_all_events(db: Session):
    return db.query(EventModel).all()


def edit_event_item(event_id: int, event: EventPostSchema, db: Session):
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


def delete_event_item(event_id: int, db: Session):
    db_Event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException()
    db.delete(db_Event)
    db.commit()
    return db_Event