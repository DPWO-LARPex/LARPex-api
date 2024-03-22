# ROUTES
This directory contains all the routes for the application. Each route is a separate file that contains the logic for the API endpoint.

### Creating rules:
1. Each route should be in a separate file.
2. Each route must be named like: `RouteName` + `Route` (e.g. `UserRoute`).
3. Each route must use APIRouter.
4. Each route must use addnotation `@router.get`, `@router.post`, `@router.put`, `@router.delete` etc.
5. In route addnotation you should specify the path of the endpoint (e.g. `@router.get("/users")`).
6. In route addnotation you should specific the response model (e.g. `response_model=UserSchema`).
7. Files should be named in lowercase and separated by underscores (e.g. `user_route.py`).
8. You must inject DB session dependency in route method.

### Example:
```python
from fastapi import APIRouter, Depends
from config.database import get_db
from schemas.simple_item.simple_item_post_schema import SimpleItemPostSchema
from schemas.simple_item.simple_item_get_schema import SimpleItemGetSchema
from services.simple_service import *

router = APIRouter(prefix="/simple")

@router.get("/", response_model=list[SimpleItemGetSchema])
def get_simple(db: Session = Depends(get_db)):
    return get_all_simple_items(db)

@router.get("/{simple_item_id}", response_model=SimpleItemGetSchema)
def get_simple_by_id(simple_item_id: int, db: Session = Depends(get_db)):
    return get_simple_item_by_id(simple_item_id, db)

@router.post("/")
def add_simple(simple: SimpleItemPostSchema, db: Session = Depends(get_db)):
    return add_simple_item(simple, db)

@router.put("/{simple_item_id}", response_model=SimpleItemGetSchema)
def edit_simple(simple_item_id: int, simpleItem: SimpleItemPostSchema, db: Session = Depends(get_db)):
    return edit_simple_item(simple_item_id, simpleItem, db)

@router.delete("/{simple_item_id}", response_model=SimpleItemGetSchema)
def delete_simple(simple_item_id: int, db: Session = Depends(get_db)):
    return delete_simple_item(simple_item_id, db)
```