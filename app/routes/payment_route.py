from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.payment.payment_get_schema import PaymentGetSchema
from schemas.payment.payment_post_schema import PaymentPostSchema
from services.payment_service import *

router = APIRouter(prefix="/payments")

@router.get("/", response_model=list[PaymentGetSchema])
async def get_payments_route(db: Session = Depends(get_db)):
    return get_all_payments(db)

@router.get("/{payment_id}", response_model=PaymentGetSchema)
async def get_payment_by_id_route(payment_id: int, db: Session = Depends(get_db)):
    return get_payment_by_id(payment_id, db)

@router.put("/{payment_id}", response_model=PaymentGetSchema)
async def edit_payment_route(payment_id: int, payment: PaymentPostSchema, db: Session = Depends(get_db)):
    return edit_payment(payment_id, payment, db)