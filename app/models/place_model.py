from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from event_model import EventModel

class PlaceModel(Base):
    __tablename__ = "statuswydarzenia"

    id = Column(Integer, primary_key=True, index=True, name="id_placowki")
    number = Column(Integer, name="numer")
    street = Column(Text, name="ulica")
    city = Column(Text, name="miejscowosc")
    event = relationship("EventModel", back_populates="place")