#------ This is a placeholder for the main application code---------------
from fastapi import FastAPI
app = FastAPI()

@app.get("/") #slash endpoint ye domain default pr redirect krta hai
def read_root():
    return {"Hello": "World"}

