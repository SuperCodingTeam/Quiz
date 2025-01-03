from starlette.middleware.cors import CORSMiddleware
from routes.score_router import score_router
from routes.user_router import user_router
from routes.room_router import room_router
from routes.quiz_router import quiz_router
from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


app.include_router(user_router)
app.include_router(room_router)
app.include_router(quiz_router)
app.include_router(score_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,  # if os.path.exists("./is-server") else 3000,
        reload=not os.path.exists("./is-server"),
    )
