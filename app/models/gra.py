from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class Gra(Base):
    __tablename__ = "gry"
    
    id_gry = Column(Integer, primary_key=True, index=True)
    nazwa = Column(Text)
    opis_gry = Column(Text)
    scenariusz = Column(Text)
    trudnosc = Column(Text)
    status = Column(Text)
    max_liczba_graczy = Column(Integer)
    id_osoby = Column(Integer, ForeignKey("osoby.id_osoby"))
    osoba = relationship("Osoba", back_populates="gry")
    mapy = relationship("Mapa", back_populates="gra")
