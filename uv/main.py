#------ This is a placeholder for the main application code---------------
# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/") #slash endpoint ye domain default pr redirect krta hai
# def read_root():
#     return {"Hello": "World"}


#---WE CAN MAKE MULTIPLE GET METHEOD AND USE BUT ENDPOINTS MUST BE UNIQUE---
from fastapi import FastAPI, Path 

app = FastAPI()

students = [
    "Safwan Ahmad Saffi","Ali", "Ahmed", "Hassan", "Hussain", "Omar",
    "Zain", "Faizan", "Saad", "Shahzaib", "Hamza",
    "Bilal", "Kashif", "Asad", "Salman", "Imran",
    "Rizwan", "Usman", "Noman", "Junaid", "Rehan",
    "Ayesha", "Fatima", "Zainab", "Maria", "Hira",
    "Sana", "Iqra", "Maham", "Laiba", "Mariam",
    "Anum", "Khadija", "Hafsa", "Areeba", "Mehwish",
    "Zoya", "Amna", "Rabia", "Nida", "Aiman"
]

#by default endpoint is same as function name
@app.get("/")
def root():
    return {"Message" : "hello world"}


@app.get("/filter-students")
def filter_students(sw: str,):
    filtered_names = []
    sw = sw.casefold()
    for student in students:
        if student.casefold().startswith(sw):
            filtered_names.append(student)
    return filtered_names


@app.get("/students")
def get_students(): # type: ignore
    return students

#this is static endpoint
@app.get("/students/Safwan Ahmad Saffi")
def get_students():  # noqa: F811
    return "Safwan Ahmad Saffi"

#this is dynamic endpoint
@app.get("/students/{id}")
def get_student(id: int = Path(ge=0, lt=len(students))):
    return students[id]
