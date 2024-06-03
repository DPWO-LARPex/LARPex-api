
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class ClassModel(Base):
    __tablename__ = "Klasa"

    class_id = Column(Integer, primary_key=True, index=True, name="id_klasy")
    name = Column(Text, name="nazwa")
    description = Column(Text, name="opis")
    bonuses = Column(Text, name="bonusy")

    #characters = relationship("CharacterModel", back_populates="class_")
    