# SERVICES

This directory contains all the services that are used in the application. Each service is a class that is responsible for a specific task. The services are used to keep the routes clean and to separate the business logic from the controllers.

### Creating rules:
1. Each service should be in a separate file.
2. Classes are not created in the services. Instead, the services are created as functions.
3. Each service should be named like: `ServiceName` + `Service` (e.g. `UserService`).
4. Files should be named in lowercase and separated by underscores (e.g. `user_service.py`).
5. Each service are having `db: Session` as a parameter in the method. This is used to interact with the database.
6. If there is any problem with the service or query, there should be raised an HTTPException with the appropriate status code and message.

### Example:
```python
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.simple_item_model import SimpleItemModel
from schemas.simple_item.simple_item_post_schema import SimpleItemPostSchema


def get_simple_item_by_id(simple_item_id: int, db: Session):
    simple_item: SimpleItemModel = db.query(SimpleItemModel).filter(SimpleItemModel.id == simple_item_id).first()
    if(simple_item is None):
        raise HTTPException(status_code=404, detail="Simple Item not found")
    return simple_item

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

def edit_simple_item(simple_item_id: int, simple_item: SimpleItemPostSchema, db: Session):
    db_simple_item = db.query(SimpleItemModel).filter(SimpleItemModel.id == simple_item_id).first()
    if(db_simple_item is None):
        raise HTTPException(status_code=404, detail="Simple Item not found")
    db_simple_item.text = simple_item.text
    db_simple_item.count = simple_item.count
    db.commit()
    db.refresh(db_simple_item)
    return db_simple_item

def delete_simple_item(simple_item_id: int, db: Session):
    db_simple_item = db.query(SimpleItemModel).filter(SimpleItemModel.id == simple_item_id).first()
    if(db_simple_item is None):
        raise HTTPException(status_code=404, detail="Simple Item not found")
    db.delete(db_simple_item)
    db.commit()
    return db_simple_item
```