from fastapi import FastAPI, Request
from mockData import Products

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World om"}
#endpoint create karta hu 
#kabhi bhi same route repeat nhi hote hai

@app.get("/Products")
def get_products():
    return Products

#path parameter
@app.get("/Products/{product_id}")
def get_one_product(product_id: int):
    for product in Products:
        if product["id"] == product_id:
            return product
    return {"message": "Product not found"}

#query parameter
@app.get("/greet")
def greet(name: str, age: int):
    return {
        "greet": f"Hello {name}, you are {age}!"
    }

@app.get("/search")
def search(request: Request):
    query_params = dict(request.query_params)
    print(query_params)
    return {
        "results": f"your name is {query_params.get('name')} and your age is {query_params.get('age')}"
    }