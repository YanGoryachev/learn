from typing import Annotated
from fastapi import FastAPI, Query
#pupupu yes yes yes
app = FastAPI()

@app.get("/{id}")
async def home(id:int | None):
    return {"name":id}
