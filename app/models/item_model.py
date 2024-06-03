
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class ItemModel(Base):
    __tablename__ = "Przedmiot"

    item_id = Column(Integer, primary_key=True, index=True, name="id_przedmiotu")
    name = Column(Text, name="nazwa")
    description = Column(Text, name="opis")

    inventories = relationship("InventoryContentModel", back_populates="item")
    payments = relationship("PaymentModel", secondary="Mikroplatnosc", back_populates="items")