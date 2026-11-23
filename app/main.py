from fastapi import FastAPI

app = FastAPI(
    title="Store Stock API",
    version="V1.0.0"
)

app.get("/")
def health_check():
    return {"Hello": "World"}