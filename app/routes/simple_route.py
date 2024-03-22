from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.simple_item.simple_item_post_schema import SimpleItemPostSchema
from schemas.simple_item.simple_item_get_schema import SimpleItemGetSchema
from services.simple_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/simple")

@router.get("/", response_model=list[SimpleItemGetSchema])
async def get_simple(db: Session = Depends(get_db)):
    return get_all_simple_items(db)

@router.get("/{simple_item_id}", response_model=SimpleItemGetSchema)
async def get_simple_by_id(simple_item_id: int, db: Session = Depends(get_db)):
    return get_simple_item_by_id(simple_item_id, db)

@router.post("/")
async def add_simple(simple: SimpleItemPostSchema, db: Session = Depends(get_db)):
    return add_simple_item(simple, db)

@router.put("/{simple_item_id}", response_model=SimpleItemGetSchema)
async def edit_simple(simple_item_id: int, simpleItem: SimpleItemPostSchema, db: Session = Depends(get_db)):
    return edit_simple_item(simple_item_id, simpleItem, db)

@router.delete("/{simple_item_id}", response_model=SimpleItemGetSchema)
async def delete_simple(simple_item_id: int, db: Session = Depends(get_db)):
    return delete_simple_item(simple_item_id, db)