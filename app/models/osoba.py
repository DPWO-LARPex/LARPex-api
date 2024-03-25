from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from models.base import Base

class Osoba(Base):
    __tablename__ = "osoby"
    
    id_osoby = Column(Integer, primary_key=True, index=True)
    imie = Column(Text)
    nazwisko = Column(Text)
    gry = relationship("Gra", back_populates="osoba")
