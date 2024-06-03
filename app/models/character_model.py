
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class CharacterModel(Base):
    __tablename__ = "Postac"
    
    character_id = Column(Integer, primary_key=True, index=True, name="id_postaci")
    name = Column(Text, name="imie")
    bio = Column(Text, name="zyciorys")
    inventory_capacity = Column(Integer, name="pojemnosc_ekwipunku")
    #race_id = Column(Integer, ForeignKey("Rasa.id_rasy"), name="id_rasy")
    #class_id = Column(Integer, ForeignKey("Klasa.id_klasy"), name="id_klasy")

    # race = relationship("RaceModel", back_populates="characters")
    # class_ = relationship("ClassModel", back_populates="characters")
    players = relationship("PlayerModel", back_populates="character")