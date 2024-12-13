# api/v1/endpoints/user.py
from fastapi import APIRouter, Depends, Response, Request, Query, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.crud.user import create_user, get_user_by_phone, verify_password, update_user_password
from app.schemas.user import UserCreate, UserLogin, UserChangePassword
from app.services.auth import create_token, refresh_token, verify_token, get_user_id_and_token
from app.core.config import settings
from app.services.user_service import user_sign_in
from app.core.constans import Constants
from app.core.result import Result
from app.services.file_upload import upload_file_to_oss


router = APIRouter()


@router.post("/register", summary="用户注册")
async def register_user(user: UserCreate, response: Response, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_phone(db, user.phone)
    if existing_user:
        return Result.fail(Constants.PHONE_ALREADY_REGISTERED)

    new_user = await create_user(db, user.nick_name, user.phone, user.password)

    token = create_token({'sub': str(new_user.id)})
    # 将 token 设置到 cookie 中
    response.set_cookie(
        key=settings.COOKIE_NAME,
        value=token,
        httponly=True,
        max_age=settings.COOKIE_EXPIRE_MINUTES * 60,
        samesite='lax'
    )
    return Result.success(Constants.REGISTER_SUCCESS)


@router.post("/login", summary="用户登录")
async def login_user(user: UserLogin, response: Response, db: AsyncSession = Depends(get_db)):
    db_user = await verify_password(db, user.phone, user.password)

    if not db_user:
        return Result.fail(Constants.VERIFICATION_FAILED)

    # 创建 JWT Token
    token = create_token({'sub': str(db_user.id)})

    # 设置 Cookie，返回 Token
    response.set_cookie(
        key=settings.COOKIE_NAME,
        value=token,
        httponly=True,
        max_age=settings.COOKIE_EXPIRE_MINUTES * 60,
        samesite="lax",
    )

    return Result.success(Constants.LOGIN_SUCCESS)


# 退出登录
@router.post("/logout", summary="退出登录")
async def logout_user(response: Response):
    # 清除 Cookie 中的 session_id
    response.delete_cookie(settings.COOKIE_NAME)
    return Result.success(Constants.LOGOUT_SUCCESSFUL)


@router.get("/sign/in", summary="签到")
async def sign_in(request: Request, response: Response, db: AsyncSession = Depends(get_db)):
    user_id, token = get_user_id_and_token(request)
    result = await user_sign_in(db, user_id)
    refresh_token(token, response)
    return result


@router.post("/change-password", summary="修改密码")
async def change_password(user: UserChangePassword, request: Request, response: Response, db: AsyncSession = Depends(get_db)):
    user_id, token = get_user_id_and_token(request)
    # 根据手机号获取用户
    db_user = await verify_password(db, user.phone, user.old_password)

    if db_user.id != user_id:
        return Result.fail("不能修改其他手机号的密码")

    if db_user is None:
        return Result.fail(Constants.VERIFICATION_FAILED)

    await update_user_password(db, db_user.id, user.new_password)

    refresh_token(token, response)
    return Result.success(Constants.MODIFY_PASSWORD_SUCCESS)


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_url = upload_file_to_oss(file)
    if file_url is None:
        return Result.fail("文件上传失败")
    return Result.success(data=file_url)
