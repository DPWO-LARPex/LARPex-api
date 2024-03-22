# MODELS

Here you can find all the models of the application.
Model is a class that represents a table in the database. It is used to interact with the database. It is ORM (Object Relational Mapping) that maps the object to the database table.

### Creating rules:
1. Each model should be in a separate file.
2. Each model should inherit from the `Base` class.
3. Each model should have a `__tablename__` attribute that specifies the name of the table in the database.
4. Each model should be named like: `ModelName` + `Model` (e.g. `UserModel`).
5. Files should be named in lowercase and separated by underscores (e.g. `user_model.py`).
