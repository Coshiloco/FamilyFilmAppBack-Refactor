from fastapi import FastAPI
from router import users, groups, genres

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(users)
app.include_router(groups)
app.include_router(genres)

