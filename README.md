# hello_api

A small FastAPI app with three endpoints:

- `GET /` returns the plain text `Online` (a quick health check)
- `GET /hello` returns a casual hello message as JSON
- `GET /goodbye` returns a casual goodbye message as JSON

## Install

Requires Python 3.10+ and [Poetry](https://python-poetry.org/).

```
poetry install
```

## Run

```
poetry run python main.py
```

The server listens on the port in the `PORT` environment variable (default `8080`):

```
PORT=9000 poetry run python main.py
```

For development with auto-reload, run uvicorn directly. The app lives in `main.py`, so the target is `main:app`:

```
poetry run uvicorn main:app --reload
```

This uses uvicorn's default port, 8000.

Then try `http://localhost:8080/`, `http://localhost:8080/hello`, and `http://localhost:8080/goodbye`.

## Deploying (Google Cloud Run)

Cloud Run installs from `requirements.txt` and sets `PORT` for you. After changing dependencies, regenerate it:

```
poetry export --without-hashes -o requirements.txt
```

Start command: `python main.py`
