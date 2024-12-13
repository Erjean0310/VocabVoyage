from pydantic import BaseModel, Field


# 用户创建时的请求模型
class UserCreate(BaseModel):
    nick_name: str = Field(..., description="用户昵称")
    phone: str = Field(..., description="用户手机号")
    password: str = Field(..., description="用户密码")


# 用户登录时的请求模型
class UserLogin(BaseModel):
    phone: str = Field(..., description="用户手机号")
    password: str = Field(..., description="用户密码")


# 数据库中的用户模型（用于返回数据）
class UserInDB(UserCreate):
    id: int = Field(..., description="用户 ID")


# 用户响应时返回的数据模型（返回给前端的数据）
class UserResponse(BaseModel):
    id: int = Field(..., description="用户 ID")
    nick_name: str = Field(..., description="用户昵称")
    phone: str = Field(..., description="用户手机号")
    avatar: str = Field(..., description="用户头像")

    class Config:
        orm_mode = True  # 使 Pydantic 能够从 ORM 模型中读取数据


class UserChangePassword(BaseModel):
    phone: str = Field(..., description="用户手机号")
    old_password: str = Field(..., description="旧密码")
    new_password: str = Field(..., description="新密码")
