from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Server Running Successfully"}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Topic(BaseModel):
    topic: str
class Login(BaseModel):
    email: str
    password: str

@app.post("/generate")
def generate(data: Topic):

    curriculum = f"""
    Curriculum for {data.topic}
    AI Curriculum for:{data.topic}

    Module 1: Introduction
    Module 2:Basics
    Module 3: Intermediate Concepts
    Module 4: Advanced Concepts
    Module 5: projects
    """

    return {"curriculum": curriculum}
@app.post("/login")
def login(data: Login):
    if data.email == "krishnaveni@gmail.com" and data.password == "08":
        return{"message": "Login Successful"}
        return {"message": "Invalide Email or password"}
  
