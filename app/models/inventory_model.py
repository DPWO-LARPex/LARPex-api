
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class InventoryModel(Base):
    __tablename__ = "Ekwipunek"

    inventory_id = Column(Integer, primary_key=True, index=True, name="id_ekwipunku")
    capacity = Column(Integer, name="pojemnosc_ekwipunku")
    player_id = Column(Integer, ForeignKey("Gracz.id_gracza"), name="id_gracza")

    player = relationship("PlayerModel", back_populates="inventory")
    items = relationship("InventoryContentModel", back_populates="inventory")
   
