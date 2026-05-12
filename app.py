from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, Body, Path, Response
from vnesh_app import vnesh_rout

# teper seryozno
app = FastAPI()
app.include_router(vnesh_rout)

class Model(BaseModel):
    id : int = Field(gt=10)
    username : str = Field(min_length=4)

@app.get("/{id}")
async def home(id:Annotated[int, Path(gt=3)]):
    a = Response()
    a.set_cookie()
    return Response()

@app.post("/post")
async def post(user:Annotated[Model, Body(max_length=10)]):
    return user
