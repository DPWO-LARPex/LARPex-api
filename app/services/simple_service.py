from sqlalchemy.orm import Session
from models.simple_item_model import SimpleItemModel
from schemas.simple_item.simple_item_post_schema import SimpleItemPostSchema


def get_simple_item_by_id(simple_item_id: int, db: Session):
    return db.query(SimpleItemModel).filter(SimpleItemModel.id == simple_item_id).first()

def add_simple_item(simple_item: SimpleItemPostSchema, db: Session):
    print(simple_item.text)
    db_simple_item = SimpleItemModel(
        text=simple_item.text,
        count=simple_item.count)
    db.add(db_simple_item)
    db.commit()
    db.refresh(db_simple_item)
    return db_simple_item

def get_all_simple_items(db: Session):
    return db.query(SimpleItemModel).all()
