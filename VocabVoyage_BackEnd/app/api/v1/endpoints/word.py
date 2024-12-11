from fastapi import APIRouter, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.crud.word import search_word_fuzzy

router = APIRouter()


@router.get("/search")
async def search_word(
        query: str = Query(..., description="搜索内容"),
        db: AsyncSession = Depends(get_db)
):
    return await search_word_fuzzy(query, db)


