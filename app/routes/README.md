# ROUTES
This directory contains all the routes for the application. Each route is a separate file that contains the logic for the API endpoint.

### Creating rules:
1. Each route should be in a separate file.
2. Each route must be named like: `RouteName` + `Route` (e.g. `UserRoute`).
3. Each route must use APIRouter.
4. Files should be named in lowercase and separated by underscores (e.g. `user_route.py`).
5. You must inject DB session dependency in route method.
