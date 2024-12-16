# api/v1/endpoints/user.py
from fastapi import APIRouter, Depends, Response, Request, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.auth import refresh_token, get_admin_id_and_token
from app.common.result import Result
from app.crud.admin import export_data


router = APIRouter()


@router.get("/check/status", summary="检查管理员身份")
async def check_admin_status(
        request: Request,
        response: Response,
        db: AsyncSession = Depends(get_db)
):
    admin_id, token = await get_admin_id_and_token(request, db)
    refresh_token(token, response)
    return Result.success()


@router.put("/export/data", summary="导出数据库数据")
async def data_export(
        request: Request,
        response: Response,
        table_name: str = Query(..., description="数据库表名"),
        db: AsyncSession = Depends(get_db)
):
    admin_id, token = await get_admin_id_and_token(request, db)
    result = await export_data(db, table_name)
    refresh_token(token, response)
    if not result:
        return Result.fail("导出失败, 请检查表名是否正确!")
    return Result.success()


