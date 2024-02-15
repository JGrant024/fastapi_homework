# fastapi_homework

FastAPI + PostgreSQL

Must Haves

Setup your enviroment

Initialize a new environment -> python -m venv env
Don't forget to activate it -> source env/bin/activate
Install the required libraries for FastAPI
Option one: Normal install
pip install fastapi uvicorn psycopg2
Option two: requirements.txt
pip install -r requirements.txt
Time for CRUD
Create a CRUD backend to manage a school.

⭐ This article might be helpful for some of the GET routes that require a JOIN statement. ⭐ This documentation about ForeignKey types will also be helpful.

Create your database
Setup a database, choose a name that sounds like a school.

Create the following tables/fields:

students
id
name
courses
'id'
name
enrollments
id
student_id -> This will be a FOREIGN KEY field pointing to students(id)
course_id -> This will be a FOREIGN KEY field pointing to courses(id)
Setup all the necessary CRUD routes
Create
POST /create/student
POST /create/course
POST /create/enrollment
Read
GET /
GET /students
GET /courses
GET /enrollment
Update
PUT /update/student/{id}
PUT /update/course/{id}
PUT /update/enrollment/{id}
Delete
PUT /delete/student/{id}
PUT /delete/course/{id}
PUT /delete/enrollment/{id}
Test your routes
Test your routes using the Swagger docs, or POSTMan (or both!)

Bonus

Write a webpage to fetch() the GET routes
Show the results on the page

Double Bonus
Write a form that accepts input to match the Create routes.
The Supplying request options to fetch() documentation will be helpful.

Level 9000
Write a form that accepts input to make updates via Update routes.
