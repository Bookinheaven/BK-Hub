from fastapi import FastAPI, Request, UploadFile, File, Form
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return( {"message": "Test 1"} )

# uvicorn main:app --reload

@app.get("/sync")
def read_sync():
    return( {"message": "Test 2"} )

@app.get("/async")
async def read_async():
    return( {"message": "Test 2"} )

# Path Parameters
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return { "item_id": item_id }
# http://127.0.0.1:8000/items/32

# Query Parameters
@app.get("/products/")
def read_product(name: str = "Book", price: float = 0.0):
    return { "name": name, "price": price}
# http://127.0.0.1:8000/products/?name=Pen&price=5.2

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items/")
def create_item(item: Item):
    return {
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock
    }

# triggers a 422 error if not in correct data type

@app.post('/raw/')
async def get_raw_body(request: Request):
    raw = await request.body()
    return {"raw_body": raw.decode()}

# Form Data
# pip install python-multipart
@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)): # Form(...) - required field
    return {"username": username, "password": password}



@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }
