from fastapi import FastAPI
from typing import Annotated
from fastapi import Query
from pydantic import BaseModel, EmailStr

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/itemms/")
# async def read_items(q: Annotated[list[str] | None, Query(description="list of query values with same keys")] = None):

#     results = {"q": q}
#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(min_length=3)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserIn(UserBase):
    password: str


@app.post("/user")
def createUser(user: UserIn) -> UserBase:
    return user
