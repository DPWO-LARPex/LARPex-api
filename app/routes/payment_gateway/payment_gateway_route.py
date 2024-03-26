from fastapi import APIRouter, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from schemas.payment_gateway.payment_method_get_schema import PaymentMethodGetSchema
from services.payment_gateway.payment_gateway_service import get_all_payment_methods, get_payment_method_by_id
from services.payment_service import add_payment
from schemas.payment.payment_get_schema import PaymentGetSchema
from schemas.payment.payment_post_schema import PaymentPostSchema

router = APIRouter(prefix="/payment-gateway")

@router.get("/", response_model=list[PaymentMethodGetSchema])
async def get_payment_methods_route(db: Session = Depends(get_db)):
    return get_all_payment_methods(db)


@router.get("/{payment_method_id}", response_model=PaymentMethodGetSchema)
async def get_payment_method_by_id_route(payment_method_id: int, db: Session = Depends(get_db)):
    return get_payment_method_by_id(payment_method_id, db)

@router.post("/", response_model=PaymentGetSchema)
async def process_payment_route(payment_post: PaymentPostSchema, db: Session = Depends(get_db)):
    return add_payment(payment_post, db)
