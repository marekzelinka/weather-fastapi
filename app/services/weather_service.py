import httpx


class WeatherService:
    def __init__(self, client: httpx.Client, api_key: str) -> None:
        self.client: httpx.Client = client
        self.api_key: str = api_key

    def get_current_weather(self, city: str) -> dict:
        response = self.client.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "units": "metric", "appid": self.api_key},
        )
        response.raise_for_status()
        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
            "powered_by": "uv",
        }
