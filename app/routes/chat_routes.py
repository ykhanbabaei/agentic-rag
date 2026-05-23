from fastapi import APIRouter

from app.agent.chat_agent import ChatAgent

router = APIRouter()

agent = ChatAgent()

@router.get("/chat/{query}")
async def chat(query: str):
    return await agent.achat(query)


@router.get("/health")
async def health():
    return {"status": "ready"}

