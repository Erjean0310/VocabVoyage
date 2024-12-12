from datetime import datetime, timedelta, UTC
import jwt
from fastapi import HTTPException, Response
from app.core.config import settings
from app.services.utils import ComplexEncoder
from app.core.constans import Constants
import logging


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

