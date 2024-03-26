
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime,Float,Text
from sqlalchemy.orm import relationship

from models.base import Base

class PaymentModel(Base):
    __tablename__ = "Platnosc"
    
    id = Column(Integer, primary_key=True, index=True, name="id_platnosci")
    date = Column(Date, name="data")
    amount = Column(Integer, name="kwota")
    payment_method_id = Column(Integer, ForeignKey('MetodaPlatnosci.id_met_plat'), name="metoda_platnosci")
    user_id = Column(Integer, ForeignKey('Osoby.id_osoby'), name="id_osoby")
    #event_id = Column(Integer, ForeignKey('Wydarzenie.id_wydarzenia'), name="id_wydarzenia")
    event_id = Column(Integer, name = "id_wydarzenia")
    
    user = relationship("User", back_populates="payments")