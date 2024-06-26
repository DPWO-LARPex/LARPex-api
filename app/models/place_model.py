from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
# from models.event_model import EventModel

class PlaceModel(Base):
    __tablename__ = "Placowka"

    id = Column(Integer, primary_key=True, index=True, name="id_placowki")
    number = Column(Integer, name="numer")
    street = Column(Text, name="ulica")
    city = Column(Text, name="miejscowosc")

    event = relationship("EventModel", back_populates="place")
    qr = relationship("QrModel", back_populates="place")