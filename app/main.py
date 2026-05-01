from fastapi import FastAPI
from .database import engine
from . import models

# This creates the table in PostgreSQL
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is working"}