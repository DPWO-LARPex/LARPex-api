"""Base generator for SQLAlchemy ORM"""
# ADD HERE YOUR MODELS
from models.base import Base
from models.game_model import GameModel
from models.simple_item_model import SimpleItemModel
from models.payment_gateway.payment_method_model import PaymentMethodModel
from models.payment_model import PaymentModel