from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from models.base import Base

class User(Base):
    __tablename__ = "Osoba"
    
    user_id = Column(Integer, primary_key=True, index=True, name="id_osoby")
    firstname = Column(Text, name="imie")
    lastname = Column(Text, name="nazwisko")

    # games = relationship("Game", back_populates="user")
    # payments = relationship("PaymentModel", back_populates="user")