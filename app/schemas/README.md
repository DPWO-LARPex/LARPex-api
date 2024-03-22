# SCHEMAS
This directory contains schemas for the application. Each schema is a separate file that contains the Pydantic model. Schema is a class that represents the structure of the data that is sent to and received from the API. It is used to validate the data that is sent to the API.

### Creating rules:
1. Each schema should be in a separate file.
2. Each schema should inherit from the `BaseModel` class.
3. Each schema should be named like: `SchemaName` + `Schema` (e.g. `UserSchema`).
4. Files should be named in lowercase and separated by underscores (e.g. `user_schema.py`).
5. If data from POST, PUT, DELETE and GET is different, there should be two separate schemas for each method. Like: `UserPostSchema` and `UserGetSchema`. Avoid duplicating the code.
6. Schema validation is automatically done by Pydantic. If the data is not valid, Pydantic will throw an exception with the appropriate message. But it could be also done manually.

### Example:
- Get schema
```python
from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class SimpleItemGetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    text: str
    count: int

```

- Post schema
```python
from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, StringConstraints

class SimpleItemPostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    text: str
    count: int
```
