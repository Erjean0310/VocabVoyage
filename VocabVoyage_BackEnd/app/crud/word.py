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


async def get_word_by_id(word_id: int, db: AsyncSession):
    try:
        # 执行查询，返回指定字段
        result = await db.execute(
            select(Word.spell, Word.meaning, Word.description).filter(Word.id == word_id)
        )
        word = result.first()  # 获取第一条记录

        if not word:
            raise HTTPException(status_code=404, detail=f"Word with id {word_id} not found")

        res = {"spell": word.spell, "meaning": word.meaning, "description": word.description}
        return res
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))


async def get_word_by_spell(spell: str, db: AsyncSession):
    try:
        result = await db.execute(
            select(Word).filter(Word.spell == spell)
        )
        word = result.scalar()

        if not word:
            raise HTTPException(status_code=404, detail=f"Word '{spell}' not found")

        jsonable_words = jsonable_encoder(word)
        return jsonable_words
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))
