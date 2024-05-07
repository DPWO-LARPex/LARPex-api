from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from models.base import Base

class GameplayMilestone(Base):
    __tablename__ = "RozgrywkaKamien"

    id = Column(Integer, primary_key=True, index=True, name="id")
    milestone_id = Column(Integer, ForeignKey("KamienMilowy.id_kamienia"), name="id_kamienia")
    gameplay_id = Column(Integer, ForeignKey("Rozgrywka.id_rozgrywki"), name="id_rozgrywki")
    is_reached = Column(Boolean, name="czy_osiagniety")

    milestone = relationship("Milestone", back_populates="gameplay_milestones")
    gameplay = relationship("Gameplay", back_populates="milestones")
