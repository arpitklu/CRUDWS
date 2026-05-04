from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas
from ..controllers import items as item_controller

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/items", response_model=schemas.ItemResponse)
def create(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return item_controller.create_item(db, item)

# READ ALL
@router.get("/items")
def read_all(db: Session = Depends(get_db)):
    return item_controller.get_items(db)

# READ ONE
@router.get("/items/{item_id}")
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = item_controller.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# UPDATE
@router.put("/items/{item_id}")
def update(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    updated = item_controller.update_item(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

# DELETE
@router.delete("/items/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    deleted = item_controller.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}