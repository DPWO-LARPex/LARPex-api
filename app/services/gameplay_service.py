from sqlalchemy.orm import Session
from schemas.milestone.milestone_with_status_schema import MilestoneWithStatusSchema
from schemas.gameplay_milestones.gameplay_milestone_get_schema import GameplayMilestoneGetSchema
from models.gameplay_milestone import GameplayMilestone
from models.gameplay_model import Gameplay
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
    
    gameplay = None
    try:
        gameplay = db.query(Gameplay).filter(Gameplay.game_id == game_id).first()
    except NotFoundException:
        raise NotFoundException(detail="Gameplay not found")
    return gameplay

def get_gameplay_by_id(gameplay_id: int, db: Session):
    gameplay = db.query(Gameplay).filter(Gameplay.gameplay_id == gameplay_id).first()
    if(gameplay is None):
        raise NotFoundException()
    
    return gameplay


def get_gameplay_milestones_by_gameplay_id(gameplay_id: int, db: Session):
    gameplay = get_gameplay_by_id(gameplay_id, db)
    gameplay_milestones =  gameplay.milestones
    collected_milestones = []
    for mstone in gameplay_milestones:
        milestone = mstone.milestone
        stone_with_status = MilestoneWithStatusSchema(
            milestone_id = milestone.milestone_id,
            name = milestone.name,
            description = milestone.description,
            is_reached = mstone.is_reached
        )
        collected_milestones.append(stone_with_status)

    res = GameplayMilestoneGetSchema(
        gameplay_id = gameplay.gameplay_id,
        milestones = collected_milestones,
    )

    return res

def get_gameplay_milestones_by_game_id(game_id: int, db: Session):
    # check if game exists
    gameplay = get_gameplay_status_by_game_id(game_id, db)
    print(gameplay.gameplay_id)

    gameplay_milestones =  gameplay.milestones
    collected_milestones = []
    for mstone in gameplay_milestones:
        milestone = mstone.milestone
        stone_with_status = MilestoneWithStatusSchema(
            milestone_id = milestone.milestone_id,
            name = milestone.name,
            description = milestone.description,
            is_reached = mstone.is_reached
        )
        collected_milestones.append(stone_with_status)

    res = GameplayMilestoneGetSchema(
        gameplay_id = gameplay.gameplay_id,
        milestones = collected_milestones,
    )

    return res


