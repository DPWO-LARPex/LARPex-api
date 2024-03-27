from models.payment_gateway.payment_method_model import PaymentMethodModel
from sqlalchemy.orm import Session
from models.user import User

def __init_payment_methods(db: Session):
    payment_gateways = ["P", "A", "U"]   # Payment gateways data

    for method in payment_gateways:
        # Check if the payment method already exists in the database
        existing_method = db.query(PaymentMethodModel).filter_by(payment_name=method).first()
        if existing_method is None:
            # If it doesn't exist, add it to the database
            new_method = PaymentMethodModel(payment_name=method)
            db.add(new_method)
            db.commit()

def __init_users(db: Session):
    
    users_data = [
        {
            "name": "Jan",
            "surname": "Kowalski"
        },
        {
            "name": "Anna",
            "surname": "Nowak"
        },
        {
            "name": "Piotr",
            "surname": "Kowalczyk"
        }
    ]

    for user in users_data:
        existing_user = db.query(User).filter_by(firstname=user["name"], lastname=user["surname"]).first()
        if existing_user is None:
            new_user = User(firstname=user["name"], lastname=user["surname"])
            db.add(new_user)
            db.commit()


def init_db_data(db: Session):
    __init_payment_methods(db)
    __init_users(db)