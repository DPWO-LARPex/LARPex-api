from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime,Float,Text

from models.base import Base

class GameModel(Base):
    __tablename__ = "game"
    
    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer)
    name = Column(Text)
    description = Column(Text)
    max_players_count = Column(Integer)
    min_players_count = Column(Integer)
    state = Column(Boolean)


