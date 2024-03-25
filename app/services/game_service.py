from sqlalchemy.orm import Session
from models.game_model import GameModel
from schemas.game.game_post_schema import GamePostSchema
from config.exceptions import NotFoundException

def get_game_item_by_id(game_id: int, db: Session):
    game: GameModel = db.query(GameModel).filter(GameModel.id == game_id).first()
    if(game is None):
        raise NotFoundException()
    return game

def add_game_item(game: GamePostSchema, db: Session):
    db_game = GameModel(
        description=game.description,
        name=game.name,
        min_players_count=game.min_players_count,
        max_players_count=game.max_players_count,
        author_id=game.author_id,
        state=False)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def get_all_game_items(db: Session):
    return db.query(GameModel).all()

def edit_game_item(game_id: int, game: GamePostSchema, db: Session):
    db_game = db.query(GameModel).filter(GameModel.id == game_id).first()
    if(db_game is None):
        raise NotFoundException()
    db_game.description = game.description
    db_game.name = game.name
    db_game.min_players_count = game.min_players_count
    db_game.max_players_count = game.max_players_count
    db_game.author_id = game.author_id
    db_game.state = game.state
    
    db.commit()
    db.refresh(db_game)
    return db_game

def delete_game_item(game_id: int, db: Session):
    db_game = db.query(GameModel).filter(GameModel.id == game_id).first()
    if(db_game is None):
        raise NotFoundException()
    db.delete(db_game)
    db.commit()
    return db_game