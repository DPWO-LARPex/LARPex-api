# SCHEMAS
This directory contains schemas for the application. Each schema is a separate file that contains the Pydantic model. Schema is a class that represents the structure of the data that is sent to and received from the API. It is used to validate the data that is sent to the API.

### Creating rules:
1. Each schema should be in a separate file.
2. Each schema should inherit from the `BaseModel` class.
3. Each schema should be named like: `SchemaName` + `Schema` (e.g. `UserSchema`).
4. Files should be named in lowercase and separated by underscores (e.g. `user_schema.py`).