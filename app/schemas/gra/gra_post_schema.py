from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict

class GraPostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_osoby: int
    nazwa: str
    opis_gry: str
    max_liczba_graczy: int
    status: str
    trudnosc: str
    scenariusz: str
