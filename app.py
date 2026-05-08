from typing import Annotated
from fastapi import FastAPI, Query
#pupupu
app = FastAPI()

@app.get("/{id}")
async def home(id:int | None):
    return {"name":id}
