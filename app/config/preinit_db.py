from models.payment_gateway.payment_method_model import PaymentMethodModel
from sqlalchemy.orm import Session

def __init_payment_methods(db: Session):
    payment_gateways = ["PayPal", "Przelewy24", "PayU"]   # Payment gateways data

    for method in payment_gateways:
        # Check if the payment method already exists in the database
        existing_method = db.query(PaymentMethodModel).filter_by(payment_name=method).first()
        if existing_method is None:
            # If it doesn't exist, add it to the database
            new_method = PaymentMethodModel(payment_name=method)
            db.add(new_method)
            db.commit()


def init_db_data(db: Session):
    __init_payment_methods(db)