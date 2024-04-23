from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class RaceModel(Base):
    __tablename__ = "Rasa"

    race_id = Column(Integer, primary_key=True, index=True, name="id_rasy")
    name = Column(Text, name="nazwa")
    description = Column(Text, name="opis")
    bonuses = Column(Text, name="bonusy")

    characters = relationship("CharacterModel", back_populates="race")

