from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routes import simple_route, game_route
from dotenv import load_dotenv
from config.exceptions import NotFoundExceptionModel

app = FastAPI()

"""ROUTES"""
app.include_router(
    simple_route.router,
    responses={404: {"model": NotFoundExceptionModel}}
    )

app.include_router(
    game_route.router)

#Add here routes

"""OPEN API DOCS"""
openapi_schema = get_openapi(
       title="Larpex API",
       version="1.0",
       description="This is a very simple API for Larpex.",
       routes=app.routes,
   )
app.openapi_schema = openapi_schema