import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import user, word, chat, admin, mistake
from app.common.response import general_exception_handler

app = FastAPI()

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174", "http://localhost:5175"],  # 允许所有域名
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有请求头
)

# 注册自定义异常处理器
app.add_exception_handler(Exception, general_exception_handler)

app.include_router(mistake.router, prefix="/mistake", tags=["错误相关接口"])
app.include_router(user.router, prefix="/user", tags=["用户相关接口"])
app.include_router(admin.router, prefix="/admin", tags=["管理员相关接口"])
app.include_router(word.router, prefix="/word", tags=["单词相关接口"])
app.include_router(chat.router, prefix="/model", tags=["大模型相关接口"])

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
