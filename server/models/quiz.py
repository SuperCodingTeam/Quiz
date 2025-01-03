from sqlalchemy import String, TEXT, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import DBObject
from models.include import Include
from typing import Dict, Any
from models.base import Base
from enum import Enum
import uuid


class AnswerEnum(Enum):
    O = "O"
    X = "X"


class Quiz(Base):
    __tablename__ = "quiz"

    quiz_uuid: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    content: Mapped[str] = mapped_column(
        TEXT, nullable=False
    )
    answer: Mapped[AnswerEnum] = mapped_column(
        SQLEnum(AnswerEnum)
    )

    explanation: Mapped[str] = mapped_column(
        TEXT, nullable=False
    )

    def __init__(self, content: str, answer: AnswerEnum, explanation: str, quiz_uuid: str | None = None):
        self.quiz_uuid = quiz_uuid if quiz_uuid else str(uuid.uuid4())
        self.content = content
        self.answer = answer
        self.explanation = explanation

    def get_properties(self) -> Dict[str, Any]:
        return {
            "quiz_uuid": self.quiz_uuid,
            "content": self.content,
            "answer": self.answer,
            "explanation": self.explanation,
        }

    @staticmethod
    def create_quiz_model(
        dbo: DBObject,
        content: str,
        answer: AnswerEnum,
        explanation: str,
        room_uuid: str,
        quiz_uuid: str | None = None,
    ) -> "Quiz":
        quiz = Quiz(content, answer, explanation, quiz_uuid)
        include = Include(room_uuid, quiz.quiz_uuid)
        with dbo.session as session:
            session.add(quiz)
            session.commit()
            session.add(include)
            session.commit()

        return quiz

    @staticmethod
    def get_quiz_by_room_uuid(dbo: DBObject, room_uuid: str):
        with dbo.session as session:
            quiz = session.query(Quiz).join(Include).filter(
                Include.room_uuid == room_uuid).all()

        return [q.get_properties() for q in quiz]
