from sqlalchemy.orm import Session
from services.player_service import get_player_by_user_id
from models.inventory_model import InventoryModel
from models.game import Game
from config.exceptions import NotFoundException, ObjectAlreadyExistsException
from schemas.inventory.inventory_get_schema import InventoryGetSchema


def get_character_inventory_by_user_id(user_id: int, db: Session):
    # find player by user_id
    player = None
    try:
        player = get_player_by_user_id(user_id, db)
    except NotFoundException:
        raise NotFoundException(detail="Player not found")
    
    player_id = player.player_id

    db_Inventory = db.query(InventoryModel).filter(InventoryModel.player_id == player_id).first()
    if(db_Inventory is None):
        raise NotFoundException()

    return db_Inventory