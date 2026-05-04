from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .database import engine
from . import models
from .routes import items

models.Base.metadata.create_all(bind=engine)

# app = FastAPI()
app = FastAPI(
    title="CRUD WS",
    description="CRUD Web Service built using FastAPI and PostgreSQL",
    version="1.0.0",
    docs_url=None   
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)

@app.get("/docs", include_in_schema=False)
def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="CRUD WS"
    )