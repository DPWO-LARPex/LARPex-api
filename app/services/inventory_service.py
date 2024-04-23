from sqlalchemy.orm import Session
from services.player_service import get_player_by_user_id
from models.inventory_model import InventoryModel
from models.game import Game
from config.exceptions import NotFoundException, ObjectAlreadyExistsException
from schemas.inventory.inventory_get_schema import InventoryGetSchema


def get_character_inventory_by_user_id(db: Session, user_id: int):
    # find player by user_id
    player = None
    try:
        player = get_player_by_user_id(user_id, db)
    except NotFoundException:
        raise NotFoundException(detail="Player not found")
    
    character_id = player.character.character_id

    db_Inventory = db.query(InventoryModel).filter(InventoryModel.character_id == character_id).first()
    if(db_Inventory is None):
        raise NotFoundException()

    inventory_dto = InventoryGetSchema(
        character_id=character_id,
        capacity=db_Inventory.capacity,
        inventory_id=db_Inventory.inventory_id,
        items=db_Inventory.items
    )
    
    return db_Inventory