
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime,Float,Text

from models.base import Base

class PaymentModel(Base):
    __tablename__ = "Platnosc"
    
    id = Column(Integer, primary_key=True, index=True, name="id_platnosci")
    date = Column(Date, name="data")
    amount = Column(Integer, name="kwota")
    payment_method_id = Column(Integer, ForeignKey('MetodaPlatnosci.id_met_plat'), name="metoda_platnosci")
    #id_osoby = Column(Integer, ForeignKey('Osoba.id_osoby'))
    person_id = Column(Integer, name="id_osoby")
    #id_wydarzenia = Column(Integer, ForeignKey('Wydarzenie.id_wydarzenia'))
    event_id = Column(Integer, name = "id_wydarzenia")