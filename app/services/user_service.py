from sqlalchemy.orm import Session
from models.user import User
from schemas.user.user_post_schema import UserPostSchema
from schemas.user.user_get_schema import UserGetSchema
from schemas.bought_item.bought_item_get_schema import BoughtItemGetSchema
from config.exceptions import NotFoundException, ObjectAlreadyExistsException


def get_game_user_by_id(user_id: int, db: Session):
    db_User: User = db.query(User).filter(User.user_id == user_id).first()
    if (db_User is None):
        raise NotFoundException()

    return db_User


def add_user(simple: UserPostSchema, db: Session):

    db_user = User(
        firstname=simple.firstname,
        lastname=simple.lastname
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_game_bought_items_by_user_id(user_id:int, db: Session):
    item_dto = BoughtItemGetSchema()
    item_dto.is_premium = True
    item_dto.virtual_currency = 120
    return item_dto