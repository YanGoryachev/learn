from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Annotated

class User(BaseModel):
    id : int
    username : str

vnesh_rout = APIRouter(prefix="/user")

@vnesh_rout.get("/")
async def get_user(user:Annotated[User, Query(le=100)]):
    return user

@vnesh_rout.post("/{id}")
async def post_user(id:int, user:User):
    return user
