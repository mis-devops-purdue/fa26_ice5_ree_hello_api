# Plan: add a root route that responds "Online"

## Context
The app has `/hello` and `/goodbye` but nothing at `/`. A basic root route that returns `Online` gives a quick "is it up?" check (handy on Cloud Run).

## Steps
1. Log this prompt with a timestamp in `PROMPTS.md` (per CLAUDE.md).
2. Save this plan as `plans/02_root_route.md`.
3. Create branch `feature_root_route` off `main` (currently on `main`).
4. In `main.py`, add before `/hello`:
   ```python
   from fastapi.responses import PlainTextResponse

   @app.get("/", response_class=PlainTextResponse)
   def root():
       return "Online"
   ```
   Plain text (not JSON) so the body is exactly `Online`. `PlainTextResponse` ships with FastAPI, so no new packages and `requirements.txt` stays as is.
5. Update `README.md`: list `GET /` (returns plain text `Online`) with the other endpoints, and add `http://localhost:8080/` to the "Then try" line.

## Verification
- `poetry run python main.py`, then `curl -i http://localhost:8080/` → `200`, `content-type: text/plain`, body `Online`.
- `/hello` and `/goodbye` still return their JSON.

No commits. You'll handle those.
