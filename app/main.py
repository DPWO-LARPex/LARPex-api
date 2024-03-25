from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routes import simple_route, game_route, payment_route
from routes.payment_gateway import payment_gateway_route
from dotenv import load_dotenv
from config.exceptions import NotFoundExceptionModel

app = FastAPI()

"""ROUTES"""

app.include_router(
    payment_gateway_route.router,
    prefix="/pay-api",
    tags=["Payment Gateway"],
    responses={404: {"model": NotFoundExceptionModel}}
    )

app.include_router(
    payment_route.router,
    prefix="/api",
    tags=["Payments"],
    responses={404: {"model": NotFoundExceptionModel}}
)

# app.include_router(
#     simple_route.router,
#     prefix="/api",
#     tags=["Simple"],
#     responses={404: {"model": NotFoundExceptionModel}}
#     )

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