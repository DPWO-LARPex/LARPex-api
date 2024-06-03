from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class Gameplay(Base):
    __tablename__ = "Rozgrywka"

    gameplay_id = Column(Integer, primary_key=True, index=True, name="id_rozgrywki")
    event_id = Column(Integer, ForeignKey("Wydarzenie.id_wydarzenia"), name="id_wydarzenia")
    player_id = Column(Integer, ForeignKey("Gracz.id_gracza"), name="id_gracza")
    points = Column(Integer, name="punkty")
    time = Column(Integer, name="czas")
    players_placement = Column(Text, name="polozenie_graczy")

    event = relationship("EventModel", back_populates="gameplays")
    players = relationship("PlayerModel", back_populates="gameplays")
    milestones = relationship("GameplayMilestone", back_populates="gameplay")