from fastapi import FastAPI
import json

app = FastAPI()

def load_data(): #to load data from json file
    #open the json file
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data
#decorator -- endpoints
@app.get("/") #to get request from api route to get fatch 
def hello():
    return {"message": "Patient management system api"} #returning json data

@app.get("/about")
def about():
    return {"message": "fully functional api to manage patient records"}    

@app.get("/view")
def view():
    data = load_data()
    return data