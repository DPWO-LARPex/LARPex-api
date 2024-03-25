from sqlalchemy.orm import Session
from models.payment_model import PaymentModel
from schemas.payment.payment_post_schema import PaymentPostSchema
from config.exceptions import NotFoundException
from services.payment_gateway.payment_gateway_service import get_payment_method_by_id
from datetime import datetime

def get_all_payments(db: Session) -> list[PaymentModel]:
    return db.query(PaymentModel).all()

def get_payment_by_id(payment_id: int, db: Session) -> PaymentModel:
    payment: PaymentModel = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
    if(payment is None):
        raise NotFoundException(detail="Payment not found")
    return payment

def add_payment(payment: PaymentPostSchema, db: Session):

    try:
        get_payment_method_by_id(payment.payment_method_id, db)
    except NotFoundException:
        raise NotFoundException(detail="Payment method not found")
    
    # TODO: check if person exists
    # TODO: check if event exists

    db_payment = PaymentModel(
        date = payment.date,
        amount = payment.amount,
        payment_method_id = payment.payment_method_id,
        person_id = payment.person_id,
        event_id = payment.event_id
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def edit_payment(payment_id: int, payment: PaymentPostSchema, db: Session):
    db_payment = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
    if(db_payment is None):
        raise NotFoundException(detail="Payment not found")
    
    try:
        get_payment_method_by_id(payment.payment_method_id, db)
    except NotFoundException:
        raise NotFoundException(detail="Payment method not found")
    
    #TODO: check if person exists
    #TODO: check if event exists
    
    db_payment.date = payment.date
    db_payment.amount = payment.amount
    db_payment.payment_method_id = payment.payment_method_id
    db_payment.person_id = payment.person_id
    db_payment.event_id = payment.event_id
    db.commit()
    db.refresh(db_payment)
    return db_payment
