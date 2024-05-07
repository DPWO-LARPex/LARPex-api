from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from routes import simple_route, game_route, event_route, event_status_route, place_route, payment_route, game_route, user_route, map_route, qr_route
from routes import microstore_route, gameplay_route, player_route
from routes.payment_gateway import payment_gateway_route
from dotenv import load_dotenv
import os
from config.exceptions import NotFoundExceptionModel

load_dotenv()
app = FastAPI()

"""ROUTES"""

PREFIX = "/api"

ORIGIN_WHITELIST = os.getenv("CORS_ORIGIN_WHITELIST")

origins = [
    "http://localhost",
    "http://localhost:5173",
]

if ORIGIN_WHITELIST:
    origin = ORIGIN_WHITELIST.split(",")
    origins.extend(origin)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

app.include_router(
    microstore_route.router,
    prefix=PREFIX,
    tags=["Microstore"],
)

app.include_router(
    gameplay_route.router,
    prefix=PREFIX,
    tags=["Gameplay"],
)

app.include_router(
    player_route.router,
    prefix=PREFIX,
    tags=["Players"],
    responses={404: {"model": NotFoundExceptionModel}}
)

app.include_router(
    qr_route.router,
    prefix=PREFIX,
    tags=["qr"],
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
