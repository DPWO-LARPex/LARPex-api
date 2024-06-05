from sqlalchemy import Boolean, Column, Integer, String, Date, Float, Text, ForeignKey, LargeBinary, Table
from sqlalchemy.orm import relationship
from models.player_model import PlayerModel
from models.base import Base
from models.user import User


class EventsPlayersModel(Base):
    __tablename__ = "UczestnicyWydarzenia"

    player_id = Column(Integer, ForeignKey("Gracz.id_gracza"), primary_key=True, name="id_gracza")
    event_id = Column(Integer, ForeignKey("Wydarzenie.id_wydarzenia"), primary_key=True, name="id_wydarzenia")
    is_joined = Column(Boolean, name="czy_dolaczyl")

    event = relationship("EventModel", back_populates="players_association")
    player = relationship("PlayerModel", back_populates="events_association")
