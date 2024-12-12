import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import user, word
from app.core.response import general_exception_handler


app = FastAPI()

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有请求头
)

# 注册自定义异常处理器
app.add_exception_handler(Exception, general_exception_handler)


app.include_router(user.router, prefix="/users", tags=["用户相关接口"])
app.include_router(word.router, prefix="/word", tags=["单词相关接口"])

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
