# Weather FastAPI

A small weather API that provides a fast, and simple REST API to get current weather info.

## Features

- ⚡ Real-time city weather

## Tech Stack

- [uv](https://github.com/astral-sh/uv) - package and project manager
- [FastAPI](https://fastapi.tiangolo.com/) - modern web framework
- [httpx](https://www.python-httpx.org/) - HTTP client for Python 3
- [uvicorn](https://www.uvicorn.org/) - web server

## Setup

This project uses the modern `pyproject.toml` standard for dependency management and requires the `uv` tool to manage the environment.

1.  **Ensure `uv` is installed** globally on your system. If not, follow the official installation guide for [`uv`](https://docs.astral.sh/uv/).


2.  **Install deps**

    ```sh
    uv sync
    ```

3.  **Setup env variables.**

    ```sh
    cp .env.example .env
    ```

4.  **GET OpenWeather API key.**

    To get the API key, you need to [subscribe](https://openweathermap.org/price) to the **Current Weather Data** API.

5.  **Start app in dev mode**

    ```sh
    uv run uvicorn app.main:app --reload
    ```

## Development

1. Setup your editor to work with [ruff](https://docs.astral.sh/ruff/editors/setup/) and [ty](https://docs.astral.sh/ty/editors/).

2. Install the [justfile extension](https://just.systems/man/en/editor-support.html) for your editor, and use the provided `./justfile` to run commands.

## Usage

### Routes

Start the server and visit [the REST API docs](http://localhost:8000/docs).

## Architecture

### Weather API

We use the [OpenWeather](https://openweathermap.org/) API to get the current weather data for a specified city. Using the [Geocoding API](https://openweathermap.org/current#geocoding) we can

### Key Files

- `./main.py` - Sets up FastAPI web server

## MVP Limitations

- Limited amount of weather data

## Next Steps

- [ ] Add tests
- [x] Refactor env loading
