from fastapi import FastAPI
#pupupu
app = FastAPI()

@app.get("/")
async def home(id:int):
    return {"name":id}
