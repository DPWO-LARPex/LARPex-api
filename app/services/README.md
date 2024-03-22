# SERVICES

This directory contains all the services that are used in the application. Each service is a class that is responsible for a specific task. The services are used to keep the routes clean and to separate the business logic from the controllers.

### Creating rules:
1. Each service should be in a separate file.
2. Each service should be named like: `ServiceName` + `Service` (e.g. `UserService`).
3. Files should be named in lowercase and separated by underscores (e.g. `user_service.py`).
4. Each service are having `db: Session` as a parameter in the method. This is used to interact with the database.