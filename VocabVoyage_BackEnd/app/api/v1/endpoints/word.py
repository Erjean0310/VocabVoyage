from app.services.auth import get_user_id_and_token, refresh_token, refresh_token_if_exists
from fastapi import APIRouter, Query, Depends, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.crud.word import search_word_fuzzy, get_word_by_id, get_word_by_spell
from app.schemas.memory import ProficiencyFilterRequest, MemorizeWordRequest
from app.services.memory import get_words, handle_memory
from app.common.result import Result

router = APIRouter()


@router.get("/search", summary="单词模糊搜索")
async def search_word(
        request: Request,
        response: Response,
        query: str = Query(..., description="搜索内容"),
        db: AsyncSession = Depends(get_db)
):
    result = await search_word_fuzzy(query, db)

    refresh_token_if_exists(request, response)
    return Result.success(data=result)


@router.get("/{word_id}", summary="根据单词 id 获取单词信息")
async def get_word(word_id: int, request: Request, response: Response, db: AsyncSession = Depends(get_db)):
    result = await get_word_by_id(word_id, db)
    refresh_token_if_exists(request, response)
    return Result.success(data=result)


@router.get("/", summary="根据单词拼写获取单词信息")
async def get_word_detail(
        request: Request,
        response: Response,
        word_spell: str = Query(..., description="单词拼写"),
        db: AsyncSession = Depends(get_db)):
    result = await get_word_by_spell(word_spell, db)
    refresh_token_if_exists(request, response)
    return Result.success(data=result)


@router.post("/memorize", summary="根据记忆结果更新熟练度值")
async def memorize_word(memorize_request: MemorizeWordRequest, request: Request, response: Response, db: AsyncSession = Depends(get_db)):
    user_id, token = get_user_id_and_token(request)
    await handle_memory(db, user_id, memorize_request.word_id, memorize_request.mem_res)
    refresh_token(token, response)
    return Result.success()


@router.post("/list/by/proficiency", summary="获取学习单词")
async def list_words_to_learn(
        proficiency_filter: ProficiencyFilterRequest,
        request: Request,
        response: Response,
        db: AsyncSession = Depends(get_db)
):
    user_id, token = get_user_id_and_token(request)
    result = await get_words(db, user_id, proficiency_filter.new_word_weight, proficiency_filter.count)
    refresh_token(token, response)
    return Result.success(data=result)
