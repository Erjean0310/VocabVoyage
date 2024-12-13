from datetime import datetime, timedelta, UTC
from fastapi import HTTPException, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.common.utils import ComplexEncoder
from app.crud.user import get_user_by_id
from app.core.constans import Constants
import logging
import jwt


# 创建新的 jwt token
def create_token(data: dict) -> str:
    expire = datetime.now(UTC) + timedelta(minutes=settings.COOKIE_EXPIRE_MINUTES)
    data.update({'exp': expire})
    token = jwt.encode(data, settings.COOKIE_SECRET, algorithm='HS256', json_encoder=ComplexEncoder)
    return token


# 验证 jwt token
def verify_token(token: str) -> dict:
    if token is None:
        raise HTTPException(status_code=401, detail=Constants.USER_NOT_LOG_IN)

    try:
        payload = jwt.decode(token, settings.COOKIE_SECRET, algorithms=['HS256'])
        return payload

    except jwt.ExpiredSignatureError:
        logging.error("Token has expired")
        raise HTTPException(status_code=401, detail=Constants.SESSION_EXPIRE)

    except jwt.InvalidTokenError as e:
        # 记录详细的错误信息
        logging.error(f"Invalid token error: {str(e)}")
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")


# 刷新 token 有效期并更新 cookie
def refresh_token(token: str, response: Response) -> None:
    response.set_cookie(
        key=settings.COOKIE_NAME,
        value=token,
        httponly=True,
        max_age=settings.COOKIE_EXPIRE_MINUTES * 60,  # 秒
        samesite='lax'
    )


# 获取 user_id 和 token
def get_user_id_and_token(request: Request):
    token = request.cookies.get(settings.COOKIE_NAME)
    payload = verify_token(token)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail=Constants.USER_NOT_LOG_IN)

    return user_id, token


# 如果有 cookie 的话 刷新 cookie
def refresh_token_if_exists(request: Request, response: Response) -> None:
    token = request.cookies.get(settings.COOKIE_NAME)
    if not token:
        return

    try:
        verify_token(token)
    except HTTPException:
        return

    response.set_cookie(
        key=settings.COOKIE_NAME,
        value=token,
        httponly=True,
        max_age=settings.COOKIE_EXPIRE_MINUTES * 60,  # 秒
        samesite='lax'
    )


# 获取 user_id 和 token
async def get_admin_id_and_token(request: Request, db: AsyncSession):
    token = request.cookies.get(settings.COOKIE_NAME)
    payload = verify_token(token)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail=Constants.USER_NOT_LOG_IN)

    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail=Constants.USER_NOT_LOG_IN)

    if user.role != Constants.ADMIN_ROLE:
        raise HTTPException(status_code=403, detail=Constants.PERMISSION_ERROR)

    return user_id, token

