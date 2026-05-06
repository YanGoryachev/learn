from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home(id:int):
    return {"name":id}
