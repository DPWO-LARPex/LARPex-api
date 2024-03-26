from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class Map(Base):
    __tablename__ = "Mapy"
    
    map_id = Column(Integer, primary_key=True, index=True, name="id_mapy")
    game_id = Column(Integer, ForeignKey("Gry.id_gry"), name="id_gry")
    game = relationship("Game", back_populates="maps")
