from fastapi import APIRouter
from backend.services.llm import llm

router=APIRouter()

@router.get("/chat")
def chat():

    response = llm.invoke(
        "Say hello from ResearchGPT."
    )

    return {
        "response": response.content
    }