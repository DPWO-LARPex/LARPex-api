from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from models.base import Base

class Milestone(Base):
    __tablename__ = "KamienMilowy"

    milestone_id = Column(Integer, primary_key=True, index=True, name="id_kamienia")
    name = Column(Text, name="nazwa")
    description = Column(Text, name="tresc")

    gameplay_milestones = relationship("GameplayMilestone", back_populates="milestone")