from sqlalchemy import String, BOOLEAN, ForeignKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import DBObject
from typing import Dict, Any
from models.base import Base
import uuid


class Score(Base):
    __tablename__ = "score"

    score_uuid: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    score: Mapped[bool] = mapped_column(
        BOOLEAN, nullable=False)
    name: Mapped[str] = mapped_column(
        String(5), primary_key=True, nullable=False
    )
    quiz_uuid: Mapped[str] = mapped_column(
        String(36), primary_key=True, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ["quiz_uuid"],
            ["quiz.quiz_uuid"],
        ), ForeignKeyConstraint(
            ["name"],
            ["user.name"],
        ),
    )

    def __init__(
        self,
        quiz_uuid: str,
        name: str,
        score: bool,
        score_uuid: str | None = None,
    ):
        self.quiz_uuid = quiz_uuid
        self.name = name
        self.score = score
        self.score_uuid = score_uuid if score_uuid else str(uuid.uuid4())

    @staticmethod
    def create_score_model(
        dbo: DBObject,
        quiz_uuid: str,
        name: str,
        score: bool,
        score_uuid: str | None = None,
    ) -> "Score":
        score = Score(quiz_uuid, name, score, score_uuid)
        with dbo.session as session:
            session.add(score)
            session.commit()

        return score

    def read_score_model(self) -> Dict[str, Any]:
        return {
            "score_uuid": self.score_uuid,
            "name": self.name,
            "score": self.score,
            "quiz_uuid": self.quiz_uuid,
        }
