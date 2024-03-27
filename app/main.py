from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routes import simple_route, game_route, event_route, event_status_route, place_route, payment_route, game_route, user_route, map_route
from routes.payment_gateway import payment_gateway_route
from dotenv import load_dotenv
from config.exceptions import NotFoundExceptionModel

app = FastAPI()

"""ROUTES"""

PREFIX = "/api"

app.include_router(
    payment_gateway_route.router,
    prefix="/pay-api",
    tags=["Payment Gateway"],
    responses={404: {"model": NotFoundExceptionModel}}
    )

app.include_router(
    payment_route.router,
    prefix=PREFIX,
    tags=["Payments"],
    responses={404: {"model": NotFoundExceptionModel}}
)

app.include_router(
    game_route.router,
    prefix=PREFIX,
    tags=["Games"],
    responses={404: {"model": NotFoundExceptionModel}}
)

app.include_router(
    user_route.router,
    prefix=PREFIX,
    tags=["Users"],
    responses={404: {"model": NotFoundExceptionModel}}
)

app.include_router(
    map_route.router,
    prefix=PREFIX,
    tags=["Maps"],
    responses={404: {"model": NotFoundExceptionModel}}
)

# app.include_router(
#     simple_route.router,
#     prefix="/api",
#     tags=["Simple"],
#     responses={404: {"model": NotFoundExceptionModel}}
#     )

app.include_router(
    event_route.router,
    prefix=PREFIX,
    tags=["Events"],
    responses={404: {"model": NotFoundExceptionModel}})

app.include_router(
    event_status_route.router,
    prefix=PREFIX,
    tags=["Event Status"],
    responses={404: {"model": NotFoundExceptionModel}})

app.include_router(
    place_route.router,
    prefix=PREFIX,
    tags=["Places"],
    responses={404: {"model": NotFoundExceptionModel}})


#Add here routes

"""OPEN API DOCS"""
openapi_schema = get_openapi(
       title="Larpex API",
       version="1.0",
       description="This is a very simple API for Larpex.",
       routes=app.routes,
   )
app.openapi_schema = openapi_schema