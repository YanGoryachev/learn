from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, Body, Path
# teper seryozno
app = FastAPI()

class Model(BaseModel):
    id : int = Field(gt=10)
    username : str = Field(min_length=4)

@app.get("/{id}")
async def home(id:Annotated[int, Path(gt=3)]):
    return id

@app.post("/post")
async def post(user:Annotated[Model, Body(max_length=10)]):
    return user
