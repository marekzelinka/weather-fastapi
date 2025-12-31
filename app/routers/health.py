import sys

from fastapi import APIRouter

router = APIRouter(prefix="/health")


@router.get("/")
async def read_health():
    return {
        "status": "OK",
        "detail": "Weather API with FastAPI and OpenWeather!",
        "python_version": sys.version,
    }
