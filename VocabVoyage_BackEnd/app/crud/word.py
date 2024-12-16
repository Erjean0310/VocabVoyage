from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from app.models.word import Word
from app.models.mistake import Mistake
from fastapi.encoders import jsonable_encoder
from app.common.response import CustomException
from app.core.constans import Constants


async def search_word_fuzzy(query: str, db: AsyncSession):
    result = await db.execute(
        select(Word.id, Word.spell).filter(Word.spell.like(f"{query}%"))
        .order_by(func.length(Word.spell).asc())
        .limit(5)
    )
    words = result.all()
    res = [{"id": word.id, "spell": word.spell} for word in words]
    return res


async def get_word_by_id(word_id: int, db: AsyncSession):
    # 执行查询，返回指定字段
    result = await db.execute(
        select(Word.spell, Word.meaning, Word.description).filter(Word.id == word_id)
    )
    word = result.first()  # 获取第一条记录

    if not word:
        raise CustomException(404, Constants.WORD_NOT_FOUND)

    res = {"spell": word.spell, "meaning": word.meaning, "description": word.description}
    return res


async def get_word_by_spell(spell: str, db: AsyncSession):
    result = await db.execute(
        select(Word).filter(Word.spell == spell)
    )
    word = result.scalar()

    if not word:
        return None

    word = jsonable_encoder(word)
    return word


async def add_mistake(db: AsyncSession, reporter_id: int, word_id: int, description: str):
    mistake = Mistake(
        word_id=word_id,
        reporter_id=reporter_id,
        description=description
    )
    db.add(mistake)
    await db.commit()


async def get_word_not_in_list(need: int, word_ids: List[int], db: AsyncSession):
    result = await db.execute(
        select(Word.id).filter(~Word.id.in_(word_ids)).limit(need)
    )
    word_ids = result.scalars().all()
    return word_ids
