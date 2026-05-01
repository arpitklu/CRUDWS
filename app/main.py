from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@app.post("/items", response_model=schemas.ItemResponse)
def create(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

# READ ALL
@app.get("/items")
def read_all(db: Session = Depends(get_db)):
    return crud.get_items(db)

# READ ONE
@app.get("/items/{item_id}")
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# UPDATE
@app.put("/items/{item_id}")
def update(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    updated = crud.update_item(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

# DELETE
@app.delete("/items/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}