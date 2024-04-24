from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
# from models.event_model import EventModel

class EventQuestionModel(Base):
    __tablename__ = "PytanieDoWydarzenia"

    id = Column(Integer, primary_key=True, index=True, name="id_pyt")
    event_id = Column(Integer, ForeignKey("Wydarzenie.id_wyd"), name="id_wyd")
    question = Column(Text, name="pytanie")

