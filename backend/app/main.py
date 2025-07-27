from fastapi import FastAPI

app = FastAPI(title="Study Assistant API")

@app.get("/ping")
def ping():
    return {"message": "pong"}