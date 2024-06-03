from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.character.character_schema import CharactersSchema
from schemas.character.class_schema import ClassSchema
from schemas.character.race_schema import RaceSchema
from services.character_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/characters")

@router.get("/{event_id}")
async def get_available_event_characters(event_id: int, db: Session = Depends(get_db)):
    return get_available_characters_for_event(event_id, db)

@router.get("/", response_model=list[CharactersSchema])
async def get_available_characters(db: Session = Depends(get_db)):
    print("Characters: : : :: : :")
    return get_all_characters(db)