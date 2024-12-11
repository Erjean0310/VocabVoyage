import uvicorn
from fastapi import FastAPI
from app.api.v1.endpoints import user
app = FastAPI()


app.include_router(user.router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)