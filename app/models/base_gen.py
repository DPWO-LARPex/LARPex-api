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