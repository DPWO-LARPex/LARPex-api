
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class PlayerModel(Base):
    __tablename__ = "Gracz"

    player_id = Column(Integer, primary_key=True, index=True, name="id_gracza")
    
    nickname = Column(Text, name="pseudonim")
    rank = Column(Text, name="ranga")
    user_id = Column(Integer, ForeignKey("Osoba.id_osoby"), name="id_osoby")
    character_id = Column(Integer, ForeignKey("Postac.id_postaci"), name="id_postaci")

    user = relationship("User", back_populates="players")
    character = relationship("CharacterModel", back_populates="players")
    gameplays = relationship("Gameplay", back_populates="players")

