from fastapi import APIRouter
from starlette.staticfiles import StaticFiles

from app.agent.chat_agent import Agent

router = APIRouter()

agent = Agent()

@router.get("/chat/{query}")
async def chat(query: str):
    return agent.chat(query)


@router.get("/health")
async def health():
    return {"status": "ready"}

