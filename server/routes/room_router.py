from models.room import Room, CategoryEnum
from database.connection import DBObject
from fastapi import APIRouter

room_router = APIRouter(
    prefix="/room",
    tags=["room"],
)


@room_router.get("/{name}")
async def get_room(name: str):
    try:
        room = Room.read_all_room(DBObject(), name)
        return room
    except Exception as e:
        print(e)
        return {"message": "Room not found"}


@room_router.post("")
async def create_room(number: int, content: str, category: CategoryEnum):
    try:
        room = Room.create_room_model(
            DBObject(), number, content=content, category=category)
        if room:
            return {"message": "Room created"}

        else:
            return {"message": "Room not created"}

    except Exception as e:
        print(e)
        return {"message": "Room already exists"}
