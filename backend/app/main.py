from fastapi import FastAPI
from app.router import upload

app = FastAPI(title="Study Assistant API")

app.include_router(upload.router, prefix="/api/upload")

@app.get("/ping")
def ping():
    return {"message": "pong"}