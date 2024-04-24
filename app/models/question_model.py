from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
# from models.event_model import EventModel

class QuestionModel(Base):
    __tablename__ = "Pytanie"

    question_id = Column(Integer, primary_key=True, index=True, name="id_pytania")
    event_id = Column(Integer, ForeignKey("Wydarzenie.id_wydarzenia"), name="id_wydarzenia")
    user_id = Column(Integer, ForeignKey("Osoba.id_osoby"), name="id_gracza")
    content = Column(Text, name="tresc")