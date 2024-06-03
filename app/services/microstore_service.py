from sqlalchemy.orm import Session
from models.item_model import ItemModel
from models.payment_model import PaymentModel
from schemas.item.item_get_schema import ItemGetSchema
from models.game import Game
from config.exceptions import NotFoundException, ObjectAlreadyExistsException
from schemas.microstore_item.microstore_item_get_schema import MicrostoreItemGetSchema

def __mocked_getAvailableItems():
    mocked = []
    mocked.append(MicrostoreItemGetSchema(
        id=1,
        name="waluta premium",
        description="description1",
        price=10,
    ))
    mocked.append(MicrostoreItemGetSchema(
        id=2,
        name="waluta premium",
        description="description2",
        price=20,
    ))
    mocked.append(MicrostoreItemGetSchema(
        id=3,
        name="waluta premium",
        description="description3",
        price=30,
    ))
    mocked.append(MicrostoreItemGetSchema(
        id=4,
        name="konto premium",
        description="description4",
        price=40,
    ))
    return mocked

def get_bought_microitems_by_user_id(user_id: int, db: Session) -> list[ItemModel]:

    db_payments = db.query(PaymentModel).filter(PaymentModel.user_id == user_id).all()
    db_items = []
    for payment in db_payments:
        if(payment.items == []):
            continue
        db_items += payment.items

    return db_items

def get_available_items(db: Session):
    #TODO: add microstore items to database
    #mocked = __mocked_getAvailableItems()

    return db.query(ItemModel).all()
