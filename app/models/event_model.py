from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from event_status_model import EventStatusModel
from place_model import PlaceModel

class EventModel(Base):
    __tablename__ = "wydarzenie"

    id = Column(Integer, primary_key=True, index=True, name="id_wydarzenia")
    icon = Column(bytes, nazwa="ikona")
    tech_desc = Column(Text, name="opis_techniczny")
    client_description = Column(Text, name="opis_klient")
    players_count = Column(Integer, name="liczba_graczy")
    date = Column(DateTime, name="data")
    price_org = Column(Float, name="cena_org")
    price_buy_in = Column(Float, name="cena_udzial")
    id_status = Column(Integer, ForeignKey("statuswydarzenia.id_stat_wyd"), name="status")
    id_osoby = Column(Integer, ForeignKey("osoba.id_osoby"))
    id_place = Column(Integer, ForeignKey("place.id_placowki"), name="id_placowki")
    status = relationship("EventStatusModel", back_populates="event")
    place = relationship("PlaceModel", back_populates="event")
    #osoby = relationship("OsobaModel", back_populates="wydarzenie") tu potrzeba odniesienia do osob
