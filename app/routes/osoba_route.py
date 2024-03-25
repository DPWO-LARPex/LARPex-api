from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.gra.gra_get_schema import GraGetSchema
from services.gra_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/osoba")

@router.get("/{id_osoby}/gry", response_model=list[GraGetSchema])
async def get_gry_by_osoba_id(id_osoby: int, db: Session = Depends(get_db)):
    return get_gry_items_by_osoba_id(id_osoby, db)
