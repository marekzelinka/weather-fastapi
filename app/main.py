from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, weather

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,  # ty:ignore[invalid-argument-type] Problem with ParamSpec.
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(weather.router)
app.include_router(health.router)
