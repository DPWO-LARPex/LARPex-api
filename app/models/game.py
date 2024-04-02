from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class Game(Base):
    __tablename__ = "Gra"
    
    game_id = Column(Integer, primary_key=True, index=True, name="id_gry")
    name = Column(Text, name="nazwa")
    description = Column(Text, name="opis_gry")
    scenario = Column(Text, name="scenariusz")
    difficulty = Column(Text, name="trudnosc")
    state = Column(Text, name="status")
    max_players_number = Column(Integer, name="max_liczba_graczy")
    user_id = Column(Integer, ForeignKey("Osoba.id_osoby"), name="id_osoby")

    # TODO: wywala bledy 
    """Could not determine join condition between parent/child tables on relationship User.games 
    - there are no foreign keys linking these tables.  
    Ensure that referencing columns are associated with a ForeignKey or ForeignKeyConstraint, 
    or specify a 'primaryjoin' expression."""
    user = relationship("User", back_populates="games")
    maps = relationship("Map", back_populates="game")
