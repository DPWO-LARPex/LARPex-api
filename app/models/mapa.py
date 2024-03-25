from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class Mapa(Base):
    __tablename__ = "mapy"
    
    id_mapy = Column(Integer, primary_key=True, index=True)
    id_gry = Column(Integer, ForeignKey("gry.id_gry"))
    gra = relationship("Gra", back_populates="mapy")
