import uvicorn
from fastapi import FastAPI
from app.api.v1.endpoints import user, word
app = FastAPI()


app.include_router(user.router, prefix="/users", tags=["用户相关接口"])
app.include_router(word.router, prefix="/word", tags=["单词相关接口"])


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
