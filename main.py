from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.get("/about")
def read_about():
    return {"message": "This is the about page."}