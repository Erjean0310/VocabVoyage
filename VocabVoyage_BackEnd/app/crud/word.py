from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from app.models.word import Word
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


async def search_word_fuzzy(query: str, db: AsyncSession):
    try:
        result = await db.execute(
            select(Word.id, Word.spell).filter(Word.spell.like(f"{query}%"))
            .order_by(func.length(Word.spell).asc())
            .limit(5)
        )
        words = result.all()
        res = [{"id": word.id, "spell": word.spell} for word in words]
        return res

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))
