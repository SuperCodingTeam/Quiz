from database.connection import DBObject
from .user import User, PositionEnum
from .include import Include
from .score import Score
from .room import Room
from .quiz import Quiz

DBObject()

tables = [Room, Quiz, User, Score, Include]
for table in tables:
    table.__table__.create(bind=DBObject.instance.engine, checkfirst=True)

try:
    User.create_user_model(DBObject.instance, "강은주", PositionEnum.FRONT)
    User.create_user_model(DBObject.instance, "박준원", PositionEnum.FRONT)
    User.create_user_model(DBObject.instance, "김태호", PositionEnum.BACK)
    User.create_user_model(DBObject.instance, "조연우", PositionEnum.BACK)

except:
    pass
