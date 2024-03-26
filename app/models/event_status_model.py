from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from event_model import EventModel

class EventStatusModel(Base):
    __tablename__ = "statuswydarzenia"

    id = Column(Integer, primary_key=True, index=True, name="id_stat_wyd")
    name = Column(Text, name="nazwa_statusu_wyd")
    event = relationship("EventModel", back_populates="status")

