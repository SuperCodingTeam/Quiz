from sqlalchemy import String, INT, TEXT, Enum as SQLEnum, or_
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import DBObject
from typing import Dict, Any, List
from models.base import Base
from .user import User, PositionEnum
from enum import Enum
import uuid


class CategoryEnum(Enum):
    ALL = "전체"
    FRONT = "프론트엔드"
    BACK = "백엔드"


class Room(Base):
    __tablename__ = "room"

    room_uuid: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    number: Mapped[int] = mapped_column(
        INT, nullable=False)
    content: Mapped[str] = mapped_column(
        TEXT,  nullable=False)
    category: Mapped[CategoryEnum] = mapped_column(
        SQLEnum(CategoryEnum), nullable=False
    )

    def __init__(
        self,
        number: int,
        content: str,
        category: CategoryEnum,
        room_uuid: str | None = None,
    ):
        self.room_uuid = room_uuid if room_uuid else str(uuid.uuid4())
        self.number = number
        self.content = content
        self.category = category

    def get_properties(self) -> Dict[str, Any]:
        return {
            "room_uuid": self.room_uuid,
            "number": self.number,
            "content": self.content,
            "category": self.category,
        }

    @staticmethod
    def create_room_model(
        dbo: DBObject,
        number: int,
        content: str,
        category: CategoryEnum,
        room_uuid: str | None = None,
    ) -> bool:
        room = Room(number, content, category, room_uuid)
        with dbo.session as session:
            session.add(room)
            session.commit()

        return True

    @staticmethod
    def read_all_room(dbo: DBObject, name: str) -> List[Dict[str, Any]]:
        with dbo.session as session:
            room = session.query(Room).filter(or_(
                Room.category == CategoryEnum.ALL, Room.category == eval(
                    f"CategoryEnum.{User.read_user_by_name(dbo, name).position.name}"))).order_by(Room.number, Room.category).all()

        return [q.get_properties() for q in room]
