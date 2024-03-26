from sqlalchemy.orm import Session
from config.exceptions import NotFoundException
from models.payment_gateway.payment_method_model import PaymentMethodModel

def get_all_payment_methods(db: Session) -> list[PaymentMethodModel]:
    return db.query(PaymentMethodModel).all()

def get_payment_method_by_id(payment_method_id: int, db: Session) -> PaymentMethodModel:
    payment_method: PaymentMethodModel = db.query(PaymentMethodModel).filter(PaymentMethodModel.id == payment_method_id).first()
    if(payment_method is None):
        raise NotFoundException()
    return payment_method

def process_payment(payment_method_id: int, db: Session):
    payment_method: PaymentMethodModel = db.query(PaymentMethodModel).filter(PaymentMethodModel.id == payment_method_id).first()
    if(payment_method is None):
        raise NotFoundException()
    
    return payment_method