from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class Game(Base):
    __tablename__ = "Gry"
    
    game_id = Column(Integer, primary_key=True, index=True, name="id_gry")
    name = Column(Text, name="nazwa")
    description = Column(Text, name="opis_gry")
    scenario = Column(Text, name="scenariusz")
    difficulty = Column(Text, name="trudnosc")
    state = Column(Text, name="status")
    max_players_number = Column(Integer, name="max_liczba_graczy")
    user_id = Column(Integer, ForeignKey("Osoby.id_osoby"), name="id_osoby")
    user = relationship("User", back_populates="games")
    maps = relationship("Map", back_populates="game")
