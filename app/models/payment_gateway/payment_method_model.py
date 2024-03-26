from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime,Float,Text

from models.base import Base

class PaymentMethodModel(Base):
    __tablename__ = "MetodaPlatnosci"

    id = Column(Integer, primary_key=True, index=True, name="id_met_plat")
    payment_name = Column(Text, name="nazwa_platnosci")