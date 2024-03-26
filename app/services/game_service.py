from sqlalchemy.orm import Session
from models.game import Game
from schemas.game.game_post_schema import GamePostSchema
from config.exceptions import NotFoundException, ObjectAlreadyExistsException

def get_game_item_by_id(game_id: int, db: Session):
    db_Game: Game = db.query(Game).filter(Game.game_id == game_id).first()
    if(db_Game is None):
        raise NotFoundException()
    
    return db_Game

def get_games_items_by_user_id(user_id: int, db: Session):
    return db.query(Game).filter(Game.user_id == user_id)

def add_game_item(game: GamePostSchema, db: Session):
    db_Game: Game = db.query(Game).filter(Game.name == game.name).first()
    if(db_Game is not None):
        raise ObjectAlreadyExistsException(detail="Gra o podanej nazwie juz istnieje")

    db_Game = Game(
        description=game.description,
        name=game.name,
        max_players_number=game.max_players_number,
        user_id=game.user_id,
        state=game.state,
        difficulty=game.difficulty,
        scenario=game.scenario)
    db.add(db_Game)
    db.commit()
    db.refresh(db_Game)
    return db_Game

def get_all_game_items(db: Session):
    return db.query(Game).all()

def edit_game_item(game_id: int, game: GamePostSchema, db: Session):
    db_Game = db.query(Game).filter(Game.name == game.name).first()
    if(db_Game is not None and db_Game.game_id != game_id):
        raise ObjectAlreadyExistsException(detail="Game o podanej nazwie juz istnieje")
    db_Game = db.query(Game).filter(Game.game_id == game_id).first()
    if(db_Game is None):
        raise NotFoundException()
    db_Game.description = game.description
    db_Game.name = game.name
    db_Game.max_players_number = game.max_players_number
    db_Game.user_id = game.user_id
    db_Game.state = game.state
    db_Game.difficulty = game.difficulty
    db_Game.scenario = game.scenario
    
    db.commit()
    db.refresh(db_Game)
    return db_Game

def delete_game_item(game_id: int, db: Session):
    db_Game = db.query(Game).filter(Game.game_id == game_id).first()
    if(db_Game is None):
        raise NotFoundException()
    db.delete(db_Game)
    db.commit()
    return db_Game