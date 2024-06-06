from fastapi import FastAPI
from app.api.endpoints import board, chat, users, notice, question, answer, auth, plans
from app.database import database
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(board.router, prefix="/board", tags=["board"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(notice.router, prefix="/notice", tags=["notice"])
app.include_router(question.router, prefix="/question", tags=["question"])
app.include_router(answer.router, prefix="/answer", tags=["answer"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(plans.router, prefix="/plans", tags=["plans"])

@app.get("/api/demo-web")
async def demo_web():
    return {"message": ""}

@app.on_event("startup")
async def startup():
    await database.connect()
    print("Database connected!")
    
    # app 디렉토리 내에 uploads 디렉토리가 존재하는지 확인
    if not os.path.exists("app/uploads"):
        os.makedirs("app/uploads")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    print("Database disconnected!")