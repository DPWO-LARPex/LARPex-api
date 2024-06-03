
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime,Float, Table,Text
from sqlalchemy.orm import relationship

from models.base import Base

class PaymentModel(Base):
    __tablename__ = "Platnosc"
    
    id = Column(Integer, primary_key=True, index=True, name="id_platnosci")
    date = Column(Date, name="data")
    amount = Column(Integer, name="kwota")
    payment_method_id = Column(Integer, ForeignKey('MetodaPlatnosci.id__met_plat'), name="metoda_platnosci")
    user_id = Column(Integer, ForeignKey('Osoba.id_osoby'), name="id_osoby")
    
    # Many to many relationships
    events = relationship("EventModel", secondary="OplataZaWydarzenie", back_populates="payments")
    games = relationship("Game", secondary="OplataZaGre", back_populates="payments")
    items = relationship("ItemModel", secondary="Mikroplatnosc", back_populates="payments")

    user = relationship("User", back_populates="payments")

# many to many PaymentForEvent

payment_for_event_association = Table('OplataZaWydarzenie', Base.metadata,
    Column('id_platnosci', Integer, ForeignKey('Platnosc.id_platnosci')),
    Column('id_wydarzenia', Integer, ForeignKey('Wydarzenie.id_wydarzenia'))
)

# many to many PaymentForGame

payment_for_game_association = Table('OplataZaGre', Base.metadata,
    Column('id_platnosci', Integer, ForeignKey('Platnosc.id_platnosci')),
    Column('id_gry', Integer, ForeignKey('Gra.id_gry'))
)

#many to many microstore_item_payment

microstore_item_payment_association = Table('Mikroplatnosc', Base.metadata,
    Column('id_platnosci', Integer, ForeignKey('Platnosc.id_platnosci')),
    Column('id_przedmiotu', Integer, ForeignKey('Przedmiot.id_przedmiotu'))
)