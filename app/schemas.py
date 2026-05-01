from pydantic import BaseModel

# Request body (like DTO for POST/PUT)
class ItemCreate(BaseModel):
    name: str
    description: str

# Response body (what API returns)
class ItemResponse(ItemCreate):
    id: int

    class Config:
        from_attributes = True