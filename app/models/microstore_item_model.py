
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime,Float,Text
from sqlalchemy.orm import relationship

from models.base import Base

class MicrostoreItemModel(Base):
    #Not existed in DB
    __tablename__ = "MicrostoreItem"

    id = Column(Integer, primary_key=True, index=True, name="id_przedmiotu")
    name = Column(String, name="nazwa")
    description = Column(Text, name="opis")
    price = Column(Float, name="cena")

#    payments = relationship("PaymentModel", secondary="Mikroplatnosc", back_populates="microstore_item")


