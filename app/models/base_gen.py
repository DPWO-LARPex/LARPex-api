"""Base generator for SQLAlchemy ORM"""
# ADD HERE YOUR MODELS
from models.base import Base
from models.user import User
from models.game import Game
from models.map import Map
from models.payment_gateway.payment_method_model import PaymentMethodModel
from models.payment_model import PaymentModel
from models.event_status_model import EventStatusModel
from models.place_model import PlaceModel
from models.event_model import EventModel

#iterate 2
from models.player_model import PlayerModel
from models.character_model import CharacterModel
from models.inventory_content_model import InventoryContentModel
from models.inventory_model import InventoryModel
from models.item_model import ItemModel
from models.microstore_item_model import MicrostoreItemModel
from models.class_model import ClassModel
from models.race_model import RaceModel
from models.gameplay_model import Gameplay
from models.gameplay_milestone import GameplayMilestone
from models.milestone import Milestone