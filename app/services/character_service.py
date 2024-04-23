from sqlalchemy.orm import Session
from models.game import Game
from config.exceptions import NotFoundException, ObjectAlreadyExistsException


def get_character_by_player_id(player_id: int, db: Session):
    db_Game: Game = db.query(Game).filter(Game.player_id == player_id).first()
    if(db_Game is None):
        raise NotFoundException()
    
    return db_Game
