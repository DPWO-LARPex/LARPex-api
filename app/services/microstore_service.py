from sqlalchemy.orm import Session
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

def get_available_items(db: Session):
    #TODO: add microstore items to database
    mocked = __mocked_getAvailableItems()
    return mocked
