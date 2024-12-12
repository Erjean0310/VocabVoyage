from http.client import HTTPException
from app.services.common import get_user_id
from fastapi import APIRouter, Query, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.crud.word import search_word_fuzzy, get_word_by_id, get_word_by_spell
from app.schemas.memory import ProficiencyFilterRequest
from app.services.memory import get_words

router = APIRouter()


@router.get("/search", summary="单词模糊搜索")
async def search_word(
        query: str = Query(..., description="搜索内容"),
        db: AsyncSession = Depends(get_db)
):
    return await search_word_fuzzy(query, db)


@router.get("/{word_id}", summary="根据单词 id 获取单词信息")
async def get_word(word_id: int, db: AsyncSession = Depends(get_db)):
    return await get_word_by_id(word_id, db)


@router.post("/", summary="根据单词拼写获取单词信息")
async def get_word_detail(word_spell: str, db: AsyncSession = Depends(get_db)):
    if not word_spell:
        raise HTTPException(status_code=400, detail="单词拼写不能为空")
    return await get_word_by_spell(word_spell, db)


@router.post("/memorize", summary="根据记忆结果更新熟练度值")
async def memorize_word(word_id: int, mem_res: int, db: AsyncSession = Depends(get_db)):
    pass


@router.post("/list/by/proficiency", summary="获取学习单词")
async def list_words_to_learn(proficiency_filter: ProficiencyFilterRequest, request: Request, db: AsyncSession = Depends(get_db)):
    uesr_id = get_user_id(request)
    result = await get_words(db, uesr_id, proficiency_filter.new_word_weight, proficiency_filter.count)
    return result
