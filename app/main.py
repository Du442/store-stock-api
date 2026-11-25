from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI(
    title="Store Stock API",
    version="V1.0.0"
)

app.include_router(
    api_router
)

app.get("/")
def health_check():
    return {"Hello": "World"}