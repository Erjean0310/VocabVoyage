from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.crud.mistake import get_mistakes_with_details
from app.common.page_query import PageQueryResult
from app.schemas.page_query_params import PageQueryParams

router = APIRouter()


@router.post("/list/", response_model=PageQueryResult, summary="分页查询错误记录")
async def list_mistakes(
    query_params: PageQueryParams,
    db: AsyncSession = Depends(get_db)
):
    mistakes = await get_mistakes_with_details(
        db,
        page=query_params.page,
        page_size=query_params.page_size,
        status=query_params.status
    )
    return PageQueryResult(mistakes=mistakes.mistakes, total=mistakes.total)
