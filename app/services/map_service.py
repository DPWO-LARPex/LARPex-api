from sqlalchemy.orm import Session
from models.map import Map
from schemas.map.map_post_schema import MapPostSchema
from config.exceptions import NotFoundException, ObjectAlreadyExistsException

def get_maps_by_game_id(game_id: int, db: Session):
    return db.query(Map).filter(Map.game_id == game_id).all()

def add_map_item_to_game(map: MapPostSchema, db: Session):
    db_Map = Map(game_id=map.game_id)
    
    db.add(db_Map)
    db.commit()
    db.refresh(db_Map)
    
    return db_Map

def delete_map_item(map_id: int, db: Session):
    db_Map = db.query(Map).filter(Map.map_id == map_id).first()
    if(db_Map is None):
        raise NotFoundException()
    db.delete(db_Map)
    db.commit()
    
    return db_Map

def get_map_item_by_id(map_id: int, db: Session):
    db_Map: Map = db.query(Map).filter(Map.map_id == map_id).first()
    if(db_Map is None):
        raise NotFoundException()
    
    return db_Map

def get_all_map_items(db: Session):
    return db.query(Map).all()
