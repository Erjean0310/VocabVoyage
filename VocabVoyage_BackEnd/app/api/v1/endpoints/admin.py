# api/v1/endpoints/user.py
from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.auth import refresh_token, get_admin_id_and_token
from app.common.result import Result


router = APIRouter()


@router.get("/check/status")
async def check_admin_status(
        request: Request,
        response: Response,
        db: AsyncSession = Depends(get_db)
):
    admin_id, token = await get_admin_id_and_token(request, db)
    refresh_token(token, response)
    return Result.success()

