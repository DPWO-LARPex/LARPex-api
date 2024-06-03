from sqlalchemy.orm import Session
from models.character_model import CharacterModel
from config.exceptions import NotFoundException, ObjectAlreadyExistsException

def get_all_characters(db: Session):
    db_Characters = db.query(CharacterModel).all()
    return db_Characters
