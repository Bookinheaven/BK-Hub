from fastapi import FastAPI, status
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
    class Config: # Configuring for automatic examples in docs
        json_schema_extra = {
            "example": {
                "name": "Pen",
                "price": 10.5,
                "in_stock": True
            }
        }

app = FastAPI()

@app.get("/item-preview", response_model=Item)
def get_item():
    return {
        "name": "MacBook Air",
        "price": 99999.99,
        "in_stock": True,
        "internal_code": "MB-2025"  # This field will be filtered out
    }

# Let’s say we store passwords but don’t want to return them.
class User(BaseModel):
    username: str
    email: str
    password: str  # internal

class SafeUser(BaseModel):
    username: str
    email: str

@app.get("/user", response_model=SafeUser)
def get_user():
    return User(username="admin", email="a@b.com", password="1234")


# Change Status Code
@app.post("/create", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item