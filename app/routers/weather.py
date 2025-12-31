from typing import Annotated

import httpx
from fastapi import APIRouter, Depends

from app.core.config import config
from app.services.weather_service import WeatherService

router = APIRouter(prefix="/weather")


def get_weather_service():
    client = httpx.Client()
    yield WeatherService(client, api_key=config.openweather_api_key)


@router.get("/{city}/")
async def read_current_weather(
    city: str, service: Annotated[WeatherService, Depends(get_weather_service)]
):
    return service.get_current_weather(city)
