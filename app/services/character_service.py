from sqlalchemy.orm import Session
from models.character_model import CharacterModel
from models.event_model import EventModel
from config.exceptions import NotFoundException, ObjectAlreadyExistsException

def get_all_characters(db: Session):
    db_Characters = db.query(CharacterModel).all()
    return db_Characters

def get_available_characters_for_event(event_id: int, db: Session):
    db_Characters = db.query(CharacterModel).all()
    db_Event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if (db_Event is None):
        raise NotFoundException(detail="Event not found")

    reserved_ids = {player.character_id for player in db_Event.players}
    result_list = [character for character in db_Characters if character.character_id not in reserved_ids]

    return result_list