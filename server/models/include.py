from sqlalchemy import String, ForeignKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import DBObject
from typing import Dict, Any, List
from models.base import Base


class Include(Base):
    __tablename__ = "include"

    room_uuid: Mapped[str] = mapped_column(
        String(36), primary_key=True
    )
    quiz_uuid: Mapped[str] = mapped_column(
        String(36), primary_key=True
    )

    __table_args__ = (
        ForeignKeyConstraint(
            ["room_uuid"],
            ["room.room_uuid"],
        ),
        ForeignKeyConstraint(
            ["quiz_uuid"],
            ["quiz.quiz_uuid"],
        ),
    )

    def get_properties(self) -> Dict[str, Any]:
        return {
            "room_uuid": self.room_uuid,
            "quiz_uuid": self.quiz_uuid,
        }

    def __init__(self, room_uuid: str, quiz_uuid: str):
        self.room_uuid = room_uuid
        self.quiz_uuid = quiz_uuid

    @staticmethod
    def create_include_model(dbo: DBObject, room_uuid: str, quiz_uuid: str) -> "Include":
        include = Include(room_uuid, quiz_uuid)
        with dbo.session as session:
            session.add(include)
            session.commit()

        return include
