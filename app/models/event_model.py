from sqlalchemy import Boolean, Column, Integer, String, Date, Float, Text, ForeignKey, Bytes
from sqlalchemy.orm import relationship
from models.base import Base
from models.event_status_model import EventStatusModel
from models.place_model import PlaceModel
from models.user import User

class EventModel(Base):
    __tablename__ = "wydarzenie"

    id = Column(Integer, primary_key=True, index=True, name="id_wydarzenia")
    icon = Column(Bytes, nazwa="ikona")
    tech_desc = Column(Text, name="opis_techniczny")
    client_description = Column(Text, name="opis_klient")
    players_count = Column(Integer, name="liczba_graczy")
    date = Column(Date, name="data")
    price_org = Column(Float, name="cena_org")
    price_buy_in = Column(Float, name="cena_udzial")
    id_status = Column(Integer, ForeignKey("statuswydarzenia.id_stat_wyd"), name="status")
    id_user = Column(Integer, ForeignKey("Osoby.id_osoby"), name="id_osoby")
    id_place = Column(Integer, ForeignKey("placowka.id_placowki"), name="id_placowki")
    status = relationship("EventStatusModel", back_populates="event")
    place = relationship("PlaceModel", back_populates="event")
    user = relationship("User", back_populates="games")
