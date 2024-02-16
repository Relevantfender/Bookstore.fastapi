from fastapi import FastAPI

from BookStoreAPI.repository.database import init_db
from BookStoreAPI.controllers.BookController import Books as Router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["https://localhost:8000",
           "https://localhost:5000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(Router, tags=["Books"], prefix="/books")



@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def index() -> dict:
    return {"message": "Welcome to books app!"}
