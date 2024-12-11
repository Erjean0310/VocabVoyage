from datetime import datetime, timedelta, UTC
import jwt
from fastapi import HTTPException, Response
from app.core.config import settings
from app.services.utils import ComplexEncoder


# 创建新的 jwt token
def create_token(data: dict) -> str:
    expire = datetime.now(UTC) + timedelta(settings.COOKIE_EXPIRE_MINUTES)
    data.update({'exp': expire})
    token = jwt.encode(data, settings.COOKIE_SECRET, algorithm='HS256', json_encoder=ComplexEncoder)
    return token


# 验证 jwt token
def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.COOKIE_SECRET, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Session is expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid session token')


# 刷新 token 有效期并更新 cookie
def refresh_token(token: str, response: Response) -> None:
    response.set_cookie(
        key=settings.COOKIE_NAME,
        value=token,
        httponly=True,
        max_age=settings.COOKIE_EXPIRE_MINUTES * 60,  # 秒
        samesite='lax'
    )