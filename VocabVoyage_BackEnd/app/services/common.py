from fastapi import APIRouter, Query, Depends, Request
from app.core.config import settings
from http.client import HTTPException
from app.services.auth import create_token, refresh_token, verify_token


def get_user_id(request: Request):
    token = request.cookies.get(settings.COOKIE_NAME)
    if not token:  # 当前未登录
        raise HTTPException(status_code=401, detail=Constants.USER_NOT_LOG_IN)

    payload = verify_token(token)
    user_id = payload.get("sub")
    return user_id
