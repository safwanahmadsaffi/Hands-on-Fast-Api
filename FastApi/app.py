from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from fastapi import HTTPException

app = FastAPI()

#define a pydentic model for data validation
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
items = {}

@app.post("/items/{item_id}", response_model=Item)
def create_item_with_id(item: Item, item_id: int):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return item

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = updated_item
    return updated_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "Item deleted"}

#-----------------------------------------------------------------------
#define a basic route end point
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# #define a route with path parameters
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# #define a route to createa an item with a post request
# @app.post("/items/")
# def create_item(item: Item):
#     return {"item": item}
#-----------------------------------------------------------------------