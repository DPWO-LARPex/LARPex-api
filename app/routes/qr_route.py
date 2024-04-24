from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.qr.qr_post_schema import QrPostSchema
from schemas.qr.qr_get_schema import QrGetSchema
from services.qr_service import *
from config.exceptions import NotFoundExceptionModel

router = APIRouter(prefix="/qr")

@router.get("/{qr_id}", response_model=QrGetSchema)
async def process_qr(qr_id: int, db: Session = Depends(get_db)):
    return processQRCode(qr_id, db)

