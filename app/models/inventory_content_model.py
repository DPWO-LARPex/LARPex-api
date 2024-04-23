
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class InventoryContentModel(Base):
    __tablename__ = "ZawartoscEkwipunku"

    inventory_id = Column(Integer, ForeignKey("Ekwipunek.id_ekwipunku"), primary_key=True, name="id_ekwipunku")
    item_id = Column(Integer, ForeignKey("Przedmiot.id_przedmiotu"), primary_key=True, name="id_przedmiotu")

    #join table between InventoryModel and ItemModel
    inventory = relationship("InventoryModel", back_populates="items")
    item = relationship("ItemModel", back_populates="inventories")