# MODELS

Here you can find all the models of the application.
Model is a class that represents a table in the database. It is used to interact with the database. It is ORM (Object Relational Mapping) that maps the object to the database table.

### Creating rules:
1. Each model should be in a separate file.
2. Each model should inherit from the `Base` class.
3. Each model should have a `__tablename__` attribute that specifies the name of the table in the database.
4. Each model should be named like: `ModelName` + `Model` (e.g. `UserModel`).
5. Files should be named in lowercase and separated by underscores (e.g. `user_model.py`).
6. Each model should have a primary key like `id` that is an `Integer` type.
7. Each collumn in model should have a type specified (e.g. `String`, `Integer`, `Boolean` etc.).

### Example:
```python
from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime,Float,Text

from models.base import Base

class SimpleItemModel(Base):
    __tablename__ = "simple_item"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    count = Column(Integer)

```