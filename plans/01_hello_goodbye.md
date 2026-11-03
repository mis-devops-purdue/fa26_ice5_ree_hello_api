# Plan: hello_api (FastAPI + Poetry)

## Context
Empty repo (only CLAUDE.md, on `main`). Build a small FastAPI app with `GET /hello` and `GET /goodbye` returning casual JSON messages, ready for Google Cloud Run (reads `PORT`, default 8080; `requirements.txt` exported from Poetry). Must follow CLAUDE.md rules.

## CLAUDE.md compliance steps (in order)
1. Create branch `feature_hello_goodbye` (underscores; never commit on `main`).
2. Create `PROMPTS.md` and log the prompt with a timestamp before any code.
3. Save this plan as `plans/01_hello_goodbye.md` once approved.
4. No commits/pushes/PRs — leave changes uncommitted for the user.
5. Write `README.md` (install + run); no secrets anywhere.

## Files
- `pyproject.toml` — via `poetry init`/hand-written; deps: `fastapi`, `uvicorn` only (no extras; `uvicorn` needed to serve). `package-mode = false` (app, not a library).
- `main.py` — FastAPI app:
  - `GET /hello` → `{"message": "Hey there! Hope you're having a great day."}`
  - `GET /goodbye` → `{"message": "See ya later! Take it easy."}`
  - `if __name__ == "__main__"`: `uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))`
- `requirements.txt` — `poetry export --without-hashes -o requirements.txt` (plugin `poetry-plugin-export` already installed).
- `.gitignore` — `.venv/`, `__pycache__/`, `.env`.
- `README.md`, `PROMPTS.md`, `plans/01_hello_goodbye.md`.

Run command documented in README: `poetry run python main.py` (honors `PORT`); Cloud Run-style: `uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}`.

## Verification
- `poetry install`, then `PORT=9000 poetry run python main.py` in background.
- `curl localhost:9000/hello` and `/goodbye` → expect JSON 200; also confirm default 8080 when `PORT` unset.
- Confirm `requirements.txt` lists fastapi/uvicorn and is in sync with `poetry.lock`.
- `git status` shows branch not `main`, nothing committed.
