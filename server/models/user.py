from sqlalchemy import String,  ForeignKeyConstraint, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import DBObject
from typing import Dict, Any
from models.base import Base
from enum import Enum
import uuid


class PositionEnum(Enum):
    FRONT = "프론트엔드"
    BACK = "백엔드"


class User(Base):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(
        String(5), primary_key=True, nullable=False, unique=True)
    position: Mapped[PositionEnum] = mapped_column(
        SQLEnum(PositionEnum)
    )

    def __init__(
        self,
        name: str,
        position: PositionEnum,
    ):
        self.name = name
        self.position = position

    def get_properties(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "position": self.position
        }

    @staticmethod
    def create_user_model(
        dbo: DBObject,
        name: str,
        position: PositionEnum,
    ) -> "User":
        user = User(name, position)
        with dbo.session as session:
            session.add(user)
            session.commit()

        return user

    @staticmethod
    def read_user_by_name(dbo: DBObject, name: str) -> "User":
        with dbo.session as session:
            user = session.query(User).filter(User.name == name).first()
            return user
