from sqlalchemy.orm import Session
from models.user import User
from schemas.player.player_info_get_schema import PlayerInfoGetSchema
from models.player_model import PlayerModel
from models.game import Game
from config.exceptions import NotFoundException, ObjectAlreadyExistsException

def create_player(player: PlayerModel, db: Session):
    db_Player = db.query(PlayerModel).filter(PlayerModel.user_id == player.user_id).first()
    if(db_Player is not None):
        raise ObjectAlreadyExistsException()
    
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def get_player_by_user_id(user_id: int, db: Session):
    #TODO: to nie ma sensu, player powinien miec swoje ID !
    db_Player: PlayerModel = db.query(PlayerModel).filter(PlayerModel.user_id == user_id).first()
    if(db_Player is None):
        raise NotFoundException()
    
    return db_Player

def get_player_info_by_user_id(user_id: int, db: Session):

    db_User: User = db.query(User).filter(User.user_id == user_id).first()
    if(db_User is None):
        raise NotFoundException()

    db_Player: PlayerModel = db.query(PlayerModel).filter(PlayerModel.user_id == user_id).first()
    if(db_Player is None):
        raise NotFoundException()
    
    player_info = PlayerInfoGetSchema(
        user_id = db_Player.user_id,
        nickname = db_Player.nickname,
        rank = db_Player.rank,
        username = db_User.firstname,
        surname = db_User.lastname,
        character_id = db_Player.character_id
    )



    return player_info
