from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import date

# Import our tools
# This is the database connection file
from db import session

# These are our models
from models import Students, Enrollments, Courses

app = FastAPI()

# Setup our origins...
# ...for now it's just our local environments
origins = [
    "http://localhost",
    "http://localhost:3000",
]

# Add the CORS middleware...
# ...this will pass the proper CORS headers
# https://fastapi.tiangolo.com/tutorial/middleware/
# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Root Route"}


@app.get('/courses')
def get_courses():
    courses = session.query(Courses)
    return courses.all()


@app.get('/students')
def get_students():
    students = session.query(Students)
    print(type( students.all()))
    return students.all()


@app.get('/enrollments')
def get_enrollments():
    enrollments = session.query(Enrollments, Students, Courses).join(Students, Students.id == Enrollments.student_id).join(Courses, Courses.id == Enrollments.course_id)
    results = enrollments.all()

    enrollment_list = [] 
    for enrollment in results: 
        enrollment_dict = { 
            "enrollment_id": enrollment.Enrollments.enrollment_id, 
            "student_name": enrollment.Students.name, 
            "course_name": enrollment.Enrollments.enrollment_date
        }
        enrollment_list.append(enrollment_dict)

    return enrollment_list 
    


@app.post('/students/add')
async def add_student(name: str):
    student = Students(name=name)
    session.add(student)
    session.commit()
    return {"Student Added": student.name}


@app.post('/courses/add')
async def add_course(name: str):
    course = Courses(name=name)
    session.add(course)
    session.commit()
    return {"Course Added": course.name}

