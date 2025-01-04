from models.score import Score
from database.connection import DBObject
from fastapi import APIRouter

score_router = APIRouter(
    prefix="/score",
    tags=["score"],
)


@score_router.get("/{name}")
async def get_score(name: str):
    try:
        score = Score.read_score_by_name(DBObject(), name)
        return score
    except Exception as e:
        print(e)
        return {"message": "Score not found"}


@score_router.post("")
async def create_score(name: str, score: bool, quiz_uuid: str):
    try:
        score = Score.create_score_model(
            DBObject(), quiz_uuid, name, score)
        if score:
            return {"message": "Score created"}

        else:
            return {"message": "Score not created"}

    except Exception as e:
        print(name)
        print(e)
        return {"message": "Score already exists"}
