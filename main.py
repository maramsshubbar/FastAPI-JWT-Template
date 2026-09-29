import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.users import router as UsersRouter
from controllers.books import router as BooksRouter
from models.review import ReviewModel
from controllers.reviews import router as ReviewsRouter

app = FastAPI()

origins = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "").split(",")
    if origin.strip()
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # Which sites can call this API
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], 
    
)
app.include_router(UsersRouter, prefix='/api')
app.include_router(BooksRouter, prefix="/api/books")
@app.get('/')
def home():
    return {'message': 'Home Page'}

app.include_router(ReviewsRouter, prefix="/api/books")