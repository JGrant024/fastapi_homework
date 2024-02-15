from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI() 
@app.get('/') 
def home(): 
    return{"message": "Hey World!"}


origins = [
    "http://localhost", 
    "http://localhost:3000"
]

