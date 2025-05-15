from fastapi import FastAPI

app = FastAPI()

#decorator 
@app.get("/") #to get request from api route to get fatch 
def hello():
    return {"message": "hello world"} #returning json data
@app.get("/about")
def about():
    return {"message": "this is about page"}    
    