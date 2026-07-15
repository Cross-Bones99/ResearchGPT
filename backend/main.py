# backend/main.py

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from backend.routes.chat import router as chat_router
from backend.routes.research_route import router as research_router

app = FastAPI(
    title="ResearchGPT API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(chat_router)
app.include_router(research_router)


@app.get("/")
def home():
    return {
        "message": "ResearchGPT Backend Running 🚀"
    }