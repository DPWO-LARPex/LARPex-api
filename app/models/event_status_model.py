from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
# from models.event_model import EventModel

class EventStatusModel(Base):
    __tablename__ = "StatusWydarzenia"

    id = Column(Integer, primary_key=True, index=True, name="id_stat_wyd")
    name = Column(Text, name="nazwa_statusu_wyd")
    event = relationship("EventModel", back_populates="status")

