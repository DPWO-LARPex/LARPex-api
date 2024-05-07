from sqlalchemy import Column, Integer, Text, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class QrModel(Base):
    __tablename__ = "KodQr"

    qr_id = Column(Integer, primary_key=True, index=True, name="id_kodqr")
    size = Column(Integer, name="rozmiar")
    icon = Column(LargeBinary, name="ikona")
    place_id = Column(Integer, ForeignKey("Placowka.id_placowki"), name="id_placowki")

    place = relationship("PlaceModel", back_populates="qr")

