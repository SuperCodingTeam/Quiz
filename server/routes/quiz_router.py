from models.quiz import Quiz, AnswerEnum
from database.connection import DBObject
from models.include import Include
from fastapi import APIRouter

quiz_router = APIRouter(
    prefix="/quiz",
    tags=["quiz"],
)


@quiz_router.get("/{room_uuid}")
async def get_quiz(room_uuid: str):
    try:
        quiz = Include.read_all_quiz_from_room(DBObject(), room_uuid)
        return quiz
    except Exception as e:
        print(e)
        return {"message": "Quiz not found"}


@quiz_router.post("")
async def create_quiz(question: str, answer: AnswerEnum, explanation: str, room_uuid: str):
    try:
        quiz = Quiz.create_quiz_model(
            DBObject(), question, answer, explanation, room_uuid)
        if quiz:
            return {"message": "Quiz created"}

        else:
            return {"message": "Quiz not created"}

    except Exception as e:
        print(e)
        return {"message": "Quiz already exists"}
