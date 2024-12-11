from http.client import HTTPException

from fastapi import APIRouter, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.crud.word import search_word_fuzzy, get_word_by_id, get_word_by_spell

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
