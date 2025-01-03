from database.connection import DBObject
from fastapi import APIRouter
from models.user import User

user_router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@user_router.get("/{name}")
async def get_user(name: str):
    try:
        user = User.read_user_by_name(DBObject(), name)
        return user.get_properties()
    except:
        return {"message": "User not found"}
