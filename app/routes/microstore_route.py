from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.item.item_get_schema import ItemGetSchema
from services.microstore_service import get_available_items
from schemas.microstore_item.microstore_item_get_schema import MicrostoreItemGetSchema
from config.database import get_db

router = APIRouter(prefix="/microstore")

@router.get("/items", response_model=list[ItemGetSchema])
async def get_available_items_route(db: Session = Depends(get_db)):
    return get_available_items(db)

