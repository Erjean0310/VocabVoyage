from app.db.session import get_db
from app.crud.mistake import get_mistakes_with_details
from app.common.page_query import PageQueryResult
from app.schemas.page_query_params import PageQueryParams
from app.services.auth import get_user_id_and_token, refresh_token
from fastapi import APIRouter, Depends, Request, Response
from app.schemas.memory import ReportMistakeRequest
from sqlalchemy.ext.asyncio import AsyncSession
from app.common.result import Result
from app.core.constans import Constants
from app.crud.word import add_mistake

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


@router.post("/report", summary="上报单词错误")
async def report_mistake(
        mistake_request: ReportMistakeRequest,
        request: Request,
        response: Response,
        db: AsyncSession = Depends(get_db)
):
    user_id, token = get_user_id_and_token(request)
    await add_mistake(db, user_id, mistake_request.word_id, mistake_request.description)
    refresh_token(token, response)
    return Result.success(Constants.REPORT_SUCCESS)
