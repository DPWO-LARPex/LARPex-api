from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime,Float,Text

from models.base import Base

class SimpleItemModel(Base):
    __tablename__ = "simple_item"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    count = Column(Integer)

