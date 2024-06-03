from sqlalchemy import Boolean, Column, Integer, String, Date, Float, Text, ForeignKey, LargeBinary, Table
from sqlalchemy.orm import relationship
from models.player_model import PlayerModel
from models.base import Base
from models.user import User
# from models.event_status_model import EventStatusModel
# from models.place_model import PlaceModel

class EventModel(Base):
    __tablename__ = "Wydarzenie"

    id = Column(Integer, primary_key=True, index=True, name="id_wydarzenia")
    icon = Column(Text, name="ikona_url")
    tech_desc = Column(Text, name="opis_techniczny")
    client_description = Column(Text, name="opis_klient")
    players_count = Column(Integer, name="liczba_graczy")
    date = Column(Date, name="data")
    price_org = Column(Float, name="cena_org")
    price_buy_in = Column(Float, name="cena_udział")
    id_status = Column(Integer, ForeignKey("StatusWydarzenia.id_stat_wyd"), name="status")
    id_user = Column(Integer, ForeignKey("Osoba.id_osoby"), name="id_osoby")
    #id_user = Column(Integer, name="id_osoby")
    id_place = Column(Integer, ForeignKey("Placowka.id_placowki"), name="id_placowki")

    gameplays = relationship("Gameplay", back_populates="event")
    status = relationship("EventStatusModel", back_populates="event")
    place = relationship("PlaceModel", back_populates="event")
    user = relationship("User", back_populates="event")
    players = relationship("PlayerModel", secondary="UczestnicyWydarzenia", back_populates="events")
    payments = relationship("PaymentModel", secondary="OplataZaWydarzenie", back_populates="events")

player_event_association = Table('UczestnicyWydarzenia', Base.metadata,
    Column('id_gracza', Integer, ForeignKey('Gracz.id_gracza')),
    Column('id_wydarzenia', Integer, ForeignKey('Wydarzenie.id_wydarzenia'))
)

# # Dodanie relacji wiele do wielu do klas Player i Event
# PlayerModel.events = relationship("EventModel", secondary=player_event_association, back_populates="players")
# EventModel.players = relationship("PlayerModel", secondary=player_event_association, back_populates="events")