from sqlalchemy.orm import Session
from services.game_service import get_game_item_by_id
from services.player_service import get_player_by_user_id
from models.inventory_model import InventoryModel
from models.game import Game
from config.exceptions import NotFoundException, ObjectAlreadyExistsException



def get_gameplay_status_by_game_id(game_id: int, db: Session):
    #TODO: dodac gameplay
    # check if game exists
    game = None
    try:
        game = get_game_item_by_id(game_id, db)
    except NotFoundException:
        raise NotFoundException(detail="Game not found")
    return "w trakcie"