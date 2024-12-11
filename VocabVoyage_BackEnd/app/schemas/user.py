from pydantic import BaseModel


# 用户创建时的请求模型
class UserCreate(BaseModel):
    nick_name: str
    phone: str
    password: str


# 用户登录时的请求模型
class UserLogin(BaseModel):
    phone: str
    password: str


# 数据库中的用户模型（用于返回数据）
class UserInDB(UserCreate):
    id: int


# 用户响应时返回的数据模型（返回给前端的数据）
class UserResponse(BaseModel):
    id: int
    nick_name: str
    phone: str

    class Config:
        orm_mode = True  # 使 Pydantic 能够从 ORM 模型中读取数据
