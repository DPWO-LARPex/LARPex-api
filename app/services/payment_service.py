from sqlalchemy.orm import Session
from models.item_model import ItemModel
from schemas.payment.payment_get_schema import PaymentGetSchema
from models.event_model import EventModel
from models.game import Game
from models.payment_gateway.payment_enum import PaymentTargetEnum
from models.race_model import RaceModel
from models.payment_model import PaymentModel
from models.user import User
from schemas.payment.payment_post_schema import PaymentPostSchema
from config.exceptions import NotFoundException
from services.payment_gateway.payment_gateway_service import get_payment_method_by_id
from datetime import datetime

def __map_payment_to_schema(payment: PaymentModel, db: Session) -> PaymentGetSchema:
    targetEnum = None
    target_id = None

    if payment.events != []:
        target_id = db.query(EventModel).filter(EventModel.id == payment.events[0].id).first().id
        targetEnum = PaymentTargetEnum.event

    if payment.games != []:
        target_id = db.query(Game).filter(Game.game_id == payment.games[0].game_id).first().game_id
        targetEnum = PaymentTargetEnum.game
    
    if payment.items != []:
        target_id = db.query(ItemModel).filter(ItemModel.item_id == payment.items[0].item_id).first().item_id
        targetEnum = PaymentTargetEnum.microitem

    if target_id is None:
        raise NotFoundException(detail="Target not found")
    
    response = PaymentGetSchema(
        id = payment.id,
        date = payment.date,
        amount = payment.amount,
        payment_method_id = payment.payment_method_id,
        user_id = payment.user_id,
        payment_target = targetEnum,
        payment_target_id = target_id
    )

    return response

def get_all_payments(db: Session) -> list[PaymentGetSchema]:
    payments = db.query(PaymentModel).all()
    return [__map_payment_to_schema(payment, db) for payment in payments]

def get_payment_by_id(payment_id: int, db: Session) -> PaymentGetSchema:
    payment: PaymentModel = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
    if(payment is None):
        raise NotFoundException(detail="Payment not found")    

    return __map_payment_to_schema(payment,db)


def __check_user_exists(user_id: int, db: Session):
    user: User = db.query(User).filter(User.user_id == user_id).first()
    if(user is None):
        raise NotFoundException(detail="User not found")

def add_payment(payment: PaymentPostSchema, db: Session):

    try:
        get_payment_method_by_id(payment.payment_method_id, db)
    except NotFoundException:
        raise NotFoundException(detail="Payment method not found")

    try:
        __check_user_exists(payment.user_id, db)
    except NotFoundException:
        raise NotFoundException(detail="User not found")
    
    target = None
    if payment.payment_target == PaymentTargetEnum.event:
        target = db.query(EventModel).filter(EventModel.id == payment.payment_target_id).first()
    elif payment.payment_target == PaymentTargetEnum.game:
        target = db.query(Game).filter(Game.game_id == payment.payment_target_id).first()
    elif payment.payment_target == PaymentTargetEnum.microitem:
        target = db.query(ItemModel).filter(ItemModel.item_id == payment.payment_target_id).first()

    if target is None:
        raise NotFoundException(detail="Target not found")

    db_payment = PaymentModel(
        date = payment.date,
        amount = payment.amount,
        payment_method_id = payment.payment_method_id,
        user_id = payment.user_id,
    )

    if payment.payment_target == PaymentTargetEnum.event:
        db_payment.events.append(target)
    elif payment.payment_target == PaymentTargetEnum.game:
        db_payment.games.append(target)
    elif payment.payment_target == PaymentTargetEnum.microitem:
        db_payment.items.append(target)

    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)

    response = PaymentGetSchema(
        id = db_payment.id,
        date = db_payment.date,
        amount = db_payment.amount,
        payment_method_id = db_payment.payment_method_id,
        user_id = db_payment.user_id,
        payment_target = payment.payment_target,
        payment_target_id = payment.payment_target_id
    )
    return response

# def edit_payment(payment_id: int, payment: PaymentPostSchema, db: Session):
#     db_payment = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
#     if(db_payment is None):
#         raise NotFoundException(detail="Payment not found")
    
#     try:
#         get_payment_method_by_id(payment.payment_method_id, db)
#     except NotFoundException:
#         raise NotFoundException(detail="Payment method not found")
    
#     try:
#         __check_user_exists(payment.user_id, db)
#     except NotFoundException:
#         raise NotFoundException(detail="User not found")
    
#     #TODO: check if event exists
    
#     db_payment.date = payment.date
#     db_payment.amount = payment.amount
#     db_payment.payment_method_id = payment.payment_method_id
#     db_payment.user_id = payment.user_id
#     db_payment.event_id = payment.event_id
#     db.commit()
#     db.refresh(db_payment)
#     return db_payment
