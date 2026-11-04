import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def root():
    return "Online"


@app.get("/hello")
def hello():
    return {"message": "Hey there! Hope you're having a great day."}


@app.get("/goodbye")
def goodbye():
    return {"message": "See ya later! Take it easy."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
