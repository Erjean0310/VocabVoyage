# api/v1/endpoints/user.py
from fastapi import APIRouter, HTTPException, Depends, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.crud.user import create_user, get_user_by_phone, verify_password
from app.schemas.user import UserCreate, UserLogin
from app.services.auth import create_token, refresh_token, verify_token
from app.core.config import settings
from app.services.user_service import user_sign_in

router = APIRouter()


@router.post("/register", summary="用户注册")
async def register_user(user: UserCreate, response: Response, db: AsyncSession = Depends(get_db)):
    # 检查手机号是否已注册
    existing_user = await get_user_by_phone(db, user.phone)
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    # 创建用户
    new_user = await create_user(db, user.nick_name, user.phone, user.password)
    token_data = {'sub': new_user.id}
    token = create_token(token_data)

    # 将 token 设置到 cookie 中
    response.set_cookie(
        key=settings.COOKIE_NAME,
        value=token,
        httponly=True,
        max_age=3600,
        samesite='lax'
    )
    return {"message": "User registered successfully"}


@router.post("/login", summary="用户登录")
async def login_user(user: UserLogin, response: Response, db: AsyncSession = Depends(get_db)):
    db_user = await verify_password(db, user.phone, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

        # 创建 JWT Token
    token_data = {"sub": db_user.phone}
    token = create_token(token_data)

    # 设置 Cookie，返回 Token
    response.set_cookie(
        key=settings.COOKIE_NAME,
        value=token,
        httponly=True,
        max_age=3600,  # 设置 Cookie 有效期为 1 小时
        samesite="lax",
    )

    return {"message": "Login successful"}


# 退出登录
@router.post("/logout", summary="退出登录")
async def logout_user(response: Response):
    # 清除 Cookie 中的 session_id
    response.delete_cookie(settings.COOKIE_NAME)
    return {"message": "Logout successful"}


@router.get("/sign/in", summary="签到")
async def sign_in(request: Request, db: AsyncSession = Depends(get_db)):
    await user_sign_in(db, 1)
    return


# # 受保护的路由，检查是否有有效的 Token
# @router.get("/test/protected-route")
# async def protected_route(request: Request, response: Response):
#     # 从 Cookie 获取 Token
#     token = request.cookies.get(settings.COOKIE_NAME)
#     if not token:
#         raise HTTPException(status_code=401, detail="Not authenticated")
#
#     # 验证 Token
#     try:
#         payload = verify_token(token)
#     except HTTPException:
#         raise HTTPException(status_code=401, detail="Session expired or invalid")
#
#     # 刷新 Cookie 的有效期
#     refresh_token(token, response)
#
#     return {"message": "Access granted, Cookie expiration refreshed"}

