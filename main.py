import logging
import sys

from starlette.staticfiles import StaticFiles

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from app.routes.chat_routes import router as chat_router

app = FastAPI()
app.include_router(chat_router)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins - NOT for production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)