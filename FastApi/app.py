from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

#define a pydentic model for data validation
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


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