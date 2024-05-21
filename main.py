from fastapi import FastAPI, Path, Query, HTTPException
from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table


DATABASE_URL = "sqlite:///test.db"
DATABASE = create_engine(DATABASE_URL)
metadata = MetaData()
database = Database(DATABASE_URL)
app = FastAPI()


cars = Table(
    "cars",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("model", String)
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(20), unique=True, nullable=False),
    Column("email", String(120), unique=True, nullable=False),
    Column("password", String(60), nullable=False)
)


metadata.create_all(DATABASE)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/users/{user_id}")
async def read_user(
        user_id: int = Path(..., title="ID користувача", description="Це ідентифікатор користувача"),
        text: str = Query("", title="Текст", description="Додатковий текст")
):
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    return {"user": user, "text": text}


@app.get("/cars/{car_id}")
async def read_car(
        car_id: int = Path(..., title="id of car", description="This is the ID of "),
        text: str = Query("", title="", description="")
):

    query = cars.select().where(cars.c.id == car_id)
    car = await database.fetch_one(query)
    return {"car": car, "text": text}
